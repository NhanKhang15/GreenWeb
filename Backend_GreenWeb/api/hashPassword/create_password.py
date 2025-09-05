import bcrypt
import sys
import os
import base64
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from database_Connection.db_connection_mysql import DatabaseConnection

def hash_and_update_passwords():
    try:
        # Kết nối database
        db = DatabaseConnection()

        # Lấy tất cả users từ database
        select_query = "SELECT UserID, Password FROM Users WHERE PasswordHashed IS NULL"
        db.cursor.execute(select_query)
        users = db.cursor.fetchall()

        # Hash từng mật khẩu và cập nhật vào database
        for user in users:
            user_id = user['UserID']
            plain_password = user['Password']
            
            # Hash mật khẩu và encode base64
            hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
            hashed_b64 = base64.b64encode(hashed_password).decode('utf-8')
            if not hashed_b64:
                continue
            
            # Cập nhật vào database
            update_query = "UPDATE Users SET PasswordHashed = %s WHERE UserID = %s"
            db.cursor.execute(update_query, (hashed_b64, user_id))

        # Commit các thay đổi
        db.conn.commit()
        return True

    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False
    finally:
        db.close()

