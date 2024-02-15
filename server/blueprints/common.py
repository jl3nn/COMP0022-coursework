from flask import jsonify, Response
import psycopg
from typing import Any, Callable, Optional

CONN_INFO = {
    "dbname": "comp0022",
    "user": "admin",
    "password": "top_secret_password",
    "host": "database",
    "port": "5432",
}


def execute_query(query: str, params: Optional[dict]) -> list[tuple]:
    with psycopg.connect(**CONN_INFO) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()

    conn.close()
    return results


def get_response(
    query: str,
    params: Optional[dict] = None,
    func: Callable[[tuple], Any] = lambda row: row[0],
) -> Response:
    try:
        results = execute_query(query, params)
        return jsonify(list(map(func, results)))
    except Exception as error:
        print(f"error: {str(error)}")
        return jsonify({"error": str(error)}), 500
