import imdb
import numpy

moviesDB = imdb.IMDb()

#FUNCIONES
#Set película
#Obtener título 
#Obtener año 
#Obtener puntuación
#Obtener nº puntuciones
#Obtener director/es
#Obtener actores 

#Devolver pelicula de IMDb
def movie_name(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  return movie

#Obtener título
def get_title(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  title = movie['title']
  return title

#Obtener año 
def get_year(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  year = movie['year']
  return year

#Obtener puntuación
def get_rating(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  rating = movie ['rating']
  return rating

#Obtener nº puntuciones
def get_votes(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  votes = movie ['votes']
  return votes

#Obtener argumento
def get_plot(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  plot = movie ['plot']
  return plot

#Obtener director/es
def get_directors(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  directors = movie['directors']
  direcStr = ' '.join(map(str, directors))
  return direcStr

#Obtener actores 
def get_actors(movie_n):
  movies = moviesDB.search_movie(movie_n)
  movie = moviesDB.get_movie(movies[0].getID())
  casting = movie['cast']
  actors = ' '.join(map(str, casting))
  return actors

def get_list_IMDB(movie_n):
  p = moviesDB.search_movie('Top Gun')
  print(p.size)


#p = moviesDB.search_person('Leonardo DiCaprio')
#print(len(p))
#print(p[3]['full-size headshot'])
#print(p[3]['long imdb name'])
n#ame = 'Emma Watson'
#mov = moviesDB.search_movie(name)
#mov = moviesDB.get_movie(mov[0].getID())
#c = mov['cast']
#for i in range(len(c)):
  #print(c[i])
#  if name.lower() == str(c[i]).lower():
#    print(c[i])
#    break
#  else:
#    print('no ta mano')
#    continue
#stri = 'Christopher Nolan'
#name = 'Leonardo DiCaprio'
#c = mov['cast']
#for i in range(len(c)):
  #print(c[i])
#  if name.lower() == str(c[i]).lower():
#    print(c[i])
#    break
#  else:
    #print('no ta mano')
#    continue
#info = moviesDB.get_person_infoset()
#print(info[2])
#print(p[0].keys())
#print(p[0].get_person_infoset())
#if 'director' in mov.keys():
#  print('yes')
#else:
#  print('no')
#r = str(mov['director'][0])
#r = r.split("_")
#print(r == stri)
#print(r)
#print(stri)
#p[4].getID() 
#print('Leonardo'.lower())