from flask import jsonify, make_response, Response, request
import psycopg
from typing import Any, Callable, Optional
from flask_caching import Cache


CONN_INFO = {
    "dbname": "comp0022",
    "user": "admin",
    "password": "top_secret_password",
    "host": "database",
    "port": "5432",
}

CACHE_SETTINGS = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": "redis://redis:6379/0",
    "CACHE_DEFAULT_TIMEOUT": 500,
}

# register cache
cache = Cache(config=CACHE_SETTINGS)


@cache.memoize()
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
