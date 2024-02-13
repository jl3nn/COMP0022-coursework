# Stage 1: Build Python image and run preprocessing.py
FROM python:3.11 AS builder

WORKDIR /app

COPY additional ./additional
COPY movielens ./movielens
COPY personality ./personality
COPY preprocessing.py .

RUN pip install --no-cache-dir -r requirements.txt

RUN python preprocessing.py

# Stage 2: Build PostgreSQL image
FROM postgres:latest

ENV POSTGRES_DB comp0022
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD top_secret_password

WORKDIR /docker-entrypoint-initdb.d

COPY init.sql .
COPY --from=builder /app/processed/*.csv .

EXPOSE 5432
