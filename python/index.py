from cgitb import html
from flask import Flask, render_template, request
from sqlalchemy import false
from numpy import empty
#from application import *
from scrapper_filmAffinity import *
from scrapperRT import * 
from scrapper_IMDb import *
from select_films import *


app = Flask(__name__)

#Devuelve el título del inicio.html
def titulo():
    id = request.form.get('Buscador')
    title = movie_name(id)
    return str(title)


"""def n_eval_RT(movie_n):
    return reviewsRT(movie_n)"""

#Llama a inicio.html con los tops de películas para enseñarlas por pantalla (Se actualizaran si las páginas cambian el top)
@app.route('/')
def principal():
    nf,hbo,mov = top_FA()

    return render_template("inicio.html", pelis_nf = nf, pelis_hbo = hbo, pelis_mov = mov)

#Llama a lookin.html que devuelve la información correspondiente a una lista de películas dada y las muestra de forma cómoda
@app.route('/busqueda', methods=['POST'])
def mostrar_info():
    n = titulo()
    m = service.get_movie(title = n)
    peli = False
    
    if (len(m) == 0):
        #actor
        peli = False
    else:
        if 'Documental' in m['genre']:
            peli = False #actor
        else:
            peli = True #peli

    
    #lista = lista_pelis_rating(n, peli)
    p = moviesDB.search_person(n)
    
    esta = False
    for i in range(len(p)):
        if n.lower() == str(p[i]).lower():
            esta = True
            break
        else:
            continue

    if peli == False and esta == False:
        return render_template('error.html')
    else:
        lista = lista_pelis_rating(n, peli)
        return render_template('lookin.html', busqueda = n, peliculas = lista) 
    #return "\nPuntuación media: " + comparar(n) + "\nPuntuación fA: " + eval_fA(n) + "\nPuntuación IMDb: " + str(eval_IMDb(n)) + "\nPuntuación RT: " + eval_RT(n) + "\nVotos fA: " + str(n_eval_fA(n)) + "\nVotos IMDb: " + str(n_eval_IMDb(n)) + "\nVotos RT: " + n_eval_RT(n) + "\nTitulo: " + n + "\nAño: " + str(anio(n)) + "\nDirector: " + dir(n) + "\nActores: " + actores(n) + "\nArgumento: " + str(argumento(n))
    #return render_template('lookin.html', puntuacion_media=comparar(n), puntuacion_fA=get_rating_fA(n), puntuacion_IMDb=str(get_rating(n)),
     #puntuacion_RT=x, titulo_texto=n, votos_fa=str(get_votes_fA(n)), votos_IMDb=str(get_votes(n)),
     #anio=str(get_year(n)), dir=get_directors(n), actores=get_actors(n), arg=str(get_argumento_fA(n)), imagen = get_img(n))
        

if __name__ == '__main__':
    app.run()


