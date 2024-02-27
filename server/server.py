import blueprints
from flask import Flask, jsonify, request
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from blueprints.common import cache, execute_query, get_response

# Initialize Flask app
app = Flask(__name__)

# Initialize cache
cache.init_app(app)

# Register blueprints
app.register_blueprint(blueprints.caching.app, url_prefix="/caching")
app.register_blueprint(blueprints.autocomplete.app, url_prefix="/autocomplete")
app.register_blueprint(blueprints.genres.app, url_prefix="/genres")
app.register_blueprint(blueprints.movies.app, url_prefix="/movies")

# Initialize cross origin resource sharing
CORS(app, origins="http://localhost")

# Create a new Prometheus metrics export configuration
PrometheusMetrics(app)


@app.route("/get-movie", methods=["GET"])
def get_movie_details():
    try:
        movie_id = request.args.get("movieId")
        query = """
            select
                m.image_url,
                m.title,
                m.year,
                round(cast(avg(r.rating) as numeric), 1),
                array_agg(distinct g.genre) as genres,
                array_agg(distinct t.tag) as tags,
                array_agg(r.rating) filter (WHERE r.rating IS NOT NULL) as ratings,
                array_agg(distinct a.name) as actors,
                array_agg(distinct d.name) as directors
            from movies m
            left join movies_genres mg ON m.movie_id = mg.movie_id
            left join genres g ON mg.genre_id = g.genre_id
            left join movies_users_tags mut on m.movie_id = mut.movie_id
            left join tags t ON mut.tag_id = t.tag_id
            left join movies_actors ma on m.movie_id = ma.movie_id
            left join actors a on ma.actor_id = a.actor_id
            left join movies_directors md on m.movie_id = md.movie_id
            left join directors d on md.director_id = d.director_id
            left join ratings r on m.movie_id = r.movie_id
            where m.movie_id = %(movie_id)s
            group by m.title, m.image_url, m.year, m.movie_id
        """
        params = {"movie_id": movie_id}
        results = execute_query(query, params)

        result_data = [
            {
                "imageUrl": row[0],
                "title": row[1],
                "year": row[2],
                "rating": row[3],
                "genres": row[4],
                "tags": row[5],
                "ratingsList": row[6],
                "actors": row[7],
                "directors": row[8]
            }
            for row in results
        ]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get-search-results", methods=["POST"])
def get_search_results():
    try:
        data = request.get_json()
        searchText = data.get("searchText", "")
        ratings = data.get("ratings", [0, 10])
        tags = data.get("tags", [])
        genres = data.get("genres", [])
        date = data.get("date", [])
        num_loaded = data.get("numLoaded", 0)

        # Initialize the query with the common part
        query = """
            select
                m.image_url,
                m.title,
                m.year,
                round(cast(avg(r.rating) as numeric), 1),
                m.movie_id
            from movies m
            left join ratings r on m.movie_id = r.movie_id
        """

        if searchText:
            query += """
            left join movies_actors ma on m.movie_id = ma.movie_id
            left join actors a on ma.actor_id = a.actor_id
            left join movies_directors md on m.movie_id = md.movie_id
            left join directors d on md.director_id = d.director_id"""

        if genres:
            query += """
            left join movies_genres mg on m.movie_id = mg.movie_id
            left join genres g on mg.genre_id = g.genre_id"""

        if tags:
            query += """
            left join tags t on m.movie_id = t.movie_id"""

        
        query += " where 1=1"

        if searchText:
            query += " and (LOWER(m.title) like lower(%(search)s) or lower(a.name) like lower(%(search)s) or lower(d.name) like lower(%(search)s))"

        if genres:
            # Adjust to use ANY with an array for genres
            query += " and g.genre = any(%(genres)s)"

        if tags:
            query += " and t.tag = any(%(tags)s)"

        # Ensure the rest of your query uses named placeholders consistently
        query += """
            and m.year between %(yearstart)s and %(yearend)s
            group by m.title, m.image_url, m.year, m.movie_id
            """
        if ratings[0] != 0 or ratings[1] != 5:
            query += """having avg(r.rating) between %(ratingstart)s and %(ratingend)s"""
        query += """
            order by count(r.rating), avg(r.rating) desc
            offset %(num_loaded)s
            limit 15
        """

        # Prepare parameters
        params = {
            'search': f"%{searchText}%",
            'genres': genres,
            'tags': tags,
            'yearstart': date[0],
            'yearend': date[1],
            'ratingstart': ratings[0],
            'ratingend': ratings[1],
            'num_loaded': num_loaded
        }

        results = get_response(query, params, lambda row: {
                "imageUrl": row[0],
                "title": row[1],
                "year": row[2],
                "rating": row[3],
                "movieId": row[4]
            })

        result_data = {'all_loaded': len(results.get_json()) < 15
                       , 'results': results.get_json()}
        return jsonify(result_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/movie-pred", methods=["POST"])
def movie_prediction():
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
