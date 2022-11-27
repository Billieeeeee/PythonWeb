from flask import Flask, render_template, request
#from flaskext.mysql import MySQL

app = Flask(__name__)
#mysql = MySQL()


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/database')
def create_db():
    init_db()
    return "La base de datos ha sido creada"

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
        
        wordlist = user.split() #split para contar espacios en blanco
        wordlist2 = apellidoP.split() #split para contar espacios en blanco
        wordlist3 = apellidoM.split() #split para contar espacios en blanco
        numChars = 0
        numChars2 = 0
        numChars3 = 0

        for word in wordlist:#recorrer toda la lista
            numChars += len(word)

        for word2 in wordlist2:#recorrer toda la lista
            numChars2 += len(word2)

        for word3 in wordlist3:#recorrer toda la lista
            numChars3 += len(word3)
        
        return render_template("consulta.html", usr = user, ap = apellidoP, am = apellidoM, cont = len(wordlist), lista = numChars, lista2 = numChars2, lista3 = numChars3)
    else:
        return render_template("login.html")
        
        #redirect se utiliza cuando solamente queremos enviar al usuario a una pag. diferente
        #secret key para enviar mensajes flash

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route('/testdb')
def testdb():
    mysql.init_app(app)
    cursor = mysql.connection.cursor()
    cursor.execute("select * from users")



if __name__ == "__main__":
    app.run(debug=True, port=5000)

