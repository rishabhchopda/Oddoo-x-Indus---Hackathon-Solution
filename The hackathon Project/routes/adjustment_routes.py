from flask import Blueprint, request, redirect
from services.adjustment_service import process_adjustment

adjustment_bp = Blueprint("adjustment_bp", __name__)

@adjustment_bp.route("/adjustments", methods=["POST"])
def create_adjustment():

    product_id = int(request.form.get("product_id"))
    new_quantity = int(request.form.get("new_quantity"))

    process_adjustment(product_id, new_quantity)

    return redirect("/dashboard")