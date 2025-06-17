import bcrypt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from database_Connection.db_connection import DatabaseConnection

def hash_and_update_passwords():
    try:
        # Kết nối database
        db = DatabaseConnection()
        if not db.connect():
            print("❌ Không thể kết nối đến database")
            return False

        # Lấy tất cả users từ database
        select_query = "SELECT UserID, Password FROM Users WHERE PasswordHashed IS NULL"
        db.cursor.execute(select_query)
        users = db.cursor.fetchall()

        if not users:
            print("✅ Không có mật khẩu nào cần hash")
            return True

        # Hash từng mật khẩu và cập nhật vào database
        for user in users:
            user_id = user[0]
            plain_password = user[1]
            
            # Hash mật khẩu
            hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
            
            # Cập nhật vào database
            update_query = "UPDATE Users SET PasswordHashed = ? WHERE UserID = ?"
            db.cursor.execute(update_query, (hashed_password, user_id))
            
            print(f"✅ Đã hash mật khẩu cho user ID: {user_id}")

        # Commit các thay đổi
        db.conn.commit()
        print("✅ Đã cập nhật tất cả mật khẩu đã hash vào database")
        return True

    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False
    finally:
        db.close()

if __name__ == '__main__':
    # Thực hiện hash và cập nhật mật khẩu
    hash_and_update_passwords() 