from flask import Flask
from config import Config
from database.db import db

# Import models so SQLAlchemy registers tables
import models.user_model
import models.product_model
import models.stock_ledger_model

# Import route blueprints
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.receipt_routes import receipt_bp
from routes.delivery_routes import delivery_bp
from routes.adjustment_routes import adjustment_bp
from routes.dashboard_routes import dashboard_bp
from routes.transfer_routes import transfer_bp
from routes.ledger_routes import ledger_bp


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register all modules
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(receipt_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(adjustment_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(transfer_bp)
    app.register_blueprint(ledger_bp)

    # Create tables if they do not exist
    with app.app_context():
        db.create_all()

    return app