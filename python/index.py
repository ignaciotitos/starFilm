from flask import Flask, render_template, request
#from application import *
from scrapper_filmAffinity import *
from scrapperRT import * 
from scrapper_IMDb import *


app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("inicio.html")

def titulo():
    id = request.form.get('Buscador')
    title = movie_name(id)
    return str(title)

def comparar(movie_n):
    eval1 = get_rating(movie_n)
    print(eval1)
    eval2 = get_rating_fA(movie_n)
    print(eval2)
    eval3 = eval_RT(movie_n)
    print(eval3)

    if eval3 == 0.0:
        suma = eval1 + float(eval2)
        media = round(suma/2.0, 1)
    else:
        suma = eval1 + float(eval2) + eval3
        media = round(suma/3.0, 1)

    return str(media)

def eval_RT(movie_n):
    return calificacion(movie_n)/10.0

"""def n_eval_RT(movie_n):
    return reviewsRT(movie_n)"""

@app.route('/busqueda', methods=['POST'])
def mostrar_info():
    n = titulo()
    x = eval_RT(n)

    if x==0.0:
        x = "No hay resultados en RT"
    #return "\nPuntuación media: " + comparar(n) + "\nPuntuación fA: " + eval_fA(n) + "\nPuntuación IMDb: " + str(eval_IMDb(n)) + "\nPuntuación RT: " + eval_RT(n) + "\nVotos fA: " + str(n_eval_fA(n)) + "\nVotos IMDb: " + str(n_eval_IMDb(n)) + "\nVotos RT: " + n_eval_RT(n) + "\nTitulo: " + n + "\nAño: " + str(anio(n)) + "\nDirector: " + dir(n) + "\nActores: " + actores(n) + "\nArgumento: " + str(argumento(n))
    return render_template('lookin.html', puntuacion_media=comparar(n), puntuacion_fA=get_rating_fA(n), puntuacion_IMDb=str(get_rating(n)),
     puntuacion_RT=x, titulo_texto=n, votos_fa=str(get_votes_fA(n)), votos_IMDb=str(get_votes(n)),
     anio=str(get_year(n)), dir=get_directors(n), actores=get_actors(n), arg=str(get_argumento_fA(n)), imagen = get_img(n))

if __name__ == '__main__':
    app.run()


