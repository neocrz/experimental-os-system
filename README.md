#  experimental-os-system
Um sistema de Ordem de Serviço (em Construção) feito em Flask. Utilizando sqlite.

Status: Parcialmente Utilizável

## Funcionalidades
- Login
- Criação de Cliente
- Criação de Ordem de Serviço
- Banco de Dados (local ou externo)

## Configuração

`.env` exemplo:
```
DB_URI= 
SECRET_KEY={secret_key}
DB_EXT=FALSE {TRUE para usar um bando de dados}
```
- `DB_URI`: conexão banco de dados
- `SECRET_KEY`: secret key
- `DB_EXT`: DB externa (TRUE para ativar db externo através de `DB_URI`)