from flask import Flask, jsonify
from flask_cors import CORS, cross_origin 
import psycopg2

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DATABASE_URL = "postgresql://admin:top_secret_password@localhost:5432/comp0022"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
@cross_origin()
def hello_world():
    query = "SELECT * FROM bla LIMIT 25;"
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
