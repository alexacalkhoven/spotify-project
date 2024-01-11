# ```python -m unittest test.test``` on cmd

import json
import unittest
from src.app import SpotifyService

class TestSpotifyService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = SpotifyService()

    def test_get_artist(self):
        taylor_swift_id = '06HL4z0CvFAxyc27GXpf02'
        artist = self.service.get_artist(taylor_swift_id)
        # print(json.dumps(artist, sort_keys=True, indent=4))
        self.assertEqual(artist['name'], "Taylor Swift")
