import pymysql

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='1234567',
                database='GoodDB',
                port=3306,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            print(f"❌ Lỗi kết nối database: {e}")
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
