from .common import concat_responses, get_response
from flask import Blueprint, request, Response
from flasgger import swag_from

app = Blueprint("autocomplete", __name__)


def autocomplete(field: str, table: str, limit: int = 5) -> Response:
    return get_response(
        f"""
        SELECT
            DISTINCT {field}
        FROM
            {table}
        WHERE
            LOWER({field}::TEXT) LIKE %(prefix)s
        LIMIT
            {limit}
        ;
        """,
        params={"prefix": request.args.get("prefix", "").lower() + "%"},
    )


@app.route("/genre", methods=["GET"])
@swag_from({
    'tags': ['Autocomplete'],
    'description': 'Autocomplete endpoint for genre names based on a search query.',
    'parameters': [
        {
            'name': 'prefix',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The search prefix for autocomplete.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of genres matching the search query.',
            'examples': {'application/json': ["Comedy", "Drama", "Action"]}
        }
    }
})
def autocomplete_genre() -> Response:
    return autocomplete("genre", "genres")


@app.route("/tag", methods=["GET"])
@swag_from({
    'tags': ['Autocomplete'],
    'description': 'Autocomplete endpoint for tag names based on a search query.',
    'parameters': [
        {
            'name': 'prefix',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The search prefix for autocomplete.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of tags matching the search query.',
            'examples': {'application/json': ["mind-bending", "dream", "subconscious"]}
        }
    }
})
def autocomplete_tag() -> Response:
    return autocomplete("tag", "tags")


@app.route("/movie", methods=["GET"])
@swag_from({
    'tags': ['Autocomplete'],
    'description': 'Autocomplete endpoint for movie titles based on a search query.',
    'parameters': [
        {
            'name': 'prefix',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The search prefix for autocomplete.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of movie titles matching the search query.',
            'examples': {'application/json': ["Inception", "The Matrix", "Interstellar"]}
        }
    }
})
def autocomplete_movie() -> Response:
    return autocomplete("title", "movies")


@app.route("/user", methods=["GET"])
@swag_from({
    'tags': ['Autocomplete'],
    'description': 'Autocomplete endpoint for user IDs based on a search query.',
    'parameters': [
        {
            'name': 'prefix',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The search prefix for autocomplete.'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of user IDs matching the search query.',
            'examples': {'application/json': [1, 2, 3]}
        }
    }
})
def autocomplete_user() -> Response:
    return autocomplete("user_id", "users")


@app.route("/search", methods=["GET"])
@swag_from({
    'tags': ['Autocomplete'],
    'description': 'Combined autocomplete endpoint for movies, actors, and directors based on a search query.',
    'parameters': [
        {
            'name': 'prefix',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The search prefix for autocomplete.'
        }
    ],
    'responses': {
        200: {
            'description': 'A combined list of movies, actors, and directors matching the search query.',
            'examples': {'application/json': {"movies": ["Inception"], "actors": ["Leonardo DiCaprio"], "directors": ["Christopher Nolan"]}}
        }
    }
})
def autocomplete_search() -> Response:
    return concat_responses(
        [
            autocomplete("title", "movies", 3),
            autocomplete("name", "actors", 3),
            autocomplete("name", "directors", 3),
        ]
    )
