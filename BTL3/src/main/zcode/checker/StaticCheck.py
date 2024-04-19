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
        self.checkParam = False # đang visit param của function hay không
        
    def compareType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if LHS.eleType == RHS.eleType and LHS.size == RHS.size:
                return True
            return False

        if type(LHS) is ArrayType:
            if LHS.eleType != type(RHS):
                return False
            return True
        
        if type(RHS) is ArrayType:
            if RHS.eleType != type(LHS):
                return False
            return True

        if type(LHS) != type(RHS):
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
        
    def visitProgram(self, ast: Program, param):
        for x in ast.decl:
            self.visit(x, param)

    def visitVarDecl(self, ast: VarDecl, param):
        # print(ast)
        if self.checkParam == True:
            varType = self.visit(ast.varType, param)
            param[self.scope].append(VarEnv(ast.name, varType))
            return varType

        if ast.varInit:
            varInitType = self.visit(ast.varInit, param)
            if type(varInitType) is VoidType:
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
            # print(ast.name, varType, varInitType)
            if self.compareType(varType, varInitType):
                param[self.scope].append(VarEnv(ast.name, varType))
            else:
                raise TypeMismatchInStatement(ast)

    def visitFuncDecl(self, ast: FuncDecl, param):
        param = param + [[]] # thêm 1 scope vào param
        newFuncEnv = self.getFuncEnvFromId(ast.name)

        # visit danh sách tham số đầu vào
        self.scope += 1
        self.checkParam = True
        paramList = []
        for x in ast.param:
            paramList.append(self.visit(x, param))
        newFuncEnv.paramList = paramList
        self.checkParam = False

        # visit body
        body = self.visit(newFuncEnv.body, param)
        param[self.scope].append(body)
        self.scope -= 1

        # lấy return type
        newFuncEnv.returnType = self.returnType
        
        param.pop(self.scope) # pop stack param
        self.returnType = VoidType() # xóa return type
        
    def visitNumberType(self, ast: NumberType, param):
        return NumberType()

    def visitBoolType(self, ast: BoolType, param):
        return BoolType()

    def visitStringType(self, ast: StringType, param):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param):
        return ast

    def visitBinaryOp(self, ast: BinaryOp, param):
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

    def visitUnaryOp(self, ast: UnaryOp, param):
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
        
        # if ast.op == '[]':
        #     if type(et) is VoidType:
        #         et = self.infer(ast.operand.name, NumberType(), param)
        #     if type(et) is not NumberType:
        #         raise TypeMismatchInExpression(ast)
        #     return NumberType() # cần phải sửa

    def visitCallExpr(self, ast: CallExpr, param):
        func = self.getFuncEnvFromId(ast.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if type(func.returnType) is VoidType:
            raise TypeMismatchInExpression(ast)

        argumentList = []
        for x in ast.args:
            argumentList.append(self.visit(x, param))

        if len(argumentList) != len(func.paramList):
            raise TypeMismatchInExpression(ast)
        
        for i, x in enumerate(argumentList):
            if self.compareType(argumentList[i], func.paramList[i]) == False:
                raise TypeMismatchInExpression(ast)
        
        return func.returnType

    def visitId(self, ast: Id, param) -> Type:
        for scope in param:
            for y in scope:
                if y.name.name == ast.name:
                    return y.returnType if type(y) is FuncEnv else y.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, param):
        # a[0]
        expr = self.visit(ast.arr, param) # a
        if type(expr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        idx = []
        for x in ast.idx:
            idx.append(self.visit(x, param)) # [0]

        size, typ = self.getSizeAndTypeOfArrayLit(idx, param, [], [])
        if expr.size != size or type(typ[0]) != NumberType:
            raise TypeMismatchInExpression(ast)
        # print(expr, size, expr.eleType)
        return expr.eleType

    def visitBlock(self, ast: Block, param):
        for x in ast.stmt:
            self.visit(x, param)

    def visitIf(self, ast: If, param):
        pass

    def visitFor(self, ast: For, param):
        self.loop += 1
        self.visit(ast.body, [{}] + param)
        self.loop -= 1

    def visitContinue(self, ast: Continue, param):
        if self.loop == 0:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast: Break, param):
        if self.loop == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, param):
        if ast.expr:
            if type(self.visit(ast.expr, param)) is VoidType:
                raise TypeCannotBeInferred(ast)
            if type(self.returnType) is not None:
                self.returnType = self.visit(ast.expr, param)
        else:
            self.returnType = VoidType()

    def visitAssign(self, ast: Assign, param):
        pass

    def visitCallStmt(self, ast: CallStmt, param):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()

    def getArrayLitEle(self, arraylit: ArrayLiteral, param):
        value = arraylit
        if value == []:
            return []
        temp = value.pop(0)
        if type(temp) is not ArrayLiteral:
            return [self.visit(temp, param)] + self.getArrayLitEle(value, param)
        return [self.getArrayLitEle(temp.value, param)] + self.getArrayLitEle(value, param)
    
    def getSizeAndTypeOfArrayLit(self, arraylit: List, param, size, typ):
        value = arraylit
        if len(value) == 0:
            return ([], None)
        if type(value[0]) is not list:
            size.append(float(len(value)))
            typ.append(self.visit(value[0], param))
            return (size, typ)
        size.append(float(len(value)))
        temp = value.pop(0)
        typ.append(ArrayType(size, temp[0]))
        return self.getSizeAndTypeOfArrayLit(temp, param, size, typ)

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        arrayLit = self.getArrayLitEle(ast.value, param)
        size, typ = self.getSizeAndTypeOfArrayLit(arrayLit, param, [], [])
        for x in arrayLit:
            if type(x) is VoidType:
                raise TypeCannotBeInferred(ast)
            if self.compareType(x, typ[0]) == False:
                raise TypeMismatchInExpression(ast)
        return ArrayType(size, typ[0])