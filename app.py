"""
Nombre: IA1
Materia: Inteligencia Artificial
Creador: Lucio David Morán Brizuela
Fecha: 23/11/2019
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola desde Flask!'

#Declarar otra ruta
@app.route('/miPagina') #Ruta: localhost:5000/miPagina
def miPagina():
    return "<html><head><title>Mi Primer Página</title></head><body><h1>Hola Mundo Peludo!</body></html>"

#Declaramos otra ruta y asociamos una función
@app.route('/miWeb')
def miWeb():
    name = "Lucio David Morán Brizuela"
    edad = 22
    materias = ["Inteligencia Artificial", "Python", "BDD NoSQL"]
    return render_template("misDatos.html", nombre= name, age = edad, listmat = materias)


if __name__ == '__main__':
    app.run()
