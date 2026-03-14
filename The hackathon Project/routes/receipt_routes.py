from flask import Blueprint, request, redirect
from services.receipt_service import process_receipt

receipt_bp = Blueprint("receipt_bp", __name__)

@receipt_bp.route("/receipts", methods=["POST"])
def create_receipt():

    product_id = int(request.form.get("product_id"))
    quantity = int(request.form.get("quantity"))

    process_receipt(product_id, quantity)

    return redirect("/dashboard")