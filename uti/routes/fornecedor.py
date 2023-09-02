from flask import render_template, redirect, url_for, flash, request,
from uti import app, db
from flask_login import login_required
from uti.models import Fornecedor

@app.route('/fornecedor', methods = ["GET", "POST"])
@login_required
def fornecedor_page():
  fornecedores = Fornecedor.query.order_by(Fornecedor.id).all()
  if request.method == "POST":
        if request.form.get('fornecedor-id'):
            fornecedor_id = request.form['fornecedor-id']
            data = Fornecedor.query.get(fornecedor_id)
            return render_template("fornecedor/fornecedor.html", fornecedores=fornecedores, data=data)

    if request.method == "GET":
        return render_template("fornecedor/fornecedor.html", fornecedores=fornecedores)
