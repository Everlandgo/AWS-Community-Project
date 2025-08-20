# 1. 베이스 이미지 선택
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app
# 2-1. DB 폴더 생성 (선택 사항)
RUN mkdir -p /app

# 3. 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY ./app ./app
COPY ./app/static ./app/static

# 5. 포트 오픈 (FastAPI 기본 8000)
EXPOSE 8000

# 6. 컨테이너 실행 시 FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
