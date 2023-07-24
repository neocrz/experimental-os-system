from flask import render_template, redirect, url_for, flash, request
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")