from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.models import Cliente
from uti.forms import AddClientForm, ModClienteForm

@app.route("/cliente", methods=["GET", "POST"])
@login_required
def cliente_page():
    clientes = Cliente.query.order_by(Cliente.name).all()

    if request.method == "POST":
        if request.form.get('cliente-id'):
            cliente_id = request.form['cliente-id']
            data = Cliente.query.get(cliente_id)
            return render_template("cliente/cliente.html", clientes=clientes, data=data)

    if request.method == "GET":
        return render_template("cliente/cliente.html", clientes=clientes)

@app.route('/cliente/adicionar', methods = ["GET", "POST"])
@login_required
def add_cliente():
    form = AddClientForm()
    if form.validate_on_submit():
        cliente_to_create = Cliente(
            name=form.name.data,
            cpf=form.cpf.data,
            cnpj=form.cnpj.data,
            rg=form.rg.data,
            endereco=form.endereco.data,
            num_endereco=form.num_endereco.data,
            bairro=form.bairro.data,
            cidade=form.cidade.data,
            estado=form.estado.data,
            cep=form.cep.data,
            telefone=form.telefone.data,
            telefone2=form.telefone2.data,
            telefone3=form.telefone3.data,
            email=form.email.data,
            insc_estadual=form.insc_estadual.data,
            insc_municipal=form.insc_municipal.data,
            contato=form.contato.data,
            razao_social=form.razao_social.data
            
        )
        db.session.add(cliente_to_create)
        db.session.commit()
        flash(f"Cliente '{cliente_to_create.name}' adicionado com sucesso!", category="success")
        return redirect(url_for('cliente_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Erro no registro de cliente: {err_msg[0]}", category="danger")
    return render_template("cliente/add-cliente.html", form=form)

@app.route('/cliente/remover', methods = ["GET", "POST"])
@login_required
def rm_cliente():
    cliente_id = request.args.get('cliente_id')
    cliente = Cliente.query.get(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash(f"Cliente '{cliente_id}' removido.")
    return redirect(url_for('cliente_page'))


@app.route('/cliente/modificar', methods = ["GET", "POST"])
@login_required
def mod_cliente():
    cliente_id = request.args.get('cliente_id')
    cliente = Cliente.query.get(cliente_id)
    
    form = ModClienteForm()

    if form.validate_on_submit():
        cliente_id = request.form['cliente_id']
        cliente = Cliente.query.get(cliente_id)
        cliente.tipo_cliente = form.tipo_cliente.data
        cliente.name=form.name.data
        cliente.cpf=form.cpf.data
        cliente.cnpj=form.cnpj.data
        cliente.rg=form.rg.data
        cliente.endereco=form.endereco.data
        cliente.num_endereco=form.num_endereco.data
        cliente.bairro=form.bairro.data
        cliente.cidade=form.cidade.data
        cliente.estado=form.estado.data
        cliente.cep=form.cep.data
        cliente.telefone=form.telefone.data
        cliente.telefone2=form.telefone2.data
        cliente.telefone3=form.telefone3.data
        cliente.email=form.email.data
        cliente.insc_estadual=form.insc_estadual.data
        cliente.insc_municipal=form.insc_municipal.data
        cliente.contato=form.contato.data
        cliente.razao_social=form.razao_social.data
        db.session.commit()

        flash(f"Cliente '{cliente.name}' modificado com sucesso!", category="success")
        return redirect(url_for('cliente_page'))
    
    form.tipo_cliente.default = cliente.tipo_cliente
    form.estado.default = cliente.estado
    form.process()

    return render_template("cliente/mod-cliente.html", form=form, cliente=cliente)

