# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0080\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3*\n\3\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5\66\n\5\3\5\3\5\3\5\3\5\5\5<\n\5\5\5>\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6I\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\5\bS\n\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\tZ\n\t\3\n\3\n\3\n\3\13\3\13\3\13\5\13b\n\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16n\n\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20|\n\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \2\4\3\2\5\7\4\2--//\2|\2\"\3\2\2\2")
        buf.write("\4)\3\2\2\2\6-\3\2\2\2\b=\3\2\2\2\n?\3\2\2\2\fJ\3\2\2")
        buf.write("\2\16R\3\2\2\2\20Y\3\2\2\2\22[\3\2\2\2\24a\3\2\2\2\26")
        buf.write("c\3\2\2\2\30e\3\2\2\2\32i\3\2\2\2\34r\3\2\2\2\36{\3\2")
        buf.write("\2\2 }\3\2\2\2\"#\5\4\3\2#$\7\2\2\3$\3\3\2\2\2%&\5\6\4")
        buf.write("\2&\'\5\4\3\2\'*\3\2\2\2(*\5\6\4\2)%\3\2\2\2)(\3\2\2\2")
        buf.write("*\5\3\2\2\2+.\5\n\6\2,.\5\b\5\2-+\3\2\2\2-,\3\2\2\2.\7")
        buf.write("\3\2\2\2/\60\7\t\2\2\60\61\7-\2\2\61\62\7\37\2\2\62>\5")
        buf.write(" \21\2\63\66\5\26\f\2\64\66\7\n\2\2\65\63\3\2\2\2\65\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67;\7-\2\289\7\37\2\29<\5 \21\2")
        buf.write(":<\3\2\2\2;8\3\2\2\2;:\3\2\2\2<>\3\2\2\2=/\3\2\2\2=\65")
        buf.write("\3\2\2\2>\t\3\2\2\2?@\7\13\2\2@A\7-\2\2AB\7\'\2\2BC\5")
        buf.write("\16\b\2CD\7(\2\2DH\5\24\13\2EI\5\30\r\2FI\5\32\16\2GI")
        buf.write("\3\2\2\2HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\13\3\2\2\2JK\7")
        buf.write("\13\2\2KL\7-\2\2LM\7\'\2\2MN\5\16\b\2NO\7(\2\2O\r\3\2")
        buf.write("\2\2PS\5\20\t\2QS\3\2\2\2RP\3\2\2\2RQ\3\2\2\2S\17\3\2")
        buf.write("\2\2TU\5\22\n\2UV\7+\2\2VW\5\20\t\2WZ\3\2\2\2XZ\5\22\n")
        buf.write("\2YT\3\2\2\2YX\3\2\2\2Z\21\3\2\2\2[\\\5\26\f\2\\]\7-\2")
        buf.write("\2]\23\3\2\2\2^_\7,\2\2_b\5\24\13\2`b\3\2\2\2a^\3\2\2")
        buf.write("\2a`\3\2\2\2b\25\3\2\2\2cd\t\2\2\2d\27\3\2\2\2ef\7\b\2")
        buf.write("\2fg\t\3\2\2gh\7,\2\2h\31\3\2\2\2im\7\24\2\2jn\7-\2\2")
        buf.write("kn\7,\2\2ln\3\2\2\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2no\3")
        buf.write("\2\2\2op\7\25\2\2pq\7,\2\2q\33\3\2\2\2rs\7)\2\2st\5\36")
        buf.write("\20\2tu\7*\2\2u\35\3\2\2\2vw\5 \21\2wx\7+\2\2xy\5\36\20")
        buf.write("\2y|\3\2\2\2z|\3\2\2\2{v\3\2\2\2{z\3\2\2\2|\37\3\2\2\2")
        buf.write("}~\7/\2\2~!\3\2\2\2\r)-\65;=HRYam{")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MOD", "EQUAL", "ASSIGN", "DIFF", "LT", 
                      "LE", "GT", "GE", "CONCAT", "CMPRSTR", "LRB", "RRB", 
                      "LSB", "RSB", "CM", "NEWLINE", "IDENTIFIER", "LINECMT", 
                      "NUMLIT", "BOOLLIT", "STRINGLIT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_funcdeclonly = 5
    RULE_parameterlist = 6
    RULE_parameterprime = 7
    RULE_param = 8
    RULE_newlinelist = 9
    RULE_typ = 10
    RULE_returnstate = 11
    RULE_blockstate = 12
    RULE_arraylit = 13
    RULE_elementlist = 14
    RULE_expression = 15

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "funcdecl", 
                   "funcdeclonly", "parameterlist", "parameterprime", "param", 
                   "newlinelist", "typ", "returnstate", "blockstate", "arraylit", 
                   "elementlist", "expression" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    PLUS=23
    MINUS=24
    MULTIPLY=25
    DIVIDE=26
    MOD=27
    EQUAL=28
    ASSIGN=29
    DIFF=30
    LT=31
    LE=32
    GT=33
    GE=34
    CONCAT=35
    CMPRSTR=36
    LRB=37
    RRB=38
    LSB=39
    RSB=40
    CM=41
    NEWLINE=42
    IDENTIFIER=43
    LINECMT=44
    NUMLIT=45
    BOOLLIT=46
    STRINGLIT=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.decllist()
            self.state = 33
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.decl()
                self.state = 36
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(ZCodeParser.VAR)
                self.state = 46
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 47
                self.match(ZCodeParser.ASSIGN)
                self.state = 48
                self.expression()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 49
                    self.typ()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 50
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 57
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN]:
                    self.state = 54
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 55
                    self.expression()
                    pass
                elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstateContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstateContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ZCodeParser.FUNC)
            self.state = 62
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 63
            self.match(ZCodeParser.LRB)
            self.state = 64
            self.parameterlist()
            self.state = 65
            self.match(ZCodeParser.RRB)
            self.state = 66
            self.newlinelist()
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 67
                self.returnstate()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 68
                self.blockstate()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclonlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdeclonly

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdeclonly" ):
                return visitor.visitFuncdeclonly(self)
            else:
                return visitor.visitChildren(self)




    def funcdeclonly(self):

        localctx = ZCodeParser.FuncdeclonlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdeclonly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ZCodeParser.FUNC)
            self.state = 73
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 74
            self.match(ZCodeParser.LRB)
            self.state = 75
            self.parameterlist()
            self.state = 76
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = ZCodeParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterlist)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.parameterprime()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def parameterprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterprime" ):
                return visitor.visitParameterprime(self)
            else:
                return visitor.visitChildren(self)




    def parameterprime(self):

        localctx = ZCodeParser.ParameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterprime)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.param()
                self.state = 83
                self.match(ZCodeParser.CM)
                self.state = 84
                self.parameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.typ()
            self.state = 90
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_newlinelist)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ZCodeParser.NEWLINE)
                self.state = 93
                self.newlinelist()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstate" ):
                return visitor.visitReturnstate(self)
            else:
                return visitor.visitChildren(self)




    def returnstate(self):

        localctx = ZCodeParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ZCodeParser.RETURN)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.IDENTIFIER or _la==ZCodeParser.NUMLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = ZCodeParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ZCodeParser.BEGIN)
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 104
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.state = 105
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [ZCodeParser.END]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 109
            self.match(ZCodeParser.END)
            self.state = 110
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def elementlist(self):
            return self.getTypedRuleContext(ZCodeParser.ElementlistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ZCodeParser.LSB)
            self.state = 113
            self.elementlist()
            self.state = 114
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def elementlist(self):
            return self.getTypedRuleContext(ZCodeParser.ElementlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elementlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementlist" ):
                return visitor.visitElementlist(self)
            else:
                return visitor.visitChildren(self)




    def elementlist(self):

        localctx = ZCodeParser.ElementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elementlist)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.expression()
                self.state = 117
                self.match(ZCodeParser.CM)
                self.state = 118
                self.elementlist()
                pass
            elif token in [ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ZCodeParser.NUMLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





