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
    body: Stmt
    
    def __init__(self, name, paramList: List[Type] = [], returnType: Type = VoidType, hasBody: bool = False, body: Stmt = None):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType
        self.hasBody = hasBody
        self.body = body

    def __str__(self):
        return f"FuncEnv(name = {str(self.name)}, paramList = [{', '.join(str(i) for i in self.paramList)}], returnType = {str(self.returnType)}, hasBody = {str(self.hasBody)})"


class VarEnv(MemberEnv):
    name: Id
    typ: Type
    isVar: int #dynamic = 0, var = 1, type = 2

    def __init__(self, name, typ, isVar = 2):
        self.name = name
        self.typ = typ
        self.isVar = isVar

class StaticChecker(BaseVisitor, Utils):
    def __init__ (self, ast):
        self.ast = ast
        self.loop = 0 # có vào loop hay chưa (check break & continue)
        self.param: List[MemberEnv] = [
            [
                FuncEnv(Id("readNumber"), [], NumberType(), True),
                FuncEnv(Id("writeNumber"), [NumberType()], VoidType(), True),
                FuncEnv(Id("readBool"), [], BoolType(), True),
                FuncEnv(Id("writeBool"), [BoolType()], VoidType(), True),
                FuncEnv(Id("readString"), [], StringType(), True),
                FuncEnv(Id("writeString"), [StringType()], VoidType(), True)
            ]
        ]
        self.scope = 0 # 0 = toàn cục, > 0 = trong hàm/block stmt
        self.returnType: Type = VoidType() # return type của hàm
        
    def compareType(self, LHS, RHS):
        if type(LHS) is not type(RHS):
            return False
        return True
        #todo: so sánh 2 biến type, kiểm tra array type sẽ kiểm tra size và eletype

    def findNameInParam(self, name: str) -> bool:
        for scope in self.param:
            for x in scope:
                if name == x.name:
                    return True
        return False
    
    def getFuncEnvFromId(self, name: Id) -> FuncEnv:
        for scope in self.param:
            for x in scope:
                if x.name == name:
                    return x
        return None
    
    def setFuncEnv(self, newFuncEnv: FuncEnv):
        for scope in self.param:
            for x in scope:
                if newFuncEnv.name == x.name:
                    x = newFuncEnv                    

    def addToParam(self, ast: Program):
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.appendFunc(x)
            else:
                self.appendVar(x)

    def appendFunc(self, newFunc: FuncDecl):
        if self.findNameInParam(newFunc.name): # có trong param -> tìm & cập nhật hasBody & body
            existingFunc = self.getFuncEnvFromId(newFunc.name)
            if existingFunc.hasBody == True:
                raise Redeclared(Function(), newFunc.name.name)
            else:
                existingFunc.hasBody = True
                existingFunc.body = newFunc.body
                self.setFuncEnv(existingFunc) # tìm FuncEnv có sẵn & sửa thuộc tính hasBody

        else: # không có trong param -> thêm mới vào
            paramType = newFunc.param # sửa lại thành self.visit(newFunc.param, self.param)
            if newFunc.body is None:
                self.param[0].append(FuncEnv(newFunc.name, paramType, VoidType(), False))
            else:
                self.param[0].append(FuncEnv(newFunc.name, paramType, VoidType(), True, newFunc.body))

        # for x in self.param[0]:
        #     print(x.name, x.body)
        # print("=================================")

    def appendVar(self, newVar: VarDecl):
        if self.findNameInParam(newVar.name):
            raise Redeclared(Variable(), newVar.name.name)
        self.param[0].append(VarEnv(newVar.name, newVar.varType, newVar.modifier))
        
    def checkNoEntryPoint(self, ast: Program):
        for x in self.param[0]: # đi tìm main ở toàn cục
            if x.name.name == "main" and x.paramList == []:
                return
        raise NoEntryPoint()
    
    def checkNoDefinition(self, ast: Program):
        for env in self.param:
            for x in env:
                if type(x) is FuncEnv and x.hasBody == False:
                    raise NoDefinition(x.name.name)
                
    def infer(self, name, typ, o):
        for sym in o:
            for x in sym:
                if x.name == name:
                    x.typ = typ
                    return x.typ
        return VoidType()
    
    def getVarEnvFromId(self, name: Id) -> VarEnv:
        for scope in self.param:
            for x in scope:
                if x.name == name:
                    return x
        return None

    def check(self):
        # thêm mọi hàm vào param
        self.addToParam(self.ast)

        # kiểm tra no entry point
        self.checkNoEntryPoint(self.ast)
        
        # kiểm tra no entry point
        self.checkNoDefinition(self.ast)

        # visit phần còn lại
        self.visit(self.ast, self.param)
        return "successful"
        
    def visitProgram(self, ast, param):
        for x in ast.decl:
            self.visit(x, param)

    def visitVarDecl(self, ast, param):
        if ast.varInit:
            varInitType = self.visit(ast.varInit, param)
            print(varInitType)

            if type(varInitType) is ArrayType:
                varInitType = varInitType.eleType

            elif type(varInitType) is VoidType:
                raise TypeCannotBeInferred(ast)
        else:
            varInitType = VoidType()

        if ast.modifier == "dynamic":
            varEnv = self.getVarEnvFromId(ast.name) # -> VarEnv
            if varEnv is None:
                varType = varInitType
            else:
                varType = varEnv.typ
            param[self.scope].append(VarEnv(ast.name, varType))

        elif ast.modifier == "var":
            varType = varInitType
            param[self.scope].append(VarEnv(ast.name, varType))

        elif ast.modifier is None:
            varType = self.visit(ast.varType, param)
            if self.compareType(varType, varInitType):
                param[self.scope].append(VarEnv(ast.name, varType))
            else:
                raise TypeMismatchInStatement(ast)

    def visitFuncDecl(self, ast: FuncDecl, param):
        param = param + [[]] # thêm 1 scope vào param
        newFuncEnv = self.getFuncEnvFromId(ast.name)

        # visit danh sách tham số đầu vào
        self.scope += 1
        for x in ast.param:
            self.visit(x, param)

        # visit body
        body = self.visit(newFuncEnv.body, param)
        param[self.scope].append(body)
        self.scope -= 1

        # lấy return type
        self.getFuncEnvFromId(ast.name).returnType = self.returnType
        
        param.pop(self.scope) # pop stack param
        self.returnType = VoidType() # xóa return type
        
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
                e1t = self.infer(ast.left.name, StringType(), param)
            if type(e2t) is VoidType:
                e2t = self.infer(ast.right.name, StringType(), param)
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        
        if ast.op == "==":
            if type(e1t) is VoidType:
                e1t = self.infer(ast.left.name, StringType(), param)
            if type(e2t) is VoidType:
                e2t = self.infer(ast.right.name, StringType(), param)
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["=", "!=", "<", ">", "<=", ">="]:
            if type(e1t) is VoidType:
                e1t = self.infer(ast.left.name, NumberType(), param)
            if type(e2t) is VoidType:
                e2t = self.infer(ast.right.name, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if ast.op in ["and", "or"]:
            if type(e1t) is VoidType:
                e1t = self.infer(ast.left.name, BoolType(), param)
            if type(e2t) is VoidType:
                e2t = self.infer(ast.right.name, BoolType(), param)
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["+", "-"]:
            if type(e1t) is VoidType:
                e1t = self.infer(ast.left.name, NumberType(), param)
            if type(e2t) is VoidType:
                e2t = self.infer(ast.right.name, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()

    def visitUnaryOp(self, ast, param):
        et = self.visit(ast.operand, param)

        if ast.op == "not":
            if type(et) is VoidType:
                et = self.infer(ast.operand.name, BoolType(), param)
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op == "-":
            if type(et) is VoidType:
                et = self.infer(ast.operand.name, NumberType(), param)
            if type(et) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if ast.op == '[]':
            if type(et) is VoidType:
                et = self.infer(ast.operand.name, NumberType(), param)
            if type(et) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType() # cần phải sửa

    def visitCallExpr(self, ast, param):
        func = self.getFuncEnvFromId(ast.name)
        print(func)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if type(func.returnType) is VoidType:
            raise TypeMismatchInExpression(ast)
        

        argumentList = []
        for x in ast.args:
            argumentList.append(self.visit(x, param))
        return

    def visitId(self, ast, param) -> Type:
        for scope in param:
            for y in scope:
                if y.name.name == ast.name:
                    return y.returnType if type(y) is FuncEnv else y.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param):
        pass

    def visitBlock(self, ast, param):
        for x in ast.stmt:
            self.visit(x, param)

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        self.loop += 1
        self.visit(ast.body, [{}] + param)
        self.loop -= 1

    def visitContinue(self, ast, param):
        if self.loop == 0:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast, param):
        if self.loop == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if ast.expr:
            if type(self.visit(ast.expr, param)) is VoidType:
                raise TypeCannotBeInferred(ast)
            if type(self.returnType) is not None:
                self.returnType = self.visit(ast.expr, param)
        else:
            self.returnType = VoidType()

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
        arrayLit = []
        for x in ast.value:
            arrayLit.append(self.visit(x, param))
        arrayLitType = arrayLit[0]
        for x in arrayLit:
            if type(x) is VoidType:
                raise TypeCannotBeInferred(ast)
            if type(x) != type(arrayLitType):
                raise TypeMismatchInExpression(ast)
        return ArrayType(arrayLit.count, arrayLitType)