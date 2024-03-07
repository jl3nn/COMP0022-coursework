from .common import get_response
from flasgger import swag_from
from flask import Blueprint, Response, request

app = Blueprint("users", __name__)


@app.route("/for-prediction", methods=["POST"])
@swag_from(
    {
        "tags": ["Prediction"],
        "description": "Retrieves a list of user IDs for users who have rated a specific movie, limited to the top 5 users.",
        "parameters": [
            {
                "in": "body",
                "name": "body",
                "description": "Parameters for the search query.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "movie": {
                            "type": "string",
                            "description": "The title of the movie to query user ratings for.",
                        },
                    },
                },
            }
        ],
        "responses": {
            200: {
                "description": "A list of user IDs who have rated the specified movie",
                "examples": {"application/json": {"user_ids": [1, 2, 3, 4, 5]}},
            }
        },
    }
)
def get_users_for_prediction() -> Response:
    return get_response(
        """
        SELECT
            r.user_id
        FROM
            ratings r
        INNER JOIN
            movies m ON r.movie_id = m.movie_id
        WHERE
            m.title = %(movie)s
        GROUP BY
            r.user_id
        LIMIT
            10
        ;
        """,
        params={"movie": request.json.get("movie", "")},
    )
