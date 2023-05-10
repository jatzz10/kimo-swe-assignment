FROM python:3.11.1-alpine

WORKDIR /course-backend-api

COPY ./requirements.txt /course-backend-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /course-backend-api/requirements.txt

COPY . /course-backend-api

RUN ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]