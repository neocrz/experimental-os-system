from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.forms import AddOrdemForm, ModOrdemForm
from uti.models import Ordem, Cliente, Equipamento

@app.route('/ordem', methods = ["GET", "POST"])
@login_required
def ordem_page():
    ordens = Ordem.query.all()

    if request.method == "POST":
        if request.form.get('ordem-id'):
            o_id = request.form['ordem-id']
            ordem_data = Ordem.query.get(o_id)
            return render_template("ordem.html", ordens=ordens, ordem_data=ordem_data)
        
    if request.method == "GET":
        return render_template("ordem.html", ordens=ordens)
    

@app.route('/ordem/adicionar', methods = ["GET", "POST"])
@login_required
def add_ordem():
    clientes = Cliente.query.all()
    equips = Equipamento.query.all()
    form = AddOrdemForm()
    if form.validate_on_submit():
        cliente_id = request.form.get('cliente_id')
        cliente = Cliente.query.get(cliente_id)
        ordem_to_create = Ordem(
            desc=form.desc.data,
            cliente_id=cliente.id,
            tipo_ordem=form.tipo_ordem.data,
            data_os=form.data_os.data,
            data_chamado=form.data_chamado.data,
            motivo_chamado=form.motivo_chamado.data,
            status_serviço=form.status_serviço.data,
            observacao=form.observacao.data,
            serv_executado=form.serv_executado.data,
            material=form.material.data,
            valor_visita=form.valor_visita.data,
            maod_obra=form.maod_obra.data,
            valor_km=form.valor_km.data,
            valor_material=form.valor_material.data,
            km_inicial=form.km_inicial.data,
            km_final=form.km_final.data,
            )
        db.session.add(ordem_to_create)
        db.session.commit()
        flash(f"Ordem '{ordem_to_create.id}' criada com sucesso!", category="success")
        return redirect(url_for('ordem_page'))

    return render_template("add-ordem.html", form=form, clientes=clientes, equips=equips)

@app.route('/ordem/modificar', methods = ["GET", "POST"])
@login_required
def mod_ordem():
    ordem_id = request.args.get('ordem_id')
    ordem = Ordem.query.get(ordem_id)
    
    form = ModOrdemForm()
    clientes = Cliente.query.all()
    equips = Equipamento.query.all()

    if form.validate_on_submit():
        cliente_id = request.form['cliente_id']
        cliente = Cliente.query.get(cliente_id)
        equip_id = request.form['equip_id']
        equip = Cliente.query.get(equip_id)
        ordem.desc=form.desc.data
        ordem.cliente_id=cliente.id
        ordem.equipamento_id=equip_id
        ordem.tipo_ordem=form.tipo_ordem.data
        ordem.data_os=form.data_os.data
        ordem.data_chamado=form.data_chamado.data
        ordem.motivo_chamado=form.motivo_chamado.data
        ordem.status_serviço=form.status_serviço.data
        ordem.observacao=form.observacao.data
        ordem.serv_executado=form.serv_executado.data
        ordem.material=form.material.data
        ordem.valor_visita=form.valor_visita.data
        ordem.maod_obra=form.maod_obra.data
        ordem.valor_km=form.valor_km.data
        ordem.valor_material=form.valor_material.data
        ordem.km_inicial=form.km_inicial.data
        ordem.km_final=form.km_final.data

        db.session.add(ordem)
        db.session.commit()
        flash(f"Ordem '{ordem.id}' Modificada com sucesso!", category="success")
        return redirect(url_for('ordem_page'))

    form.tipo_ordem.default = ordem.tipo_ordem
    form.status_serviço.default = ordem.status_serviço
    form.process()

    return render_template("mod-ordem.html", form=form, ordem=ordem, clientes=clientes, equips=equips)

@app.route('/ordem/remover', methods = ["GET", "POST"])
@login_required
def rm_ordem():
    ordem_id = request.args.get('ordem_id')
    ordem = Ordem.query.get(ordem_id)
    db.session.delete(ordem)
    db.session.commit()
    return redirect(url_for('ordem_page'))

@app.route('/ordem/imprimir')
@login_required
def print_ordem():
    ordem_id = request.args.get('ordem_id')
    ordem = Ordem.query.get(ordem_id)
    return render_template("print-ordem.html", ordem=ordem)