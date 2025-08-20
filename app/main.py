from fastapi import FastAPI
from . import models, db
from .routes import router
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="FastAPI Comment Service",
    openapi_url="/api/openapi.json",  # OpenAPI 정의 경로
    docs_url="/api/docs"              # Swagger UI 경로
)

# DB 테이블 생성
models.Base.metadata.create_all(bind=db.engine)

# 라우터 등록
app.include_router(router, prefix="/api", tags=["Comments"])

app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Health check
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


# static/index.html 제공
<<<<<<< HEAD
app.mount("/", StaticFiles(directory="static", html=True), name="static")
=======
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# 테스트 용도 ! 
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",  # 테스트용으로 모든 도메인 허용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
>>>>>>> trial


# static/index.html 제공
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# 테스트 용도 ! 
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",  # 테스트용으로 모든 도메인 허용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)