import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_300(self):
        input = """number a"""
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        input = """number a[1]
            number a <- 2
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([1.0], NumberType())),
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(2.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_302(self):
        input = """number a[1]
            number a <- 2
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([1.0], NumberType())),
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(2.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_303(self):
        input = """var a <- 1
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "var", NumberLiteral(1.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_304(self):
        input = """string a
        """
        expect = str(Program([
            VarDecl(Id("a"), StringType())
            ]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_305(self):
        input = """number a <- 15.35e-30
        bool b <- false
        string c <- "Hello World"
        bool d[10]
        """
        expect = str(Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(15.35e-30)),
            VarDecl(Id("b"), BoolType(), None, BooleanLiteral(False)),
            VarDecl(Id("c"), StringType(), None, StringLiteral("Hello World")),
            VarDecl(Id("d"), ArrayType([10.0], BoolType())),
            ]))
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_306(self):
        input = """dynamic a <- 15.35e-30
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "dynamic", NumberLiteral(15.35e-30))
            ]))
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_307(self):
        input = """number a[5,3,4.2] <- 1
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
            ]))
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_308(self):
        input = """number a[5,3,4.2] <- [1,2,3]
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])),
            ]))
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_309(self):
        input = """number a[5,3,4.2] <- "Hello World"
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, StringLiteral("Hello World")),
            ]))
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test_310(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_311(self):
        input = """
            func main()
            begin
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_312(self):
        input = """
            func main(number a)
            begin
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Block([]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_313(self):
        input = """
            func main(number a) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_314(self):
        input = """
            func main(number a[2,3]) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType()))], Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_315(self):
        input = """
            func main(number a[2,3], string b) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),],
                             Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_316(self):
        input = """
            func main(number a[2,3], string b)
            begin
                return 1
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),],
                             Block([Return(NumberLiteral(1.0))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_317(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                return c + b
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Return(BinaryOp("+", Id("c"), Id("b")))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_318(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                continue
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Continue()]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test_319(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                break
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Break()]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test_320(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_321(self):
        input = """
            number a
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType()),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_322(self):
        input = """
            number a <- [3, 2.0, 1e2]
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None, ArrayLiteral([NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(100.0)])),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_323(self):
        input = """
            number a <- [3, 2.0, 1e2]
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a)
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None, ArrayLiteral([NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(100.0)])),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_324(self):
        input = """
            func main()
            begin
                var x <- 1
                var x <- "123"
                var x <- true
                var x <- false
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                                 VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                                 VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                                 VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_325(self):
        input = """
            func main()
            begin
                var x <- [1, "a", true, false]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_326(self):
        input = """
            func main()
            begin
                var x <- [1, "a", true, false, [1, 2, 3]]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_327(self):
        input = """
            func main()
            begin
                var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test_328(self):
        input = """
            func main()
            begin
                var x <- - [1.0, [1], -2]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  UnaryOp("-", ArrayLiteral([NumberLiteral(1.0), ArrayLiteral([NumberLiteral(1.0)]), UnaryOp("-", NumberLiteral(2.0))])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_329(self):
        input = """
            func main()
            begin
                var x <- foo() ... bar()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", CallExpr(Id("foo"), []), CallExpr(Id("bar"), [])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_330(self):
        input = """
            func main()
            begin
                var x <- foo(1 + 1, "a", [2,[2, [2]]]) ... bar()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", CallExpr(Id("foo"), [
                                     BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)),
                                     StringLiteral("a"),
                                     ArrayLiteral([NumberLiteral(2.0), ArrayLiteral([NumberLiteral(2.0), ArrayLiteral([NumberLiteral(2.0)])])])]),
                                                                         CallExpr(Id("bar"), [])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test_331(self):
        input = """
            func main()
            begin
                var x <- foo(bar(foo()))
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), [CallExpr(Id("bar"), [CallExpr(Id("foo"), [])])]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_332(self):
        input = """
            func main()
            begin
                var x <- (2 + 3) * 4
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("*", BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 332))
        
    def test_333(self):
        input = """
            func main()
            begin
                var x <- (2 + foo()) * 4
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("*", BinaryOp("+", NumberLiteral(2.0), CallExpr(Id("foo"), [])), NumberLiteral(4.0)))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_334(self):
        input = """
            func main()
            begin
                var x <- printInt(4)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  CallExpr(Id("printInt"), [NumberLiteral(4.0)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_335(self):
        input = """
            func main()
            begin
                if (a > 0)
                    if (a > 1) return 1
                    else return 2
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 If(BinaryOp(">", Id("a"), NumberLiteral(0.0)), If(BinaryOp(">", Id("a"), NumberLiteral(1.0)), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(2.0))))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test_336(self):
        input = """
            func main()
            begin
                number a[1.8]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("a"), ArrayType([1.8], NumberType()))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_337(self):
        input = """
            func main()
            begin
                if (1)
                    b()
                elif (2)
                    if (3)
                        c()
                    elif (4)
                        d()
                    else
                        e()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 If(NumberLiteral(1.0), CallStmt(Id("b"), []), [(NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id("c"), []), [(NumberLiteral(4.0), CallStmt(Id("d"), []))], CallStmt(Id("e"), [])))])
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_338(self):
        input = """
            func main()
            begin
                for i until i <= 10 by 1
                    printInt(1)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("printInt"), [NumberLiteral(1.0)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_339(self):
        input = """
            func main()
            begin
                for i until i <= 10 by 1
                    for j until j <= 10 by 1
                        printInt(1)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), For(Id("j"), BinaryOp("<=", Id("j"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("printInt"), [NumberLiteral(1.0)])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test_340(self):
        input = """
            func main()
            begin
                begin
                    begin
                    end
                end
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 Block([Block([])])
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_341(self):
        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_342(self):
        input = """
            func main()
                begin
                    return  1 + 1
                    return
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_343(self):
        input = """
            func foo (string a, bool b)
            func main()
            begin
                printInt(a / 4)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [
                        VarDecl(Id("a"), StringType()), VarDecl(Id("b"), BoolType())
                        ]),
                    FuncDecl(Id("main"), [], Block([
                        CallStmt(Id("printInt"), [BinaryOp("/", Id("a"), NumberLiteral(4.0))])
                        ])),
                ]))
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_344(self):
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_345(self):
        input = """
            func main()
                begin
                    for i until i > 15 by 1 + 1
                        print(1)
                end
            func foo()
                begin
                    for i until i by [1]
                    begin
                        if (true) print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(15.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
                    FuncDecl(Id("foo"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    If(BooleanLiteral(True), CallStmt(Id("print"), [NumberLiteral(1.0)]))]))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_346(self):
        input = """
            func main()
            begin
                return main(2) * foo(2) 
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Return(BinaryOp("*", CallExpr(Id("main"), [NumberLiteral(2.0)]), CallExpr(Id("foo"), [NumberLiteral(2.0)])))
                        ])),
                ]))
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_347(self):
        input = """
            number a <- 1
            func main()
            begin
                for x until a > x by foo(x)
                    x <- x + 1
            end
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
                    FuncDecl(Id("main"), [], Block([
                        For(Id("x"), BinaryOp(">", Id("a"), Id("x")), CallExpr(Id("foo"), [Id("x")]), Assign(Id("x"), BinaryOp("+", Id("x"), NumberLiteral(1.0))))
                        ])),
                ]))
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_348(self):
        input = """
            number a[4,5]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([4.0, 5.0], NumberType()))]))
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_349(self):
        input = """
            func foo(number a[5], string b)
            begin
                var i <- 0
                for i until i >= 5 by 1
                    begin
                        a[i] <- i * i + 5
                    end
                return -1
            end
        """
        expect = str(Program([
            FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayType([5.0], NumberType())), VarDecl(Id("b"), StringType())],Block([
                VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
                For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("a"), [Id("i")]),BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])),
                Return(UnaryOp("-", NumberLiteral(1.0)))
            ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_350(self):
        input = """
            func areDivisors(number num1, number num2) return ((num1 % num2 = 0) or (num2 % num1 = 0))
        """
        expect = str(Program([
                    FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType()), VarDecl(Id("num2"), NumberType())], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0)))))
                ]))
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_351(self):
        input = """
            func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])),
                        VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])),
                        If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_352(self):
        input = """
            func areDivisors(number num1, number num2) return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = str(Program([
                    FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType()), VarDecl(Id("num2"), NumberType())], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0))))),
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])),
                        VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])),
                        If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_353(self):
        input = """
            func isPrime(number x)
            
            func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) writeString("Yes")
                else writeString("No")
            end
            
            func isPrime(number x)
            begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
                return true
            end
        """
        expect = str(Program([
                        FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())]),
                        FuncDecl(Id("main"), [], Block([
                            VarDecl(Id("x"), NumberType(), None, CallExpr(Id("readNumber"), [])),
                            If(CallExpr(Id("isPrime"), [Id("x")]), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))
                    ])),
                        FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())], Block([
                            If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Return(BooleanLiteral(False))),
                            VarDecl(Id("i"), None, "var", NumberLiteral(2.0)),
                            For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), Block([
                                If(BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(False)))
                            ])),
                            Return(BooleanLiteral(True))
                        ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_354(self):
        input = """
            func main()
            begin
                number a[5] <- [1, 2, 3, 4, 5]
                number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])),
                        VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0),]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0),])])),
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_355(self):
        input = """
            func main()
            begin
                ## This is a single comment.
                a <- 5
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Assign(Id("a"), NumberLiteral(5.0))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_356(self):
        input = """
            func main()
            begin
                ## This is a single comment.
                a[3 + foo(2)] <- a[b[2, 3]] + 4
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(3.0), CallExpr(Id("foo"), [NumberLiteral(2.0)]))]), BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [NumberLiteral(2.0), NumberLiteral(3.0)])]), NumberLiteral(4.0)))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test_357(self):
        input = """
            func main()
            begin
                ## This is a single comment.
                aPI <- 3.14
                l[3] <- value * aPi
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Assign(Id("aPI"), NumberLiteral(3.14)),
                        Assign(ArrayCell(Id("l"), [NumberLiteral(3.0)]), BinaryOp("*", Id("value"), Id("aPi"))),
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test_358(self):
        input = """
            func main()
            begin
                ## This is a single comment.
                var i <- 0
                for i until i >= 10 by 1
                    writeNumber(i)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
                        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("writeNumber"), [Id("i")]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_359(self):
        input = """
            func main()
            begin
                ## This is a single comment.
                number r
                number s
                r <- 2.0
                number a[5]
                number b[5]
                s <- r * r * 3.14
                a[0] <- s
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("r"), NumberType()),
                        VarDecl(Id("s"), NumberType()),
                        Assign(Id("r"), NumberLiteral(2.0)),
                        VarDecl(Id("a"), ArrayType([5.0], NumberType())),
                        VarDecl(Id("b"), ArrayType([5.0], NumberType())),
                        Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), NumberLiteral(3.14))),
                        Assign(ArrayCell(Id("a"), [NumberLiteral(0.0)]), Id("s"))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test_360(self):
        input = """number a"""
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """number a[1]
            number a <- 2
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([1.0], NumberType())),
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(2.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,361))
        
    def test_362(self):
        input = """number a[1]
            number a <- 2
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([1.0], NumberType())),
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(2.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,362))
        
    def test_363(self):
        input = """var a <- 1
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "var", NumberLiteral(1.0))
            ]))
        self.assertTrue(TestAST.test(input,expect,363))
        
    def test_364(self):
        input = """string a
        """
        expect = str(Program([
            VarDecl(Id("a"), StringType())
            ]))
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test_365(self):
        input = """number a <- 15.35e-36
        bool b <- false
        string c <- "Hello World"
        bool d[10]
        """
        expect = str(Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(15.35e-36)),
            VarDecl(Id("b"), BoolType(), None, BooleanLiteral(False)),
            VarDecl(Id("c"), StringType(), None, StringLiteral("Hello World")),
            VarDecl(Id("d"), ArrayType([10.0], BoolType())),
            ]))
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test_366(self):
        input = """dynamic a <- 15.35e-36
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "dynamic", NumberLiteral(15.35e-36))
            ]))
        self.assertTrue(TestAST.test(input,expect,366))
        
    def test_367(self):
        input = """number a[5,3,4.2] <- 1
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
            ]))
        self.assertTrue(TestAST.test(input,expect,367))
        
    def test_368(self):
        input = """number a[5,3,4.2] <- [1,2,3]
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])),
            ]))
        self.assertTrue(TestAST.test(input,expect,368))
        
    def test_369(self):
        input = """number a[5,3,4.2] <- "Hello World"
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, StringLiteral("Hello World")),
            ]))
        self.assertTrue(TestAST.test(input,expect,369))
        
    def test_370(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test_371(self):
        input = """
            func main()
            begin
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test_372(self):
        input = """
            func main(number a)
            begin
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Block([]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 372))
        
    def test_373(self):
        input = """
            func main(number a) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test_374(self):
        input = """
            func main(number a[2,3]) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType()))], Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test_375(self):
        input = """
            func main(number a[2,3], string b) return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),],
                             Return(NumberLiteral(1.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test_376(self):
        input = """
            func main(number a[2,3], string b)
            begin
                return 1
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),],
                             Block([Return(NumberLiteral(1.0))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_377(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                return c + b
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Return(BinaryOp("+", Id("c"), Id("b")))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test_378(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                continue
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Continue()]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_379(self):
        input = """
            func main(number a[2,3], string b, bool c)
            begin
                break
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType())),
                                          VarDecl(Id("b"), StringType()),
                                          VarDecl(Id("c"), BoolType()),],
                             Block([Break()]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test_380(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test_381(self):
        input = """
            number a
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType()),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test_382(self):
        input = """
            number a <- [3, 2.0, 1e2]
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None, ArrayLiteral([NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(100.0)])),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 382))
        
    def test_383(self):
        input = """
            number a <- [3, 2.0, 1e2]
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a)
                return
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None, ArrayLiteral([NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(100.0)])),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Return())
                ]))
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test_384(self):
        input = """
            func main()
            begin
                var x <- 1
                var x <- "123"
                var x <- true
                var x <- false
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                                 VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                                 VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                                 VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test_385(self):
        input = """
            func main()
            begin
                var x <- [1, "a", true, false]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_386(self):
        input = """
            func main()
            begin
                var x <- [1, "a", true, false, [1, 2, 3]]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_387(self):
        input = """
            func main()
            begin
                var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_388(self):
        input = """
            func main()
            begin
                var x <- - [1.0, [1], -2]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  UnaryOp("-", ArrayLiteral([NumberLiteral(1.0), ArrayLiteral([NumberLiteral(1.0)]), UnaryOp("-", NumberLiteral(2.0))])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_389(self):
        input = """
            func main()
            begin
                var x <- foo() ... bar()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", CallExpr(Id("foo"), []), CallExpr(Id("bar"), [])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test_390(self):
        input = """
            func main()
            begin
                var x <- foo(1 + 1, "a", [2,[2, [2]]]) ... bar()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("...", CallExpr(Id("foo"), [
                                     BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)),
                                     StringLiteral("a"),
                                     ArrayLiteral([NumberLiteral(2.0), ArrayLiteral([NumberLiteral(2.0), ArrayLiteral([NumberLiteral(2.0)])])])]),
                                                                         CallExpr(Id("bar"), [])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test_391(self):
        input = """
            func main()
            begin
                var x <- foo(bar(foo()))
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), [CallExpr(Id("bar"), [CallExpr(Id("foo"), [])])]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test_392(self):
        input = """
            func main()
            begin
                var x <- (2 + 3) * 4
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("*", BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test_393(self):
        input = """
            func main()
            begin
                var x <- (2 + foo()) * 4
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  BinaryOp("*", BinaryOp("+", NumberLiteral(2.0), CallExpr(Id("foo"), [])), NumberLiteral(4.0)))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test_394(self):
        input = """
            func main()
            begin
                var x <- printInt(4)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("x"), None, "var",  CallExpr(Id("printInt"), [NumberLiteral(4.0)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test_395(self):
        input = """
            func main()
            begin
                if (a > 0)
                    if (a > 1) return 1
                    else return 2
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 If(BinaryOp(">", Id("a"), NumberLiteral(0.0)), If(BinaryOp(">", Id("a"), NumberLiteral(1.0)), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(2.0))))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_396(self):
        input = """
            func main()
            begin
                number a[1.8]
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 VarDecl(Id("a"), ArrayType([1.8], NumberType()))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_397(self):
        input = """
            func main()
            begin
                if (1)
                    b()
                elif (2)
                    if (3)
                        c()
                    elif (4)
                        d()
                    else
                        e()
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 If(NumberLiteral(1.0), CallStmt(Id("b"), []), [(NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id("c"), []), [(NumberLiteral(4.0), CallStmt(Id("d"), []))], CallStmt(Id("e"), [])))])
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_398(self):
        input = """
            func main()
            begin
                for i until i <= 10 by 1
                    printInt(1)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("printInt"), [NumberLiteral(1.0)]))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test_399(self):
        input = """
            func main()
            begin
                for i until i <= 10 by 1
                    for j until j <= 10 by 1
                        printInt(1)
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                             Block([
                                 For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), For(Id("j"), BinaryOp("<=", Id("j"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("printInt"), [NumberLiteral(1.0)])))
                                 ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 399))