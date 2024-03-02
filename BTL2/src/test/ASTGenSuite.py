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
        input = """dynamic a
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "dynamic", None)
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