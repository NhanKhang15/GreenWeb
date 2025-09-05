from flask import Blueprint, request, jsonify
import bcrypt
import base64
from database_Connection.db_connection_mysql import DatabaseConnection


login_bp = Blueprint('login', __name__)

def hash_password(password: str) -> str:
    # Trả về chuỗi '$2b$...'
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, stored_hash: str) -> bool:
    """
    Hỗ trợ cả 2 kiểu:
    1) Chuỗi bcrypt gốc: '$2a$' | '$2b$' | '$2y$'
    2) (Fallback) Chuỗi base64-encode của bcrypt bytes (nếu từng lỡ lưu kiểu này)
    """
    try:
        # Case 1: bcrypt gốc
        if stored_hash.startswith(('$2a$', '$2b$', '$2y$')):
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))

        # Case 2: thử decode base64 (cho dữ liệu cũ nếu có)
        try:
            decoded = base64.b64decode(stored_hash.encode('utf-8'), validate=True)
            return bcrypt.checkpw(password.encode('utf-8'), decoded)
        except Exception:
            # Không decode được → không đúng định dạng hash hợp lệ
            return False
    except Exception as e:
        print(f"❌ Lỗi verify password: {e}")
        return False
    
@login_bp.route('/login', methods=['POST'])
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
        db = DatabaseConnection()
        if not db.connect():
            return jsonify({
                'success': False,
                'message': 'Database connection error'
            }), 500
        try:
            select_query = "SELECT UserID, UserName, Email, PasswordHashed FROM Users WHERE UserName = %s"
            db.cursor.execute(select_query, (username,))
            user = db.cursor.fetchone()
            if not user:
                return jsonify({
                    'success': False,
                    'message': 'Invalid username or password'
                }), 401
            user_id = user['UserID']
            username_db = user['UserName']
            email = user['Email']
            hashed_password = user['PasswordHashed']
            if not hashed_password:
                return jsonify({
                    'success': False,
                    'message': 'Account needs to be updated. Please contact administrator.'
                }), 401
            if not verify_password(password, hashed_password):
                return jsonify({
                    'success': False,
                    'message': 'Invalid username or password'
                }), 401
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user_id,
                    'username': username_db,
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