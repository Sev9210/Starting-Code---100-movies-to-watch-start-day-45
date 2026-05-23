# Write your code below this line 👇
import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movies = response.text

soup = BeautifulSoup(movies, 'html.parser')


movies = soup.select('div.article-title-description__text h3')
movie_list = [title.getText()for title in movies]
top_one_hundred_movies = sorted(
    movie_list,
    key=lambda x: int(''.join(filter(str.isdigit, x.split()[0])))
)

with open('Movies', 'w', encoding='utf-8') as fav_movies:
    for title in top_one_hundred_movies:
        fav_movies.write(f'{title}\n')
