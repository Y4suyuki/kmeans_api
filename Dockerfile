FROM python:3.9.12-slim
WORKDIR /app
COPY . /app
RUN apt-get -y update && apt-get -y install gcc python3-dev
RUN pip install --no-cache-dir -r requirements.txt
