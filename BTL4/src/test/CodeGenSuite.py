import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """ number a <- 1
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
