FROM python:3.9.12-slim
WORKDIR /app
COPY . /app
RUN apt-get -y update && apt-get -y install gcc python3-dev
RUN pip install --no-cache-dir -r requirements.txt

RUN gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
