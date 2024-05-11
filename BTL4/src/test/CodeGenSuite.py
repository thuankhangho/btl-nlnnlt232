import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """number a <- 100
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
