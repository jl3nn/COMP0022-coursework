from .common import json_response, json_error
from .connector import execute_query
from flask import Blueprint, request, Response

app = Blueprint("autocomplete", __name__)


def autocomplete(field: str, table: str, limit: int = 5) -> Response:
    try:
        results = execute_query(
            f"""
            SELECT DISTINCT
                {field}
            FROM
                {table}
            WHERE
                LOWER({field}) LIKE %(prefix)s
            LIMIT
                {limit}
            ;
            """,
            {"prefix": request.args.get("prefix", "").lower() + "%"},
        )

        return json_response(results, lambda row: row[0])
    except Exception as e:
        return json_error(e)


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
        return json_response(matches, lambda row: row)
    except Exception as e:
        return json_error(e)


@app.route("/metric", methods=["GET"])
def autocomplete_metric():
    sample_personalities = ["serendipity", "popularity", "diversity"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [
            user for user in sample_personalities if user.lower().startswith(prefix)
        ]
        return json_response(matches, lambda row: row)
    except Exception as e:
        return json_error(e)
