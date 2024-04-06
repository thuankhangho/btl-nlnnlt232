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
    name: Id
    typ: Type
    isVar: int #dynamic = 0, var = 1, type = 2

    def __init__(self, name, typ, isVar = 2):
        self.name = name
        self.typ = typ
        self.isVar = isVar

class VoidType(Type):
    pass

class Utils:
    def infer(name, typ, o):
        for sym in o:
            for x in sym:
                if x.name.name == name:
                    x.typ = typ
                    return x.typ

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
        for x in ast.decl:
            # print(self.visit(x, param))
            param[self.scope] = param[self.scope] + [self.visit(x, param)]
        
        # for x in param:
        #     print(x)
        # for i in param:
        #     for x in i:
        #         if x.name.name == "main" and type(x) is FuncEnv:
        #             return
        # raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        varInitType = self.visit(ast.varInit, param)

        if ast.modifier == "dynamic":
            varType = Utils.infer(ast.name.name, varInitType, param)
            return VarEnv(ast.name, varType, 0)

        if ast.modifier == "var":
            varType = Utils.infer(ast.name.name, varInitType, param)
            return VarEnv(ast.name, varType, 1)

        if ast.modifier is None:
            varType = self.visit(ast.varType, param)
            return VarEnv(ast.name, varType, 2)

    def visitFuncDecl(self, ast, param):
        name = self.visit(ast.name, param)
        paramList = []
        for x in ast.param:
            paramList = paramList + [self.visit(x, param)]
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
        e1t = self.visit(ast.left, param)
        e2t = self.visit(ast.right, param)

        if ast.op == "...":
            if type(e1t) is VoidType:
                e1t = Utils.infer(ast.left.name, StringType(), param)
            if type(e2t) is VoidType:
                e2t = Utils.infer(ast.right.name, StringType(), param)
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        
        if ast.op in ["=", "!=", "<", ">", "<=", ">="]:
            if type(e1t) is VoidType:
                e1t = Utils.infer(ast.left.name, NumberType(), param)
            if type(e2t) is VoidType:
                e2t = Utils.infer(ast.right.name, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if ast.op in ["and", "or"]:
            if type(e1t) is VoidType:
                e1t = Utils.infer(ast.left.name, BoolType(), param)
            if type(e2t) is VoidType:
                e2t = Utils.infer(ast.right.name, BoolType(), param)
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["+", "-"]:
            if type(e1t) is VoidType:
                e1t = Utils.infer(ast.left.name, NumberType(), param)
            if type(e2t) is VoidType:
                e2t = Utils.infer(ast.right.name, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()


    def visitUnaryOp(self, ast, param):
        et = self.visit(ast.operand, param)

        if ast.op == "not":
            if type(et) is VoidType:
                et = Utils.infer(ast.operand.name, BoolType(), param)
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op == "-":
            if type(et) is VoidType:
                et = Utils.infer(ast.operand.name, NumberType(), param)        
            if type(et) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if ast.op == '[]':
            if type(et) is VoidType:
                et = Utils.infer(ast.operand.name, NumberType(), param)
            if type(et) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType() # cần phải sửa

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        for x in param:
            if x.name == ast.name:
                return x.typ
        raise Undeclared(Identifier(), ast.name)

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
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        pass
