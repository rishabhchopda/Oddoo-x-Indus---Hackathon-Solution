from database.db import db

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)

    sku = db.Column(db.String(80), unique=True, nullable=False)

    category = db.Column(db.String(80))

    unit = db.Column(db.String(20))

    stock_quantity = db.Column(db.Integer, default=0)

    location = db.Column(db.String(100))

    reorder_level = db.Column(db.Float)