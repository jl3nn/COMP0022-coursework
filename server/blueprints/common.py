from flask import jsonify, make_response, Response
import json
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
        return make_response(jsonify(list(map(func, results))), 200)
    except Exception as error:
        print(f"error: {str(error)}")
        return make_response(jsonify({"error": str(error)}), 500)


def is_error(results: Any) -> bool:
    return isinstance(results, dict) and "error" in results


def transform_response(response: Response, func: Callable[[Any], Any]) -> Response:
    results = json.loads(response.data.decode("utf-8"))

    if is_error(results):
        return response
    else:
        return make_response(jsonify(func(results)), 200)


def concat_responses(responses: list[Response]) -> Response:
    rows = []

    for response in responses:
        results = json.loads(response.data.decode("utf-8"))

        if is_error(results):
            return response
        else:
            rows.extend(results)

    return make_response(jsonify(rows), 200)
