from .connector import execute_query
from flask import Blueprint, jsonify, request, Response

app = Blueprint("autocomplete", __name__)


@app.route("/genre", methods=["GET"])
def autocomplete_genre():
    sample_genres = ["Action", "Comedy", "Drama", "Horror", "Science Fiction"]
    try:
        # limit to five and replace with a sql query
        prefix = request.args.get("prefix", "").lower()
        matches = [genre for genre in sample_genres if genre.lower().startswith(prefix)]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/tag", methods=["GET"])
def autocomplete_tag() -> Response:
    try:
        results = execute_query(
            "SELECT DISTINCT tag FROM tags WHERE LOWER(tag) LIKE %(prefix)s LIMIT 5",
            {"prefix": request.args.get("prefix", "").lower() + "%"},
        )

        tags = list(map(lambda row: row[0], results))
        return jsonify(tags)
    except Exception as e:
        print(f"[autocomplete_tag] error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/movie", methods=["GET"])
def autocomplete_movie() -> Response:
    try:
        results = execute_query(
            "SELECT DISTINCT title FROM movies WHERE LOWER(title) LIKE %(prefix)s LIMIT 5",
            {"prefix": request.args.get("prefix", "").lower() + "%"},
        )

        films = list(map(lambda row: row[0], results))
        return jsonify(films)
    except Exception as e:
        print(f"[autocomplete_movie] error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/user", methods=["GET"])
def autocomplete_user():
    # Replace this with actual data retrieval logic from your database
    sample_users = ["User1", "User2", "User3", "User4", "User5"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [user for user in sample_users if user.lower().startswith(prefix)]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/metric-degree", methods=["GET"])
def autocomplete_metric_degree():
    sample_personalities = ["low", "med", "high"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [
            user for user in sample_personalities if user.lower().startswith(prefix)
        ]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/metric", methods=["GET"])
def autocomplete_metric():
    sample_personalities = ["serendipity", "popularity", "diversity"]
    try:
        prefix = request.args.get("prefix", "").lower()
        matches = [
            user for user in sample_personalities if user.lower().startswith(prefix)
        ]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
