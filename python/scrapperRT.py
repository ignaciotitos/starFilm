from bs4 import BeautifulSoup
import requests
from rotten_tomatoes_scraper.rt_scraper import MovieScraper, DirectorScraper, CelebrityScraper

def puntuacionRT(data):
    data = data.replace(' ', '_')
    data = data.replace(':', '_')
    website = 'https://www.rottentomatoes.com/m/'+data+''
    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('div', id='mainColumn')
    box2 = box.find('div', class_='thumbnail-scoreboard-wrap')
    atributo = box2.select_one('score-board')

    resultado = atributo.get_attribute_list('tomatometerscore')

    return(str(resultado[0]))

def reviewsRT(data):
    data = data.replace(' ', '_')
    data = data.replace(':', '_')
    website = 'https://www.rottentomatoes.com/m/'+data+''
    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('div', id='mainColumn')
    box2 = box.find('div', class_='thumbnail-scoreboard-wrap')

    numeroReviews = soup.find('a', class_='scoreboard__link scoreboard__link--tomatometer').get_text()

    return(numeroReviews)

def calificacion(movie):
    try:
        movie = movie.replace(':', ' ')
        movie_scraper = MovieScraper(movie_title=movie)
        movie_scraper.extract_metadata()

        return(float(movie_scraper.metadata['Score_Rotten']))
    except BaseException:
        return(0.0)

#movie = DirectorScraper(director_name='Christopher Nolan')
#person = CelebrityScraper(celebrity_name='Leonardo')
#person.extract_metadata(section='highest')
#print(person.metadata.keys())
#movies = person.metadata['movie_titles']
#print(movies)
#movie.extract_metadata()
#rt_movie = MovieScraper(movie_title = 'Catch Me if You Can')
#rt_movie.extract_metadata()
#print(rt_movie.metadata.keys())
#r = list(movie.metadata.keys())
#print(r)
#stri = 'Tenet'
#index = r.index(stri)
#title = r[index]
#print(movie.metadata[title]['Score_Rotten'])