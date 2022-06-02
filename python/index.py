from flask import Flask, render_template, request
#from application import *
from scrapper_filmAffinity import movie, weee
from scrapperRT import * 

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("inicio.html")

@app.route('/busqueda', methods=['POST'])
def busqueda():
    id = request.form.get('Buscador')
    y = weee(id)
    x = puntuacionRT(id)
    z = reviewsRT(id)
    #print(y)
    return 'Hola ' + y + ' Puntuacion(RottenTomatoes) = '+ x +' Nº Reviews(RottenTomatoes) = '+z


if __name__ == '__main__':
    app.run()


