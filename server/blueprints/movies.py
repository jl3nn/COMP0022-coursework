from .common import get_response, transform_response
from flask import Blueprint, Response, request
from flasgger import swag_from

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
        INNER JOIN
            relevant_users ru ON r.user_id = ru.user_id
        WHERE
            m.title != %(movie)s
        GROUP BY
            m.title
        ORDER BY
            avg_rating DESC,
            COUNT(r.rating) DESC
        ;
        """,
        params={"movie": request.json.get("movie", "")},
        func=lambda row: {"id": row[0], "avg_rating": row[1]},
    )


@app.route("/get-by-id", methods=["GET"])
@swag_from({
    'tags': ['Movie Details'],
    'description': 'Retrieves detailed information for a specific movie by its ID.',
    'parameters': [
        {
            'name': 'movieId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the movie to retrieve details for.'
        }
    ],
    'responses': {
        200: {
            'description': 'Detailed information about the specified movie, including image URL, title, year, average rating, genres, tags, individual ratings, actors, and directors.',
            'examples': {
                'application/json': {
                    "imageUrl": "http://example.com/image.jpg",
                    "title": "Inception",
                    "year": 2010,
                    "rating": 8.8,
                    "genres": ["Action", "Adventure", "Sci-Fi"],
                    "tags": ["mind-bending", "dream", "subconscious"],
                    "ratingsList": [9, 8, 10, 7],
                    "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
                    "directors": ["Christopher Nolan"]
                }
            }
        }
    }
})
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
@swag_from({
    'tags': ['Search'],
    'description': 'Performs a search query on movies database based on various filters like text, ratings, tags, genres, and date range. Returns a list of movies that match the criteria.',
    'consumes': ['application/json'],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'description': 'Parameters for the search query.',
            'schema': {
                'type': 'object',
                'properties': {
                        'searchText': {
                            'type': 'string',
                            'description': 'Text to search for in movie titles, actor names, and director names.'
                        },
                        'ratings': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            },
                            'description': 'Array containing minimum and maximum ratings to filter by.'
                        },
                        'tags': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            },
                            'description': 'List of tags to filter movies by.'
                        },
                        'genres': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            },
                            'description': 'List of genres to filter movies by.'
                        },
                        'date': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            },
                            'description': 'Array containing start and end years to filter movies by their release date.'
                        },
                        'numLoaded': {
                            'type': 'integer',
                            'description': 'Number of movies already loaded, used for pagination.'
                        }
                    }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'A list of movies that match the search criteria, along with a flag indicating if all movies have been loaded.',
            'examples': {
                'application/json': {
                    "all_loaded": False,
                    "results": [
                        {
                            "imageUrl": "http://example.com/image.jpg",
                            "title": "Inception",
                            "year": 2010,
                            "rating": 8.8,
                            "movieId": 1
                        },
                        {
                            "imageUrl": "http://anotherexample.com/image.jpg",
                            "title": "The Matrix",
                            "year": 1999,
                            "rating": 9.0,
                            "movieId": 2
                        }
                    ]
                }
            }
        }
    }
}
)
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
        LEFT JOIN
            ratings r ON m.movie_id = r.movie_id
    """

    if search_text:
        query += """
            LEFT JOIN
                movies_actors ma ON m.movie_id = ma.movie_id
            LEFT JOIN
                actors a ON ma.actor_id = a.actor_id
            LEFT JOIN
                movies_directors md ON m.movie_id = md.movie_id
            LEFT JOIN
                directors d ON md.director_id = d.director_id
        """

    if genres:
        query += """
            LEFT JOIN
                movies_genres mg ON m.movie_id = mg.movie_id
            LEFT JOIN
                genres g ON mg.genre_id = g.genre_id
        """

    if tags:
        query += """
            LEFT JOIN
                movies_users_tags mut ON m.movie_id = mut.movie_id
            LEFT JOIN
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
        func=lambda results: {"all_loaded": len(results) < 15, "results": results},
    )


@app.route("/user-preferences", methods=["POST"])
@swag_from({
    'tags': ['User Preferences'],
    'description': 'Retrieves movies based on user preference indicated by the opinion value. Opinion values correspond to different rating preferences.',
    'parameters': [
        {
            'name': 'opinion',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'opinion': {
                        'type': 'integer',
                        'description': 'User opinion indicating preference. 1 for high-rated (4 to 5), 2 for low-rated (0 to 2), any other value for mid-range rated (2 to 4) movies.'
                    }
                },
                'required': ['opinion'],
                'example': {'opinion': 1}
            },
            'required': True,
            'description': 'JSON payload containing the user opinion on movie ratings.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of movies filtered by user preference based on the opinion provided.',
            'examples': {
                'application/json': [
                    {
                        "movieId": 1,
                        "title": "Highly Rated Movie",
                        "rating": 4.5
                    },
                    {
                        "movieId": 2,
                        "title": "Another Highly Rated Movie",
                        "rating": 4.7
                    }
                ]
            }
        }
    }
})
def get_user_preferences() -> Response:
    opinion = request.json.get("opinion", 0)

    if opinion == 1:
        return get_movies_by_user_preference(4, 5)

    if opinion == 2:
        return get_movies_by_user_preference(0, 2)

    return get_movies_by_user_preference(2, 4)
