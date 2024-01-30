# Generated from d:/Pony/btl-nlnnlt232/BTL1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,1,
        2,3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,52,8,3,1,3,1,3,1,3,1,3,
        3,3,58,8,3,3,3,60,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,71,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,81,8,6,1,7,1,7,1,7,1,7,1,
        7,3,7,88,8,7,1,8,1,8,1,8,1,9,1,9,1,9,3,9,96,8,9,1,10,1,10,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,108,8,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,122,8,14,1,15,1,
        15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,
        0,3,5,2,0,43,43,45,45,122,0,32,1,0,0,0,2,39,1,0,0,0,4,43,1,0,0,0,
        6,59,1,0,0,0,8,61,1,0,0,0,10,72,1,0,0,0,12,80,1,0,0,0,14,87,1,0,
        0,0,16,89,1,0,0,0,18,95,1,0,0,0,20,97,1,0,0,0,22,99,1,0,0,0,24,103,
        1,0,0,0,26,112,1,0,0,0,28,121,1,0,0,0,30,123,1,0,0,0,32,33,3,2,1,
        0,33,34,5,0,0,1,34,1,1,0,0,0,35,36,3,4,2,0,36,37,3,2,1,0,37,40,1,
        0,0,0,38,40,3,4,2,0,39,35,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,
        44,3,8,4,0,42,44,3,6,3,0,43,41,1,0,0,0,43,42,1,0,0,0,44,5,1,0,0,
        0,45,46,5,7,0,0,46,47,5,43,0,0,47,48,5,29,0,0,48,60,3,30,15,0,49,
        52,3,20,10,0,50,52,5,8,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,1,0,
        0,0,53,57,5,43,0,0,54,55,5,29,0,0,55,58,3,30,15,0,56,58,1,0,0,0,
        57,54,1,0,0,0,57,56,1,0,0,0,58,60,1,0,0,0,59,45,1,0,0,0,59,51,1,
        0,0,0,60,7,1,0,0,0,61,62,5,9,0,0,62,63,5,43,0,0,63,64,5,37,0,0,64,
        65,3,12,6,0,65,66,5,38,0,0,66,70,3,18,9,0,67,71,3,22,11,0,68,71,
        3,24,12,0,69,71,1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,
        0,71,9,1,0,0,0,72,73,5,9,0,0,73,74,5,43,0,0,74,75,5,37,0,0,75,76,
        3,12,6,0,76,77,5,38,0,0,77,11,1,0,0,0,78,81,3,14,7,0,79,81,1,0,0,
        0,80,78,1,0,0,0,80,79,1,0,0,0,81,13,1,0,0,0,82,83,3,16,8,0,83,84,
        5,41,0,0,84,85,3,14,7,0,85,88,1,0,0,0,86,88,3,16,8,0,87,82,1,0,0,
        0,87,86,1,0,0,0,88,15,1,0,0,0,89,90,3,20,10,0,90,91,5,43,0,0,91,
        17,1,0,0,0,92,93,5,42,0,0,93,96,3,18,9,0,94,96,1,0,0,0,95,92,1,0,
        0,0,95,94,1,0,0,0,96,19,1,0,0,0,97,98,7,0,0,0,98,21,1,0,0,0,99,100,
        5,6,0,0,100,101,7,1,0,0,101,102,5,42,0,0,102,23,1,0,0,0,103,107,
        5,18,0,0,104,108,5,43,0,0,105,108,5,42,0,0,106,108,1,0,0,0,107,104,
        1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,110,
        5,19,0,0,110,111,5,42,0,0,111,25,1,0,0,0,112,113,5,39,0,0,113,114,
        3,28,14,0,114,115,5,40,0,0,115,27,1,0,0,0,116,117,3,30,15,0,117,
        118,5,41,0,0,118,119,3,28,14,0,119,122,1,0,0,0,120,122,1,0,0,0,121,
        116,1,0,0,0,121,120,1,0,0,0,122,29,1,0,0,0,123,124,5,45,0,0,124,
        31,1,0,0,0,11,39,43,51,57,59,70,80,87,95,107,121
    ]

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
                     "'\\n'" ]

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
        self.checkVersion("4.13.1")
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.funcdecl()
                pass
            elif token in [3, 4, 5, 7, 8]:
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




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
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
            elif token in [3, 4, 5, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 49
                    self.typ()
                    pass
                elif token in [8]:
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
                if token in [29]:
                    self.state = 54
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 55
                    self.expression()
                    pass
                elif token in [-1, 3, 4, 5, 7, 8, 9]:
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
            if token in [6]:
                self.state = 67
                self.returnstate()
                pass
            elif token in [18]:
                self.state = 68
                self.blockstate()
                pass
            elif token in [-1, 3, 4, 5, 7, 8, 9]:
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




    def parameterlist(self):

        localctx = ZCodeParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterlist)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.parameterprime()
                pass
            elif token in [38]:
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




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_newlinelist)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ZCodeParser.NEWLINE)
                self.state = 93
                self.newlinelist()
                pass
            elif token in [-1, 3, 4, 5, 6, 7, 8, 9, 18]:
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




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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
            if not(_la==43 or _la==45):
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
            if token in [43]:
                self.state = 104
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [42]:
                self.state = 105
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [19]:
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




    def elementlist(self):

        localctx = ZCodeParser.ElementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elementlist)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.expression()
                self.state = 117
                self.match(ZCodeParser.CM)
                self.state = 118
                self.elementlist()
                pass
            elif token in [40]:
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





