# CoreInventory – Inventory Management System

## Overview

**CoreInventory** is a modular Inventory Management System (IMS) built for the Odoo × Indus University Hackathon.
The system digitizes and streamlines stock-related operations in a business by replacing manual registers and spreadsheets with a centralized, real-time web application.

The application allows inventory managers and warehouse staff to track products, manage incoming and outgoing stock, perform internal transfers, and maintain a stock movement history.

---

## Key Features

### Authentication

* User Registration
* User Login
* Logout functionality
* Secure user authentication

---

### Dashboard

The dashboard provides a quick overview of inventory status.

Displayed metrics include:

* Total Products
* Low Stock Products
* Out of Stock Products
* Inventory Analytics Charts
* Stock Summary Table

---

### Product Management

Users can manage products within the system.

Features:

* Add new products
* View product inventory
* Product attributes include:

  * Product Name
  * SKU / Code
  * Category
  * Unit of Measure
  * Initial Stock
  * Warehouse Location
  * Reorder Level

---

### Inventory Operations

#### 1. Receipts (Incoming Stock)

Used when products arrive from suppliers.

Example:

```
Receive 50 Steel Rods → Stock increases by 50
```

---

#### 2. Delivery Orders (Outgoing Stock)

Used when stock leaves the warehouse for customer delivery.

Example:

```
Deliver 10 Wooden Chairs → Stock decreases by 10
```

---

#### 3. Stock Adjustment

Used to correct discrepancies between physical stock and recorded inventory.

Example:

```
System shows 50 units but physical count is 47 → Adjustment −3
```

---

#### 4. Internal Transfer

Moves stock between warehouse locations.

Example:

```
Main Warehouse → Production Rack
```

Stock quantity remains the same, but location is updated.

---

### Stock Ledger / Movement History

Every inventory operation is logged in the **Stock Ledger**.

The ledger tracks:

* Product ID
* Movement Type (Receipt, Delivery, Adjustment, Transfer)
* Quantity
* Source
* Destination
* Timestamp

This ensures **full traceability of stock movement**.

---

## System Architecture

```
Frontend
   │
   │ (HTML + CSS Templates)
   │
Flask Web Application
   │
Routes Layer
   │
Services Layer
   │
Database Layer
   │
SQLite Database
```

---

## Technology Stack

**Backend**

* Python
* Flask
* SQLAlchemy ORM

**Frontend**

* HTML
* CSS
* Jinja2 Templates
* Chart.js (Dashboard Analytics)

**Database**

* SQLite

---

## Project Structure

```
inventory_management_system/

app.py
run.py
config.py

database/
    db.py

models/
    user_model.py
    product_model.py
    stock_ledger_model.py

routes/
    auth_routes.py
    product_routes.py
    receipt_routes.py
    delivery_routes.py
    adjustment_routes.py
    transfer_routes.py
    ledger_routes.py
    dashboard_routes.py

services/
    stock_service.py
    receipt_service.py
    delivery_service.py
    adjustment_service.py
    transfer_service.py

templates/
    login.html
    register.html
    dashboard.html
    ledger.html
    products/
        add_product.html
        product_list.html
    operations/
        receive_stock.html
        deliver_stock.html
        adjust_stock.html
        transfer.html

static/
    style.css
```

---

## Installation & Setup

### 1. Clone the repository

```
git clone <repository-url>
cd coreinventory
```

---

### 2. Install dependencies

```
pip install flask flask_sqlalchemy
```

---

### 3. Run the application

```
python run.py
```

---

### 4. Open the application

```
http://127.0.0.1:5000
```

---

## Example Inventory Workflow

1. Add Product
2. Receive Stock from Supplier
3. Deliver Products to Customer
4. Transfer Stock between Locations
5. Adjust Stock if mismatch occurs
6. View Stock Movement History in Ledger

---

## Future Improvements

Possible enhancements include:

* OTP-based password reset
* Product search by SKU
* Multi-warehouse management
* Role-based access control
* Inventory alerts & reorder suggestions
* REST API integration

---

## Team Contributions

| Module      | Responsibility        |
| ----------- | --------------------- |
| Developer 1 | Authentication System |
| Developer 2 | Product Management    |
| Developer 3 | Inventory Operations  |
| Developer 4 | Dashboard & Analytics |

---

## License

This project was developed for educational and hackathon purposes.

---

## Acknowledgements

Developed for the **Odoo × Indus University Hackathon**.
