from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.forms import *
from uti.models import *


@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html")

# dinamic css - allow to use jinja syntax in css
@app.route('/css/base')
def css():
    resp = make_response(render_template("style.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp

@app.route('/script/base')
def script():
    resp = make_response(render_template("script.js"))
    resp.headers['Content-type'] = 'text/javascript'
    return resp

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            attemped_user = User.query.filter_by(username=form.username.data).first()
            if attemped_user and attemped_user.check_password_correction(attemped_password=form.password.data):
                login_user(attemped_user)
                flash(f"Sucesso! Logado como {attemped_user.name}.", category="success")
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
    return redirect(url_for("index"))







