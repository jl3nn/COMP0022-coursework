from collections import defaultdict
from .common import Database, get_response, transform_response
from flasgger import swag_from
from flask import Blueprint, Response

app = Blueprint("personality", __name__)


@app.route("/skew", methods=["GET"])
@swag_from(
    {
        "tags": ["Personality Analysis"],
        "description": "Calculate personality skew based on movie preferences.",
        "responses": {
            200: {
                "description": "A list of personality types with their corresponding movie genres and Pearson coefficients.",
                "examples": {
                    "application/json": {
                        "openness": {"x": ["Drama", "Comedy"], "y": [0.95, 0.85]},
                        "agreeableness": {
                            "x": ["Family", "Adventure"],
                            "y": [0.90, 0.88],
                        },
                    }
                },
            }
        },
    }
)
def calculate_personalities_skew() -> Response:
    def format_results(results: list[tuple]) -> dict[str, list]:
        personality_genres = defaultdict(list)

        for personality_type, genre, pearson_coeff in results:
            personality_genres[personality_type].append((genre, float(pearson_coeff)))

        formatted_results = {}

        for personality, genres in personality_genres.items():
            sorted_genres = sorted(genres, key=lambda x: x[1], reverse=True)
            genres_list, coeffs_list = zip(*sorted_genres)
            formatted_results[personality] = {
                "x": list(genres_list),
                "y": list(coeffs_list),
            }

        return formatted_results

    return transform_response(
        get_response(
            """
            WITH PearsonCoefficients AS (
                SELECT
                    g.genre,
                    p.trait AS personality_type,
                    (
                        (COUNT(*) * SUM(r.rating * p.value) - SUM(r.rating) * SUM(p.value))
                        /
                        (SQRT(COUNT(*) * SUM(r.rating * r.rating) - SUM(r.rating) * SUM(rating))
                        * SQRT(COUNT(*) * SUM(p.value * p.value) - SUM(p.value) * SUM(p.value)))
                    ) AS pearson_coeff
                FROM users u
                JOIN ratings r ON r.user_id = u.user_id
                JOIN movies m ON r.movie_id = m.movie_id
                JOIN movie_genre mg ON mg.movie_id = m.movie_id
                JOIN genres g ON g.genre_id = mg.genre_id
                JOIN (
                    SELECT user_id, 'openness' AS trait, openness AS value FROM users
                    UNION ALL
                    SELECT user_id, 'agreeableness', agreeableness FROM users
                    UNION ALL
                    SELECT user_id, 'emotional_stability', emotional_stability FROM users
                    UNION ALL
                    SELECT user_id, 'conscientiousness', conscientiousness FROM users
                    UNION ALL
                    SELECT user_id, 'extraversion', extraversion FROM users
                ) p ON u.user_id = p.user_id
                GROUP BY g.genre, p.trait
            ),
            TopGenres AS (
                SELECT
                    personality_type,
                    genre,
                    pearson_coeff,
                    ROW_NUMBER() OVER (PARTITION BY personality_type ORDER BY pearson_coeff DESC) AS row_number
                FROM PearsonCoefficients
            )
            SELECT
                personality_type,
                genre,
                pearson_coeff
            FROM TopGenres;
            """,
            func=lambda row: row,
            db=Database.PERSONALITY,
        ),
        format_results,
    )
