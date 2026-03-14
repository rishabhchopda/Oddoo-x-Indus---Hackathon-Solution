from flask import Blueprint, request, jsonify, render_template
from database.db import db
from models.product_model import Product

product_bp = Blueprint("product_bp", __name__)


@product_bp.route("/products", methods=["POST"])
def create_product():

    name = request.form.get("name")
    sku = request.form.get("sku")
    category = request.form.get("category")
    unit = request.form.get("unit")
    stock_quantity = request.form.get("stock_quantity")
    location = request.form.get("location")
    reorder_level = request.form.get("reorder_level")

    product = Product(
        name=name,
        sku=sku,
        category=category,
        unit=unit,
        stock_quantity=stock_quantity,
        location=location,
        reorder_level=reorder_level
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"})

@product_bp.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()

    result = []

    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "sku": p.sku,
            "stock_quantity": p.stock_quantity
        })

    return jsonify(result)

@product_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    data = request.get_json()

    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if "name" in data:
        product.name = data["name"]

    if "sku" in data:
        product.sku = data["sku"]

    if "category" in data:
        product.category = data["category"]

    if "unit" in data:
        product.unit = data["unit"]

    if "stock_quantity" in data:
        product.stock_quantity = data["stock_quantity"]

    if "location" in data:
        product.location = data["location"]

    if "reorder_level" in data:
        product.reorder_level = data["reorder_level"]

    db.session.commit()

    return jsonify({"message": "Product updated"})

@product_bp.route("/low-stock", methods=["GET"])
def low_stock():

    products = Product.query.filter(
        Product.stock_quantity <= Product.reorder_level
    ).all()

    result = []

    for p in products:

        result.append({
            "product_id": p.id,
            "product_name": p.name,
            "stock": p.stock_quantity,
            "reorder_level": p.reorder_level
        })

    return jsonify(result)

@product_bp.route("/products_page")
def products_page():
    return render_template("products/add_product.html")

@product_bp.route("/receipts_page")
def receipts_page():
    return render_template("operations/receive_stock.html")

@product_bp.route("/deliveries_page")
def deliveries_page():
    return render_template("operations/deliver_stock.html")

@product_bp.route("/adjustments_page")
def adjustments_page():
    return render_template("operations/adjust_stock.html")

@product_bp.route("/products_list")
def products_list():
    products = Product.query.all()
    return render_template("products/product_list.html", products=products)