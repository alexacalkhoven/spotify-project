# ```python -m unittest test.test``` on cmd

import unittest

from src.spotify_service import SpotifyService


class TestSpotifyService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = SpotifyService()

    def test_get_artist(self):
        artist_id = '06HL4z0CvFAxyc27GXpf02'
        artist = self.service.get_artist(artist_id)
        self.assertEqual(artist['name'], "Taylor Swift")

    def test_get_n_recent_tracks(self):
        n = 5
        tracks = self.service.get_n_recent_tracks(n)
        self.assertLessEqual(len(tracks), n) # we should get at most n tracks back

    def test_get_properties(self):
        song_id = '3vkCueOmm7xQDoJ17W1Pm3'
        properties = self.service.get_properties(song_id)
        self.assertEqual(properties['name'], 'My Love Mine All Mine')
        self.assertEqual(properties['artist'], 'Mitski')
        self.assertEqual(properties['tempo'], 113.95)