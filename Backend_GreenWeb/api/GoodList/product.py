from database_Connection.db_connection_mysql import DatabaseConnection

class Product:
    @staticmethod
    def get_all_products():
        """Lấy tất cả sản phẩm từ database"""
        db = DatabaseConnection()
        try:
            if not db.connect():
                raise Exception("Không thể kết nối database")
            query = """
                SELECT ID, Name, Image, Price, Discount, Place, Link
                FROM GoodList;
            """
            db.cursor.execute(query)
            items = db.cursor.fetchall()
            return items
        except Exception as e:
            raise e
        finally:
            db.close()
    