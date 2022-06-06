from operator import itemgetter
from types import NoneType
from scrapper_IMDb import *
from scrapper_filmAffinity import *
from scrapperRT import *

#Función Clave: Devuelve una lista con las películas que más se parecen al nombre dado por el usuario, dicha lista contiene conjuntos que contienen a su vez el id de FA, el id de IMDb y la puntuación de RT
def seleccion(movie_title):
    ## Nombres de los scrappers importados de sus respectivas clases
    #imdb --> moviesDB
    #FA --> service
    #RT --> MovieScraper()

    # Obtengo las películas de una búsqueda en imdb y en FilmAffinity
    # Tienen un tope por default a no ser que se lo pongas tu.
    im = moviesDB.search_movie(movie_title) 
    fa = service.search(title = movie_title)
    
    # Para guardar las peliculas
    pelis = []

    #print(len(fa))
    #print(len(im))
    
    #Vamos a iterar las películas obtenidas en FA.
    #Creemos que era mejor así ya que era el que más tardaba en obtener los datos.
    for i in range(len(fa)):
        fa_movie = service.get_movie(id = fa[i]['id']) #Obtengo la pelicula 0, ya que lo que cogemos con el search devuelve una lista de peliculas con todos sus datos
        fa_year = int(fa_movie['year']) #Obtengo el año para comparar y cerciorarnos de que es la misma pelicula
        fa_director = str(fa_movie['directors'][0]) #Obtengo el director para cerciorarme x2 de que es la misma pelicula
        #print(i,' : fa : ',fa_year)
        fila = []

        for j in range(len(im)): #iteramos las peliculas de imdb obtenidas
            im_movie = moviesDB.get_movie(im[j].getID())
            
            if 'director' in im_movie.keys(): #si hay director, porque es posible que no este el dato de 'director'
                imdb_year = int(im_movie['year']) #obtenemos el año y el director.
                imdb_director = str(im_movie['director'][0]) #puede que haya dos directores, con el primero nos basta

                if fa_year == imdb_year: 
                    if fa_director == imdb_director:
                        fila.append(fa_movie['id']) #metemos el id de la peli, ya que es lo mas fiable porque el titulo puede derivar en dos peliculas distintas
                        fila.append(im_movie['imdbID']) #idem con el de imdb
                        director_RT = DirectorScraper(director_name=fa_director) #hacemos lo de antes pero con rotten
                        director_RT.extract_metadata() #extraemos los datos.
                        movies_RT = list(director_RT.metadata.keys())
                        try: #es posible que rotten no tenga valoracion, por lo que probamos para que no salten errores
                            index = movies_RT.index(im[j]['title'])
                            title = movies_RT[index]
                            fila.append(director_RT.metadata[title]['Score_Rotten'])
                        except ValueError:
                            fila.append(int(0.0))

                        del im[j] #si ya se ha visto la pelicula la borramos para no seguir iterandola más tarde.
                        pelis.append(fila)
                        break
            else:
                del im[j] #si no tiene director borramos la pelicula porque no nos interesa.
                break
                 
    return pelis

#p = seleccion('Top Gun')
#print(p)

def actores(name): #vamos a hacer la seleccion por actores
    
    rt_actor = CelebrityScraper(celebrity_name = name) #Cogemos el actor por el scrapper de rotten
    rt_actor.extract_metadata(section='highest')
    movies = rt_actor.metadata['movie_titles'] #Esto nos permite sacar las peliculas de una manera fácil
    pelis = []

    for i in range(len(movies)): #Vamos a iterar las películas obtenidas
        fila = []
        
        im = moviesDB.search_movie(movies[i]) #Sacamos las películas con ese título, o todas las posibles
        im = moviesDB.get_movie(im[0].getID()) #Con esto vamos a sacar la información completa de la primera película, ya que al tener el título completo, seguramente la primera sea la buena
        
        c = im['cast'] #Sacamos los actores de la pelicula
        for j in range(len(c)):
            if str(name).lower() == str(c[j]).lower(): #Con esto vemos si el actor pertenece al reparto.
                fa = service.search(title = movies[i]) #si pertenece, buscamos la pelicula en FA y hacemos lo mismo, 
                fa = service.get_movie(id = fa[0]['id']) #sacamos el reparto y vemos si el actor pertenece a el.
                
                if name in fa['actors']: #en caso de que pertenezca
                    rt_movie = MovieScraper(movie_title = movies[i]) #Sacamos la pelicula de rotten para obtener su puntuacion, que nos viene bien luego para hacer la media.
                    try:                #hay posibles errores al obtener puntuaciones y no haya, por lo que probamos que no nos de ese error.
                        mov = rt_movie.extract_metadata()
                    except HTTPError: 
                        break
                    fila.append(fa['id'])
                    fila.append(im['imdbID'])
                    #rt_movie = MovieScraper(movie_title = movies[i])
                    #rt_movie.extract_metadata()

                    if rt_movie.metadata['Score_Rotten'] == '':
                        fila.append(0.0)
                    else:
                        fila.append(rt_movie.metadata['Score_Rotten'])
                    pelis.append(fila)
                    break
                else:
                    continue
            else:
                continue
    return pelis #Obtenemos una lista de listas igual que en peliculas ya que para el siguiente metodo nos viene bien y no tener que hacer dos.

#Función Clave: Devuelve una lista con la informacion perteneciente a cada una de las películas que se relacionan con lo que el usuario haya introducido (actor o película)
def lista_pelis_rating(title, peli_actor):
    info_total = []
    #Vemos si los datos son referentes a un actor o una pelicula.
    if peli_actor == True:
        pelis = seleccion(title)
    else:
        pelis = actores(title)

    for i in range(len(pelis)): #iteramos todas las peliculas que haya
        print(i)
        sum = 0
        img = ""
        info_parcial = []
        for j in range(len(pelis[i])): #iteramos lo que hay en 1--> id_FA, 2--> id_IMDB, 3--> Valoracion rotten
            if j == 0:
                fa = service.get_movie(id = pelis[i][j])
                if fa['rating'] is not NoneType: #Si es nonetype, es decir, no hay valoracion, se coge un 0
                    sum += float(fa['rating'])
                else:
                    sum += 0.0
                img = get_img(id = pelis[i][j]) #Se obtiene la imagen para plasmarla en el html
            elif j == 1: 
                ia = moviesDB.get_movie(pelis[i][j])
                sum += ia['rating']
            else:
                sum += ( float(pelis[i][j]) / 10.0 )
                if pelis[i][j] == 0.0:
                    sum /= 2.0
                else:
                    sum /= 3.0
                    
        info_parcial.append(ia['title'])
        info_parcial.append(img)
        info_parcial.append(fa['rating'])
        info_parcial.append(ia['rating'])
        info_parcial.append(pelis[i][j])
        info_parcial.append(sum)
        info_parcial.append(ia['cast'])
        info_parcial.append(ia['directors'])
        info_parcial.append(ia['year'])
        info_parcial.append(ia['plot'])
        info_total.append(info_parcial)

    #print(info_total)
    sorted(info_total, key=itemgetter(5))
    return info_total

#Obtiene la calificación de RT pero en formato de 0 a 10
def eval_RT(movie_n):
    return calificacion(movie_n)/10.0

#Obtiene la media de los ratings de las peliculas 
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

#a = lista_pelis_rating("Jack Nicholson", False)
#a = numpy.array(a, dtype=object)
#print(a)
#a = actores('Jack Nicholson')
#print(a)

#Función Clave: Devuelve la información de las películas que se encuentran en el top 3 más populares en Netflix, HBO y Movistar
def top_FA():
    top_NF = service.top_netflix(top = 3)
    top_HBO = service.top_hbo(top = 3)
    top_MOV = service.top_movistar(top = 3)
    return top_NF, top_HBO, top_MOV

