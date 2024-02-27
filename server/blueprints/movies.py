from .common import get_response, transform_response
from flask import Blueprint, Response, request

app = Blueprint("movies", __name__)


def get_movies_by_user_preference(
    min_rating: int = 0, max_rating: int = 5, precision: int = 3
) -> Response:
    return get_response(
        f"""
        WITH relevant_users AS (
            SELECT
                DISTINCT r.user_id
            FROM
                ratings r
            INNER JOIN
                movies m ON r.movie_id = m.movie_id
            WHERE
                m.title = %(movie)s
            GROUP BY
                r.user_id
            HAVING
                AVG(r.rating) BETWEEN {min_rating} AND {max_rating}
        )
        
        SELECT
            m.title,
            ROUND(AVG(r.rating)::NUMERIC, {precision}) AS avg_rating
        FROM
            ratings r
        INNER JOIN
            movies m ON r.movie_id = m.movie_id
        WHERE
            r.user_id IN (SELECT user_id FROM relevant_users)
            AND m.title != %(movie)s
        GROUP BY
            m.title
        ORDER BY
            avg_rating DESC
        ;
        """,
        params={"movie": request.json.get("movie", "")},
        func=lambda row: {"id": row[0], "avg_rating": row[1]},
    )


@app.route("/get-by-id", methods=["GET"])
def get_by_id() -> Response:
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
        INNER JOIN
            movies_genres mg ON m.movie_id = mg.movie_id
        INNER JOIN
            genres g ON mg.genre_id = g.genre_id
        INNER JOIN
            movies_users_tags mut ON m.movie_id = mut.movie_id
        INNER JOIN
            tags t ON mut.tag_id = t.tag_id
        INNER JOIN
            movies_actors ma ON m.movie_id = ma.movie_id
        INNER JOIN
            actors a ON ma.actor_id = a.actor_id
        INNER JOIN
            movies_directors md ON m.movie_id = md.movie_id
        INNER JOIN
            directors d ON md.director_id = d.director_id
        INNER JOIN
            ratings r ON m.movie_id = r.movie_id
        WHERE
            m.movie_id = %(movie_id)s
        GROUP BY
            m.movie_id,
            m.image_url,
            m.title,
            m.year
        ;
        """,
        params={"movie_id": request.args.get("movieId")},
        func=lambda row: {
            "imageUrl": row[0],
            "title": row[1],
            "year": row[2],
            "rating": row[3],
            "genres": row[4],
            "tags": row[5],
            "ratingsList": row[6],
            "actors": row[7],
            "directors": row[8],
        },
    )


@app.route("/get-search-results", methods=["POST"])
def get_search_results() -> Response:
    search_text = request.json.get("searchText", "")
    ratings = request.json.get("ratings", [0, 10])
    tags = request.json.get("tags", [])
    genres = request.json.get("genres", [])
    date = request.json.get("date", [])
    num_loaded = request.json.get("numLoaded", 0)

    query = """
        SELECT
            m.image_url,
            m.title,
            m.year,
            ROUND(AVG(r.rating)::NUMERIC, 1) as avg_rating,
            m.movie_id
        FROM
            movies m
        INNER JOIN
            ratings r ON m.movie_id = r.movie_id
    """

    if search_text:
        query += """
            INNER JOIN
                movies_actors ma ON m.movie_id = ma.movie_id
            INNER JOIN
                actors a ON ma.actor_id = a.actor_id
            INNER JOIN
                movies_directors md ON m.movie_id = md.movie_id
            INNER JOIN
                directors d ON md.director_id = d.director_id
        """

    if genres:
        query += """
            INNER JOIN
                movies_genres mg ON m.movie_id = mg.movie_id
            INNER JOIN
                genres g ON mg.genre_id = g.genre_id
        """

    if tags:
        query += """
            INNER JOIN
                movies_users_tags mut ON m.movie_id = mut.movie_id
            INNER JOIN
                tags t ON mut.tag_id = t.tag_id
        """

    query += """
        WHERE
            1=1
    """

    if search_text:
        query += """
                AND (
                    LOWER(m.title) LIKE LOWER(%(search)s)
                    OR LOWER(a.name) LIKE LOWER(%(search)s)
                    OR LOWER(d.name) LIKE LOWER(%(search)s)
                )
        """

    if genres:
        query += """
                AND g.genre = ANY(%(genres)s)
        """

    if tags:
        query += """
                AND t.tag = ANY(%(tags)s)
        """

    query += """
            AND m.year between %(year_start)s and %(year_end)s
        GROUP BY
            m.movie_id,
            m.image_url,
            m.title,
            m.year
    """

    if ratings[0] != 0 or ratings[1] != 5:
        query += """
            HAVING
                AVG(r.rating) BETWEEN %(rating_start)s AND %(rating_end)s
        """

    query += """
        ORDER BY
            COUNT(r.rating) DESC,
            avg_rating DESC
        OFFSET
            %(num_loaded)s
        LIMIT
            15
        ;
    """

    return transform_response(
        get_response(
            query,
            params={
                "search": f"%{search_text}%",
                "genres": genres,
                "tags": tags,
                "year_start": date[0],
                "year_end": date[1],
                "rating_start": ratings[0],
                "rating_end": ratings[1],
                "num_loaded": num_loaded,
            },
            func=lambda row: {
                "imageUrl": row[0],
                "title": row[1],
                "year": row[2],
                "rating": row[3],
                "movieId": row[4],
            },
        ),
        lambda results: {"all_loaded": len(results) < 15, "results": results},
    )


@app.route("/user-preferences", methods=["POST"])
def get_user_preferences() -> Response:
    opinion = request.json.get("opinion", 0)

    if opinion == 1:
        return get_movies_by_user_preference(4, 5)

    if opinion == 2:
        return get_movies_by_user_preference(0, 2)

    return get_movies_by_user_preference(2, 4)
