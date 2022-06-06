from flask import Flask, render_template, request
#from application import *
from scrapper_filmAffinity import *
from scrapperRT import * 
from scrapper_IMDb import *
from select_films import *


app = Flask(__name__)

def titulo():
    id = request.form.get('Buscador')
    title = movie_name(id)
    return str(title)


"""def n_eval_RT(movie_n):
    return reviewsRT(movie_n)"""

@app.route('/')
def principal():
    nf,hbo,mov = top_FA()

    return render_template("inicio.html", pelis_nf = nf, pelis_hbo = hbo, pelis_mov = mov)

@app.route('/busqueda', methods=['POST'])
def mostrar_info():
    n = titulo()
    lista = lista_pelis_rating(n)

    #return "\nPuntuación media: " + comparar(n) + "\nPuntuación fA: " + eval_fA(n) + "\nPuntuación IMDb: " + str(eval_IMDb(n)) + "\nPuntuación RT: " + eval_RT(n) + "\nVotos fA: " + str(n_eval_fA(n)) + "\nVotos IMDb: " + str(n_eval_IMDb(n)) + "\nVotos RT: " + n_eval_RT(n) + "\nTitulo: " + n + "\nAño: " + str(anio(n)) + "\nDirector: " + dir(n) + "\nActores: " + actores(n) + "\nArgumento: " + str(argumento(n))
    #return render_template('lookin.html', puntuacion_media=comparar(n), puntuacion_fA=get_rating_fA(n), puntuacion_IMDb=str(get_rating(n)),
     #puntuacion_RT=x, titulo_texto=n, votos_fa=str(get_votes_fA(n)), votos_IMDb=str(get_votes(n)),
     #anio=str(get_year(n)), dir=get_directors(n), actores=get_actors(n), arg=str(get_argumento_fA(n)), imagen = get_img(n))
    return render_template('lookin.html', busqueda = n, peliculas = lista) 

if __name__ == '__main__':
    app.run()


