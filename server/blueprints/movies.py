from .connector import execute_query
from flask import Blueprint, jsonify, Response

app = Blueprint("movies", __name__)


@app.route("/popular", methods=["GET"])
def get_popular_movies() -> Response:
    try:
        result_data = ["Some Genre" for _ in range(10)]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/controversial", methods=["GET"])
def get_controversial_movies() -> Response:
    try:
        result_data = ["Some Other Genre" for _ in range(10)]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
