import os

import requests
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'
SAMPLE_ARTIST_ID = '06HL4z0CvFAxyc27GXpf02'

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
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
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