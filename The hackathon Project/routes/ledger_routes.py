from flask import Blueprint, render_template
from models.stock_ledger_model import StockLedger

ledger_bp = Blueprint("ledger_bp", __name__)

@ledger_bp.route("/ledger")
def view_ledger():

    movements = StockLedger.query.all()

    return render_template("ledger.html", movements=movements)