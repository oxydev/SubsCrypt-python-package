from unittest import TestCase

from subscrypt import Subscrypt


class TestSubscrypt(TestCase):
    def setUp(self):
        self.client = Subscrypt()

    def test_is_connected_returns_true(self):
        self.assertTrue(self.client.is_connected())
