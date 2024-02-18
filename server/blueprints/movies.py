from .common import get_response
from flask import Blueprint, Response, request

app = Blueprint("movies", __name__)


def get_movies_by_user_preference(
    min_rating: int = 0, max_rating: int = 5, precision: int = 3, order: str = "DESC", limit: int = 10
) -> Response:
    movie = request.json.get("movie")
    return get_response(
        f"""
        WITH RelevantUsers AS (
            SELECT
                DISTINCT r.user_id
            FROM
                ratings r
            INNER JOIN
                movies m ON r.movie_id = m.movie_id
            WHERE
                m.title = %(movie)s
            GROUP BY
                r.user_id
            HAVING
                AVG(r.rating) BETWEEN {min_rating} AND {max_rating}
        )

        SELECT
            m.title,
            ROUND(AVG(r.rating)::NUMERIC, {precision}) AS AvgRating
        FROM
            ratings r
        INNER JOIN
            movies m ON r.movie_id = m.movie_id
        WHERE
            r.user_id IN (SELECT user_id FROM RelevantUsers)
            AND m.title != %(movie)s
        GROUP BY
            m.title
        ORDER BY
            AvgRating {order}
        """,
        params={"movie": movie},
        func=lambda row: {"id": row[0], "avg_rating": row[1]},
    )


@app.route("/user-preferences", methods=["POST"])
def get_user_preferences() -> Response:
    opinion = request.json.get("opinion")
    if opinion == 1:
        return get_movies_by_user_preference(4, 5)
    if opinion == 2:
        return get_movies_by_user_preference(0, 2)
    return get_movies_by_user_preference(2, 4)
