from flask import Blueprint, jsonify
from api.GoodList.product import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.get_all_products()
        return jsonify({
            'success': True,
            'products': products
        })
    except Exception as e:
        print(f"❌ Lỗi lấy sản phẩm: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Không thể lấy danh sách sản phẩm'
        }), 500 