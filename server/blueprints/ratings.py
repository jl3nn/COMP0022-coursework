from .common import get_response
from flask import Blueprint, Response, request

app = Blueprint("ratings", __name__)


@app.route("/prediction", methods=["POST"])
def get_prediction():
    try:
        data = request.get_json()
        movie = data.get("movie", "")
        users = data.get("users", [])
        if users and movie:
            rating = 4.37
            return jsonify(rating)
        else:
            return (
                jsonify({"error": "Please provide at least one user and a movie."}),
                400,
            )
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
