from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = 'portfolio.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/projects', methods=['GET'])
def get_projects():
    if not os.path.exists(DB_PATH):
        return jsonify([])
    
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    
    return jsonify([dict(ix) for ix in projects])

@app.route('/api/projects/categories', methods=['GET'])
def get_categories():
    if not os.path.exists(DB_PATH):
        return jsonify([])
    
    conn = get_db_connection()
    categories = conn.execute('SELECT DISTINCT category FROM projects').fetchall()
    conn.close()
    
    return jsonify([row['category'] for row in categories])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
