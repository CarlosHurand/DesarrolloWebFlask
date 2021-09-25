from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con.Escuela
cuentas = db.alumno

app = Flask (__name__)

@app.route('/')
def index():
    
    cursor = cuentas.find()
    user = []
    for doc in cursor:
        user.append(doc)

    return render_template('/users.html', data = user)

@app.route('/insert')
def insert():
    
    user = {"matricula": "34", "nombre": "Julion", "correo": "julion@itesm.mx", "contrasena": "2314" }
    
    try:
        cuentas.insert_one(user)
        return "<a href = '/'> Ver usuarios </a>"
    
    except Exception as e:
        return "%s" % e

@app.route('/login', methods = ["GET", "POST"])
def login():
    
    if request.method == 'POST':
        
        password = request.form["password"]
    
        return "Tu password es: %s" % password
    else:
        return "No jala"

@app.route('/test<data>')
def test(data):
    return "Hola %s!" % data

if __name__ == "__main__":
    app.run(debug = True)

