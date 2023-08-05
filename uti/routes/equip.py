from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.models import Equipamento
from uti.forms import AddEquipForm, ModEquipForm

@app.route('/equip', methods = ["GET", "POST"])
@login_required
def equip_page():
    equips = Equipamento.query.all()

    if request.method == "POST":
        if request.form.get('equip-id'):
            equip_id = request.form['equip-id']
            data = Equipamento.query.get(equip_id)
            return render_template("equip/equip.html", equips=equips, data=data)
        
    if request.method == "GET":
        return render_template("equip/equip.html", equips=equips)
    
@app.route('/equip/adicionar', methods = ["GET", "POST"])
@login_required
def add_equip():
    form = AddEquipForm()
    if form.validate_on_submit():
        equip_to_create = Equipamento(
            name=form.name.data,
            modelo=form.modelo.data,
            marca=form.marca.data,
            sn=form.sn.data,
            )
        db.session.add(equip_to_create)
        db.session.commit()
        flash(f"Equipamento '{equip_to_create.id}' adicionado com sucesso!", category="success")
        return redirect(url_for('equip_page'))

    return render_template("equip/add-equip.html", form=form)

@app.route('/equip/remover', methods = ["GET", "POST"])
@login_required
def rm_equip():
    equip_id = request.args.get('equip_id')
    equip = Equipamento.query.get(equip_id)
    db.session.delete(equip)
    db.session.commit()
    flash(f"Equipamento '{equip_id}' removido.")
    return redirect(url_for('equip_page'))

@app.route('/equip/modificar', methods = ["GET", "POST"])
@login_required
def mod_equip():
    equip_id = request.args.get('equip_id')
    equip = Equipamento.query.get(equip_id)
    
    form = ModEquipForm()

    if form.validate_on_submit():
        equip_id = request.form['equip_id']
        equip = Equipamento.query.get(equip_id)
        equip.name=form.name.data
        equip.modelo=form.modelo.data
        equip.marca=form.marca.data
        equip.sn=form.sn.data

        db.session.commit()
        flash(f"Equipamento '{equip.id}' modificado com sucesso!", category="success")
        return redirect(url_for('equip_page'))


    return render_template("equip/mod-equip.html", form=form, equip=equip)