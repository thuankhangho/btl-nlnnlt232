from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Dict, List

class MemberEnv:
    pass

class FuncEnv(MemberEnv):
    pass

class VarEnv(MemberEnv):
    pass

class TypeVarDynamicEnv(MemberEnv):
    pass

class LiteralEnv(MemberEnv):
    pass

class GlobalManager:
    funcList = Dict[str, MemberEnv]
    pass

class StaticChecker(BaseVisitor, Utils):
    def __init__ (self, ast):
        self.ast = ast
        
    def check(self):
        # print(self.ast)
        param = {}
        self.visit(self.ast, param)
        
    def visitProgram(self, ast, param):
        # print(ast.decl)
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
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

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