from fastapi import FastAPI
from . import models, db
from .routes import router

app = FastAPI(title="FastAPI Comment Service")

# DB 테이블 생성
models.Base.metadata.create_all(bind=db.engine)

# 라우터 등록
app.include_router(router, prefix="/api", tags=["Comments"])
app = FastAPI(
    title="FastAPI Comment Service",
    openapi_url="/api/openapi.json",  # OpenAPI 정의 파일 경로
    docs_url="/api/docs"              # Swagger UI 경로
)
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
