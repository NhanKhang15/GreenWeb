from Backend_GreenWeb.database_Connection.db_connection_mysql import DatabaseConnection
import base64
import bcrypt

def check_user_passwords():
    db = DatabaseConnection()
    try:
        # Lấy tất cả users
        db.cursor.execute("SELECT UserID, UserName, Password, PasswordHashed FROM Users")
        users = db.cursor.fetchall()
        
        for user in users:
            user_id = user['UserID']
            username = user['UserName']
            password = user['Password']
            hashed = user['PasswordHashed']
            print(f"User: {username}")
            if hashed:
                try:
                    hashed_bytes = base64.b64decode(hashed.encode('utf-8'))
                    print("  -> Hash hợp lệ base64")
                except Exception as e:
                    print(f"  -> Hash lỗi: {str(e)}")
            else:
                print("  -> Chưa có password hash")
                
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
    finally:
        db.close()
