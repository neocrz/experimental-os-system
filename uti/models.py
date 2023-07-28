from uti import db, login_manager
from uti import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    def __repr__(self):
        return f'Item {self.name}'

class Empresa(Base):
    
    endereco = db.Column(db.String(length=64), nullable=True, unique=False)
    bairro = db.Column(db.String(length=64), nullable=True, unique=False)
    cidade = db.Column(db.String(length=32), nullable=True, unique=False)
    estado = db.Column(db.String(length=32), nullable=True, unique=False)
    cep = db.Column(db.String(length=32), nullable=True, unique=False)
    telefone = db.Column(db.String(length=32), nullable=True, unique=False)
    telefone2 = db.Column(db.String(length=32), nullable=True, unique=False)
    email = db.Column(db.String(length=64), nullable=True, unique=False)
    razao_social = db.Column(db.String(length=64), nullable=True, unique=False)
    insc_estadual = db.Column(db.String(length=32), nullable=True, unique=False)
    insc_municipal = db.Column(db.String(length=32), nullable=True, unique=False)
    cpf = db.Column(db.String(length=32), nullable=True, unique=False)
    cnpj = db.Column(db.String(length=32), nullable=True, unique=False)
    rg = db.Column(db.String(length=32), nullable=True, unique=False)

class System(Empresa):
    # empresa responsável pelo sistema
    logo_location = db.Column(db.String(length=64), nullable=True, unique=False)
    pass

class Fornecedor(Empresa):
    # empresas fornecedoras
    tipo_fornecedor = db.Column(db.String(length=10), nullable=False, default="Física") #Física ou Jurídica
    __tablename__ = 'fornecedores'    

class Cliente(Empresa):
    # empresas clientes
    __tablename__ = 'clientes'
    tipo_cliente = db.Column(db.String(length=10), nullable=False, default="Física") #Física ou Jurídica
    
class Role(Base):
    # roles de usuários do sistema
    __tablename__ = 'roles'

    def __repr__(self):
        return f'<Role {self.name}>'
    users = db.relationship('User', backref='role')

class User(Base, UserMixin):
    # usuários do sistema
    __tablename__ = 'users'
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
    
class Equipamento(Base, db.Model):
    __tablename__ = 'equipamentos'

class Peca(Base, db.Model):
    __tablename__ = 'pecas'
