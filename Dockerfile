FROM python:3.9.6-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt
# COPY app /app/app
# COPY tests /app/tests
# COPY config.py /app/config.py
# COPY main.py /app/main.py

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]