from bs4 import BeautifulSoup
import requests

def puntuacionRT(data):
    data = data.replace(' ', '_')
    data = data.replace(': ', '_')
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
    data = data.replace(': ', '_')
    website = 'https://www.rottentomatoes.com/m/'+data+''
    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('div', id='mainColumn')
    box2 = box.find('div', class_='thumbnail-scoreboard-wrap')

    numeroReviews = soup.find('a', class_='scoreboard__link scoreboard__link--tomatometer').get_text()

    return(numeroReviews)