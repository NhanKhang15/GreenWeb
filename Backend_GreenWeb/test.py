import base64
import bcrypt
from database_Connection.db_connection_mysql import DatabaseConnection

def is_base64(s):
    try:
        if not s or not isinstance(s, str):
            return False
        base64.b64decode(s.encode('utf-8'))
        return True
    except Exception:
        return False

def verify_password(plain_password, hashed_b64):
    try:
        hashed_bytes = base64.b64decode(hashed_b64.encode('utf-8'))
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_bytes)
    except Exception as e:
        print("Lỗi verify password:", e)
        return False

def main():
    # 1. Kết nối DB
    db = DatabaseConnection()
    if not db.connect():
        print("Kết nối DB thất bại")
        return

    cursor = db.cursor
    try:
        cursor.execute("SELECT UserID, PasswordHashed FROM Users")
        users = cursor.fetchall()
    except Exception as e:
        print("Lỗi khi truy vấn:", e)
        return
    finally:
        cursor.close()
        db.close()

    # 3. Xử lý dữ liệu
    for user in users:
        print(f"UserID: {user['UserID']}, Hash: {user['PasswordHashed']}")
        if not is_base64(user['PasswordHashed']):
            print(f"UserID {user['UserID']} có hash không hợp lệ")

    # 4. Test verify với password nhập từ input
    if users:
        test_pass = input("Nhập password để test verify với user đầu tiên: ")
        ok = verify_password(test_pass, users[0]['PasswordHashed'])
        print("Verify:", ok)

if __name__ == "__main__":
    main()
