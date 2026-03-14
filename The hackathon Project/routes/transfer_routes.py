from flask import Blueprint, request, redirect, render_template
from services.transfer_service import process_transfer

transfer_bp = Blueprint("transfer_bp", __name__)

@transfer_bp.route("/transfer_page")
def transfer_page():
    return render_template("operations/transfer.html")


@transfer_bp.route("/transfer", methods=["POST"])
def create_transfer():

    product_id = int(request.form.get("product_id"))
    from_location = request.form.get("from_location")
    to_location = request.form.get("to_location")
    quantity = int(request.form.get("quantity"))

    process_transfer(product_id, from_location, to_location, quantity)

    return redirect("/dashboard")