from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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

class AddClientForm(FlaskForm):
    name = StringField(
        label="Nome",
        validators=[
            DataRequired(),
            Length( max=64, message="Nome de identificação" )
            ]
    )

    cpf_cnpj = StringField(
        label="Nome",
        validators=[
            DataRequired(),
            Length( max=14, message="CPF/CNPJ" )
            ]
    )

    endereco = StringField(
        label="Endereço",
        validators=[
            DataRequired(),
            Length( max=64, message="CPF/CNPJ" )
            ]
    )

    bairro = StringField(
        label="Bairro",
        validators=[
            Length( max=64, message="Bairro" )
            ]
    )

    submit = SubmitField(label="Criar Cliente")
