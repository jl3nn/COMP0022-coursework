import blueprints
from flask import Flask, jsonify, request
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(blueprints.autocomplete.app, url_prefix="/autocomplete")
app.register_blueprint(blueprints.genres.app, url_prefix="/genres")
app.register_blueprint(blueprints.movies.app, url_prefix="/movies")

# Initialize cross origin resource sharing
CORS(app, origins="http://localhost")

# Create a new Prometheus metrics export configuration
PrometheusMetrics(app)


@app.route("/user-skew", methods=["POST"])
def calculate_users_skew():
    try:
        data = request.get_json()
        genres = data.get("genres")
        films = data.get("films")
        opinion = data.get("opinion")

        if opinion and (films or genres):
            better = ["Genre 1", "Genre 2", "Genre 3"]
            worse = ["Genre 4", "Genre 5", "Genre 6"]
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
