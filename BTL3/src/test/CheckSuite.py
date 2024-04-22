import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_400(self):
        input = """
        func main() begin
          number a[2] <- [1, "true"]
          dynamic b
          dynamic c <- a[0] + b
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(true))"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
        func main() return
        number a
        func f()
        begin
            a[0] <- 2
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_402(self):
        input = """
        dynamic e <- "2"
        func j()
        begin
            dynamic e <- 3
            dynamic f
            f <- e
            number a <- 2 + e
        end
        func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """
            func main() return
            var c <- true
            dynamic a <- 2
            string b <- 3
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
            func f() begin
                number c[3,2] <- [[6,7],[4,5],[4,5]]
                return c[2,0]
            end
            func main() begin
                number a[1] <- f()
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """
            func main() begin
                number age <- name + 12
                string name
            end
        """
        expect = "Undeclared Identifier: name"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
            dynamic a
            dynamic x <- a == (a + 2)
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
            func main()
            func foo()
            begin
                number a <- main()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main), [])"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
            func foo(number a, number b[1, 2])
            func foo(number a, number b[1, 2])
            func main() begin
            end
            func foo(number a, number b[1, 2]) return 1
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
            func a() return 1
            number a <- 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
            func foo(number x, number x) 
            begin
            end
            func main() return
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
            func foo()
            begin
                number a <- 3
            end
            func foo()
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
            func test()
            begin
                dynamic a
                return 1
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_413(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
            func foo() begin
                return 1
            end
            func test()
            begin
                string x <- foo()
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), StringType, None, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
            func foo(number x) begin
                return 1
            end
            func test()
            begin
                number x <- 2 / foo()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        number i <- 2
        number x <- 10
        func test()
        begin
            var a <- 3
            for i until i > x / 2 by 1
            begin
                var e <- 3
                a <- 1 + 2
            end
            e <- 5
        end
            func main() return
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                a <- 1
                b <- a
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        func main() begin
          number a
          dynamic b
          dynamic c <- b
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            bool a
            if (a) writeString("Yes")
            else writeString("No")
            return 1
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 422))