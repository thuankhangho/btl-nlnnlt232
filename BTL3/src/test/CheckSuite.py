import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    # def test_400(self):
    #     input = """
    #     func main() begin
    #       dynamic a
    #       dynamic b
    #       dynamic c <- a[0] + b
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
        func main() return
        func f()begin
dynamic a <- [[[1]], [1, 2], [3, 4]]
end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 401))
