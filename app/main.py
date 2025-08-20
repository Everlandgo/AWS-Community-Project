import os
from fastapi import FastAPI
from . import models, db
from .routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# BASE_DIR 정의 (현재 파일 기준)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    title="FastAPI Comment Service",
    openapi_url="/api/openapi.json",  # OpenAPI 정의 경로
    docs_url="/api/docs"              # Swagger UI 경로
)

# DB 테이블 생성
models.Base.metadata.create_all(bind=db.engine)

# API 라우터 등록
app.include_router(router, prefix="/api", tags=["Comments"])

# StaticFiles mount
app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "static"), html=True), name="static")

# Health check
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

# CORS 설정 (테스트용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
