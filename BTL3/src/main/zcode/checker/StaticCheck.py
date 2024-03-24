from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Dict, List

class MemberEnv:
    pass

class FuncEnv(MemberEnv):
    name: Id
    paramList: List[Type]
    returnType: Type
    hasBody: bool
    
    def __init__(self, name, paramList: List[Type] = [], returnType: Type = None, hasBody: bool = False):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType
        self.hasBody = hasBody

class VarEnv(MemberEnv):
    pass

class TypeVarDynamicEnv(MemberEnv):
    pass

class LiteralEnv(MemberEnv):
    pass

class StaticChecker(BaseVisitor, Utils):
    def __init__ (self, ast):
        self.ast = ast
        self.loop = 0 # có vào loop hay chưa (check break & continue)
        self.param = [{
                "readNumber": FuncEnv(Id("readNumber"), [], NumberType()),
                "writeNumber": FuncEnv(Id("writeNumber"), [NumberType()], VoidType()),
                "readBool": FuncEnv(Id("readBool"), [], BoolType()),
                "writeBool": FuncEnv(Id("writeBool"), [BoolType()], VoidType()),
                "readString": FuncEnv(Id("readString"), [], StringType()),
                "writeString": FuncEnv(Id("writeString"), [StringType()], VoidType())
            }]
        
    def check(self):
        # print(self.ast)
        self.visit(self.ast, self.param)
        return "successful"
        
    def visitProgram(self, ast, param):
        # if not in ast.decl:
        # for x in ast.decl():
            
        print(ast.decl[0])
        reduce(lambda _, decl: self.visit(decl, param), ast.decl, [])

    def visitVarDecl(self, ast, param):
        print(ast)

    def visitFuncDecl(self, ast, param):
        pass

    def visitNumberType(self, ast, param):
        return ast

    def visitBoolType(self, ast, param):
        return ast

    def visitStringType(self, ast, param):
        return ast

    def visitArrayType(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitBlock(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        self.loop = self.loop + 1
        self.visit(ast.body, [{}] + param)
        self.loop = self.loop - 1

    def visitContinue(self, ast, param):
        if self.loop == 0:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast, param):
        if self.loop == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        return NumberLiteral()

    def visitBooleanLiteral(self, ast, param):
        return BooleanLiteral()

    def visitStringLiteral(self, ast, param):
        return StringLiteral()

    def visitArrayLiteral(self, ast, param):
        pass