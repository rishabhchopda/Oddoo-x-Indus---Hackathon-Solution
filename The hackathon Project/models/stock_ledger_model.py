from database.db import db
from datetime import datetime

class StockLedger(db.Model):

    __tablename__ = "stock_ledger"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer)

    movement_type = db.Column(db.String(50))

    quantity = db.Column(db.Integer)

    source = db.Column(db.String(100))

    destination = db.Column(db.String(100))

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)