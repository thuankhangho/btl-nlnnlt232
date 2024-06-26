from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Dict, List

class MemberEnv:
    pass

class NoneType(Type):
    def __str__(self):
        return "NoneType"

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
        
    def __str__(self):
        return f"VarEnv({str(self.name)}, {str(self.typ) if self.typ else 'None'}, isVar = {str(self.isVar)})"

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
        self.currentFunc = "" # kiểm tra hàm hiện tại đang check là gì
        
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

    def findNameInParam(self, name: Id, param) -> bool:
        for scope in param:
            for x in scope:
                if name == x.name:
                    return True
        return False
    
    def getFuncEnvFromId(self, name: Id, param) -> FuncEnv:
        for scope in param:
            for x in scope:
                if x.name == name and type(x) is FuncEnv:
                    return x
        return None
    
    def setFuncEnv(self, newFuncEnv: FuncEnv, param):
        for scope in param:
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
        if self.findNameInParam(newFunc.name, self.param) and self.getFuncEnvFromId(newFunc.name, self.param): # có trong param -> tìm & cập nhật hasBody & body
            existingFunc = self.getFuncEnvFromId(newFunc.name, self.param)
            if existingFunc.hasBody == True:
                raise Redeclared(Function(), newFunc.name.name)
            else:
                existingFunc.hasBody = True
                existingFunc.body = newFunc.body
                self.setFuncEnv(existingFunc, self.param) # tìm FuncEnv có sẵn & sửa thuộc tính hasBody

        else: # không có trong param -> thêm mới vào
            paramList = []
            for x in newFunc.param:
                if x not in paramList:
                    paramList.append(x)
                else:
                    raise Redeclared(Parameter(), x.name.name)
            if newFunc.body is None:
                self.param[0].append(FuncEnv(newFunc.name, paramList, VoidType(), False))
            else:
                self.param[0].append(FuncEnv(newFunc.name, paramList, VoidType(), True, newFunc.body))

    def appendVar(self, newVar: VarDecl):
        if self.findNameInParam(newVar.name, self.param) and self.getVarEnvFromId(newVar.name, self.param):
            raise Redeclared(Variable(), newVar.name.name)
        if newVar.varType is None:
            self.param[0].append(VarEnv(newVar.name, NoneType(), 0 if newVar.modifier == "dynamic" else 1))
        else:
            self.param[0].append(VarEnv(newVar.name, newVar.varType, 2))
        
    def checkNoEntryPoint(self, ast: Program):
        for x in self.param[0]: # đi tìm main ở toàn cục
            if type(x) is FuncEnv and x.name.name == "main" and x.paramList == []:
                return
        raise NoEntryPoint()
    
    def checkNoDefinition(self, ast: Program):
        for env in self.param:
            for x in env:
                if type(x) is FuncEnv and x.hasBody == False:
                    raise NoDefinition(x.name.name)
                
    def infer(self, name, typ, param):
        for sym in param:
            for x in sym:
                if x.name == name:
                    x.typ = typ
                    return x.typ
        return None
    
    def getVarEnvFromId(self, name: Id, param) -> VarEnv:
        for scope in param:
            for x in scope:
                if x.name == name and type(x) is VarEnv:
                    return x
        return None

    def check(self):
        # thêm mọi hàm vào param
        self.addToParam(self.ast)

        # kiểm tra no entry point
        self.checkNoEntryPoint(self.ast)
        
        # kiểm tra no definition
        self.checkNoDefinition(self.ast)

        # visit phần còn lại
        self.visit(self.ast, self.param)
        return "successful"
        
    def visitProgram(self, ast: Program, param):
        for x in ast.decl:
            self.visit(x, param)

    def visitVarDecl(self, ast: VarDecl, param):
        if self.checkParam == True:
            varType = self.visit(ast.varType, param)
            param[self.scope].append(VarEnv(ast.name, varType))
            return varType

        if ast.varInit: # nếu có varInit
            varInitType = self.visit(ast.varInit, param)
            if type(varInitType) is VoidType or type(varInitType) is NoneType:
                raise TypeCannotBeInferred(ast)
        else:
            varInitType = None

        if ast.modifier == "dynamic": # Dynamic
            if self.scope == 0:
                varEnv = self.getVarEnvFromId(ast.name, param)
                if type(varEnv.typ) is NoneType and varInitType is not None:
                    varEnv.typ = varInitType
                    return VarEnv(ast.name, varInitType, 2)
                return VarEnv(ast.name, varEnv.typ, 2)
            else:
                for x in param[self.scope]:
                    if x.name == ast.name and type(x) is VarEnv:
                        raise Redeclared(Variable(), ast.name.name)
            if varInitType is None:
                param[self.scope].append(VarEnv(ast.name, NoneType(), 0))
                return VarEnv(ast.name, NoneType(), 0)
            elif type(varInitType) is NoneType:
                raise TypeCannotBeInferred(ast)
            param[self.scope].append(VarEnv(ast.name, varInitType))
            return VarEnv(ast.name, varInitType, 0)

        elif ast.modifier == "var": # Var
            if self.scope == 0:
                varEnv = self.getVarEnvFromId(ast.name, param) # -> VarEnv
                varEnv.typ = varInitType
                return VarEnv(ast.name, varEnv.typ, 2)
            else:
                for x in param[self.scope]:
                    if x.name == ast.name and type(x) is VarEnv:
                        raise Redeclared(Variable(), ast.name.name)
            
            # varEnv = self.getVarEnvFromId(ast.name, param)
            # if varEnv is not None:
            #     varEnv.typ = varInitType
            # else:
            #     param[self.scope].append(VarEnv(ast.name, varInitType, 1))
            # return VarEnv(ast.name, varInitType, 1)
            
            # varEnv = self.getVarEnvFromId(ast.name, param) # -> VarEnv
            # varEnv.typ = varInitType
            # varEnv.isVar = 1
            param[self.scope].append(VarEnv(ast.name, varInitType, 1))
            return VarEnv(ast.name, varInitType, 1)
            # param[self.scope].append(VarEnv(ast.name, varType))

        elif ast.modifier is None: # Type
            if self.scope == 0:
                varEnv = self.getVarEnvFromId(ast.name, param)
                if varInitType is None:
                    return VarEnv(ast.name, varEnv.typ, 2)
                if self.compareType(varEnv.typ, varInitType) and type(varInitType) is not VoidType and type(varInitType) is not NoneType:
                    varEnv.typ = varInitType
                    return VarEnv(ast.name, varInitType, 1)
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                for x in param[self.scope]:
                    if x.name == ast.name and type(x) is VarEnv:
                        raise Redeclared(Variable(), ast.name.name)
            
            varType = self.visit(ast.varType, param)
            if varInitType is None:
                param[self.scope].append(VarEnv(ast.name, varType, 2))
                return VarEnv(ast.name, varType, 2)
            else:
                if self.compareType(varType, varInitType):
                    param[self.scope].append(VarEnv(ast.name, varInitType, 2))
                    return VarEnv(ast.name, varInitType, 2)
                else:
                    raise TypeMismatchInStatement(ast)

    def visitFuncDecl(self, ast: FuncDecl, param):
        self.currentFunc = ast.name.name
        param = param + [[]] # thêm 1 scope vào param
        newFuncEnv = self.getFuncEnvFromId(ast.name, param)
        self.scope += 1

        # visit danh sách tham số đầu vào
        self.checkParam = True
        paramList = []
        for x in ast.param:
            paramList.append(self.visit(x, param))
        newFuncEnv.paramList = paramList
        self.checkParam = False

        # visit body
        self.visit(newFuncEnv.body, param)

        # lấy return type
        newFuncEnv.returnType = self.returnType
        
        # xóa khỏi stack param
        self.scope -= 1 # giảm scope
        param.pop(self.scope) # pop phần tử cuối khỏi stack param
        self.returnType = VoidType() # xóa return type
        self.currentFunc = "" # xóa tên hàm đang check hiện tại
        
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
            if type(e1t) is VoidType or e1t is None:
                e1t = self.infer(ast.left, StringType(), param)
            if type(e2t) is VoidType or e2t is None:
                e2t = self.infer(ast.right, StringType(), param)
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        
        if ast.op == "==":
            if type(e1t) is VoidType or e1t is None:
                e1t = self.infer(ast.left, StringType(), param)
            if type(e2t) is VoidType or e2t is None:
                e2t = self.infer(ast.right, StringType(), param)
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["=", "!=", "<", ">", "<=", ">="]:
            if type(e1t) is VoidType or e1t is None:
                e1t = self.infer(ast.left, NumberType(), param)
            if type(e2t) is VoidType or e2t is None:
                e2t = self.infer(ast.right, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["and", "or"]:
            if type(e1t) is VoidType or e1t is None:
                e1t = self.infer(ast.left, BoolType(), param)
            if type(e2t) is VoidType or e2t is None:
                e2t = self.infer(ast.right, BoolType(), param)
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op in ["+", "-", "*", "/", "%"]:
            if type(e1t) is VoidType or e1t is None:
                e1t = self.infer(ast.left, NumberType(), param)
            if type(e2t) is VoidType or e2t is None:
                e2t = self.infer(ast.right, NumberType(), param)
            if type(e1t) is not NumberType or type(e2t) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()

    def visitUnaryOp(self, ast: UnaryOp, param):
        et = self.visit(ast.operand, param)

        if ast.op == "not":
            if type(et) is VoidType or et is None:
                et = self.infer(ast.operand, BoolType(), param)
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if ast.op == "-":
            if type(et) is VoidType or et is None:
                et = self.infer(ast.operand, NumberType(), param)
            if type(et) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()

    def visitCallExpr(self, ast: CallExpr, param):
        func = self.getFuncEnvFromId(ast.name, param)
        if func is None:
            raise Undeclared(Function(), ast.name.name)
        if type(func.returnType) is VoidType:
            raise TypeMismatchInExpression(ast)

        # lấy argument
        argumentList = []
        for x in ast.args:
            argumentList.append(self.visit(x, param))

        # kiểm tra argument
        if len(argumentList) != len(func.paramList):
            raise TypeMismatchInExpression(ast)
        for i, x in enumerate(argumentList):
            if type(argumentList[i]) is VoidType:
                raise TypeCannotBeInferred(ast)
            if self.compareType(argumentList[i], func.paramList[i]) == False:
                raise TypeMismatchInExpression(ast)
        
        return func.returnType

    def visitId(self, ast: Id, param) -> Type:
        newParam = list(reversed(param))
        for scope in newParam:
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
        if len(expr.size) != size[0] or type(typ[-1]) is not NumberType:
            raise TypeMismatchInExpression(ast)
        return expr.eleType

    def visitBlock(self, ast: Block, param):
        for x in ast.stmt:
           self.visit(x, param)

        # stmtList = []
        # for x in ast.stmt:
        #    stmtList.append(self.visit(x, param))
        # return stmtList

    def visitIf(self, ast: If, param):
        param = param + [[]]
        self.scope += 1
        
        expr = self.visit(ast.expr, param)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, param)

        for x in ast.elifStmt:
            self.visit(x, param)
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
        
        param.pop(self.scope) # pop stack param
        self.scope -= 1


    def visitFor(self, ast: For, param):
        param = param + [[]] # thêm 1 scope vào param
        self.scope += 1
        name = self.visit(ast.name, param)
        if type(name) is not NumberType:
            raise TypeMismatchInStatement(ast)
        condExpr = self.visit(ast.condExpr, param)
        if type(condExpr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        updExpr = self.visit(ast.updExpr, param)

        self.loop += 1
        param[self.scope] = self.visit(ast.body, param)
        self.loop -= 1
        
        param.pop(self.scope) # pop stack param
        self.scope -= 1

    def visitContinue(self, ast: Continue, param):
        if self.loop == 0:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast: Break, param):
        if self.loop == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, param):
        if ast.expr:
            if self.currentFunc == "main":
                raise NoEntryPoint()
            returnExpr = self.visit(ast.expr, param)
            if type(returnExpr) is VoidType or type(returnExpr) is NoneType:
                raise TypeCannotBeInferred(ast)
            self.returnType = returnExpr
        else:
            self.returnType = VoidType()
        # if ast.expr:
        #     returnExpr = self.visit(ast.expr, param)
        #     if type(returnExpr) is VoidType:
        #         raise TypeCannotBeInferred(ast)
        #     if type(self.returnType) is not VoidType:
        #         self.returnType = self.visit(ast.expr, param)
        # if self.currentFunc == "main":
        #     returnExpr = self.visit(ast.expr, param)
        #     if ast.expr or type(returnExpr) is not VoidType:
        #         raise NoEntryPoint()
        # else:
        #     self.returnType = VoidType()

    def visitAssign(self, ast: Assign, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)

        if type(lhs) is NoneType and type(rhs) is NoneType:
            raise TypeCannotBeInferred(ast)
        if type(lhs) is NoneType:
            varEnv = self.getVarEnvFromId(ast.lhs, param)
            varEnv.typ = rhs
            return
        
        if type(lhs) is VoidType and type(rhs) is VoidType:
            raise TypeCannotBeInferred(ast)
        if type(lhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(rhs) is VoidType:
            rhs = lhs
            return
        if self.compareType(lhs, rhs) == False:
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, param):
        func = self.getFuncEnvFromId(ast.name, param)
        if func is None:
            raise Undeclared(Function(), ast.name.name)
        if type(func.returnType) is not VoidType:
            raise TypeMismatchInStatement(ast)

        # lấy argument
        argumentList = []
        for x in ast.args:
            argumentList.append(self.visit(x, param))

        # kiểm tra argument
        if len(argumentList) != len(func.paramList):
            raise TypeMismatchInStatement(ast)
        for i, x in enumerate(argumentList):
            if type(argumentList[i]) is VoidType or argumentList[i] is None:
                raise TypeCannotBeInferred(ast)
            if self.compareType(argumentList[i], func.paramList[i]) == False:
                raise TypeMismatchInStatement(ast)
        
        return func.returnType

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()

    def getArrayLitEle(self, arraylit: ArrayLiteral, param):
        value = arraylit.copy()
        if value == []:
            return []
        temp = value.pop(0)
        if type(temp) is not ArrayLiteral:
            return [self.visit(temp, param)] + self.getArrayLitEle(value, param)
        return [self.getArrayLitEle(temp.value, param)] + self.getArrayLitEle(value, param)
    
    def getSizeAndTypeOfArrayLit(self, arraylit: List, param, size, typ):
        value = arraylit.copy()
        if len(value) == 0:
            return ([], VoidType())
        if type(value[0]) is VoidType:
            size.append(float(len(value)))
            typ.append(VoidType)
            return (size, typ)
        if type(value[0]) is not list:
            size.append(float(len(value)))
            typ.append(self.visit(value[0], param))
            return (size, typ)
        size.append(float(len(value)))
        temp = value.pop(0)
        typ.append(ArrayType(size, temp[0]))
        return self.getSizeAndTypeOfArrayLit(temp, param, size, typ)
    
    def conformToTheType(self, naughtylist, typ):
        value = naughtylist.copy()
        if value == []:
            return True
        temp = value.pop(0)
        if type(temp) is list:
            return self.conformToTheType(temp, typ) and self.conformToTheType(value, typ)
        return (self.compareType(temp, typ)) and self.conformToTheType(value, typ)
    
    def conformToTheSize(self, naughtylist, size, idx):
        value = naughtylist.copy()
        if len(value) != size[idx]:
            return False
        for x in naughtylist:
            if type(x) is list:
                if self.conformToTheSize(x, size, idx + 1) == False:
                    return False
        return True

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        arrayLit = self.getArrayLitEle(ast.value, param)
        size, typ = self.getSizeAndTypeOfArrayLit(arrayLit, param, [], [])
        if self.conformToTheSize(arrayLit, size, 0) == False:
            raise TypeMismatchInExpression(ast)
        for x in arrayLit:
            if type(x) is VoidType:
                raise TypeCannotBeInferred(ast)
            if type(x) is list:
                if len(size) <= 1:
                    raise TypeMismatchInExpression(ast)
                if self.conformToTheType(x, typ[-1]) == False:
                    raise TypeMismatchInExpression(ast)
            elif self.compareType(x, typ[0]) == False:
                raise TypeMismatchInExpression(ast)
        return ArrayType(size, typ[-1])