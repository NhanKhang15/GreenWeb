from database_Connection.db_connection import DatabaseConnection
import bcrypt
import base64

def update_user_password(username, new_password):
    # Hash mật khẩu mới
    hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    hashed_str = base64.b64encode(hashed).decode('utf-8')
    
    db = DatabaseConnection()
    if not db.connect():
        print("❌ Không thể kết nối database")
        return False
    
    try:
        # Cập nhật mật khẩu
        update_query = """
        UPDATE Users 
        SET Password = ?, PasswordHashed = ? 
        WHERE UserName = ?
        """
        db.cursor.execute(update_query, (new_password, hashed_str, username))
        db.conn.commit()
        print(f"✅ Đã cập nhật mật khẩu cho user {username}")
        return True
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    # Cập nhật mật khẩu cho user admin
    update_user_password("admin", "1234567") 