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
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        if ctx.typdecl():
            return self.visit(ctx.typdecl())
        return self.visit(ctx.implidecl())
    
    
    # typdecl: typ (IDENTIFIER | arraytype) (ASSIGN expr | );
    def visitTypdecl(self, ctx: ZCodeParser.TypdeclContext):
        # print(VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType(), None, None))
        typ = self.visit(ctx.typ())
        if ctx.expr():
            if ctx.IDENTIFIER():
                return VarDecl(Id(ctx.IDENTIFIER().getText()), typ, None, self.visit(ctx.expr()))
            if ctx.arraytype():
                return VarDecl(self.visit(ctx.arraytype())[0], ArrayType(self.visit(ctx.arraytype())[1], typ), None, self.visit(ctx.expr()))
                # print("Test 304", VarDecl(self.visit(ctx.arraytype())[0], ArrayType(self.visit(ctx.arraytype())[1], typ), None, None))
        else:
            if ctx.IDENTIFIER():
                return VarDecl(Id(ctx.IDENTIFIER().getText()), typ, None, None)
            if ctx.arraytype():
                return VarDecl(self.visit(ctx.arraytype())[0], ArrayType(self.visit(ctx.arraytype())[1], typ), None, None)


    # implidecl: implivardecl | implidynadecl;
    def visitImplidecl(self, ctx:ZCodeParser.ImplideclContext):
        return self.visit(ctx.implivardecl()) if ctx.implivardecl() else self.visit(ctx.implidynadecl())


    # implivardecl: VAR IDENTIFIER ASSIGN expr;
    def visitImplivardecl(self, ctx:ZCodeParser.ImplivardeclContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "var", self.visit(ctx.expr()))


    # implidynadecl: DYNAMIC IDENTIFIER (ASSIGN expr | );
    def visitImplidynadecl(self, ctx:ZCodeParser.ImplidynadeclContext):
        if ctx.expr():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic", self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic", None)


    # funcdecl: FUNC IDENTIFIER LRB parameterlist RRB nullablenewlinelist (returnstate | blockstate | nullablenewlinelist);
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        parameterlist = self.visit(ctx.parameterlist())
        if ctx.returnstate():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), parameterlist, self.visit(ctx.returnstate()))
        if ctx.blockstate():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), parameterlist, self.visit(ctx.blockstate()))
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), parameterlist)


    # parameterlist: parameterprime | ;
    def visitParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.parameterprime())


    # parameterprime: param CM parameterprime | param;
    def visitParameterprime(self, ctx:ZCodeParser.ParameterprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.parameterprime())


    # param: typ (IDENTIFIER | arraytype);
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        if ctx.IDENTIFIER():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()))
        return VarDecl(self.visit(ctx.arraytype())[0], ArrayType(self.visit(ctx.arraytype())[1], self.visit(ctx.typ())))


    # newlinelist: NEWLINE newlinelist | NEWLINE;
    def visitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        pass


    # nullablenewlinelist: NEWLINE nullablenewlinelist | ;
    def visitNullablenewlinelist(self, ctx:ZCodeParser.NullablenewlinelistContext):
        pass


    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()


    # arraylit: LSB elementlist RSB;
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.elementlist()))


    # elementlist: expr CM elementlist | expr;
    def visitElementlist(self, ctx:ZCodeParser.ElementlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.elementlist())


    # functioncall: IDENTIFIER LRB argumentlist RRB;
    def visitFunctioncall(self, ctx:ZCodeParser.FunctioncallContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argumentlist()))


    # relational: EQUAL | CMPRSTR | DIFF | LT | GT | LE | GE;
    def visitRelational(self, ctx:ZCodeParser.RelationalContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.CMPRSTR():
            return ctx.CMPRSTR().getText()
        elif ctx.DIFF():
            return ctx.DIFF().getText()
        elif ctx.LT():
            return ctx.LT().getText()
        elif ctx.GT():
            return ctx.GT().getText()
        elif ctx.LE():
            return ctx.LE().getText()
        return ctx.GE().getText()


    # logical: AND | OR;
    def visitLogical(self, ctx:ZCodeParser.LogicalContext):
        if ctx.AND():
            return ctx.AND().getText()
        return ctx.OR().getText()


    # adding: PLUS | MINUS;
    def visitAdding(self, ctx:ZCodeParser.AddingContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        return ctx.MINUS().getText()


    # multiplying: MULTIPLY | DIVIDE | MOD;
    def visitMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.DIVIDE():
            return ctx.DIVIDE().getText()
        return ctx.MOD().getText()


    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1()[0])
        return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expr1()[0]), self.visit(ctx.expr1()[1]))


    # expr1: expr2 relational expr2 | expr2;
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2()[0])
        return BinaryOp(self.visit(ctx.relational()), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1]))


    # expr2: expr2 logical expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        return BinaryOp(self.visit(ctx.logical()), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    # expr3: expr3 adding expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        return BinaryOp(self.visit(ctx.adding()), self.visit(ctx.expr3()), self.visit(ctx.expr4()))


    # expr4: expr4 multiplying expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        return BinaryOp(self.visit(ctx.multiplying()), self.visit(ctx.expr4()), self.visit(ctx.expr5()))


    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))


    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.MINUS().getText(),self.visit(ctx.expr6()))


    # expr7: (IDENTIFIER | functioncall) LSB exprlist RSB | expr8;
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        elif ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
        elif ctx.functioncall():
            return ArrayCell(self.visit(ctx.functioncall()), self.visit(ctx.exprlist()))
        

    # expr8: IDENTIFIER | literal | LRB expr RRB | functioncall;
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.functioncall())


    # literal: NUMLIT | boollit | STRINGLIT | arraytype | arraylit;
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        if ctx.boollit():
            return self.visit(ctx.boollit())
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.arraytype():
            return self.visit(ctx.arraytype())
        return self.visit(ctx.arraylit())


    # arraytype: IDENTIFIER LSB numlist RSB;
    def visitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        return (Id(ctx.IDENTIFIER().getText()), self.visit(ctx.numlist()))


    # numlist: NUMLIT CM numlist | NUMLIT;
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMLIT().getText())]
        return [float(ctx.NUMLIT().getText())] + self.visit(ctx.numlist())


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


    # lhs: lhs: IDENTIFIER | IDENTIFIER LSB exprlist RSB;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return Id(ctx.IDENTIFIER().getText()) if ctx.getChildCount() == 1 else ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))


    # ifstate: IF LRB expr RRB nullablenewlinelist stmt elifstatelist (elsestate | );
    def visitIfstate(self, ctx:ZCodeParser.IfstateContext):
        elifstatelist = self.visit(ctx.elifstatelist())
        if ctx.elsestate():
            # print(If(self.visit(ctx.expr()), self.visit(ctx.stmt()), elifstatelist, self.visit(ctx.elsestate())))
            return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), elifstatelist, self.visit(ctx.elsestate()))
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), elifstatelist, None)
        

    # elsestate: ELSE stmt;
    def visitElsestate(self, ctx:ZCodeParser.ElsestateContext):
        return self.visit(ctx.stmt())


    # elifstatelist: elifstate elifstatelist | ;
    def visitElifstatelist(self, ctx:ZCodeParser.ElifstatelistContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.elifstate())] + self.visit(ctx.elifstatelist())


    # elifstate: ELIF LRB expr RRB nullablenewlinelist stmt;
    def visitElifstate(self, ctx:ZCodeParser.ElifstateContext):
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))


    # forstate: FOR IDENTIFIER UNTIL expr BY expr nullablenewlinelist stmt;
    def visitForstate(self, ctx:ZCodeParser.ForstateContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()[0]), self.visit(ctx.expr()[1]), self.visit(ctx.stmt()))


    # breakstate: BREAK nullablenewlinelist;
    def visitBreakstate(self, ctx:ZCodeParser.BreakstateContext):
        return Break()


    # continuestate: CONTINUE nullablenewlinelist;
    def visitContinuestate(self, ctx:ZCodeParser.ContinuestateContext):
        return Continue()


    # RETURN (expr | ) newlinelist;
    def visitReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()


    # functioncallstate: IDENTIFIER LRB argumentlist RRB newlinelist;
    def visitFunctioncallstate(self, ctx:ZCodeParser.FunctioncallstateContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argumentlist()))


    # argumentlist: argumentprime | ;
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        if ctx.argumentprime():
            return self.visit(ctx.argumentprime())
        return []


    # argumentprime: expr CM argumentprime | expr;
    def visitArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.argumentprime())


    # blockstate: BEGIN newlinelist (stmtlist | ) END newlinelist;
    def visitBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        if ctx.stmtlist():
            return Block(self.visit(ctx.stmtlist()))
        return Block([])


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