from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "Dados"

    cpf = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String())
    telefone = db.Column(db.String())
    cnpj = db.Column(db.String())
    nasc = db.Column(db.String())

    def __init__(self, nome, cpf, email, telefone, cnpj, nasc):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.cnpj = cnpj
        self.nasc = nasc
    def __repr__(self):
        return f"{self.nome}:{self.cpf}"