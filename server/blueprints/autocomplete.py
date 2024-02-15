from .utils import get_response
from flask import Blueprint, jsonify, request, Response

app = Blueprint("autocomplete", __name__)


def autocomplete(field: str, table: str, limit: int = 5) -> Response:
    return get_response(
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
