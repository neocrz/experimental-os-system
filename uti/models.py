from uti import db, login_manager
from uti import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Cliente(db.Model):
    # empresas clientes
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    razao_social = db.Column(db.String(length=64), nullable=False, unique=True)
    __tablename__ = 'clientes'
    endereco = db.Column(db.String(length=64), nullable=True, unique=False)
    num_endereco = db.Column(db.String(length=16), nullable=True, unique=False)
    bairro = db.Column(db.String(length=64), nullable=True, unique=False)
    cidade = db.Column(db.String(length=32), nullable=True, unique=False)
    estado = db.Column(db.String(length=32), nullable=True, unique=False)
    cep = db.Column(db.String(length=32), nullable=True, unique=False)
    telefone = db.Column(db.String(length=32), nullable=True, unique=False)
    telefone2 = db.Column(db.String(length=32), nullable=True, unique=False)
    telefone3 = db.Column(db.String(length=32), nullable=True, unique=False)
    email = db.Column(db.String(length=64), nullable=True, unique=False)
    contato = db.Column(db.String(length=64), nullable=True, unique=False)
    insc_estadual = db.Column(db.String(length=32), nullable=True, unique=False)
    insc_municipal = db.Column(db.String(length=32), nullable=True, unique=False)
    cpf = db.Column(db.String(length=32), nullable=True, unique=False)
    cnpj = db.Column(db.String(length=32), nullable=True, unique=False)
    rg = db.Column(db.String(length=32), nullable=True, unique=False)
    tipo_cliente = db.Column(db.String(length=10), nullable=False, default="Física") #Física ou Jurídica
    ordens = db.relationship('Ordem', backref='cliente')


class Equipamento(db.Model):

    __tablename__ = 'equipamentos'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=128), nullable=False, unique=True)
    modelo = db.Column(db.String(length=128), nullable=True, unique=False)
    marca = db.Column(db.String(length=128), nullable=True, unique=False)
    sn = db.Column(db.String(length=64), nullable=True, unique=False)
    ordens = db.relationship('Ordem', backref='equipamento')

class Ordem(db.Model):

    __tablename__ = 'ordens'
    id = db.Column(db.Integer(), primary_key=True)
    constatado = db.Column(db.String(length=256), nullable=True, unique=False)
    tipo_ordem = db.Column(db.String(length=32), nullable=False, default="Ordem de Serviço") # Ordem de Serviço ou Orçamento
    data_os = db.Column(db.String(length=32), nullable=True, unique=False) # Data Criação ou Modificação OS
    data_chamado = db.Column(db.String(length=32), nullable=True, unique=False) # Data Criação ou Modificação OS
    motivo_chamado = db.Column(db.String(length=512), nullable=True, unique=False)
    status_serviço = db.Column(db.String(length=32), nullable=False, default="Concluído") # Concluído, Não Concluido, A Continuar
    observacao = db.Column(db.String(length=512), nullable=True, unique=False) # Observação Serviço
    serv_executado = db.Column(db.String(length=512), nullable=True, unique=False) # Desc Serviço Executado
    material = db.Column(db.String(length=512), nullable=True, unique=False) # material usado
    tipo_material = db.Column(db.String(length=512), nullable=True, unique=False, default="Aplicado") # material 'Aplicado' ou 'Fornecido'
    valor_visita = db.Column(db.String(length=16), nullable=True, unique=False) 
    maod_obra = db.Column(db.String(length=16), nullable=True, unique=False)
    valor_km = db.Column(db.String(length=16), nullable=True, unique=False)
    valor_material = db.Column(db.String(length=16), nullable=True, unique=False)
    km_inicial = db.Column(db.String(length=16), nullable=True, unique=False)
    km_final = db.Column(db.String(length=16), nullable=True, unique=False)
    valor_final = db.Column(db.String(length=16), nullable=True, unique=False)
    
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamentos.id'))
    

    def __repr__(self):
        return f'Ordem {self.id}'


class Role(db.Model):
    # roles de usuários do sistema
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f'<Role {self.name}>'
    

class User(db.Model, UserMixin):
    # usuários do sistema
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    username = db.Column(db.String(length=64), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=64), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'<User {self.username}>'
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attemped_password):
        return bcrypt.check_password_hash(self.password_hash, attemped_password)
