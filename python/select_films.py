from scrapper_IMDb import *
from scrapper_filmAffinity import *
from scrapperRT import *

def seleccion(movie_title):
    ## Nombres de los scrappers importados de sus respectivas clases
    #imdb --> moviesDB
    #FA --> service
    #RT --> MovieScraper()

    im = moviesDB.search_movie(movie_title)
    fa = service.search(title = movie_title)
    tam = 0
    if len(im) > len(fa):
        tam = len(fa)
    else:
        tam = len(im)
    
    pelis = []

    #print(len(fa))
    #print(len(im))
    
    for i in range(len(fa)):
        fa_movie = service.get_movie(id = fa[i]['id'])
        fa_year = int(fa_movie['year'])
        fa_director = str(fa_movie['directors'][0])
        print(i,' : fa : ',fa_year)
        fila = []

        for j in range(len(im)):
            im_movie = moviesDB.get_movie(im[j].getID())

            if 'director' in im_movie.keys():
                imdb_year = int(im_movie['year'])
                imdb_director = str(im_movie['director'][0])
                print(j,' : fa : ',imdb_year)

                if fa_year == imdb_year:
                    if fa_director == imdb_director:
                        fila.append(fa_movie['title'])
                        fila.append(im[j]['title'])
                        del im[j]
                        pelis.append(fila)
                        break
            else:
                print('No hay na')
                 
    return pelis

p = seleccion('Origen')
print(p)

"""""
im = moviesDB.search_movie('Top Gun')
fa = service.search(title = 'Top Gun')
print(im[0]['year'])
mov = service.get_movie(title = fa[0]['title'])
print(mov['year'])"""""

