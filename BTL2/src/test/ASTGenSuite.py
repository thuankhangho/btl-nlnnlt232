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
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.535e-29)),
            VarDecl(Id("b"), BoolType(), None, BooleanLiteral(False)),
            VarDecl(Id("c"), StringType(), None, StringLiteral("Hello World")),
            VarDecl(Id("d"), ArrayType([10.0], BoolType())),
            ]))
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_306(self):
        input = """dynamic a <- 15.35e-30
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.535e-29))
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
        
    # def test_353(self):
    #     input = """
    #         func isPrime(number x)
            
    #         func main()
    #         begin
    #             number x <- readNumber()
    #             if (isPrime(x)) writeString("Yes")
    #             else writeString("No")
    #         end
            
    #         func isPrime(number x)
    #         begin
    #             if (x <= 1) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #             begin
    #                 if (x % i = 0) return false
    #             end
    #             return true
    #         end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], 
    #                          Block([
    #                              VarDecl(Id("x"), None, "var",  CallExpr(Id("printInt"), [NumberLiteral(4.0)]))
    #                              ]))
    #             ]))
    #     self.assertTrue(TestAST.test(input, expect, 353))
    
    # def test_declared(self):
    #     input = """
    #         number temp
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("temp"), NumberType())
    #         ]))
    #     self.assertTrue(TestAST.test(input, expect, 301))
        
    #     input = """
    #         string VoTien <- 1
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("VoTien"), StringType(), None, NumberLiteral(1.0))
    #         ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 302))
        
    #     input = """
    #         string Votien
    #         bool Votien
    #         string Votien <- 1
    #         bool Votien <- 1
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("Votien"), StringType()),
    #             VarDecl(Id("Votien"), BoolType()),
    #             VarDecl(Id("Votien"), StringType(), None, NumberLiteral(1.0)),
    #             VarDecl(Id("Votien"), BoolType(), None, NumberLiteral(1.0))
    #         ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 303))
        
    #     input = """
    #         string VoTien[5] <- 1
    #         string VoTien[5]
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("VoTien"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
    #             VarDecl(Id("VoTien"), ArrayType([5.0], StringType()))
    #         ]))
    #     self.assertTrue(TestAST.test(input, expect, 304))
        
    #     input = """
    #         number VoTien[5,3,4.2] <- 1
    #         bool VoTien[2,3,4]
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("VoTien"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
    #             VarDecl(Id("VoTien"), ArrayType([2.0, 3.0, 4.0], BoolType()))
    #         ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 305))
        
    #     input = """
    #         dynamic Votien <- 1
    #         dynamic Votien
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("Votien"), None, "dynamic", NumberLiteral(1.0)),
    #                 VarDecl(Id("Votien"), None, "dynamic")
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 306))
        
    #     input = """
    #         var Votien <- 1
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("Votien"), None, "var", NumberLiteral(1.0))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 307))
        
    #     input = """
    #         func main()
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], None)
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 308))
        
    #     input = """
    #         func main()
    #             begin
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 309))

    #     input = """
    #         func main()
    #             begin
    #             break
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 Break()]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 310))
                
    #     input = """
    #         func main(number a)
    #         func main(number a, string a, bool a[2])
    #         func main(number Votien[1,2])
    #             return
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
    #                 FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
    #                                       VarDecl(Id("a"), StringType()), 
    #                                       VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
    #                 FuncDecl(Id("main"), [VarDecl(Id("Votien"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
    #             ]))
    #     # print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 311))
        
    # def test_Expression(self):
    #     """Expression Expression Expression"""
    #     input = """
    #         var x <- 1
    #         var x <- "123"
    #         var x <- true
    #         var x <- false
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
    #                 VarDecl(Id("x"), None, "var",  StringLiteral("123")),
    #                 VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
    #                 VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 312))
        
    #     input = """
    #         var x <- [1, "a", true, false]
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 313))   
        
    #     input = """
    #         var x <- [[1], [1]]
    #         var x <- [[1]]
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
    #                 VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 314))  
        
    #     input = """
    #         var x <- 1 ... "2"
    #         var x <- 1 <= "2"
    #         var x <- 1 and 2 or 3
    #         var x <- 1 + 2 - 3
    #         var x <- 1 * 2 / 3 % 4
    #         var x <- ---1
    #         var x <- not not 1
    #         var x <- x 
    #         var x <- a[1,2,3]
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
    #                 VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
    #                 VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
    #                 VarDecl(Id("x"), None, "var",  Id("x")),
    #                 VarDecl(Id("x"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 315))  
        
    #     input = """
    #         var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
    #     """
    #     expect = str(Program([
    #             VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
    #         ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 316))  
        
    #     input = """
    #         var x <- -a[1+2] ... 2
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 317))  
        
    #     input = """
    #         var x <- fun()
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 318)) 
        
    #     input = """
    #         var x <- fun(1+1, "a")
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 319)) 
        
    #     input = """
    #         var x <- fun(fun())
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 320)) 
        
    #     input = """
    #         var x <- (2 ... 3) ... 4
    #     """
    #     expect = str(Program([
    #                 VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 321)) 
         
    # def test_Statements(self):
    #     """Statements Statements Statements"""
    #     input = """
    #         func main()
    #             begin
    #                 continue
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 Continue()]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 322))

    #     input = """
    #         func main()
    #             begin
    #                 continue
    #                 continue
    #                 break
    #                 begin
    #                     continue
    #                     continue
    #                     break                    
    #                 end
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 Continue(),
    #                 Continue(),
    #                 Break(),
    #                     Block([
    #                     Continue(),
    #                     Continue(),
    #                     Break()])]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 323))
        
    #     input = """
    #         func main()
    #             begin
    #                 return  1 + 1
    #                 return
    #             end
    #         func main()
    #             return 1
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
    #                 Return()])),
    #                 FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 324))

    #     input = """
    #         func main()
    #             begin
    #                 main(a)
    #                 main(1,1)
    #             end
    #         func main()
    #             begin
    #             main()
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 CallStmt(Id("main"), [Id("a")]),
    #                 CallStmt(Id("main"), [NumberLiteral(1.0), NumberLiteral(1.0)])])),
    #                 FuncDecl(Id("main"), [], Block([
    #                 CallStmt(Id("main"), [])]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 325))
        
    #     input = """
    #         func main()
    #             begin
    #                 a <- 1
    #                 a[1] <- 2
    #                 a[3,2] <- 4 + 2
    #             end
    #         func main()
    #             begin
    #             a[1+1, 3] <- 1
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 Assign(Id("a"), NumberLiteral(1.0)),
    #                 Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
    #                 Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))])),
    #                 FuncDecl(Id("main"), [], Block([
    #                 Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 326))
        
    #     input = """
    #         func main()
    #             begin
    #                 for i until i > 2 by 1 + 1
    #                     print(1)
    #             end
    #         func main()
    #             begin
    #                 for i until i by [1]
    #                 begin
    #                     print(1)
    #                 end
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
    #                 FuncDecl(Id("main"), [], Block([
    #                 For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
    #                 CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 327))
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true) return 1
    #             end
    #         func main()
    #             begin
    #                 if (true) return 2
    #                 else return 3
    #             end
    #     """
    #     expect = str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)])),
    #                 FuncDecl(Id("main"), [], Block([
    #                 If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [] ,Return(NumberLiteral(3.0)))]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 328))
        

    #     input = """
    #         func main()
    #             begin
    #                 if (true) return 1
    #                 elif (true) return 1
    #                 elif (true) return 1
    #                 else return 1
    #             end

    #     """
    #     expect =str(Program([
    #                 FuncDecl(Id("main"), [], Block([
    #                 If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
    #                    [(BooleanLiteral(True),Return(NumberLiteral(1.0))),
    #                     (BooleanLiteral(True),Return(NumberLiteral(1.0)))] 
    #                 ,Return(NumberLiteral(1.0)))]))
    #             ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 329))     
        
    #     input = """
    #         var c <- a[1,2]
    #         var c <- fun()[1,2]
    #         var c <- fun(1,2)[1,3]
    #     """
    #     expect = str(Program([
    #         VarDecl(Id("c"), None, "var", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
    #         VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
    #         VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
    #     ]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 330))    
        
    #     input = """
    #         func main()
    #         begin
    #             var c <- 2e5
    #             dynamic c <- 2.56
    #             dynamic c
    #             number c[2e2, 2] <- 3.6
    #             string c[3.823]
    #         end
    #     """
    #     expect = str(Program([
    #         FuncDecl(Id("main"), [], Block(
    #             [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)), 
    #              VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)), 
    #              VarDecl(Id("c"), None, "dynamic"),
    #              VarDecl(Id("c"), ArrayType([200.0, 2.0], NumberType()), None, NumberLiteral(3.6)),
    #              VarDecl(Id("c"), ArrayType([3.823], StringType()), None)
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 331))    
        
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true)
    #                     if(true) return 1
    #                     else return 1
    #             end

    #     """
    #     expect =str(Program([FuncDecl(Id("main"), [], Block([
    #         If(BooleanLiteral(True), 
    #            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 332))     
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true)
    #                     if(true) return 1
    #                     else return 1
    #                 else return 1
    #             end

    #     """
    #     expect =str(Program([FuncDecl(Id("main"), [], Block([
    #         If(BooleanLiteral(True), 
    #            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), 
    #            [], Return(NumberLiteral(1.0)))
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 333))   
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true)
    #                     if(true) return 1
    #                     elif (true) return 1
    #                     else return 1
    #             end

    #     """
    #     expect =str(Program([FuncDecl(Id("main"), [], Block([
    #         If(BooleanLiteral(True), 
    #            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), [], None)
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 334))   
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true)
    #                     if(true) return 1
    #                     elif (true) return 1
    #                     elif (true) return 1
    #             end

    #     """
    #     expect =str(Program([FuncDecl(Id("main"), [], Block([
    #         If(BooleanLiteral(True), 
    #            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))]), [], None)
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 335))   
        
    #     input = """
    #         func main()
    #             begin
    #                 if (true)
    #                     if(true) return 1
    #                     elif (true) return 1
    #                     elif (true) return 1
    #                     else return 1
    #                 elif (true) return 1
    #                 elif (true) return 1                        
    #                 else return 1
    #             end

    #     """
    #     expect =str(Program([FuncDecl(Id("main"), [], Block([
    #         If(BooleanLiteral(True), 
    #            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
    #         , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
    #         ]))]))
    #     #print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 336))
    
from abc import ABC, abstractmethod, ABCMeta
# from Visitor import Visitor
from dataclasses import dataclass
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


class Expr(AST):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class Type(AST):
    __metaclass__ = ABCMeta
    pass


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class Id(LHS):
    # name: str
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Id({self.name})"


# used for binary expression
class BinaryOp(Expr):
    # op: str
    # left: Expr
    # right: Expr

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryOp({self.op}, {str(self.left)}, {str(self.right)})"


# used for unary expression with orerand like !,+,-
class UnaryOp(Expr):
    # op: str
    # operand: Expr

    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def __str__(self):
        return f"UnaryOp({self.op}, {str(self.operand)})"


class CallExpr(Expr):
    # name: Id
    # args: List[Expr]

    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"CallExpr({str(self.name)}, [{', '.join(str(i) for i in self.args)}])"


class ArrayCell(LHS):
    # arr: Expr
    # idx: List[Expr]

    def __init__(self, arr, idx):
        self.arr = arr
        self.idx = idx

    def __str__(self):
        return f"ArrayCell({str(self.arr)}, [{', '.join(str(i) for i in self.idx)}])"


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass


class NumberLiteral(Literal):
    # value: float

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"NumLit({str(self.value)})"


class StringLiteral(Literal):
    # value: str

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"StringLit({self.value})"


class BooleanLiteral(Literal):
    # value: bool

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"BooleanLit({'True' if self.value else 'False'})"


@dataclass
class ArrayLiteral(Literal):
    # value: List[Expr]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ArrayLit({', '.join(str(i) for i in self.value)})"


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class Assign(Stmt):
    # lhs: Expr
    # exp: Expr

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"AssignStmt({str(self.lhs)}, {str(self.rhs)})"


class If(Stmt):
    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch

    def __init__(self, expr, thenStmt, elifStmt=[], elseStmt=None):
        self.expr = expr
        self.thenStmt = thenStmt
        self.elifStmt = elifStmt
        self.elseStmt = elseStmt

    def __str__(self):
        return f"If(({str(self.expr)}, {str(self.thenStmt)}), [{', '.join(f'({str(x[0])}, {str(x[1])})' for x in self.elifStmt)}], {str(self.elseStmt) if self.elseStmt else 'None'})"


class For(Stmt):
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt

    def __init__(self, name, condExpr, updExpr, body):
        self.name = name
        self.condExpr = condExpr
        self.updExpr = updExpr
        self.body = body

    def __str__(self):
        return f"For({str(self.name)}, {str(self.condExpr)}, {str(self.updExpr)}, {str(self.body)})"


class Break(Stmt):
    def __str__(self):
        return "Break"


class Continue(Stmt):
    def __str__(self):
        return "Continue"


class Return(Stmt):
    # expr: Expr = None  # None if there is no expression after return

    def __init__(self, expr=None):
        self.expr = expr

    def __str__(self):
        return f"Return({str(self.expr) if self.expr else ''})"


class CallStmt(Stmt):
    # name: Id
    # args: List[Expr]  # empty list if there is no argument

    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"CallStmt({str(self.name)}, [{', '.join(str(i) for i in self.args)}])"


class Block(Stmt):
    # stmt: List[Stmt]  # empty list if there is no statement in block

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Block([{', '.join(str(i) for i in self.stmt)}])"


# used for variable or parameter declaration
class VarDecl(Decl, Stmt):
    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial

    def __init__(self, name, varType=None, modifier=None, varInit=None):
        self.name = name
        self.varType = varType
        self.modifier = modifier
        self.varInit = varInit

    def __str__(self):
        return f"VarDecl({str(self.name)}, {str(self.varType) if self.varType else 'None'}, {str(self.modifier) if self.modifier else 'None'}, {str(self.varInit) if self.varInit else 'None'})"


# used for a function declaration
class FuncDecl(Decl):
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part

    def __init__(self, name, param, body=None):
        self.name = name
        self.param = param
        self.body = body

    def __str__(self):
        return f"FuncDecl({str(self.name)}, [{', '.join(str(i) for i in self.param)}], {str(self.body) if self.body else 'None'})"


class NumberType(Type):
    def __str__(self):
        return "NumberType"


class BoolType(Type):
    def __str__(self):
        return "BoolType"


class StringType(Type):
    def __str__(self):
        return "StringType"


class ArrayType(Type):
    # size: List[float]
    # eleType: Type

    def __init__(self, size, eleType):
        self.size = size
        self.eleType = eleType

    def __str__(self):
        return f"ArrayType([{', '.join(str(i) for i in self.size)}], {str(self.eleType)})"


# used for whole program
class Program(AST):
    # decl: List[Decl]  # empty list if there is no statement in block

    def __init__(self, decl):
        self.decl = decl

    def __str__(self):
        return f"Program([{', '.join(str(i) for i in self.decl)}])"