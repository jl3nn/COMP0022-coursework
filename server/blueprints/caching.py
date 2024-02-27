from flask import Blueprint, Response, request, jsonify
from .common import cache, get_response

app = Blueprint("caching", __name__)


# Testing endpoint to flush the cache
@app.route("/flush", methods=["GET"])
def flush_cache():
    cache.clear()
    return jsonify({"message": "Cache flushed"})


# Testing endpoint with a heavy query to check if the cache is working
@app.route("/test", methods=["GET"])
def test():
    return get_response(f"""
         select
                m.image_url,
                m.title,
                m.year,
                avg(r.rating),
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
            group by m.title, m.image_url, m.year, m.movie_id
            limit 200
    """)
