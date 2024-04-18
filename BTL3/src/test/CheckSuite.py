import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """
        func test() return 1
        func x()
        begin
            number a <- test()
            return
        end
        func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 400))
