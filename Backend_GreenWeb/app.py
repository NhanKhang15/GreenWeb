from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import bcrypt
import base64

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from database_Connection.db_connection import DatabaseConnection

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def hash_password(password):
    """Hash a password using bcrypt and return as base64 string"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return base64.b64encode(hashed).decode('utf-8')

def verify_password(password, hashed_password_str):
    """Verify a password against a hashed password stored as base64 string"""
    try:
        hashed_bytes = base64.b64decode(hashed_password_str.encode('utf-8'))
        return bcrypt.checkpw(password.encode('utf-8'), hashed_bytes)
    except Exception as e:
        print(f"❌ Lỗi verify password: {str(e)}")
        return False

# Signup endpoint
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

        # Hash password trước khi lưu
        hashed_password = hash_password(password)

        # Kết nối database
        db = DatabaseConnection()
        if not db.connect():
            return jsonify({
                'success': False,
                'message': 'Database connection error'
            }), 500

        try:
            # Kiểm tra username đã tồn tại chưa
            check_query = "SELECT UserID FROM Users WHERE UserName = ?"
            db.cursor.execute(check_query, (username,))
            if db.cursor.fetchone():
                return jsonify({
                    'success': False,
                    'message': 'Username already exists'
                }), 400

            # Kiểm tra email đã tồn tại chưa
            check_email_query = "SELECT UserID FROM Users WHERE Email = ?"
            db.cursor.execute(check_email_query, (email,))
            if db.cursor.fetchone():
                return jsonify({
                    'success': False,
                    'message': 'Email already exists'
                }), 400

            # Lưu user với mật khẩu đã hash
            insert_query = """
            INSERT INTO Users (UserName, Email, Password, PasswordHashed) 
            VALUES (?, ?, ?, ?)
            """
            db.cursor.execute(insert_query, (username, email, password, hashed_password))
            db.conn.commit()

            print("✅ Đã đăng ký user thành công!")
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

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({
                'success': False,
                'message': 'Username and password are required'
            }), 400

        # Kết nối database
        db = DatabaseConnection()
        if not db.connect():
            return jsonify({
                'success': False,
                'message': 'Database connection error'
            }), 500

        try:
            # Tìm user trong database
            select_query = "SELECT UserID, UserName, Email, PasswordHashed FROM Users WHERE UserName = ?"
            db.cursor.execute(select_query, (username,))
            user = db.cursor.fetchone()

            if not user:
                return jsonify({
                    'success': False,
                    'message': 'Invalid username or password'
                }), 401

            # Lấy thông tin user
            user_id, username, email, hashed_password = user

            if not hashed_password:
                return jsonify({
                    'success': False,
                    'message': 'Account needs to be updated. Please contact administrator.'
                }), 401

            # Verify password với bcrypt
            if not verify_password(password, hashed_password):
                return jsonify({
                    'success': False,
                    'message': 'Invalid username or password'
                }), 401

            # Đăng nhập thành công
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user_id,
                    'username': username,
                    'email': email
                }
            })

        except Exception as e:
            print(f"❌ Lỗi khi xử lý đăng nhập: {str(e)}")
            return jsonify({
                'success': False,
                'message': 'An error occurred during login'
            }), 500
        finally:
            db.close()

    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'An error occurred'
        }), 500

if __name__ == '__main__':
    print("🚀 Server đang chạy tại http://localhost:8000")
    print("📝 Endpoints:")
    print("   - POST /api/signup - Đăng ký tài khoản")
    print("   - POST /api/login  - Đăng nhập")
    app.run(port=8000, debug=True) 