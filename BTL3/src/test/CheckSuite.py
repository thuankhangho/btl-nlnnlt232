import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """
        func main() return 1
        number a <- 1
        number a <- 2
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
