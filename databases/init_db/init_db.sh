#!/bin/bash
set -e

# Replace placeholders with environment variable values
SQL_SCRIPT=$(cat /docker-entrypoint-initdb.d/create_readonly_user.sql.template)
SQL_SCRIPT=${SQL_SCRIPT//"{{READONLY_DB_USER}}"/$READONLY_DB_USER}
SQL_SCRIPT=${SQL_SCRIPT//"{{READONLY_DB_PASSWORD}}"/$READONLY_DB_PASSWORD}
SQL_SCRIPT=${SQL_SCRIPT//"{{POSTGRES_DB}}"/$POSTGRES_DB}


# Execute the SQL script
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    $SQL_SCRIPT
EOSQL
