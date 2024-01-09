# Use an official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_DB comp0022
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD top_secret_password

# Create a directory to store SQL scripts and CSV files
WORKDIR /docker-entrypoint-initdb.d

# Copy SQL scripts and CSV files to the container
COPY init.sql .
COPY preprocessing/processed_data/*.csv .

# Expose the PostgreSQL port
EXPOSE 5432
