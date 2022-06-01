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

print(id)
urllib3.disable_warnings()
service = python_filmaffinity.FilmAffinity()
movie = service.get_movie(title='Top Gun')
print(movie['title'])
print(movie['directors'])
print(movie['actors'])
print(movie['rating'])
#t = service.get_movie(title='El padrino (1979)', images=True)
#print(welcome)
def weee (data):
    mov = service.get_movie(title=data)
    return mov['title']