from app import create_app
from app.migrate import init_db
from flask import render_template, request, url_for, redirect, flash
from app.models import Videojuegos, db, Personas, Users


app = create_app()


@app.route('/database')
def create_db():
    init_db()
    return "La base de datos ha sido creada"


@app.route('/index', methods=["POST", "GET"])
def index():
    #return redirect(url_for('index'))
    return render_template("index.html")


@app.route('/todolist')
def prueba():
    return render_template("prueba.html", x = Videojuegos.query.all())

@app.route('/', methods=["POST", "GET"])
def registro():
    
    if request.method == "POST":
        user = request.form["user"]
        passw = request.form["pss"]
        
        auxuser = Users.query.filter_by(usuarioN = user).first()

        if auxuser:
            flash("Usuario ya registrado, intente de nuevo")
            return render_template("login.html")

        else:

            usuarion = Users(
                usuarioN = user,
                password = passw,

            )

            db.session.add(usuarion)
            db.session.commit()
            return render_template("index.html")
        
        
    else:
        return render_template("login.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    
    if request.method == "POST":
        user = request.form["usr2"]
        passw = request.form["contra2"]
        
        auxuser = Users.query.filter_by(usuarioN = user, password = passw).first()

        if auxuser:
            return render_template("index.html")

        else:
            flash("Usuario no encontrado, intente de nuevo")
            return render_template("login.html")

    else:
        return render_template("login.html")
        
       
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



@app.route('/altas', methods=["POST", "GET"])
def alta():
    
    if request.method == "POST":
        nombre = request.form["nom"]
        apPaterno = request.form["apPat"]
        apMaterno = request.form["amMat"]   
        correo = request.form["gmail"]   
        animeFav = request.form["daram"]   
        
        pochita = Personas(
            nombre = nombre, #izquierda variables de models, derecha vienen de linea 58
            apellidoPaterno  = apPaterno,
            apellidoMaterno = apMaterno,
            correo = correo,
            animeFav  = animeFav,
        )

        db.session.add(pochita)
        db.session.commit()

        return render_template("consulta.html", nbr = nombre, paterno = apPaterno, materno = apPaterno, mail = correo, animeF = animeFav, regi=Personas.query.all())
    else:
        return render_template("consulta.html")
        


@app.route('/Consultas', methods=["GET", "POST"])
def consulta():

    if request.method == "POST":

        idBuscar = request.form.getlist('idElim')
        #print(request.form.get("idElim"))
        #print(idBuscar)
        
        Personas.query.filter_by(idPersona=idBuscar).delete()
        db.session.commit()
         
        return render_template("consulta.html", regi=Personas.query.all())

    else:
        return render_template("consulta.html", regi=Personas.query.all())


@app.route('/Bajas', methods=["GET", "POST"])
def baja():

    if request.method == "POST":

        idBuscar = request.form.getlist('idElim')
        print(request.form.get("idElim"))
        print(idBuscar)
        
        #Personas.query.filter_by(id=idBuscar).delete()
        #db.session.commit()
         
        return render_template("consulta.html", regi=Personas.query.all())

    else:
        return render_template("consulta.html", regi=Personas.query.all())

    

@app.route('/update/<int:idPersona>', methods=['GET', 'POST'])
def update(idPersona):


   # prsnUP = Personas.query.get_or_404(idPersona)

    foundPrsn1 = Personas.query.filter_by(idPersona=idPersona).first()
    
    if request.method == "POST":

        foundPrsn = Personas.query.filter_by(idPersona=idPersona).first()
        foundPrsn.nombre = request.form["nom2"]
        foundPrsn.apellidoPaterno = request.form["apPat2"]
        foundPrsn.apellidoMaterno = request.form["amMat2"]
        foundPrsn.correo = request.form["gmail2"]
        foundPrsn.animeFav = request.form["daram2"]
        print(foundPrsn)

        db.session.commit()

        return render_template("consulta.html", regi=Personas.query.all())

    else:
        return render_template("update.html", foundPrsn = foundPrsn1)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

