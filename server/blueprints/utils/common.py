from .connector import execute_query
from flask import jsonify, Response
from typing import Any, Callable, Optional


def jsonify_results(results: list[tuple], func: Callable[[tuple], Any]) -> Response:
    return jsonify(list(map(func, results)))


def jsonify_error(error: Exception) -> Response:
    print(f"error: {str(error)}")
    return jsonify({"error": str(error)}), 500


def get_response(
    query: str,
    params: Optional[dict] = None,
    func: Callable[[tuple], Any] = lambda row: row[0],
) -> Response:
    try:
        results = execute_query(query, params)
        return jsonify_results(results, func)
    except Exception as error:
        return jsonify_error(error)
