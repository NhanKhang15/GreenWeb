import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Backend_GreenWeb.database_Connection.db_connection_mysql import DatabaseConnection

db = DatabaseConnection()
try:
    if db.connect():
        print("kết nối thành công")
    else:
        print("Kết nối thất bại")
        sys.exit(1)
except Exception as e:
    print(f"Kết nối thất bại: {e}")
    sys.exit(1)
finally:
    db.close()