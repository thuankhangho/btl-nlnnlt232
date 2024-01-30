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


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdeclonly.
    def visitFuncdeclonly(self, ctx:ZCodeParser.FuncdeclonlyContext):
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


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstate.
    def visitReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstate.
    def visitBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elementlist.
    def visitElementlist(self, ctx:ZCodeParser.ElementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)



del ZCodeParser