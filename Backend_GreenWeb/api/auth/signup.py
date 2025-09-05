from flask import Blueprint, request, jsonify
import bcrypt
import base64
from database_Connection.db_connection_mysql import DatabaseConnection

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
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

        hashed_password = hash_password(password)
        db = DatabaseConnection()
        if not db.connect():
            return jsonify({
                'success': False,
                'message': 'Database connection error'
            }), 500
        try:
            check_query = "SELECT UserID FROM Users WHERE UserName = %s"
            db.cursor.execute(check_query, (username,))
            if db.cursor.fetchone():
                return jsonify({
                    'success': False,
                    'message': 'Username already exists'
                }), 400
            check_email_query = "SELECT UserID FROM Users WHERE Email = %s"
            db.cursor.execute(check_email_query, (email,))
            if db.cursor.fetchone():
                return jsonify({
                    'success': False,
                    'message': 'Email already exists'
                }), 400
            insert_query = """
            INSERT INTO Users (UserName, Email, Password, PasswordHashed) 
            VALUES (%s, %s, %s, %s)
            """
            db.cursor.execute(insert_query, (username, email, password, hashed_password))
            db.conn.commit()
            return jsonify({
                'success': True,
                'message': 'User registered successfully'
            })
        except Exception as e:
            print(f"❌ Lỗi khi lưu user: {str(e)}")
            return jsonify({
                'success': False,
                'message': 'Failed to register user'
            }), 500
        finally:
            db.close()
    except Exception as e:
        print(f"❌ Lỗi đăng ký: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
