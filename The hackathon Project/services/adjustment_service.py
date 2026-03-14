from services.stock_service import adjust_stock

def process_adjustment(product_id, new_quantity):
    return adjust_stock(product_id, new_quantity)