from .common import get_response
from flask import Blueprint, Response, request

app = Blueprint("genres", __name__)


def get_genres_by_statistic(agg_func: str, precision: int = 3) -> Response:
    return get_response(
        f"""
        SELECT
            g.genre,
            ROUND({agg_func}(r.rating)::NUMERIC, {precision}) AS statistic
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
        func=lambda row: {"genre": row[0], "statistic": row[1]},
    )


def get_genres_by_user_preference(
    min_rating: int = 0, max_rating: int = 5, precision: int = 3
) -> Response:
    return get_response(
        f"""
        WITH relevant_users AS (
            SELECT
                DISTINCT r.user_id
            FROM
                ratings r
            INNER JOIN
                movies_genres mg ON r.movie_id = mg.movie_id
            INNER JOIN
                genres g ON mg.genre_id = g.genre_id
            WHERE
                g.genre = %(genre)s
            GROUP BY
                r.user_id
            HAVING
                AVG(r.rating) BETWEEN {min_rating} AND {max_rating}
        )
        
        SELECT
            g.genre,
            ROUND(AVG(r.rating)::NUMERIC, {precision}) AS avg_rating
        FROM
            movies_genres mg
        INNER JOIN
            genres g ON mg.genre_id = g.genre_id
        INNER JOIN
            ratings r ON mg.movie_id = r.movie_id
        INNER JOIN
            relevant_users ru ON r.user_id = ru.user_id
        WHERE
            g.genre != %(genre)s
        GROUP BY
            g.genre
        ORDER BY
            avg_rating DESC
        ;
        """,
        params={"genre": request.json.get("genre", "")},
        func=lambda row: {"id": row[0], "avg_rating": row[1]},
    )


@app.route("/popular", methods=["GET"])
def get_popular_genres() -> Response:
    return get_genres_by_statistic("AVG")


@app.route("/controversial", methods=["GET"])
def get_controversial_genres() -> Response:
    return get_genres_by_statistic("STDDEV")


@app.route("/user-preferences", methods=["POST"])
def get_user_preferences() -> Response:
    opinion = request.json.get("opinion", 0)

    if opinion == 1:
        return get_genres_by_user_preference(4, 5)

    if opinion == 2:
        return get_genres_by_user_preference(0, 2)

    return get_genres_by_user_preference(2, 4)
