import os

import requests
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import json

load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-read-recently-played user-library-read'
CACHE = '.spotipyoauthcache'

class SpotifyService():
    '''
    This class holds functions related to the Spotify API

    Member vars
    -----------
    spotify : Spotify API client
    headers : formatted access token for requests
    '''
    def __init__(self):
        '''
        Perform auth request with id/secret in env file
        '''
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(), auth_manager=SpotifyOAuth(scope=SCOPE, redirect_uri=SPOTIPY_REDIRECT_URI))
        auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
            })

        # convert the response to JSON
        auth_response_data = auth_response.json()

        # save the access token
        access_token = auth_response_data['access_token']
        self.headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
        
    def test(self): # pass in "self" to member functions
        print("test")
    
    def get_artist(self, id):
        artist = self.spotify.artist(id)
        return artist

    ### TODO ###

    def get_playlist(self, id):
        '''
        get playlist given playlist id 
        '''

    def get_n_tracks(self, playlist, n):
        '''
        get list of n random tracks (TODO: or lyrics?) from the playlist
        TODO: lyric scraping: --> https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3 
        '''

    def get_playlist_cover(self, lyrics):
        '''
        generate AI image using list of lyrics scraped
        '''

    def put_playlist_cover(self, image):
        '''
        after confirmation, set the playlist cover to AI image generated
        '''

    ### DATA EXPERIMENTATION ###
        
    def get_n_recent_tracks(self, n):
        tracks = self.spotify.current_user_recently_played(n)
        return tracks
    
    def get_properties(self, id):
        '''
        ** CREDIT: anushakuppahally on GitHub **
        This function returns the characteristics for a track
        This function uses a track's ID as an input 
        Then, this function returns a list of strings, floats, and integers
        Example output: ['Buzzcut Season', 'Pure Heroine', 'Lorde', '2013-09-27', 246755, 67, 0.606, 0.733, 0.62, 0.305, 0.117, -10.525, 0.075, 111.039, 4]
        '''
        meta = self.spotify.track(id)
        features = self.spotify.audio_features(id)
        name = meta['name']
        album = meta['album']['name']
        artist = meta['album']['artists'][0]['name']
        release_date = meta['album']['release_date']
        length = meta['duration_ms']
        popularity = meta['popularity']

        #song features
        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
        energy = features[0]['energy']
        instrumentalness = features[0]['instrumentalness']
        liveness = features[0]['liveness']
        loudness = features[0]['loudness']
        speechiness = features[0]['speechiness']
        tempo = features[0]['tempo']
        time_signature = features[0]['time_signature']

        track = {
        "name": name, 
        "album": album, 
        "artist": artist, 
        "release_date": release_date, 
        "length": length,
        "popularity": popularity,
        "acousticness": acousticness,
        "danceability": danceability,
        "energy": energy,
        "instrumentalness": instrumentalness,
        "liveness": liveness,
        "loudness": loudness,
        "speechiness": speechiness,
        "tempo": tempo,
        "time_signature": time_signature
        }

        return track


service = SpotifyService()
response = service.get_n_recent_tracks(5)
items = response['items']
track_ids = [track['track']['id'] for track in items]
for track_id in track_ids:
    properties = service.get_properties(track_id)
    print(json.dumps(properties, indent=4))
