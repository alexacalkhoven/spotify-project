# ```python -m unittest test.test``` on cmd

import unittest

from src.app import SpotifyService


class TestSpotifyService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = SpotifyService()

    def test_get_artist(self):
        taylor_swift_id = '06HL4z0CvFAxyc27GXpf02'
        artist = self.service.get_artist(taylor_swift_id)
        self.assertEqual(artist['name'], "Taylor Swift")

    # def test_get_n_recent_tracks(self):
    #     n = 5
    #     tracks = self.service.get_n_recent_tracks(n)
    #     self.assertLessEqual(len(tracks), n) # we should get at most n tracks back

