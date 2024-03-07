from flask import jsonify, make_response, Response
from flask_caching import Cache
import json
import os
import psycopg
from typing import Any, Callable, Optional

CONN_INFO = {
    "movielens": {
        "dbname": os.environ.get("MOVIELENS_DB_NAME"),
        "user": os.environ.get("MOVIELENS_DB_USER"),
        "password": os.environ.get("MOVIELENS_DB_PASSWORD"),
        "host": os.environ.get("MOVIELENS_DB_HOST"),
        "port": os.environ.get("MOVIELENS_DB_PORT"),
    },
    "personality": {
        "dbname": os.environ.get("PERSONALITY_DB_NAME"),
        "user": os.environ.get("PERSONALITY_DB_USER"),
        "password": os.environ.get("PERSONALITY_DB_PASSWORD"),
        "host": os.environ.get("PERSONALITY_DB_HOST"),
        "port": os.environ.get("PERSONALITY_DB_PORT"),
    },
}

CACHE_SETTINGS = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": os.environ.get("CACHE_HOST"),
    "CACHE_REDIS_PORT": os.environ.get("CACHE_PORT"),
    "CACHE_REDIS_PASSWORD": os.environ.get("CACHE_PASSWORD"),
    "CACHE_DEFAULT_TIMEOUT": os.environ.get("CACHE_TIMEOUT"),
}

cache = Cache(config=CACHE_SETTINGS)


@cache.memoize()
def execute_query(query: str, params: Optional[dict], db: str) -> list[tuple]:
    with psycopg.connect(**CONN_INFO[db]) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()

    conn.close()
    return results


def get_response(
    query: str,
    params: Optional[dict] = None,
    func: Callable[[tuple], Any] = lambda row: row[0],
    db: str = "movielens",
) -> Response:
    try:
        results = execute_query(query, params, db)
        return make_response(jsonify(list(map(func, results))), 200)
    except Exception as error:
        print(f"error: {str(error)}")
        return make_response(jsonify({"error": str(error)}), 500)


def is_error(results: Any) -> bool:
    return isinstance(results, dict) and "error" in results


def transform_response(
    response: Response, func: Callable[[Any], Any] = lambda results: results[0]
) -> Response:
    results = json.loads(response.data.decode("utf-8"))

    if is_error(results):
        return response

    return make_response(jsonify(func(results)), 200)


def concat_responses(responses: list[Response]) -> Response:
    rows = set()

    for response in responses:
        results = json.loads(response.data.decode("utf-8"))

        if is_error(results):
            return response

        rows.update(results)

    return make_response(jsonify(list(rows)), 200)
