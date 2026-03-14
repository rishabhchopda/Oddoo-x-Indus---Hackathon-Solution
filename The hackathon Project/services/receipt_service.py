from services.stock_service import increase_stock

def process_receipt(product_id, quantity):
    return increase_stock(product_id, quantity)