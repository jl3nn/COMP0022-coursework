#!/bin/bash

set -e

# Replace placeholders with environment variable values
SQL_SCRIPT=$(cat /docker-entrypoint-initdb.d/readonly-user.sql.template)
SQL_SCRIPT=${SQL_SCRIPT//"{{DB_USER_READONLY}}"/$DB_USER_READONLY}
SQL_SCRIPT=${SQL_SCRIPT//"{{DB_PASSWORD_READONLY}}"/$DB_PASSWORD_READONLY}
SQL_SCRIPT=${SQL_SCRIPT//"{{POSTGRES_DB}}"/$POSTGRES_DB}

# Execute the SQL script
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<- EOSQL
    $SQL_SCRIPT
EOSQL
