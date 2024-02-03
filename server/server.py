import blueprints
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin 
import psycopg
from flask import request
from prometheus_flask_exporter import PrometheusMetrics

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


@app.route("/movies/popular", methods=["GET"])
def get_popular_movies():
    try:
        result_data = [
            'Some Genre'
            for _ in range(10)
        ]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/movies/contrevertial", methods=["GET"])
def get_controvertial_movies():
    try:
        result_data = [
            'Some Other Genre'
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
        opinion = data.get("opinion")

        if opinion and (films or genres):
            better = ['Genre 1', 'Genre 2', 'Genre 3']
            worse = ['Genre 4', 'Genre 5', 'Genre 6']
            return jsonify({"better": better, "worse": worse})
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
        movie = data.get("movie", '')
        users = data.get("users", [])
        if users and movie:
            rating = 4.37
            return jsonify(rating)
        else:
            return (
                jsonify(
                    {"error": "Please provide at least one user and a movie."}
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
