import pyodbc

class DatabaseConnection:
    def __init__(self):
        self.conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost,1433;"  # Server và port của bạn
            "DATABASE=GreenWebsite;"  # Tên database
            "UID=sa;"  # User SQL Server
            "PWD=1234567;"  # Mật khẩu SQL Server
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            print(f"❌ Lỗi kết nối database: {e}")
            return False

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except:
            pass

    def save_user(self, username, email, password):
        try:
            if not self.connect():
                return False
            
            insert_query = "INSERT INTO Users (UserName, Email, Password) VALUES (?, ?, ?)"
            self.cursor.execute(insert_query, (username, email, password))
            self.conn.commit()
            print("✅ Đã lưu thông tin người dùng thành công!")
            return True
        except Exception as e:
            print(f"❌ Lỗi khi lưu vào database: {e}")
            return False
        finally:
            self.close() 