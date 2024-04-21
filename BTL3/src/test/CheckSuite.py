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

    # def test_401(self):
    #     input = """
    #     func main() return
    #     number a
    #     func f()
    #     begin
    #         a[0] <- 2
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
        
    # def test_402(self):
    #     input = """
    #     dynamic e <- "2"
    #     func main() return
    #     func j()
    #     begin
    #         dynamic e <- 3
    #         dynamic f
    #         f <- e
    #         number a <- 2 + e
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_413(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 413))