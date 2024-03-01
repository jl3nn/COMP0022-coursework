from .common import get_response
from flask import Blueprint, Response, request

app = Blueprint("users", __name__)


@app.route("/for-prediction", methods=["POST"])
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
