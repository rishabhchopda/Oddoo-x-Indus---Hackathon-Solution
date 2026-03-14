from database.db import db
from models.product_model import Product
from models.stock_ledger_model import StockLedger

def increase_stock(product_id, quantity):

    product = Product.query.get(product_id)

    if not product:
        return None

    product.stock_quantity += quantity

    ledger = StockLedger(
        product_id=product_id,
        movement_type="RECEIPT",
        quantity=quantity,
        source="Supplier",
        destination=product.location
    )

    db.session.add(ledger)
    db.session.commit()

    return product

def decrease_stock(product_id, quantity):

    product = Product.query.get(product_id)

    if not product:
        return None

    product.stock_quantity -= quantity

    ledger = StockLedger(
        product_id=product_id,
        movement_type="DELIVERY",
        quantity=quantity,
        source=product.location,
        destination="Customer"
    )

    db.session.add(ledger)
    db.session.commit()

    return product

def adjust_stock(product_id, new_quantity):

    product = Product.query.get(product_id)

    if not product:
        return None

    difference = new_quantity - product.stock_quantity

    product.stock_quantity = new_quantity

    ledger = StockLedger(
        product_id=product_id,
        movement_type="ADJUSTMENT",
        quantity=difference,
        source="Inventory",
        destination="Correction"
    )

    db.session.add(ledger)
    db.session.commit()

    return product