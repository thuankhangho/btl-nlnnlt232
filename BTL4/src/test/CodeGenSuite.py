import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """number a <- 1
        func main() return
        func foo(number x) return 1
        func foo1(number y) return false
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
