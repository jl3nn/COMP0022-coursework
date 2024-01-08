from flask import Flask, jsonify
from flask_cors import CORS, cross_origin 
import psycopg2

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

@app.route('/ratings')
@cross_origin()
def get_ratings():
    query = "SELECT * FROM ratings LIMIT 5;"
    result = execute_query(query)
    result = [{'userId': row[0], 'movieId': row[1], 'rating': row[2], 'timestamp': row[3]} for row in result]
    return jsonify(result)

@app.route('/tags')
@cross_origin()
def get_tags():
    query = "SELECT * FROM tags LIMIT 5;"
    result = execute_query(query)
    result = [{'userId': row[0], 'movieId': row[1], 'tag': row[2], 'timestamp': row[3]} for row in result]
    return jsonify(result)

@app.route('/movies')
@cross_origin()
def get_movies():
    query = "SELECT * FROM movies LIMIT 5;"
    result = execute_query(query)
    result = [{'movieId': row[0], 'title': row[1], 'genres': row[2]} for row in result]
    return jsonify(result)

@app.route('/links')
@cross_origin()
def get_links():
    query = "SELECT * FROM links LIMIT 5;"
    result = execute_query(query)
    result = [{'movieId': row[0], 'imdbId': row[1], 'tmdbId': row[2]} for row in result]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
