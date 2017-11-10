# -*- coding: utf-8 -*-

from context import pscv
import unittest

class TestHelloUnitTest(unittest.TestCase):
    def test_add(self):
        x = 1
        actual = pscv.object_detection.f(x)
        expected = 2
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()