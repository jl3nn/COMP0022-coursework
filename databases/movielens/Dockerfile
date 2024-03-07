# Stage 1: Build Python image and run preprocessing.py
FROM python:3.12 AS builder

WORKDIR /app

COPY raw ./raw
COPY requirements.txt .
COPY preprocessing.py .
COPY additional ./additional

RUN pip install --no-cache-dir -r requirements.txt

RUN python preprocessing.py

# Stage 2: Build PostgreSQL image
FROM postgres:latest

WORKDIR /docker-entrypoint-initdb.d

COPY init.sql .
COPY --from=builder /app/processed/*.csv .
