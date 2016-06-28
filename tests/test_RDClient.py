from unittest import TestCase
from pyrdstation.client import RDClient

__author__ = 'zamboni'


class TestRDClient(TestCase):
    def setUp(self):
        self.obj = RDClient(token="test_token", private_token="test_private_token")

    def test_token(self):
        self.assertEqual(self.obj._token, self.obj.token)
        self.assertEqual(self.obj._token, "test_token")

    def test_private_token(self):
        self.assertEqual(self.obj._private_token, self.obj.private_token)
        self.assertEqual(self.obj._private_token, "test_private_token")

    def test_track_conversion(self):
        # TODO: Check with Resultados Digitais if they have a public test endpoint
        pass
