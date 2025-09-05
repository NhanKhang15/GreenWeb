from flask import Flask
from flask_cors import CORS
from api.routes.product import product_bp
from api.auth.login import login_bp
from api.auth.signup import signup_bp
from database_Connection.db_connection_mysql import DatabaseConnection

app = Flask(__name__)
CORS(app)


app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(login_bp, url_prefix='/api')
app.register_blueprint(signup_bp, url_prefix='/api')

if __name__ == '__main__':
    print("🚀 Server đang chạy tại http://localhost:8000")
    print("📝 Endpoints:")
    print("   - POST /api/signup - Đăng ký tài khoản")
    print("   - POST /api/login  - Đăng nhập")
    print("   - GET  /api/products - Lấy danh sách sản phẩm")
    app.run(port=8000, debug=True) 