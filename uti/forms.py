from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from uti import app
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from uti.models import User

class LoginForm(FlaskForm):
    username = StringField(
        label="Usuário:",
        validators=[DataRequired()]
    )
    password = PasswordField(
        label="Senha:",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Acessar")

class ClienteForm(FlaskForm):
    name = StringField(
        label="Nome:",
        validators=[
            DataRequired(),
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )

    tipo_cliente = SelectField(
        u'Tipo', 
        choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')]
        )

    cpf = StringField(
        label="CPF:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para CPF" )
            ]
    )

    cnpj = StringField(
        label="CNPJ:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para CNPJ" )
            ]
    )

    rg = StringField(
        label="RG:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para RG" )
            ]
    )

    endereco = StringField(
        label="Endereço:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )
    num_endereco = StringField(
        label="Nº:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres" )
            ]
    )

    bairro = StringField(
        label="Bairro:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )

    cidade = StringField(
        label="Cidade:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )

    estado = StringField(
        label="Estado:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )

    cep = StringField(
        label="CEP:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para CEP" )
            ]
    )

    telefone = StringField(
        label="Telefone:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para Telefone" )
            ]
    )

    telefone2 = StringField(
        label="Telefone 2:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para Telefone" )
            ]
    )

    razao_social = StringField(
        label="Razão Social:",
        validators=[
            Length( max=64, message="No máximo 32 caracteres" )
            ]
    )

    email = StringField(
        label="Email:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
            ]
    )

    insc_estadual = StringField(
        label="Inscrição Estadual:",
        validators=[
            Length( max=32, message="No máximo 64 caracteres" )
            ]
    )

    insc_municipal = StringField(
        label="Inscrição Municipal:",
        validators=[
            Length( max=32, message="No máximo 64 caracteres" )
            ]
    )

class AddClientForm(ClienteForm):

    submit = SubmitField(label="Criar Cliente")

class ModClienteForm(ClienteForm):
    submit = SubmitField(label="Modificar Cliente")

class OrdemForm(FlaskForm):
    desc = StringField(
        label="Descrição:",
        validators=[
            Length( max=256, message="No máximo 256 caracteres para a descrição" )
            ]
    )

class AddOrdemForm(OrdemForm):
    submit = SubmitField(label="Criar Ordem")

class ModOrdemForm(OrdemForm):
    submit = SubmitField(label="Modificar Ordem")