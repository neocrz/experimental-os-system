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

    contato = StringField(
        label="Contato:",
        validators=[
            Length( max=64, message="No máximo 64 caracteres" )
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
            Length( max=256, message="No máximo 256 caracteres para 'Descrição'" )
            ]
    )

    tipo_ordem = SelectField(
        u'Tipo de Ordem:', 
        choices=[('Ordem de Serviço', 'Ordem de Serviço'), ('Orçamento', 'Orçamento')]
        )
    
    
    data_os = StringField(
        label="Data da OS:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para 'Data da OS'" )
            ]
    )

    data_chamado = StringField(
        label="Data do Chamado:",
        validators=[
            Length( max=32, message="No máximo 32 caracteres para 'Data do Chamado'" )
            ]
    )

    motivo_chamado = StringField(
        label="Motivo do Chamado:",
        validators=[
            Length( max=512, message="No máximo 512 caracteres para 'Motivo do Chamado'" )
            ]
    )

    status_serviço = SelectField(
        u'Status do Serviço:', 
        choices=[('Concluído', 'Concluído'), ('Não Concluido', 'Não Concluido'), ('A Continuar', 'A Continuar')]
    )

    observacao = StringField(
        label="Observações:",
        validators=[
            Length( max=512, message="No máximo 512 caracteres para 'Observações'" )
            ]
    )

    serv_executado = StringField(
        label="Serviço Executado:",
        validators=[
            Length( max=512, message="No máximo 512 caracteres para 'Serviço Executado'" )
            ]
    )

    material = StringField(
        label="Material Utilizado:",
        validators=[
            Length( max=512, message="No máximo 512 caracteres para 'Material Utilizado'" )
            ]
    )

    valor_visita = StringField(
        label="Valor da Visita:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Valor da Visita'" )
            ]
    )

    maod_obra = StringField(
        label="Mão de Obra:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Mão de Obra'" )
            ]
    )

    valor_km = StringField(
        label="Valor da Km:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Valor da Km'" )
            ]
    )

    valor_material = StringField(
        label="Valor do Material:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Valor do Material'" )
            ]
    )

    km_inicial = StringField(
        label="Km Inicial:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Km Inicial'" )
            ]
    )

    km_final = StringField(
        label="Km Final:",
        validators=[
            Length( max=16, message="No máximo 16 caracteres para 'Km Final'" )
            ]
    )




class AddOrdemForm(OrdemForm):
    submit = SubmitField(label="Criar Ordem")

class ModOrdemForm(OrdemForm):
    submit = SubmitField(label="Modificar Ordem")