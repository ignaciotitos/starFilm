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
    n = titulo() #Se obtiene lo que se ha puesto en el buscador.
    m = service.get_movie(title = n) #Se obtiene la pelicula
    peli = False #con esto vemos si es pelicula o actor lo que se busca
    
    if (len(m) == 0): #si es 0, es decir, no hay nada cuando buscas una pelicula, es porque será actor
        #actor
        peli = False
    else:
        if 'Documental' in m['genre']: #si en el género es un documental en la pelicula que obtienes es porque estas buscando un actor que han hecho un documental sobre el.
            peli = False #actor
        else: #sino pues sera una pelicula
            peli = True #peli

    p = moviesDB.search_person(n) #buscamos la persona para ver los actores que salen con ese nombre
    
    esta = False
    for i in range(len(p)):
        if n.lower() == str(p[i]).lower(): #Vemos si el actor esta contenido, lo que seguramente sea asi ya que salen los actores relacionados con el nombre.
            esta = True
            break
        else:
            continue

    if peli == False and esta == False: # si no sale pelicula ni actor que lance un error.
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


