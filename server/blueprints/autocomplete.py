import json
from .common import get_response
from flask import Blueprint, jsonify, make_response, request, Response

app = Blueprint("autocomplete", __name__)


def autocomplete(field: str, table: str, limit: int = 5) -> Response:
    return get_response(
        f"""
        SELECT DISTINCT
            {field}
        FROM
            {table}
        WHERE
            {field} LIKE %(prefix)s
        GROUP BY
            {field}
        LIMIT
            {limit}
        ;
        """,
        params={"prefix": request.args.get("prefix", "").lower() + "%"},
    )


@app.route("/genre", methods=["GET"])
def autocomplete_genre() -> Response:
    return autocomplete("genre", "genres")


@app.route("/tag", methods=["GET"])
def autocomplete_tag() -> Response:
    return autocomplete("tag", "tags")


@app.route("/movie", methods=["GET"])
def autocomplete_movie() -> Response:
    return autocomplete("title", "movies")


@app.route("/user", methods=["GET"])
def autocomplete_user() -> Response:
    return autocomplete("user_id", "users")


@app.route("/metric-degree", methods=["GET"])
def autocomplete_metric_degree():
    sample_personalities = ["low", "med", "high"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [
            user for user in sample_personalities if user.lower().startswith(prefix)
        ]
        return jsonify(list(map(lambda row: row, matches)))
    except Exception as error:
        print(f"error: {str(error)}")
        return jsonify({"error": str(error)}), 500


@app.route("/metric", methods=["GET"])
def autocomplete_metric():
    sample_personalities = ["serendipity", "popularity", "diversity"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [
            user for user in sample_personalities if user.lower().startswith(prefix)
        ]
        return jsonify(list(map(lambda row: row, matches)))
    except Exception as error:
        print(f"error: {str(error)}")
        return jsonify({"error": str(error)}), 500

@app.route("/search", methods=["GET"])
def autocomplete_search():
    movies = autocomplete("title", "movies", 3)
    actors = autocomplete("name", "actors", 3)
    directors = autocomplete("name", "directors", 3)
    movies_data = json.loads(movies.data.decode('utf-8'))
    actors_data = json.loads(actors.data.decode('utf-8'))
    directors_data = json.loads(directors.data.decode('utf-8'))
    combined_data = movies_data + actors_data + directors_data
    return make_response(jsonify(combined_data), 200)
