from datetime import datetime
from typing import Any
from dataclasses import dataclass
from Data.base import db

@dataclass
#db.Model
class Oficina():
    # Informações Básicas da Empresa
    id:int #= db.Column(db.Integer, primary_key#=True)
    cnpj: int #= db.Column(db.Integer(14))
    razao_social: str  #= db.Column(db.String)
    nome_fantasia: str  #= db.Column(db.String)

    # Informações de Contato:
    logradouro: str  #= db.Column(db.String)
    numero: int #= db.Column(db.Integer(4))
    bairro: str  #= db.Column(db.String)
    cidade: str  #= db.Column(db.String)
    uf: str  #= db.Column(db.String(2))
    cep: int #= db.Column(db.Integer(8))
    telefone: int #= db.Column(db.Integer)
    email: str  #= db.Column(db.String)

    # Responsáveis e Contato Comercial
    nome_responsavel: str  #= db.Column(db.String)
    cargo_responsavel: str  #= db.Column(db.String)
    telefone_comercial: int #= db.Column(db.Integer)
    email_comercial: str  #= db.Column(db.String)

    # Informações Financeiras:
    dados_bancarios: str  #= db.Column(db.String)


   