from collections import defaultdict
import blueprints
from flask import Flask, jsonify, request
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask app
app = Flask(__name__)

# Initialize cache
blueprints.common.cache.init_app(app)

# Register blueprints
app.register_blueprint(blueprints.autocomplete.app, url_prefix="/autocomplete")
app.register_blueprint(blueprints.caching.app, url_prefix="/caching")
app.register_blueprint(blueprints.genres.app, url_prefix="/genres")
app.register_blueprint(blueprints.movies.app, url_prefix="/movies")
app.register_blueprint(blueprints.ratings.app, url_prefix="/ratings")

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


@app.route("/personality-skew", methods=["GET"])
def calculate_personalities_skew():
    try:
        query = """
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
        FROM TopGenres
        """

        params = {}

        results = execute_query(query, params, conn_name="personality")

        personality_genres = defaultdict(list)
        for personality_type, genre, pearson_coeff in results:
            personality_genres[personality_type].append((genre, float(pearson_coeff)))

        formatted_result = {}
        for personality, genres in personality_genres.items():
            sorted_genres = sorted(genres, key=lambda x: x[1], reverse=True)
            genres_list, coeffs_list = zip(*sorted_genres)
            formatted_result[personality] = {'x': list(genres_list), 'y': list(coeffs_list)}

        return jsonify(formatted_result)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
