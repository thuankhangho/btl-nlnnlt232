import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """func test() return 0
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
