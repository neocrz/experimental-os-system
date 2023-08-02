#  experimental-os-system
Um sistema de Ordem de Serviço (em Construção) feito em Flask. Utilizando sqlite.

Status: Minimamente Utilizável

## Funcionalidades
- Login
- Criação de Cliente
- Criação de Equipamentos
- Criação de Ordem de Serviço
- Impressão de Ordem de Serviço
- Banco de Dados (local ou externo)

## Configuração

`.env` exemplo:
```
DB_URI=
SECRET_KEY=
DB_EXT=
OS_OWNER_NAME=
OS_OWNER_INFO=
OS_OWNER_INFO2=
OS_OWNER_LOGO=
```

- `DB_URI`: conexão banco de dados
- `SECRET_KEY`: secret key
- `DB_EXT`: DB externa (TRUE para ativar db externo através de `DB_URI`)
- `OS_OWNER_NAME`: Nome da empresa a utilizar o sistema 
- `OS_OWNER_INFO`: String de informações sobre a empresa(endereço, bairro, cidade, estado, cep..)
- `OS_OWNER_INFO2`: String de informações sobre a empresa(email, telefone, cnpj)
- `OS_OWNER_LOGO`: URL do logo da empresa