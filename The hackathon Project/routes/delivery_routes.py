from flask import Blueprint, request, redirect
from services.delivery_service import process_delivery

delivery_bp = Blueprint("delivery_bp", __name__)

@delivery_bp.route("/deliveries", methods=["POST"])
def create_delivery():

    product_id = int(request.form.get("product_id"))
    quantity = int(request.form.get("quantity"))

    process_delivery(product_id, quantity)

    return redirect("/dashboard")