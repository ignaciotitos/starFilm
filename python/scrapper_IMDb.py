import imdb

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
