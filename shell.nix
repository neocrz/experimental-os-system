# shell.nix
{ pkgs ? import <nixpkgs> {} }:
let
  my-python-packages = ps: with ps; [
    flask
    requests
    flask-sqlalchemy
    wtforms
    python-dotenv
    gunicorn
    psycopg2
    flask-wtf
    flask-login
    flask-bcrypt
    email-validator
    bcrypt
    # other python packages
  ];
  my-python = pkgs.python3.withPackages my-python-packages;
in my-python.env
