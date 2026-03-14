from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from flask_bcrypt import Bcrypt

auth_bp = Blueprint("auth_bp", __name__)
bcrypt = Bcrypt()

def get_db():
    conn = sqlite3.connect("instance/inventory.db")
    return conn


# Login page
@auth_bp.route("/")
def login_page():
    return render_template("login.html")


# Register page
@auth_bp.route("/register")
def register_page():
    return render_template("register.html")


# Register user
@auth_bp.route("/register_user", methods=["POST"])
def register_user():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",
        (name,email,hashed_password,role)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("auth_bp.login_page"))


# LOGIN USER
@auth_bp.route("/login_user", methods=["POST"])
def login_user():

    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    conn.close()

    if user:
        if bcrypt.check_password_hash(user[3], password):
            return redirect("/dashboard")
        else:
            return "Invalid password"
    else:
        return "User not found"
    
@auth_bp.route("/logout")
def logout():
    return redirect("/")