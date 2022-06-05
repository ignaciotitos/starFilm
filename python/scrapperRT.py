from bs4 import BeautifulSoup
import requests
from rotten_tomatoes_scraper.rt_scraper import MovieScraper

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

#movie = MovieScraper(movie_title='Top Gun')
#movie.extract_metadata()
#print(movie.metadata)