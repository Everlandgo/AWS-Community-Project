from fastapi import FastAPI
from . import models, db
from .routes import router

app = FastAPI(title="FastAPI Comment Service")

# DB 테이블 생성
models.Base.metadata.create_all(bind=db.engine)

# 라우터 등록
app.include_router(router, prefix="/api")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
