#################################################################################################################################
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
    
    
class VoidType(Type):
    def __str__(self):
        return "VoidType"

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
#################################################################################################################################

from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # path: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access(): # dùng khi visit expression
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft # nếu true -> biến này nằm bên trái -> store, nếu false -> biến này nằm bên phải -> load
        self.isFirst = isFirst # bỏ qua

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        # astTree: AST
        # env: List[List[Symbol]]
        # path: File

        self.astTree = astTree
        self.className = "ZCodeClass"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.returnCodeAndType = (None, None)
        self.functionList = []
        self.functionScopeList = []
        self.currentFunction: FuncType = None

    def visitProgram(self, ast: Program, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        env = [[]]

        # visit các biến toàn cục
        for decl in ast.decl:
            if type(decl) is VarDecl: # -> VarType
                self.visit(decl, Access(None, env, False))

        # xử lý main
        # mainFunc: FuncType = None
        mainDecl: FuncDecl = None
        for decl in ast.decl:
            if type(decl) is FuncDecl and decl.body is not None: # -> MethodType
                # lấy param
                paramList = []
                for x in decl.param:
                    paramList.append(x)
                self.functionList.append(FuncType(decl.name.name, None, paramList))
                
                # lưu hàm main
                if decl.name.name == "main":
                    # mainFunc = self.functionList[-1]
                    mainDecl = decl
                
        # for x in env.sym:
        #     print(x)

        # Sinh code cho constructor của class ZCodeClass
        # self.emit.printout(self.emit.emitMETHOD("<init>", MType("<init>", [], VoidType()), False, Frame("<init>", VoidType())))
        self.genFunc(FuncDecl(Id("<init>"), [], Block([])), env, Frame("<init>", VoidType()))
        
        # Sinh code cho biến toàn cục
        self.genGlobalVarInit(env, Frame("<clinit>", VoidType()), ast.decl)
        
        # Sinh code cho hàm khác main
        i = 0
        for decl in ast.decl:
            if type(decl) is FuncDecl and decl.body is not None and decl.name.name != "main":
                self.currentFunction = self.functionList[i]
                self.visit(decl, Access(None, env, False))
            if type(decl) is FuncDecl and decl.body is not None:
                i = i + 1
        
        # Sinh code cho main
        self.genFunc(mainDecl, env, Frame("main", VoidType()))
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast: VarDecl, o: Access):
        if o.frame is None: # biến toàn cục
            # code = self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, "")
            # self.emit.printout(code)
            # if ast.modifier is None:
            o.sym[0].append(VarType(ast.name.name, ast.varType, -1, True if ast.varInit else False))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, self.className))
            o.sym[0][-1].line = self.emit.setNewLine()
        else: # biến cục bộ
            idx = o.frame.getNewIndex()
            o.sym[0].append(VarType(ast.name.name, ast.varType, idx, True if ast.varInit else False))
            code = self.emit.emitVAR(idx, ast.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel())
            self.emit.printout(code)
            if ast.init:
                codeInit, initTyp = self.visit(ast.init, o)
        #         codeWrite = self.emit.emitWRITEVAR(ast.name, ast.varType, idx, o.frame)
        #         self.emit.printout(codeInit + code + codeWrite)
            else:
                if type(ast.varType) is NumberType:
                    varInit = NumberLiteral(0)
                elif type(ast.varType) is BoolType:
                    varInit = BooleanLiteral(False)
                elif type(ast.varType) is StringType:
                    varInit = StringLiteral("")
                # else: 
                #     self.visit(Assign(ast.name,ArrayLiteral([])),o)
                codeInit, initTyp = self.visit(varInit, o)
        #         self.emit.printout(code)
            # self.emit.printout(codeInit + code)
        #     return SubBody(o.frame, [Symbol(ast.name.name, ast.varType, Index(idx))] + o.sym)
            return VarType(ast.name.name, ast.varType, idx)
            
    def visitFuncDecl(self, ast: FuncDecl, o):
        if ast.body is not None:
            o.frame = Frame(ast.name.name, None, o.sym)
            self.visit(ast.body, o)
            
            self.functionList.append(FuncType(ast.name.name, self.returnCodeAndType[1], [i.varType for i in ast.param]))
            self.functionScopeList.append(FuncScopeType(ast.name.name, ast.body, [i for i in ast.param]))
            
            self.genFunc(ast, o, Frame(ast.name.name, self.returnCodeAndType[1]))
            self.returnCodeAndType = (None, None)
        # for x in env.sym:
        #     print(x)
        # frame = Frame(ast.name, ast.return_type)
        
        # name = ast.name
        # symbol = Symbol(name, MType([x.typ for x in ast.params], ast.return_type), CName(self.className))
        
        # env = SubBody(None, [symbol] + o.sym)
        
        # self.genMETHOD(ast, env.sym, frame) #funcdecl, o, frame
        # return env

    def visitNumberType(self, ast, o):
        return None, NumberType()

    def visitBoolType(self, ast, o):
        return None, BoolType()

    def visitStringType(self, ast, o):
        return None, StringType()

    def visitArrayType(self, ast, o):
        return None, ast
    
    def visitVoidType(self, ast, o):
        return None, VoidType()

    def visitBinaryOp(self, ast: BinaryOp, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)

        if type(e1t) is type(e2t):
            rt = e1t
        # nếu 1 trong e1t & e2t chưa biết type
            
        if ast.op in ["+", "-"]:
            code = self.emit.emitADDOP(ast.op, rt, o.frame)
        elif ast.op in ["*", "/"]:
            code = self.emit.emitMULOP(ast.op, rt, o.frame)
        elif ast.op == "%":
            code = self.emit.emitMOD(o.frame)

        return e1c + e2c + code, rt

    def visitUnaryOp(self, ast, o):
        pass

    def visitCallExpr(self, ast, o):
        pass

    def visitId(self, ast, o: Access):
        # for scope in o.sym:
        #     for x in scope:
        #         print(x.name, ast.name)
        #         if x.name == ast.name:
        #                 if x.typ:
        #                     return None, x.typ
        #                 else: return None, x
        for scope in o.sym:
            for x in scope:
                print(x.name, ast.name)
                if x.name == ast.name:
                    if x.index < 0: # biến toàn cục
                        if o.isLeft == False:
                            code = self.emit.emitGETSTATIC(self.className + '.' + x.name, x.typ, o.frame)
                            typ = x.typ
                            return code, typ
                        else:
                            code = self.emit.emitPUTSTATIC(self.className + '.' + x.name, x.typ, o.frame)
                            typ = x.typ
                            return code, typ
        # if type(sym.value) is CName: # bien toan cuc
        #     code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
        # else: # bien cuc bo
        #     code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)

    def visitArrayCell(self, ast, o):
        pass

    def visitBlock(self, ast, o):
        pass

    def visitIf(self, ast, o):
        pass

    def visitFor(self, ast, o):
        pass

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitReturn(self, ast: Return, o):
        if ast.expr:
            code, typ = self.visit(ast.expr, Access(o.frame, o.sym, False))
            # self.emit.printout(code)
            self.returnCodeAndType = (code, typ)
        else:
            self.returnCodeAndType = (None, VoidType())
        # self.emit.printout(self.emit.emitRETURN(o.frame.returnType, o.frame))

    def visitAssign(self, ast, o):
        rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True))

        self.emit.printout(rc)
        self.emit.printout(lc)

    def visitCallStmt(self, ast, o):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, o):
        code = self.emit.emitPUSHFCONST(str(ast.value), o.frame)
        typ = NumberType()
        return code, typ

    def visitBooleanLiteral(self, ast, o):
        val = "true" if ast.value == True else "false"
        code = self.emit.emitPUSHICONST(val, o.frame)
        typ = BoolType()
        return code, typ

    def visitStringLiteral(self, ast, o):
        code = self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame)
        typ = StringType()
        return code, typ
    
    def visitArrayLiteral(self, ast, o):
        pass

    def genFunc(self, funcdecl: FuncDecl, o, frame): # viết lại
        # self.genFunc(FuncDecl("<init>", [], Block([])), env, Frame("<init>", VoidType()))

        # self.emit.emitMETHOD("<init>", MType("init", [], VoidType()), False, Frame("<init>", VoidType))

        isInit = funcdecl.name.name == "<init>"
        isMain = funcdecl.name.name == "main" and len(funcdecl.param) == 0

        if isInit: # constructor của class ZCodeClass
            self.emit.printout(self.emit.emitMETHOD("<init>", FuncType("<init>", VoidType(), []), False, frame))
            frame.enterScope(True)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", self.className, frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))   
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()
        elif isMain: # hàm main
            self.emit.printout(self.emit.emitMETHOD("main", FuncType("main", VoidType(), [ArrayType([1], StringType())]), True, frame))
            frame.enterScope(True)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            # newIndex = frame.getNewIndex()
            # self.emit.printout(self.emit.emitVAR(newIndex, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
            # self.visit(funcdecl.body, Access(frame, [[VarType("for", NumberType(), newIndex, True)]] + o, False))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()
        else: # các hàm khác
            # paramList = []
            # for x in funcdecl.param:
            #     print(self.visit(x, o))
            #     paramList.append(self.visit(x, o))
                
            self.emit.printout(self.emit.emitMETHOD(funcdecl.name.name, self.functionList[-1], True, frame))
            frame.enterScope(True)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            returnType = None
            if type(self.returnCodeAndType[1]) in [NumberType, BoolType, StringType]:
                frame.push()
                returnType = self.returnCodeAndType[1]
            self.emit.printout(self.returnCodeAndType[0])
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()

        # isMain = consdecl.name.name == "main" and len(consdecl.param) == 0
        # returnType = VoidType() if isInit else consdecl.returnType
        # methodName = "<init>" if isInit else consdecl.name.name
        # intype = [ArrayType(0, StringType())] if isMain else list(map(lambda x: x.typ, consdecl.param))
        # mtype = MType(intype, returnType)

        # self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        # frame.enterScope(True)

        # glenv = o

        # # Generate code for parameter declarations
        # # if isInit:
        #     # self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        # if isMain:
        #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        # else:
        #     local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), consdecl.param, SubBody(frame, []))
        #     glenv = local.sym + glenv

        # body = consdecl.body
        # self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # # Generate code for statements
        # if isMain:
        #     # self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
        #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        # self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # if type(returnType) is VoidType:
        #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # self.emit.printout(self.emit.emitENDMETHOD(frame))
        # frame.exitScope()

    def genGlobalVarInit(self, env, frame, decls): # viết lại
        self.emit.printout(self.emit.emitMETHOD("<clinit>", FuncType("clinit", VoidType(), []), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Sinh mã cho varInit của var ở toàn cục
        for decl in decls:
            if type(decl) is VarDecl and decl.varInit:
                if type(decl.varType) is not ArrayType:
                    codeInit, initTyp = self.visit(decl.varInit, Access(frame, env, False)) 
                    codeWrite = self.emit.emitPUTSTATIC(self.className + "/" + decl.name.name, initTyp, frame)
                    self.emit.printout(codeInit + codeWrite)
                else:
                    continue

        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()