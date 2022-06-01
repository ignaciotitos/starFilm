from bs4 import BeautifulSoup
import requests
import urllib3
import python_filmaffinity
#website = 'https://www.filmaffinity.com/es/main.html'
#response = requests.get(website)

#content = response.text

#soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

#<div id="movie-rat-avg" itemprop="ratingValue" content="7.8"> 7,8 </div>

urllib3.disable_warnings()
service = python_filmaffinity.FilmAffinity()
movie = service.get_movie(title='Indiana Jones 5')
print(movie['title'])
print(movie['directors'])
print(movie['actors'])