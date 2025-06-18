import unittest
from app.hello import greet

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
