from pyramid import testing

import unittest


class TestBar(unittest.TestCase):

    def test_bar(self):
        self.assertEqual(1, 1)
