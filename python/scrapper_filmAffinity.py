from ctypes import cast
from turtle import title
from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib3
import python_filmaffinity
#from index import welcome
#website = 'https://www.filmaffinity.com/es/main.html'
#response = requests.get(website)

#content = response.text

#soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

#<div id="movie-rat-avg" itemprop="ratingValue" content="7.8"> 7,8 </div>

#print(id)
urllib3.disable_warnings()
service = python_filmaffinity.FilmAffinity()

#movie = service.get_movie(title='Top Gun')
#print(movie['title'])
#print(movie['directors'])
#print(movie['actors'])
#print(movie['rating'])

#print(dir(service)) 
#print(movie.keys()) #para ver todas las opciones que se pueden buscar
p = service.search(10, title = 'Top Gun')
#print(p[0])
ti = p[1]['title']
print(ti)
#print(movie.items())
def weee (data):
    mov = service.get_movie(title=data)
    id = mov['id']
    web = 'https://www.filmaffinity.com/es/film'+id+'.html'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    img = soup.find('div', id='right-column').find('div', id='movie-main-image-container').find('a', class_='lightbox').get('href')
    #img2 = mov['poster'] 

    return mov['title'], mov['rating'], mov['votes'], img #img2

def ratingFA(data):
    mov = service.get_movie(title=data)
    return mov['rating']