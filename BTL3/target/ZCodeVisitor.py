# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typdecl.
    def visitTypdecl(self, ctx:ZCodeParser.TypdeclContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraytype.
    def visitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlist.
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardeclstate.
    def visitVardeclstate(self, ctx:ZCodeParser.VardeclstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstate.
    def visitAssignstate(self, ctx:ZCodeParser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstate.
    def visitIfstate(self, ctx:ZCodeParser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsestate.
    def visitElsestate(self, ctx:ZCodeParser.ElsestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstatelist.
    def visitElifstatelist(self, ctx:ZCodeParser.ElifstatelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstate.
    def visitElifstate(self, ctx:ZCodeParser.ElifstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstate.
    def visitForstate(self, ctx:ZCodeParser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstate.
    def visitBreakstate(self, ctx:ZCodeParser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestate.
    def visitContinuestate(self, ctx:ZCodeParser.ContinuestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstate.
    def visitReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functioncallstate.
    def visitFunctioncallstate(self, ctx:ZCodeParser.FunctioncallstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentprime.
    def visitArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstate.
    def visitBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boollit.
    def visitBoollit(self, ctx:ZCodeParser.BoollitContext):
        return self.visitChildren(ctx)



del ZCodeParser