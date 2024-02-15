import psycopg
from typing import Optional

DB_PARAMS = {
    "dbname": "comp0022",
    "user": "admin",
    "password": "top_secret_password",
    "host": "database",
    "port": "5432",
}


def execute_query(query: str, query_params: Optional[dict] = None) -> list[tuple]:
    with psycopg.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, query_params)
            results = cursor.fetchall()

    conn.close()
    return results
