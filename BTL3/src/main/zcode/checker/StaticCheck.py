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

class TypeVarEnv(MemberEnv):
    name: Id
    typ: Type

    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

class ImplicitVarEnv(MemberEnv):
    name: Id
    typ: Type
    isDynamic: bool #var = false, dynamic = true

    def __init__(self, name, typ, isDynamic):
        self.name = name
        self.typ = typ



class StaticChecker(BaseVisitor, Utils):
    def __init__ (self, ast):
        self.ast = ast
        self.loop = 0 # có vào loop hay chưa (check break & continue)
        self.param = [
            [
                FuncEnv(Id("readNumber"), [], NumberType()),
                FuncEnv(Id("writeNumber"), [NumberType()], VoidType()),
                FuncEnv(Id("readBool"), [], BoolType()),
                FuncEnv(Id("writeBool"), [BoolType()], VoidType()),
                FuncEnv(Id("readString"), [], StringType()),
                FuncEnv(Id("writeString"), [StringType()], VoidType())
            ]
        ]
        self.scope = 0 # 0 = toàn cục, > 0 = trong hàm/block stmt
        
    def compareType(self, LHS, RHS):
        if type(LHS) is not type(RHS):
            return False
        return True
        #todo: so sánh 2 biến type, kiểm tra array type sẽ kiểm tra size và eletype   
        
    def check(self):
        # print(self.ast)
        self.visit(self.ast, self.param)
        return "successful"
        
    def visitProgram(self, ast, param):
        # if not in ast.decl:
        # for x in ast.decl:
            
        # print(ast.decl[0])
        # reduce(lambda acc, cur: self.visit(cur, acc), ast.decl, param)
        for x in ast.decl:
            param[0] = param[0] + [x]
        print(param)

        for i in param:
            for x in i:
                if x.name.name == "main" and type(x) is FuncEnv:
                    print(x)
                    return
        raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        pass

    def visitFuncDecl(self, ast, param):
        name = self.visit(ast.name, param)
        param = self.visit(ast.param, param)
        body = self.visit(ast.body, param)

        return FuncEnv(name, param)

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType()

    def visitBinaryOp(self, ast, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        if ast.op == "...":
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if ast.op in ["=", "!=", "<", ">", "<=", ">="]:
            if type(left) is not NumberType or type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if ast.op in ["and", "or"]:
            if type(left) is not BoolType or type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ["+", "-"]:
            if type(left) is not NumberType or type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()


    def visitUnaryOp(self, ast, param):
        e = self.visit(ast.operand, param)
        if ctx.op == "not":
            if type(e) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ctx.op == "-":
            if type(e) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if ctx.op == '[]':
            if type(e) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType() # cần phải sửa

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
