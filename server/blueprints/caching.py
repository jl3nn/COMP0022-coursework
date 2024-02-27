from .common import cache, get_response
from flask import Blueprint, Response, jsonify, make_response

app = Blueprint("caching", __name__)


# Testing endpoint to flush the cache
@app.route("/flush", methods=["GET"])
def flush_cache() -> Response:
    cache.clear()
    return make_response(jsonify({"message": "Cache flushed"}), 200)


# Testing endpoint with a heavy query to check if the cache is working
@app.route("/test", methods=["GET"])
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
