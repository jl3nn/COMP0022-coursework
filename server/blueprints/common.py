from flask import jsonify, Response
from typing import Any, Callable


def json_response(results: list[tuple], func: Callable[[tuple], Any]) -> Response:
    return jsonify(list(map(func, results)))


def json_error(e: Exception) -> Response:
    print(f"error: {str(e)}")
    return jsonify({"error": str(e)}), 500
