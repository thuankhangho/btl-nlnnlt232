# Student ID: 2011357
# Student name: Ho Thuan Khang

from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # program: nullablenewlinelist decllist EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
    
    # decl: funcdecl | vardecl;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        return self.visit(ctx.vardecl())


    # vardecl: (typdecl | implidecl) nullablenewlinelist;
    def visitVarDecl(self, ctx: ZCodeParser.VardeclContext):
        # print(self.visit(ctx.typdecl()))
        if ctx.typdecl():
            return self.visit(ctx.typdecl())
        return self.visit(ctx.implidecl())
    
    # typdecl: typ (IDENTIFIER | arraytype) (ASSIGN expr | );
    def visitTypDecl(self, ctx: ZCodeParser.TypdeclContext):
        # print(VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType(), None, None))
        if ctx.IDENTIFIER():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType(), None, None)
        return VarDecl(self.visit(ctx.arraytype()), NumberType(), None, None)


    # Visit a parse tree produced by ZCodeParser#implidecl.
    def visitImplidecl(self, ctx:ZCodeParser.ImplideclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implivardecl.
    def visitImplivardecl(self, ctx:ZCodeParser.ImplivardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implidynadecl.
    def visitImplidynadecl(self, ctx:ZCodeParser.ImplidynadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameterlist.
    def visitParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameterprime.
    def visitParameterprime(self, ctx:ZCodeParser.ParameterprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinelist.
    def visitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullablenewlinelist.
    def visitNullablenewlinelist(self, ctx:ZCodeParser.NullablenewlinelistContext):
        return self.visitChildren(ctx)


    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elementlist.
    def visitElementlist(self, ctx:ZCodeParser.ElementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functioncall.
    def visitFunctioncall(self, ctx:ZCodeParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational.
    def visitRelational(self, ctx:ZCodeParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical.
    def visitLogical(self, ctx:ZCodeParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding.
    def visitAdding(self, ctx:ZCodeParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying.
    def visitMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # literal: NUMLIT | boollit | STRINGLIT | arraytype;
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.NUMLIT():
            return NumberLiteral(int(ctx.NUMLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        return self.visit(ctx.arraytype())


    # arraytype: IDENTIFIER LSB numlist RSB;
    def visitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        return ArrayCell()


    # numlist: NUMLIT CM numlist | NUMLIT;
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        return self.visitChildren(ctx)


    # exprlist: expr CM exprlist | expr;
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # vardeclstate: (typdecl | implidecl) newlinelist;
    def visitVardeclstate(self, ctx:ZCodeParser.VardeclstateContext):
        if ctx.typdecl():
            return self.visit(ctx.typdecl())
        return self.visit(ctx.implidecl())


    # assignstate: lhs ASSIGN expr newlinelist;
    def visitAssignstate(self, ctx:ZCodeParser.AssignstateContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    # lhs: IDENTIFIER | arraytype;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return ctx.IDENTIFIER().getText() if ctx.IDENTIFIER else self.visit(ctx.arraytype())


    # ifstate: IF LRB expr RRB nullablenewlinelist stmt (elifstatelist | ) (elsestate | );
    def visitIfstate(self, ctx:ZCodeParser.IfstateContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), self.visit(ctx.elsestatelist()), self.visit(ctx.elsestate()))
        

    # elsestate: ELSE stmt;
    def visitElsestate(self, ctx:ZCodeParser.ElsestateContext):
        return self.visit(ctx.stmt())


    # elifstatelist: elifstate elifstatelist | elifstate;
    def visitElifstatelist(self, ctx:ZCodeParser.ElifstatelistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.elifstate())]
        return [self.visit(ctx.elifstate())] + self.visit(ctx.elifstatelist())


    # elifstate: ELIF LRB expr RRB nullablenewlinelist stmt;
    def visitElifstate(self, ctx:ZCodeParser.ElifstateContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()))


    # forstate: FOR IDENTIFIER UNTIL expr BY expr nullablenewlinelist stmt;
    def visitForstate(self, ctx:ZCodeParser.ForstateContext):
        return For(ctx.IDENTIFIER().getText(), self.visit(ctx.expr()[0]), self.visit(ctx.expr()[1]), self.visit(ctx.stmt()))


    # breakstate: BREAK nullablenewlinelist;
    def visitBreakstate(self, ctx:ZCodeParser.BreakstateContext):
        return Break()


    # continuestate: CONTINUE nullablenewlinelist;
    def visitContinuestate(self, ctx:ZCodeParser.ContinuestateContext):
        return Continue()


    # RETURN (expr | ) newlinelist;
    def visitReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        return Return(self.visit(ctx.expr()))


    # functioncallstate: IDENTIFIER LRB argumentlist RRB newlinelist;
    def visitFunctioncallstate(self, ctx:ZCodeParser.FunctioncallstateContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.argumentlist()))


    # argumentlist: argumentprime | ;
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        if ctx.argumentprime():
            return self.visit(ctx.argumentprime())
        return None


    # argumentprime: expr CM argumentprime | expr;
    def visitArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        if ctx.expr():
            return [self.visit(ctx.expr())]
        expr = self.visit(ctx.expr())
        argumentprime = self.visit(ctx.argumentprime())
        return [self.visit(ctx.expr())] + self.visit(ctx.argumentprime())


    # blockstate: BEGIN newlinelist (stmtlist | ) END newlinelist;
    def visitBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        if ctx.stmtlist():
            return Block(self.visit(ctx.stmtlist()))
        return Block()


    # stmtlist: stmt stmtlist | stmt;
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())


    # stmt: vardeclstate | assignstate | ifstate | forstate | breakstate | continuestate | returnstate | functioncallstate | blockstate;
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.vardeclstate():
            return self.visit(ctx.vardeclstate())
        elif ctx.assignstate():
            return self.visit(ctx.assignstate())
        elif ctx.ifstate():
            return self.visit(ctx.ifstate())
        elif ctx.forstate():
            return self.visit(ctx.forstate())
        elif ctx.breakstate():
            return self.visit(ctx.breakstate())
        elif ctx.continuestate():
            return self.visit(ctx.continuestate())
        elif ctx.returnstate():
            return self.visit(ctx.returnstate())
        elif ctx.functioncallstate():
            return self.visit(ctx.functioncallstate())
        elif ctx.blockstate():
            return self.visit(ctx.blockstate())
    
    # boollit: TRUE | FALSE;
    def visitBoollit(self, ctx: ZCodeParser.BoollitContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        return BooleanLiteral(False)


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
        return f"If({str(self.expr)}, {str(self.thenStmt)}), [{', '.join(f'({str(x[0])}, {str(x[1])})' for x in self.elifStmt)}], {str(self.elseStmt) if self.elseStmt else 'None'}"


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