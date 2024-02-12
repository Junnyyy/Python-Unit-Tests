import unittest
from src.interleave import Interleave


class TestInterleave(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def setUp(self):
        self.Interleave = Interleave()

    def test_interleave_true(self):
        self.assertTrue(self.Interleave.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_interleave_false(self):
        self.assertFalse(self.Interleave.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_interleave_empty(self):
        self.assertTrue(self.Interleave.isInterleave("", "", ""))

    def test_interleave_single(self):
        self.assertTrue(self.Interleave.isInterleave("a", "", "a"))
        self.assertTrue(self.Interleave.isInterleave("", "a", "a"))
        self.assertFalse(self.Interleave.isInterleave("a", "", "b"))
        self.assertFalse(self.Interleave.isInterleave("", "a", "b"))
