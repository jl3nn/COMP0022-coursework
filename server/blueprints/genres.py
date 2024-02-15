from .common import get_response
from flask import Blueprint, Response

app = Blueprint("genres", __name__)


def get_genres(agg_func: str, precision: int = 3) -> Response:
    return get_response(
        f"""
        SELECT
            g.genre,
            round({agg_func}(r.rating)::numeric, {precision}) AS statistic
        FROM
            genres g
        INNER JOIN
            movies_genres mg ON g.genre_id = mg.genre_id
        INNER JOIN
            ratings r ON mg.movie_id = r.movie_id
        GROUP BY
            g.genre_id
        ORDER BY
            statistic DESC
        ;
        """,
        # TODO: Modify client to include statistic
        # func=lambda row: {"genre": row[0], "statistic": row[1]},
    )


@app.route("/popular", methods=["GET"])
def get_popular_genres() -> Response:
    return get_genres("avg")


@app.route("/controversial", methods=["GET"])
def get_controversial_genres() -> Response:
    return get_genres("stddev")
