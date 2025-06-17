from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(root_dir)

from Backend_GreenWeb.database_Connection.db_connection import DatabaseConnection

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({
                'success': False,
                'message': 'Missing required fields'
            }), 400

        db = DatabaseConnection()
        if db.save_user(username, email, password):
            return jsonify({
                'success': True,
                'message': 'User registered successfully'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to register user'
            }), 500

    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True) 