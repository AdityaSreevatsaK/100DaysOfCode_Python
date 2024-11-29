import requests
from bs4 import BeautifulSoup

ehm_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
top_movies_webpage_response = requests.get(ehm_url)
top_movies_webpage_contents = top_movies_webpage_response.text

soup = BeautifulSoup(top_movies_webpage_contents, features='html.parser')
top_movies = []
h3_tags = soup.find_all(name='h3', class_='title')
movies = [movie.getText() for movie in h3_tags][::-1]

with open('Top 100 Greatest Movies of All Time.txt', mode='w', encoding='utf-8') as movies_file:
    for item in movies:
        try:
            movies_file.write(item + '\n')
        except UnicodeEncodeError as uee:
            print(f'Error encountered at item {item}')
print('Data written into file successfully.')
