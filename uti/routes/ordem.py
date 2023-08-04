from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.forms import AddOrdemForm, ModOrdemForm
from uti.models import Ordem, Cliente, Equipamento
from uti.utils import formatar_valor, valor_tostring
import os

@app.route('/ordem', methods = ["GET", "POST"])
@login_required
def ordem_page():
    ordens = Ordem.query.all()

    if request.method == "POST":
        if request.form.get('ordem-id'):
            o_id = request.form['ordem-id']
            data = Ordem.query.get(o_id)
            return render_template("ordem/ordem.html", ordens=ordens, data=data)
        
    if request.method == "GET":
        return render_template("ordem/ordem.html", ordens=ordens)
    

@app.route('/ordem/adicionar', methods = ["GET", "POST"])
@login_required
def add_ordem():
    clientes = Cliente.query.all()
    equips = Equipamento.query.all()
    form = AddOrdemForm()
    if form.validate_on_submit():
        cliente_id = request.form.get('cliente_id')
        cliente = Cliente.query.get(cliente_id)
        equip_id = request.form.get('equip_id')
        equip = Cliente.query.get(equip_id)
        ordem_to_create = Ordem(
            constatado=form.constatado.data,
            cliente_id=cliente.id,
            equipamento_id=equip.id,
            tipo_ordem=form.tipo_ordem.data,
            data_os=form.data_os.data,
            data_chamado=form.data_chamado.data,
            motivo_chamado=form.motivo_chamado.data,
            status_serviço=form.status_serviço.data,
            observacao=form.observacao.data,
            serv_executado=form.serv_executado.data,
            tipo_material=form.tipo_material.data,
            material=form.material.data,
            valor_visita=form.valor_visita.data,
            maod_obra=form.maod_obra.data,
            valor_km=valor_tostring(int(formatar_valor(form.km_final.data) - formatar_valor(form.km_inicial.data))),
            valor_material=form.valor_material.data,
            km_inicial=form.km_inicial.data,
            km_final=form.km_final.data,
            valor_final=valor_tostring( formatar_valor(form.valor_material.data) + formatar_valor(form.valor_visita.data) + formatar_valor(form.maod_obra.data)),
            )
        db.session.add(ordem_to_create)
        db.session.commit()
        flash(f"Ordem '{ordem_to_create.id}' criada com sucesso!", category="success")
        return redirect(url_for('ordem_page'))

    return render_template("ordem/add-ordem.html", form=form, clientes=clientes, equips=equips)

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
        equip = Equipamento.query.get(equip_id)
        ordem.constatado=form.constatado.data
        ordem.cliente_id=cliente.id
        ordem.equipamento_id=equip.id
        ordem.tipo_ordem=form.tipo_ordem.data
        ordem.data_os=form.data_os.data
        ordem.data_chamado=form.data_chamado.data
        ordem.motivo_chamado=form.motivo_chamado.data
        ordem.status_serviço=form.status_serviço.data
        ordem.observacao=form.observacao.data
        ordem.serv_executado=form.serv_executado.data
        ordem.tipo_material=form.tipo_material.data
        ordem.material=form.material.data
        ordem.valor_visita=form.valor_visita.data
        ordem.maod_obra=form.maod_obra.data
        ordem.valor_km=valor_tostring(int(formatar_valor(form.km_final.data) - formatar_valor(form.km_inicial.data)))
        ordem.valor_material=form.valor_material.data
        ordem.km_inicial=form.km_inicial.data
        ordem.km_final=form.km_final.data
        ordem.valor_final=valor_tostring( formatar_valor(form.valor_material.data) + formatar_valor(form.valor_visita.data) + formatar_valor(form.maod_obra.data))

        db.session.add(ordem)
        db.session.commit()
        flash(f"Ordem '{ordem.id}' Modificada com sucesso!", category="success")
        return redirect(url_for('ordem_page'))

    form.tipo_ordem.default = ordem.tipo_ordem
    form.status_serviço.default = ordem.status_serviço
    form.tipo_material.default = ordem.tipo_material
    form.process()

    return render_template("ordem/mod-ordem.html", form=form, ordem=ordem, clientes=clientes, equips=equips)

@app.route('/ordem/remover', methods = ["GET", "POST"])
@login_required
def rm_ordem():
    ordem_id = request.args.get('ordem_id')
    ordem = Ordem.query.get(ordem_id)
    db.session.delete(ordem)
    db.session.commit()
    return redirect(url_for('ordem_page'))

@app.route('/ordem/imprimir', methods = ["GET", "POST"])
@login_required
def print_ordem():
    
    sys_name = os.environ.get("OS_OWNER_NAME")
    sys_info = os.environ.get("OS_OWNER_INFO")
    sys_info2 = os.environ.get("OS_OWNER_INFO2")
    sys_info3 = os.environ.get("OS_OWNER_INFO3")
    sys_logo = os.environ.get("OS_OWNER_LOGO")
    sys_tec = os.environ.get("OS_OWNER_TEC")
    ordem_id = request.args.get('ordem_id')
    ordem = Ordem.query.get(ordem_id)

    if request.method == "GET":
        return render_template(
        "ordem/print-ordem.html", 
        ordem=ordem, 
        modelo="print-ordem-os",
        sys_name=sys_name, 
        sys_info=sys_info, 
        sys_info2=sys_info2,
        sys_info3=sys_info3,
        sys_logo=sys_logo,
        sys_tec=sys_tec
        )
    
    if request.method == "POST":
        if request.form.get('modelo'):
            modelo = request.form['modelo']
            return render_template(
            "ordem/print-ordem.html", 
            ordem=ordem, 
            modelo=modelo,
            sys_name=sys_name, 
            sys_info=sys_info, 
            sys_info2=sys_info2,
            sys_info3=sys_info3,
            sys_logo=sys_logo,
            sys_tec=sys_tec
            )