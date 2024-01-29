import blueprints
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin 
import psycopg
from flask import request
from prometheus_flask_exporter import PrometheusMetrics
from blueprints.connector import execute_query

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.register_blueprint(blueprints.autocomplete.app, url_prefix="/autocomplete")
CORS(app, origins="http://localhost")


@app.route("/get-search-results", methods=["POST"])
def get_search_results():
    try:
        data = request.get_json()
        searchText = data.get("searchText", "")
        ratings = data.get("ratings", [0, 10])
        tags = data.get("tags", [])
        genres = data.get("genres", [])
        date = data.get("date", [])

        # Initialize the query with the common part
        query = """
            SELECT
                m.image_url,
                m.title,
                AVG(r.rating),
                ARRAY_AGG(DISTINCT g.genre) AS genres,
                ARRAY_AGG(DISTINCT t.tag) AS tags,
                ARRAY_AGG(r.rating) FILTER (WHERE r.rating IS NOT NULL) AS ratings
            FROM movies m
            LEFT JOIN ratings r ON m.movie_id = r.movie_id
            LEFT JOIN movies_genres mg ON m.movie_id = mg.movie_id
            LEFT JOIN genres g ON mg.genre_id = g.genre_id
            LEFT JOIN tags t ON m.movie_id = t.movie_id
            WHERE 1=1
        """

        # Add conditions based on whether the values are set
        if searchText:
            query += " AND LOWER(m.title) LIKE LOWER(%(title)s)"
        if genres:
            query += " AND g.genre IN %(genres)s"
        if tags:
            query += " AND t.tag IN %(tags)s"

        query += """
            AND m.year BETWEEN %(yearstart)s AND %(yearend)s
            GROUP BY m.title, m.image_url
            HAVING AVG(r.rating) BETWEEN %(ratingstart)s AND %(ratingend)s
            ORDER BY AVG(r.rating) DESC
            LIMIT 15
        """

        # Prepare parameters
        params = {
            'title': f"%{searchText}%",
            'genres': tuple(genres),
            'tags': tuple(tags),
            'yearstart': date[0],
            'yearend': date[1],
            'ratingstart': ratings[0],
            'ratingend': ratings[1]
        }

        results = execute_query(query, params)

        result_data = [
            {
                "imageUrl": row[0],
                "title": row[1],
                "averageRating": row[2],
                "genres": row[3],
                "tags": row[4],
                "ratingsList": row[5]
            }
            for row in results
        ]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/movies/popular", methods=["GET"])
def get_popular_movies():
    try:
        result_data = [
            {
                "imageUrl": "https://resizing.flixster.com/dV1vfa4w_dB4wzk7A_VzThWUWw8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzEyZDMyYjZmLThmNzAtNDliNC1hMjFmLTA2ZWY4M2UyMjJhMi5qcGc=",
                "title": "Server is UP",
                "rating": 5,
                "genre": "Bar",
                "tags": ["bla"],
                "ratingsList": [1, 2, 3, 4, 5],
            }
            for _ in range(10)
        ]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/movies/contrevertial", methods=["GET"])
def get_controvertial_movies():
    try:
        result_data = [
            {
                "imageUrl": "https://resizing.flixster.com/dV1vfa4w_dB4wzk7A_VzThWUWw8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzEyZDMyYjZmLThmNzAtNDliNC1hMjFmLTA2ZWY4M2UyMjJhMi5qcGc=",
                "title": "Server is UP",
                "rating": 5,
                "genre": "Bar",
                "tags": ["bla"],
                "ratingsList": [1, 2, 3, 4, 5],
            }
            for _ in range(10)
        ]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/user-skew", methods=["POST"])
def calculate_users_skew():
    try:
        data = request.get_json()
        genres = data.get("genres")
        films = data.get("films")
        users = data.get("users")

        if users and (films or genres):
            skew_result = "higher"  # Replace with your actual skew calculation
            return jsonify(skew_result)
        else:
            return (
                jsonify(
                    {"error": "Please provide at least one user and one film or genre."}
                ),
                400,
            )

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/movie-pred", methods=["POST"])
def movie_prediction():
    try:
        data = request.get_json()
        tags = data.get("tags", [])
        users = data.get("users", [])
        ratings = data.get("ratings", [0, 10])
        if tags or users or ratings:
            rating = 4.37
            return jsonify(rating)
        else:
            return (
                jsonify(
                    {"error": "Please provide at least one user and one film or genre."}
                ),
                400,
            )

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/personality-skew", methods=["POST"])
def calculate_personalities_skew():
    try:
        data = request.get_json()
        genre = data.get("genre")
        metric = data.get("metric")
        metric_degree = data.get("metric_degree")
        openness = data.get("openness")
        agreeableness = data.get("agreeableness")
        emotional_stability = data.get("emotional_stability")
        conscientiousness = data.get("conscientiousness")
        extraversion = data.get("extraversion")

        if genre:
            skew_result = "higher"
            return jsonify(skew_result)
        else:
            return (
                jsonify(
                    {"error": "Please provide at least one user and one film or genre."}
                ),
                400,
            )

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
