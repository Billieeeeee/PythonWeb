from app import create_app
from app.migrate import init_db
from flask import render_template, request, url_for, redirect
from app.models import *
from sqlalchemy import delete

app = create_app()


@app.route('/database')
def create_db():
    init_db()
    return "La base de datos ha sido creada"


@app.route('/', methods=["POST", "GET"])
def index():
    #return redirect(url_for('index'))
    return render_template("index.html")


@app.route('/todolist')
def prueba():
    lista = ['APEX', 'VALORANT', 'HALO']
    return render_template("prueba.html", x=lista)

@app.route("/login", methods=["POST", "GET"])
def login():
    
    if request.method == "POST":
        user = request.form["nm"]
        apellidoP = request.form["ap"]
        apellidoM = request.form["am"]   
        
        videog = Videojuegos(
            name = user,
            apePa = apellidoP,
            apeMa = apellidoM
        )

        db.session.add(videog)
        db.session.commit()

        return render_template("consulta.html", usr = user, ap = apellidoP, am = apellidoM, values=Videojuegos.query.all())
    else:
        return render_template("login.html")
        
        #redirect se utiliza cuando solamente queremos enviar al usuario a una pag. diferente
        #secret key para enviar mensajes flash

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



@app.route('/Consultas', methods=["GET", "POST"])
def consulta():

    if request.method == "POST":
        idBuscar = request.form["idEl"]

        idEliminar = Videojuegos.query.get(idBuscar)
        
        db.session.delete(idEliminar)
        db.session.commit()
         
        return render_template("consulta.html", values=Videojuegos.query.all())

    else:
        return render_template("consulta.html", values=Videojuegos.query.all())



if __name__ == "__main__":
    app.run(debug=True, port=5000)

