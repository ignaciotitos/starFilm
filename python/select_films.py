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
    
    pelis = []

    #print(len(fa))
    #print(len(im))
    
    for i in range(len(fa)):
        fa_movie = service.get_movie(id = fa[i]['id'])
        fa_year = int(fa_movie['year'])
        fa_director = str(fa_movie['directors'][0])
        #print(i,' : fa : ',fa_year)
        fila = []

        for j in range(len(im)):
            im_movie = moviesDB.get_movie(im[j].getID())
            #print(j,"yii")
            if 'director' in im_movie.keys():
                imdb_year = int(im_movie['year'])
                imdb_director = str(im_movie['director'][0])
                #print(j,' : imdb : ',imdb_year)

                if fa_year == imdb_year:
                    if fa_director == imdb_director:
                        fila.append(fa_movie['title'])
                        fila.append(im_movie['title'])
                        director_RT = DirectorScraper(director_name=fa_director)
                        director_RT.extract_metadata()
                        movies_RT = list(director_RT.metadata.keys())
                        try:
                            index = movies_RT.index(im[j]['title'])
                            title = movies_RT[index]
                            fila.append(director_RT.metadata[title]['Score_Rotten'])
                        except ValueError:
                            fila.append('NaN')
                            
                        del im[j]
                        pelis.append(fila)
                        break
            else:
                del im[j]
                break
                 
    return pelis

p = seleccion('Top Gun')
print(p)

def top_pelis_FA():
    top = service.top_netflix()
    return top

#t = top_pelis_FA()
#print(t)

"""""
im = moviesDB.search_movie('Top Gun')
fa = service.search(title = 'Top Gun')
print(im[0]['year'])
mov = service.get_movie(title = fa[0]['title'])
print(mov['year'])"""""

