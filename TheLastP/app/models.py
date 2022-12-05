from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'usuario'
    idUsers = db.Column(db.Integer, primary_key=True)
    usuarioN = db.Column(db.String(45))
    password = db.Column(db.String(64))

class Videojuegos(db.Model):
    __tablename__ = 'videojuegos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    apePa = db.Column(db.String(30))
    apeMa = db.Column(db.String(30))

class Personas(db.Model):
    __tablename__ = 'persona'
    idPersona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(30))
    apellidoPaterno = db.Column(db.String(30))
    apellidoMaterno = db.Column(db.String(30))
    correo = db.Column(db.String(64))
    animeFav = db.Column(db.String(35))