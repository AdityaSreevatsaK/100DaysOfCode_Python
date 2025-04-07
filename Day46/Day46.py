from datetime import datetime

import requests
import spotipy
from bs4 import BeautifulSoup
from IPython.lib.pretty import pprint
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = '************'
spotify_client_secret = '************'

date_to_fetch_top_songs = 0
date_incorrectly_formatted = True
while date_incorrectly_formatted:
    try:
        date_to_fetch_top_songs = input(str('Which date would you like to travel to? /'
                                            'Please enter the date in YYYY-MM-DD:'))
        date_to_fetch_top_songs = datetime.strptime(date_to_fetch_top_songs, '%Y-%m-%d')
        date_incorrectly_formatted = False
    except ValueError:
        print("Invalid date format!")
date_to_fetch_top_songs = str(date_to_fetch_top_songs)[:10]

billboard_url = 'https://www.billboard.com/charts/hot-100/' + date_to_fetch_top_songs + '/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'
}

print(f'Performing web scraping to fetch top 100 songs from date {date_to_fetch_top_songs}')
billboard_response = requests.get(url=billboard_url, headers=header)
billboard_contents = billboard_response.text
soup = BeautifulSoup(billboard_contents, features='html.parser')

song_names_h3 = soup.select('li ul li h3')
song_names = [song.getText().strip() for song in song_names_h3]

print(f'Top hundred trending songs on {date_to_fetch_top_songs} : {song_names}')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-private',
                                               redirect_uri='http://example.com',
                                               client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               username='ASK'))
user_id = sp.current_user()['id']

song_uris = []
year = date_to_fetch_top_songs.split('-')[0]
for song in song_names:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

spotify_playlist = sp.user_playlist_create(user=user_id, name=f'{date_to_fetch_top_songs} Billboard 100', public=False)
pprint(spotify_playlist)
sp.playlist_add_items(playlist_id=spotify_playlist['id'], items=song_uris)
del sp
