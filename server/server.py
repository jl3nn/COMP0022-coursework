from flask import Flask, jsonify
from flask_cors import CORS, cross_origin 
import psycopg2
from flask import request

app = Flask(__name__)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db_params = {
    'dbname': 'comp0022',
    'user': 'admin',
    'password': 'top_secret_password',
    'host': 'database',
    'port': '5432'
}

def execute_query(query):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/")
@cross_origin()
def hello_world():
    return 'Hello, World!'

@cross_origin()
@app.route('/get-search-results', methods=['POST'])
def get_search_results():
    try:
        data = request.get_json()
        searchText = data.get('searchText', '')
        ratings = data.get('ratings', [0, 10])
        tags = data.get('tags', [])
        genres = data.get('genres', [])
        # Mock data for testing purposes
        result_data = [{
            'imageUrl': 'https://resizing.flixster.com/dV1vfa4w_dB4wzk7A_VzThWUWw8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzEyZDMyYjZmLThmNzAtNDliNC1hMjFmLTA2ZWY4M2UyMjJhMi5qcGc=',
            'title': 'Server is UP',
            'rating': 5,
            'genre': 'Bar',
            'tags': ['bla'],
            'ratingsList': [1, 2, 3, 4, 5]
        }]
        return jsonify(result_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cross_origin()
@app.route('/genre-autocomplete', methods=['GET'])
def genre_autocomplete():
    sample_genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Science Fiction']
    try:
        # limit to five and replace with a sql query
        prefix = request.args.get('prefix', '').lower()
        matches = [genre for genre in sample_genres if genre.lower().startswith(prefix)]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@cross_origin()
@app.route('/tags-autocomplete', methods=['GET'])
def tags_autocomplete():
    # limit to five and replace with a sql query
    sample_tags = ['Adventure', 'Romance', 'Thriller', 'Fantasy', 'Mystery']
    try:
        prefix = request.args.get('prefix', '').lower()
        matches = [tag for tag in sample_tags if tag.lower().startswith(prefix)]
        return jsonify(matches)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
