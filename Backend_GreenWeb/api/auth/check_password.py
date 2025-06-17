from database_Connection.db_connection import DatabaseConnection
import base64
import bcrypt

def check_user_passwords():
    db = DatabaseConnection()
    if not db.connect():
        print("❌ Không thể kết nối database")
        return
    
    try:
        # Lấy tất cả users
        db.cursor.execute("SELECT UserID, UserName, Password, PasswordHashed FROM Users")
        users = db.cursor.fetchall()
        
        print("\n=== Kiểm tra mật khẩu trong database ===")
        for user in users:
            user_id, username, password, hashed = user
            print(f"\nUser: {username}")
            print(f"Password gốc: {password}")
            print(f"Password đã hash: {hashed}")
            
            if hashed:
                try:
                    # Thử decode base64
                    hashed_bytes = base64.b64decode(hashed.encode('utf-8'))
                    print("✅ Password hash có thể decode base64")
                except Exception as e:
                    print(f"❌ Lỗi decode base64: {str(e)}")
            else:
                print("❌ Chưa có password hash")
                
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    check_user_passwords() 