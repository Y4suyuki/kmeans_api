FROM python:3.9.12-slim
WORKDIR /app
ADD . /app
RUN apt-get -y update && apt-get -y install gcc python3-dev
RUN pip install -r requirements.txt
