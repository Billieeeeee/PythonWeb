from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Videojuegos(db.Model):
    __tablename__ = 'videojuegos'
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(20))
    noplayers = db.column(db.Integer)