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
        func main() return 1
        func j()
        begin
            dynamic e <- 3
            dynamic f
            f <- e
            number a <- 2 + e
        end
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

    def test_423(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
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
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
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
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
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
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
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
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
        func main() return
        number a
        func f()
        begin
            a[0] <- 2
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_432(self):
        input = """
        dynamic e <- "2"
        func main() return
        func j()
        begin
            dynamic e <- 3
            dynamic f
            f <- e
            number a <- 2 + e
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(f), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
            func main() return
            var c <- true
            dynamic a <- 2
            string b <- 3
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
            func f() begin
                number c[3,2] <- [[6,7],[4,5],[4,5]]
                return c[2,0]
            end
            func main() begin
                number a[1] <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
            func main() begin
                number age <- name + 12
                string name
            end
        """
        expect = "Undeclared Identifier: name"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
            dynamic a
            dynamic x <- a == (a + 2)
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
            func main()
            func foo()
            begin
                number a <- main()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main), [])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
            func foo(number a, number b[1, 2])
            func foo(number a, number b[1, 2])
            func main() begin
            end
            func foo(number a, number b[1, 2]) return 1
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
            func a() return 1
            number a <- 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
            func foo(number x, number x) 
            begin
            end
            func main() return
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
            func foo()
            begin
                number a <- 3
            end
            func foo()
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
            func test()
            begin
                dynamic a
                return 1
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_443(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
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
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
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
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
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
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
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
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
        func main() begin
          number a
          dynamic b
          dynamic c <- b
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
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
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
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
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
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
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
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
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
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
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
        func main() return
        number a
        func f()
        begin
            a[0] <- 2
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_462(self):
        input = """
        dynamic e <- "2"
        func main() return
        func j()
        begin
            dynamic e <- 3
            dynamic f
            f <- e
            number a <- 2 + e
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(f), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
            func main() return
            var c <- true
            dynamic a <- 2
            string b <- 3
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
            func f() begin
                number c[3,2] <- [[6,7],[4,5],[4,5]]
                return c[2,0]
            end
            func main() begin
                number a[1] <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
            func main() begin
                number age <- name + 12
                string name
            end
        """
        expect = "Undeclared Identifier: name"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """
            dynamic a
            dynamic x <- a == (a + 2)
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
            func main()
            func foo()
            begin
                number a <- main()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main), [])"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
            func foo(number a, number b[1, 2])
            func foo(number a, number b[1, 2])
            func main() begin
            end
            func foo(number a, number b[1, 2]) return 1
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
            func a() return 1
            number a <- 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
            func foo(number x, number x) 
            begin
            end
            func main() return
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
            func foo()
            begin
                number a <- 3
            end
            func foo()
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
            func test()
            begin
                dynamic a
                return 1
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_473(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
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
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
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
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
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
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
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
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
        func main() begin
          number a
          dynamic b
          dynamic c <- b
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
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
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
            dynamic d
            func test(number a, number b) begin
                dynamic e
                string d
            end
            func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
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
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
            func foo() begin
                number a
                string a
            end
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
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
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
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
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
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
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
            number a
            func main() begin 
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
        func main() return
        number a
        func f()
        begin
            a[0] <- 2
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 491))
        
    def test_492(self):
        input = """
        dynamic e <- "2"
        func main() return
        func j()
        begin
            dynamic e <- 3
            dynamic f
            f <- e
            number a <- 2 + e
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(f), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
            func main() return
            var c <- true
            dynamic a <- 2
            string b <- 3
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
            func f() begin
                number c[3,2] <- [[6,7],[4,5],[4,5]]
                return c[2,0]
            end
            func main() begin
                number a[1] <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
            func main() begin
                number age <- name + 12
                string name
            end
        """
        expect = "Undeclared Identifier: name"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
            dynamic a
            dynamic x <- a == (a + 2)
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
            func main()
            func foo()
            begin
                number a <- main()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main), [])"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
            func foo(number a, number b[1, 2])
            func foo(number a, number b[1, 2])
            func main() begin
            end
            func foo(number a, number b[1, 2]) return 1
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
            func a() return 1
            number a <- 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))
