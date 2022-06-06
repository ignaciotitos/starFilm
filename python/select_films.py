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
                        fila.append(fa_movie['id'])
                        fila.append(im_movie['imdbID'])
                        director_RT = DirectorScraper(director_name=fa_director)
                        director_RT.extract_metadata()
                        movies_RT = list(director_RT.metadata.keys())
                        try:
                            index = movies_RT.index(im[j]['title'])
                            title = movies_RT[index]
                            fila.append(director_RT.metadata[title]['Score_Rotten'])
                        except ValueError:
                            fila.append(int(0.0))

                        del im[j]
                        pelis.append(fila)
                        break
            else:
                del im[j]
                break
                 
    return pelis

#p = seleccion('Top Gun')
#print(p)

def actores(name):
    #imdb_actor = moviesDB.search_person(name)
    #fa_actor = service.search(cast = name)
    rt_actor = CelebrityScraper(celebrity_name = name)
    rt_actor.extract_metadata(section='highest')
    movies = rt_actor.metadata['movie_titles']
    pelis = []
    for i in range(len(movies)):
        fila = []
        print('rt ', movies[i])
        im = moviesDB.search_movie(movies[i])
        im = moviesDB.get_movie(im[0].getID())
        print('imbd ', im['title'])
        c = im['cast']
        for j in range(len(c)):
            if str(name).lower() == str(c[j]).lower():
                fa = service.search(title = movies[i])
                fa = service.get_movie(id = fa[0]['id'])
                print('fa', fa['title'])
                if name in fa['actors']:
                    fila.append(fa['id'])
                    fila.append(im['imdbID'])
                    rt_movie = MovieScraper(movie_title = movies[i])
                    rt_movie.extract_metadata()
                    fila.append(rt_movie.metadata['Score_Rotten'])
                    pelis.append(fila)
                    break
            else:
                continue
    return pelis

def lista_pelis_rating(title, peli_actor):
    info_total = []
    if peli_actor == True:
        pelis = seleccion(title)
    else:
        pelis = actores(title)
    
    for i in range(len(pelis)):
        sum = 0
        img = ""
        info_parcial = []
        for j in range(len(pelis[i])):
            if j == 0:
                fa = service.get_movie(id = pelis[i][j])
                sum += float(fa['rating'])
                img = get_img(id = pelis[i][j])
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

    return info_total

def eval_RT(movie_n):
    return calificacion(movie_n)/10.0

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

#a = actores("Leonardo DiCaprio")
#print(a)

def top_FA():
    top_NF = service.top_netflix(top = 3)
    top_HBO = service.top_hbo(top = 3)
    top_MOV = service.top_movistar(top = 3)
    return top_NF, top_HBO, top_MOV

#nf, hbo, mov = top_FA()
#print(hbo)

#pelis = seleccion('Top Gun')
#pelis[0][0] = ('6.5')
#print(pelis)
#print(len(pelis[0]))

"""""
im = moviesDB.search_movie('Top Gun')
fa = service.search(title = 'Top Gun')
print(im[0]['year'])
mov = service.get_movie(title = fa[0]['title'])
print(mov['year'])"""""

