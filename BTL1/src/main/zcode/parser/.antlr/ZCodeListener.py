# Generated from d:/Pony/btl-nlnnlt232/BTL1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decllist.
    def enterDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decllist.
    def exitDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typdecl.
    def enterTypdecl(self, ctx:ZCodeParser.TypdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typdecl.
    def exitTypdecl(self, ctx:ZCodeParser.TypdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implidecl.
    def enterImplidecl(self, ctx:ZCodeParser.ImplideclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implidecl.
    def exitImplidecl(self, ctx:ZCodeParser.ImplideclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implivardecl.
    def enterImplivardecl(self, ctx:ZCodeParser.ImplivardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implivardecl.
    def exitImplivardecl(self, ctx:ZCodeParser.ImplivardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implidynadecl.
    def enterImplidynadecl(self, ctx:ZCodeParser.ImplidynadeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implidynadecl.
    def exitImplidynadecl(self, ctx:ZCodeParser.ImplidynadeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameterlist.
    def enterParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameterlist.
    def exitParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameterprime.
    def enterParameterprime(self, ctx:ZCodeParser.ParameterprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameterprime.
    def exitParameterprime(self, ctx:ZCodeParser.ParameterprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newlinelist.
    def enterNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newlinelist.
    def exitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullablenewlinelist.
    def enterNullablenewlinelist(self, ctx:ZCodeParser.NullablenewlinelistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullablenewlinelist.
    def exitNullablenewlinelist(self, ctx:ZCodeParser.NullablenewlinelistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraylit.
    def enterArraylit(self, ctx:ZCodeParser.ArraylitContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraylit.
    def exitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elementlist.
    def enterElementlist(self, ctx:ZCodeParser.ElementlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elementlist.
    def exitElementlist(self, ctx:ZCodeParser.ElementlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functioncall.
    def enterFunctioncall(self, ctx:ZCodeParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functioncall.
    def exitFunctioncall(self, ctx:ZCodeParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relational.
    def enterRelational(self, ctx:ZCodeParser.RelationalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational.
    def exitRelational(self, ctx:ZCodeParser.RelationalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logical.
    def enterLogical(self, ctx:ZCodeParser.LogicalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logical.
    def exitLogical(self, ctx:ZCodeParser.LogicalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#adding.
    def enterAdding(self, ctx:ZCodeParser.AddingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#adding.
    def exitAdding(self, ctx:ZCodeParser.AddingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiplying.
    def enterMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiplying.
    def exitMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr7.
    def enterExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr7.
    def exitExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr8.
    def enterExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr8.
    def exitExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraytype.
    def enterArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraytype.
    def exitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numlist.
    def enterNumlist(self, ctx:ZCodeParser.NumlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numlist.
    def exitNumlist(self, ctx:ZCodeParser.NumlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprlist.
    def enterExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprlist.
    def exitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardeclstate.
    def enterVardeclstate(self, ctx:ZCodeParser.VardeclstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardeclstate.
    def exitVardeclstate(self, ctx:ZCodeParser.VardeclstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstate.
    def enterAssignstate(self, ctx:ZCodeParser.AssignstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstate.
    def exitAssignstate(self, ctx:ZCodeParser.AssignstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstate.
    def enterIfstate(self, ctx:ZCodeParser.IfstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstate.
    def exitIfstate(self, ctx:ZCodeParser.IfstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elsestate.
    def enterElsestate(self, ctx:ZCodeParser.ElsestateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elsestate.
    def exitElsestate(self, ctx:ZCodeParser.ElsestateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifstatelist.
    def enterElifstatelist(self, ctx:ZCodeParser.ElifstatelistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifstatelist.
    def exitElifstatelist(self, ctx:ZCodeParser.ElifstatelistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifstate.
    def enterElifstate(self, ctx:ZCodeParser.ElifstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifstate.
    def exitElifstate(self, ctx:ZCodeParser.ElifstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstate.
    def enterForstate(self, ctx:ZCodeParser.ForstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstate.
    def exitForstate(self, ctx:ZCodeParser.ForstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstate.
    def enterBreakstate(self, ctx:ZCodeParser.BreakstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstate.
    def exitBreakstate(self, ctx:ZCodeParser.BreakstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continuestate.
    def enterContinuestate(self, ctx:ZCodeParser.ContinuestateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continuestate.
    def exitContinuestate(self, ctx:ZCodeParser.ContinuestateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstate.
    def enterReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstate.
    def exitReturnstate(self, ctx:ZCodeParser.ReturnstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functioncallstate.
    def enterFunctioncallstate(self, ctx:ZCodeParser.FunctioncallstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functioncallstate.
    def exitFunctioncallstate(self, ctx:ZCodeParser.FunctioncallstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argumentlist.
    def enterArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argumentlist.
    def exitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argumentprime.
    def enterArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argumentprime.
    def exitArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstate.
    def enterBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstate.
    def exitBlockstate(self, ctx:ZCodeParser.BlockstateContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmtlist.
    def enterStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmtlist.
    def exitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass



del ZCodeParser