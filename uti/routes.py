from flask import render_template, redirect, url_for, flash, request, make_response
from uti import app, db
from flask_login import login_user, logout_user, login_required, current_user
from uti.forms import LoginForm, AddClientForm, ModClienteForm, AddOrdemForm
from uti.models import User, Cliente, Ordem

@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html")

# dinamic css - allow to use jinja syntax in css
@app.route('/style.css')
def css():
    resp = make_response(render_template("style.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp

@app.route('/script.css')
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

@app.route("/clientes", methods=["GET", "POST"])
@login_required
def client_page():
    # clientes = Cliente.query.all()
    clientes = Cliente.query.order_by(Cliente.name).all()
    

    if request.method == "POST":
        if request.form.get('client-id'):
            c_id = request.form['client-id']
            client_data = Cliente.query.get(c_id)
            return render_template("client.html", clientes=clientes, client_data=client_data)
        if request.form.get('client-name'):
            c_name = request.form["client-name"]
            client_data = Cliente.query.filter_by(name=c_name).first()
            return render_template("client.html", clientes=clientes, client_data=client_data)
    

    if request.method == "GET":
        return render_template("client.html", clientes=clientes)

@app.route('/clientes/excluir')
@login_required
def excluir_cliente():
    client_id = request.args.get('client_id')
    client = Cliente.query.get(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('client_page'))

@app.route('/clientes/modificar', methods=["GET", "POST"])
@login_required
def modificar_cliente():
    client_id = request.args.get('client_id')
    cliente = Cliente.query.get(client_id)
    form = ModClienteForm()
    

    if form.validate_on_submit():
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
        cliente.email=form.email.data
        cliente.insc_estadual=form.insc_estadual.data
        cliente.insc_municipal=form.insc_municipal.data
        cliente.razao_social=form.razao_social.data
        db.session.commit()
        return redirect(url_for('client_page'))

    form.tipo_cliente.default = cliente.tipo_cliente
    form.process()
    
    return render_template('mod-client.html', cliente=cliente, form=form)

@app.route('/clientes/cadastro', methods = ["GET", "POST"])
@login_required
def cadastro_cliente():
    form = AddClientForm()
    if form.validate_on_submit():
        client_to_create = Cliente(name=form.name.data,
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
                              email=form.email.data,
                              insc_estadual=form.insc_estadual.data,
                              insc_municipal=form.insc_municipal.data,
                              razao_social=form.razao_social.data
                              )
        db.session.add(client_to_create)
        db.session.commit()
        flash(f"Cliente '{client_to_create.name}' criado com sucesso!", category="success")
        return redirect(url_for('client_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Erro no registro de cliente: {err_msg[0]}", category="danger")
    
    return render_template("add-client.html", form=form)

@app.route('/ordem', methods = ["GET", "POST"])
@login_required
def ordem_page():
    return render_template("ordem.html")

@app.route('/ordem/adicionar', methods = ["GET", "POST"])
@login_required
def add_ordem():
    form = AddOrdemForm()
    if form.validate_on_submit():
        ordem_to_create = Ordem(desc=form.desc.data)
        db.session.add(ordem_to_create)
        db.session.commit()

    return render_template("add-ordem.html", form=form)