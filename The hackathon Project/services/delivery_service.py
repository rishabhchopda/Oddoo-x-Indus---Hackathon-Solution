from services.stock_service import decrease_stock

def process_delivery(product_id, quantity):
    return decrease_stock(product_id, quantity)