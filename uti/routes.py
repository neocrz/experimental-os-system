from flask import render_template, redirect, url_for, flash, request
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.forms import LoginForm
from uti.models import User
@app.route('/')
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            attemped_user = User.query.filter_by(username=form.username.data).first()
            if attemped_user and attemped_user.check_password_correction(attemped_password=form.password.data):
                login_user(attemped_user)
                flash(f"Sucesso! Logado como {attemped_user.username}.", category="success")
                return redirect(url_for("system_page"))
            else:
                flash("Usuário e/ou senha não válidos. Tente novamente", category="danger")
                return redirect(url_for('login_page'))
    if request.method == "GET":
        return render_template("login.html", form=form)

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/system")
@login_required
def system_page():
    return render_template("system.html")

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Deslogado com sucesso.", category="info")
    return redirect(url_for("home_page"))