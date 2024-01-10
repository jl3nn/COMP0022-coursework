# Stage 1: Build Python Image and Run preprocessing.py
FROM python:3.9 AS builder

WORKDIR /app

COPY *.csv /app/
COPY preprocessing.py /app/

RUN pip install pandas

RUN python preprocessing.py

# Stage 2: Build PostgreSQL Image
FROM postgres:latest

ENV POSTGRES_DB comp0022
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD top_secret_password

WORKDIR /docker-entrypoint-initdb.d

COPY init.sql /docker-entrypoint-initdb.d/
COPY --from=builder /app/processed/*.csv /docker-entrypoint-initdb.d/

EXPOSE 5432