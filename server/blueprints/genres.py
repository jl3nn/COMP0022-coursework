from .common import get_response
from flask import Blueprint, Response, request
from flasgger import swag_from

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
@swag_from({
    'tags': ['Genres'],
    'description': 'Retrieves genres sorted by their average ratings to identify the most popular genres.',
    'responses': {
        200: {
            'description': 'A list of popular genres based on average ratings.',
            'examples': {
                'application/json': [
                    {"genre": "Comedy", "statistic": 4.5},
                    {"genre": "Drama", "statistic": 4.3}
                ]
            }
        }
    }
})
def get_popular_genres() -> Response:
    return get_genres_by_statistic("AVG")


@app.route("/controversial", methods=["GET"])
@swag_from({
    'tags': ['Genres'],
    'description': 'Retrieves genres sorted by the standard deviation of their ratings to identify the most controversial genres.',
    'responses': {
        200: {
            'description': 'A list of controversial genres based on the standard deviation of ratings.',
            'examples': {
                'application/json': [
                    {"genre": "Horror", "statistic": 2.1},
                    {"genre": "Sci-Fi", "statistic": 2.0}
                ]
            }
        }
    }
})
def get_controversial_genres() -> Response:
    return get_genres_by_statistic("STDDEV")


@app.route("/user-preferences", methods=["POST"])
@swag_from({
    'tags': ['Genres'],
    'description': 'Retrieves genres based on user preference for high, low, or mid-range rated movies, indicated by the opinion value.',
    'parameters': [
        {
            'name': 'opinion',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'opinion': {
                        'type': 'integer',
                        'description': 'User opinion indicating preference. 1 for high-rated (4 to 5), 2 for low-rated (0 to 2), any other value for mid-range rated (2 to 4) movies.'
                    }
                },
                'required': ['opinion'],
                'example': {'opinion': 1}
            },
            'required': True,
            'description': 'JSON payload containing the user opinion on movie ratings.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of genres based on the specified user preference.',
            'examples': {
                'application/json': [
                    {"genre": "Adventure", "preference": 4.5},
                    {"genre": "Action", "preference": 4.7}
                ]
            }
        }
    }
})
def get_user_preferences() -> Response:
    opinion = request.json.get("opinion", 0)

    if opinion == 1:
        return get_genres_by_user_preference(4, 5)

    if opinion == 2:
        return get_genres_by_user_preference(0, 2)

    return get_genres_by_user_preference(2, 4)
