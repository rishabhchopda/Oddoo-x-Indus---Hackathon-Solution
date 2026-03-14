from database.db import db
from models.product_model import Product
from models.stock_ledger_model import StockLedger

def process_transfer(product_id, from_location, to_location, quantity):

    product = Product.query.get(product_id)

    if not product:
        return None

    ledger = StockLedger(
        product_id=product_id,
        movement_type="TRANSFER",
        quantity=quantity,
        source=from_location,
        destination=to_location
    )

    product.location = to_location

    db.session.add(ledger)
    db.session.commit()

    return product