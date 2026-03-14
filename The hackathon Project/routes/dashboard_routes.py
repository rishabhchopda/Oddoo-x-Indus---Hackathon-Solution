from flask import Blueprint, render_template
from models.product_model import Product
from database.db import db

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():

    products_db = Product.query.all()

    products = []
    categories_map = {}

    for p in products_db:

        warehouse = "Main Warehouse"

        products.append((p.name, p.category, p.stock_quantity, warehouse))

        if p.category not in categories_map:
            categories_map[p.category] = 0

        categories_map[p.category] += p.stock_quantity


    total_products = len(products_db)

    low_stock = len([
    p for p in products_db
    if p.reorder_level and p.stock_quantity <= p.reorder_level
])

    out_of_stock = len([p for p in products_db if p.stock_quantity == 0])

    pending_receipts = 0
    pending_deliveries = 0
    scheduled_transfers = 0


    categories = list(categories_map.keys())
    stocks = list(categories_map.values())

    warehouses = ["Main Warehouse"]
    warehouse_stock = [sum(stocks)]


    return render_template(
        "dashboard.html",
        total_products=total_products,
        low_stock=low_stock,
        out_of_stock=out_of_stock,
        pending_receipts=pending_receipts,
        pending_deliveries=pending_deliveries,
        scheduled_transfers=scheduled_transfers,
        products=products,
        categories=categories,
        stocks=stocks,
        warehouses=warehouses,
        warehouse_stock=warehouse_stock
    )