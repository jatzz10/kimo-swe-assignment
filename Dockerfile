FROM python:3.11.1-alpine

WORKDIR /backend-service

COPY ./requirements.txt /course-backend-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /course-backend-api/requirements.txt

COPY . /course-backend-api

RUN ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt

# COPY app /app/app
# COPY tests /app/tests
# COPY config.py /app/config.py
# COPY main.py /app/main.py

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]