from bs4 import BeautifulSoup
import requests

website = 'https://www.rottentomatoes.com/m/paris_13th_district'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('div', id='mainColumn')
box2 = box.find('div', class_='thumbnail-scoreboard-wrap')
atributo = box2.select_one('score-board')

score = atributo.get_attribute_list('tomatometerscore')
print("Puntuacion =",int(score[0]))

numeroReviews = box2.find('a', class_='scoreboard__link scoreboard__link--tomatometer').get_text()
print(numeroReviews)