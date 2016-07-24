from pyramid import testing

import unittest


class TestFoo(unittest.TestCase):

    def test_foo(self):
        import pdb;pdb.set_trace()
        self.assertEqual(1, 1)
