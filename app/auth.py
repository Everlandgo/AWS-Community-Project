import os
from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWKClient, InvalidTokenError

bearer = HTTPBearer(auto_error=True)

COGNITO_REGION = os.getenv("COGNITO_REGION")
POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
ISSUER = os.getenv("COGNITO_ISSUER") or f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{POOL_ID}"
JWKS_URL = f"{ISSUER}/.well-known/jwks.json"

_jwk_client = PyJWKClient(JWKS_URL)

def verify_cognito_token(credentials: HTTPAuthorizationCredentials = Security(bearer)):
    token = credentials.credentials
    try:
        signing_key = _jwk_client.get_signing_key_from_jwt(token).key
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            issuer=ISSUER,
            options={"verify_aud": False},
            leeway=10,
        )

        token_use = payload.get("token_use")
        if token_use == "id":
            if payload.get("aud") != CLIENT_ID:
                raise HTTPException(status_code=401, detail="Invalid audience for ID token")
        elif token_use == "access":
            if payload.get("client_id") != CLIENT_ID:
                raise HTTPException(status_code=401, detail="Invalid client_id for Access token")
        else:
            raise HTTPException(status_code=401, detail="Unsupported token_use")

        return payload

    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
