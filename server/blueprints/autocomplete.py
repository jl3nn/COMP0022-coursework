from .common import concat_responses, get_response
from flask import Blueprint, request, Response

app = Blueprint("autocomplete", __name__)


def autocomplete(field: str, table: str, limit: int = 5) -> Response:
    return get_response(
        f"""
        SELECT
            DISTINCT {field}
        FROM
            {table}
        WHERE
            LOWER({field}::TEXT) LIKE %(prefix)s
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


@app.route("/search", methods=["GET"])
def autocomplete_search() -> Response:
    return concat_responses(
        [
            autocomplete("title", "movies", 3),
            autocomplete("name", "actors", 3),
            autocomplete("name", "directors", 3),
        ]
    )
