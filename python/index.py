from flask import Flask, render_template, request
#from application import *
from scrapper_filmAffinity import *
from scrapperRT import * 
from scrapper_IMDb import *

app = Flask(__name__)

def comparar(movie_n):
    eval1 = get_rating(movie_n)
    eval2 = ratingFA(movie_n)
    eval3 = float(puntuacionRT(movie_n))/10.0
    suma = eval1 + float(eval2) + eval3
    media = round(suma/3.0, 1)
    return str(media)

@app.route('/')
def principal():
    return render_template("inicio.html")

@app.route('/busqueda', methods=['POST'])
def busqueda():
    id = request.form.get('Buscador')
    media = comparar(id)
    y, r, v, img = weee(id)
    x = puntuacionRT(id)
    z = reviewsRT(id)
    #print(y)
    return 'Hola ' + y + ' Puntuacion(RottenTomatoes) = '+ x +' Nº Reviews(RottenTomatoes) = '+z + ' '+img+'\n'+media


if __name__ == '__main__':
    app.run()


