from .common import json_response, json_error
from .connector import execute_query
from flask import Blueprint, Response

app = Blueprint("genres", __name__)


def get_genres(agg_func: str, precision: int = 3) -> Response:
    try:
        results = execute_query(
            f"""
            SELECT
                g.genre,
                round({agg_func}(r.rating)::numeric, {precision}) AS statistic
            FROM
                genres g
            INNER JOIN
                movies_genres mg ON g.genre_id = mg.genre_id
            INNER JOIN
                movies m ON mg.movie_id = m.movie_id
            LEFT JOIN
                ratings r ON m.movie_id = r.movie_id
            GROUP BY
                g.genre
            HAVING
                {agg_func}(r.rating) IS NOT NULL
            ORDER BY
                statistic DESC
            ;
            """
        )

        # TODO: Modify client to include statistic
        # return json_response(results, lambda row: {"genre": row[0], agg_func: row[1]})
        return json_response(results, lambda row: row[0])
    except Exception as e:
        return json_error(e)


@app.route("/popular", methods=["GET"])
def get_popular_genres() -> Response:
    return get_genres("avg")


@app.route("/controversial", methods=["GET"])
def get_controversial_genres() -> Response:
    return get_genres("stddev")
