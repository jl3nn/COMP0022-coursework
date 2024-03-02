from .common import cache, get_response
from flask import Blueprint, Response, jsonify, make_response
from flasgger import swag_from

app = Blueprint("caching", __name__)


@app.route("/flush", methods=["GET"])
@swag_from({
    'tags': ['Cache Management'],
    'description': 'Clears the application cache, flushing all stored data.',
    'responses': {
        200: {
            'description': 'Confirmation message that the cache has been flushed.',
            'examples': {
                'application/json': {"message": "Cache flushed"}
            }
        }
    }
})
def flush_cache() -> Response:
    cache.clear()
    return make_response(jsonify({"message": "Cache flushed"}), 200)


@app.route("/test", methods=["GET"])
@swag_from({
    'tags': ['Testing'],
    'description': 'A test endpoint to fetch a limited set of movie data for testing database connection and query execution.',
    'responses': {
        200: {
            'description': 'A limited list of movie data including various attributes such as image URL, title, year, average rating, genres, tags, ratings, actors, and directors.',
            'examples': {
                'application/json': [
                    {
                        "imageUrl": "http://example.com/image.jpg",
                        "title": "Inception",
                        "year": 2010,
                        "rating": 8.8,
                        "genres": ["Action", "Adventure", "Sci-Fi"],
                        "tags": ["mind-bending", "dream", "subconscious"],
                        "ratings": [9, 8, 10, 7],
                        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
                        "directors": ["Christopher Nolan"]
                    }
                ]
            }
        }
    }
})
def test() -> Response:
    return get_response(
        """
        SELECT
            m.image_url,
            m.title,
            m.year,
            ROUND(AVG(r.rating)::NUMERIC, 1),
            ARRAY_AGG(DISTINCT g.genre) AS genres,
            ARRAY_AGG(DISTINCT t.tag) AS tags,
            ARRAY_AGG(r.rating) AS ratings,
            ARRAY_AGG(DISTINCT a.name) AS actors,
            ARRAY_AGG(DISTINCT d.name) AS directors
        FROM
            movies m
        LEFT JOIN
            movies_genres mg ON m.movie_id = mg.movie_id
        LEFT JOIN
            genres g ON mg.genre_id = g.genre_id
        LEFT JOIN
            movies_users_tags mut ON m.movie_id = mut.movie_id
        LEFT JOIN
            tags t ON mut.tag_id = t.tag_id
        LEFT JOIN
            movies_actors ma ON m.movie_id = ma.movie_id
        LEFT JOIN
            actors a ON ma.actor_id = a.actor_id
        LEFT JOIN
            movies_directors md ON m.movie_id = md.movie_id
        LEFT JOIN
            directors d ON md.director_id = d.director_id
        LEFT JOIN
            ratings r ON m.movie_id = r.movie_id
        GROUP BY
            m.movie_id,
            m.image_url,
            m.title,
            m.year
        LIMIT
            200
        ;
        """
    )
