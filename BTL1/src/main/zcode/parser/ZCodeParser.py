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
        buf.write("\u0127\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3R\n\3\3\4\3\4\5\4V\n\4\3\5\3")
        buf.write("\5\5\5Z\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6c\n\6\3\7\3")
        buf.write("\7\5\7g\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\ts\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n~\n\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u008a")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u0091\n\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\5\17\u0099\n\17\3\20\3\20\3\20\5\20\u009e")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\22\5\22\u00a5\n\22\3\22\3")
        buf.write("\22\3\23\3\23\3\23\5\23\u00ac\n\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00ba\n")
        buf.write("\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00c9\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u00d0\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u00d9\n\34\f\34\16\34\u00dc\13\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\7\35\u00e5\n\35\f\35\16\35\u00e8")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u00f1\n")
        buf.write("\36\f\36\16\36\u00f4\13\36\3\37\3\37\3\37\5\37\u00f9\n")
        buf.write("\37\3 \3 \3 \5 \u00fe\n \3!\3!\3!\3!\3!\3!\3!\3!\7!\u0108")
        buf.write("\n!\f!\16!\u010b\13!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0113")
        buf.write("\n\"\3#\3#\3#\3#\5#\u0119\n#\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\5%\u0125\n%\3%\2\6\668:@&\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\7\3\2")
        buf.write("\5\7\5\2\36\36 $&&\3\2\27\30\3\2\31\32\3\2\33\35\2\u011f")
        buf.write("\2J\3\2\2\2\4Q\3\2\2\2\6U\3\2\2\2\bY\3\2\2\2\n]\3\2\2")
        buf.write("\2\ff\3\2\2\2\16h\3\2\2\2\20m\3\2\2\2\22t\3\2\2\2\24\u0081")
        buf.write("\3\2\2\2\26\u0089\3\2\2\2\30\u0090\3\2\2\2\32\u0092\3")
        buf.write("\2\2\2\34\u0098\3\2\2\2\36\u009d\3\2\2\2 \u009f\3\2\2")
        buf.write("\2\"\u00a1\3\2\2\2$\u00a8\3\2\2\2&\u00b0\3\2\2\2(\u00b9")
        buf.write("\3\2\2\2*\u00bb\3\2\2\2,\u00bd\3\2\2\2.\u00bf\3\2\2\2")
        buf.write("\60\u00c1\3\2\2\2\62\u00c8\3\2\2\2\64\u00cf\3\2\2\2\66")
        buf.write("\u00d1\3\2\2\28\u00dd\3\2\2\2:\u00e9\3\2\2\2<\u00f8\3")
        buf.write("\2\2\2>\u00fd\3\2\2\2@\u00ff\3\2\2\2B\u0112\3\2\2\2D\u0118")
        buf.write("\3\2\2\2F\u011a\3\2\2\2H\u0124\3\2\2\2JK\5\4\3\2KL\7\2")
        buf.write("\2\3L\3\3\2\2\2MN\5\6\4\2NO\5\4\3\2OR\3\2\2\2PR\5\6\4")
        buf.write("\2QM\3\2\2\2QP\3\2\2\2R\5\3\2\2\2SV\5\22\n\2TV\5\b\5\2")
        buf.write("US\3\2\2\2UT\3\2\2\2V\7\3\2\2\2WZ\5\n\6\2XZ\5\f\7\2YW")
        buf.write("\3\2\2\2YX\3\2\2\2Z[\3\2\2\2[\\\5\36\20\2\\\t\3\2\2\2")
        buf.write("]^\5 \21\2^b\7-\2\2_`\7\37\2\2`c\5\62\32\2ac\3\2\2\2b")
        buf.write("_\3\2\2\2ba\3\2\2\2c\13\3\2\2\2dg\5\16\b\2eg\5\20\t\2")
        buf.write("fd\3\2\2\2fe\3\2\2\2g\r\3\2\2\2hi\7\t\2\2ij\7-\2\2jk\7")
        buf.write("\37\2\2kl\5\62\32\2l\17\3\2\2\2mn\7\n\2\2nr\7-\2\2op\7")
        buf.write("\37\2\2ps\5\62\32\2qs\3\2\2\2ro\3\2\2\2rq\3\2\2\2s\21")
        buf.write("\3\2\2\2tu\7\13\2\2uv\7-\2\2vw\7\'\2\2wx\5\26\f\2xy\7")
        buf.write("(\2\2y}\5\36\20\2z~\5\"\22\2{~\5$\23\2|~\3\2\2\2}z\3\2")
        buf.write("\2\2}{\3\2\2\2}|\3\2\2\2~\177\3\2\2\2\177\u0080\5\36\20")
        buf.write("\2\u0080\23\3\2\2\2\u0081\u0082\7\13\2\2\u0082\u0083\7")
        buf.write("-\2\2\u0083\u0084\7\'\2\2\u0084\u0085\5\26\f\2\u0085\u0086")
        buf.write("\7(\2\2\u0086\25\3\2\2\2\u0087\u008a\5\30\r\2\u0088\u008a")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\27\3\2\2\2\u008b\u008c\5\32\16\2\u008c\u008d\7+\2\2\u008d")
        buf.write("\u008e\5\30\r\2\u008e\u0091\3\2\2\2\u008f\u0091\5\32\16")
        buf.write("\2\u0090\u008b\3\2\2\2\u0090\u008f\3\2\2\2\u0091\31\3")
        buf.write("\2\2\2\u0092\u0093\5 \21\2\u0093\u0094\7-\2\2\u0094\33")
        buf.write("\3\2\2\2\u0095\u0096\7,\2\2\u0096\u0099\5\34\17\2\u0097")
        buf.write("\u0099\7,\2\2\u0098\u0095\3\2\2\2\u0098\u0097\3\2\2\2")
        buf.write("\u0099\35\3\2\2\2\u009a\u009b\7,\2\2\u009b\u009e\5\36")
        buf.write("\20\2\u009c\u009e\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\37\3\2\2\2\u009f\u00a0\t\2\2\2\u00a0!\3")
        buf.write("\2\2\2\u00a1\u00a4\7\b\2\2\u00a2\u00a5\5\62\32\2\u00a3")
        buf.write("\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a7\5\34\17\2\u00a7#\3\2")
        buf.write("\2\2\u00a8\u00ab\7\24\2\2\u00a9\u00ac\5\62\32\2\u00aa")
        buf.write("\u00ac\5\34\17\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2")
        buf.write("\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7\25\2\2\u00ae\u00af")
        buf.write("\5\34\17\2\u00af%\3\2\2\2\u00b0\u00b1\7)\2\2\u00b1\u00b2")
        buf.write("\5(\25\2\u00b2\u00b3\7*\2\2\u00b3\'\3\2\2\2\u00b4\u00b5")
        buf.write("\5\62\32\2\u00b5\u00b6\7+\2\2\u00b6\u00b7\5(\25\2\u00b7")
        buf.write("\u00ba\3\2\2\2\u00b8\u00ba\5\62\32\2\u00b9\u00b4\3\2\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba)\3\2\2\2\u00bb\u00bc\t\3")
        buf.write("\2\2\u00bc+\3\2\2\2\u00bd\u00be\t\4\2\2\u00be-\3\2\2\2")
        buf.write("\u00bf\u00c0\t\5\2\2\u00c0/\3\2\2\2\u00c1\u00c2\t\6\2")
        buf.write("\2\u00c2\61\3\2\2\2\u00c3\u00c4\5\64\33\2\u00c4\u00c5")
        buf.write("\7%\2\2\u00c5\u00c6\5\64\33\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c9\5\64\33\2\u00c8\u00c3\3\2\2\2\u00c8\u00c7\3\2\2")
        buf.write("\2\u00c9\63\3\2\2\2\u00ca\u00cb\5\66\34\2\u00cb\u00cc")
        buf.write("\5*\26\2\u00cc\u00cd\5\66\34\2\u00cd\u00d0\3\2\2\2\u00ce")
        buf.write("\u00d0\5\66\34\2\u00cf\u00ca\3\2\2\2\u00cf\u00ce\3\2\2")
        buf.write("\2\u00d0\65\3\2\2\2\u00d1\u00d2\b\34\1\2\u00d2\u00d3\5")
        buf.write("8\35\2\u00d3\u00da\3\2\2\2\u00d4\u00d5\f\4\2\2\u00d5\u00d6")
        buf.write("\5,\27\2\u00d6\u00d7\58\35\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d4\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\67\3\2\2\2\u00dc\u00da\3\2")
        buf.write("\2\2\u00dd\u00de\b\35\1\2\u00de\u00df\5:\36\2\u00df\u00e6")
        buf.write("\3\2\2\2\u00e0\u00e1\f\4\2\2\u00e1\u00e2\5.\30\2\u00e2")
        buf.write("\u00e3\5:\36\2\u00e3\u00e5\3\2\2\2\u00e4\u00e0\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e79\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\b\36\1\2\u00ea\u00eb\5<\37\2\u00eb\u00f2\3\2\2\2\u00ec")
        buf.write("\u00ed\f\4\2\2\u00ed\u00ee\5\60\31\2\u00ee\u00ef\5<\37")
        buf.write("\2\u00ef\u00f1\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write(";\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7\26\2\2\u00f6")
        buf.write("\u00f9\5<\37\2\u00f7\u00f9\5> \2\u00f8\u00f5\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9=\3\2\2\2\u00fa\u00fb\7\32\2\2\u00fb")
        buf.write("\u00fe\5> \2\u00fc\u00fe\5@!\2\u00fd\u00fa\3\2\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe?\3\2\2\2\u00ff\u0100\b!\1\2\u0100")
        buf.write("\u0101\5B\"\2\u0101\u0109\3\2\2\2\u0102\u0103\f\4\2\2")
        buf.write("\u0103\u0104\7)\2\2\u0104\u0105\5H%\2\u0105\u0106\7*\2")
        buf.write("\2\u0106\u0108\3\2\2\2\u0107\u0102\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("A\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u0113\7-\2\2\u010d")
        buf.write("\u0113\5D#\2\u010e\u010f\7\'\2\2\u010f\u0110\5\62\32\2")
        buf.write("\u0110\u0111\7(\2\2\u0111\u0113\3\2\2\2\u0112\u010c\3")
        buf.write("\2\2\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0113C")
        buf.write("\3\2\2\2\u0114\u0119\7/\2\2\u0115\u0119\7\60\2\2\u0116")
        buf.write("\u0119\7\61\2\2\u0117\u0119\5F$\2\u0118\u0114\3\2\2\2")
        buf.write("\u0118\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3")
        buf.write("\2\2\2\u0119E\3\2\2\2\u011a\u011b\7-\2\2\u011b\u011c\7")
        buf.write(")\2\2\u011c\u011d\5H%\2\u011d\u011e\7*\2\2\u011eG\3\2")
        buf.write("\2\2\u011f\u0120\5\62\32\2\u0120\u0121\7+\2\2\u0121\u0122")
        buf.write("\5H%\2\u0122\u0125\3\2\2\2\u0123\u0125\5\62\32\2\u0124")
        buf.write("\u011f\3\2\2\2\u0124\u0123\3\2\2\2\u0125I\3\2\2\2\33Q")
        buf.write("UYbfr}\u0089\u0090\u0098\u009d\u00a4\u00ab\u00b9\u00c8")
        buf.write("\u00cf\u00da\u00e6\u00f2\u00f8\u00fd\u0109\u0112\u0118")
        buf.write("\u0124")
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
    RULE_typdecl = 4
    RULE_implidecl = 5
    RULE_implivardecl = 6
    RULE_implidynadecl = 7
    RULE_funcdecl = 8
    RULE_funcdeclonly = 9
    RULE_parameterlist = 10
    RULE_parameterprime = 11
    RULE_param = 12
    RULE_newlinelist = 13
    RULE_nullablenewlinelist = 14
    RULE_typ = 15
    RULE_returnstate = 16
    RULE_blockstate = 17
    RULE_arraylit = 18
    RULE_elementlist = 19
    RULE_relational = 20
    RULE_logical = 21
    RULE_adding = 22
    RULE_multiplying = 23
    RULE_expr = 24
    RULE_expr1 = 25
    RULE_expr2 = 26
    RULE_expr3 = 27
    RULE_expr4 = 28
    RULE_expr5 = 29
    RULE_expr6 = 30
    RULE_expr7 = 31
    RULE_expr8 = 32
    RULE_literal = 33
    RULE_arraytype = 34
    RULE_exprlist = 35

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "typdecl", 
                   "implidecl", "implivardecl", "implidynadecl", "funcdecl", 
                   "funcdeclonly", "parameterlist", "parameterprime", "param", 
                   "newlinelist", "nullablenewlinelist", "typ", "returnstate", 
                   "blockstate", "arraylit", "elementlist", "relational", 
                   "logical", "adding", "multiplying", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "literal", "arraytype", "exprlist" ]

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
            self.state = 72
            self.decllist()
            self.state = 73
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.decl()
                self.state = 76
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
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

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def typdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypdeclContext,0)


        def implidecl(self):
            return self.getTypedRuleContext(ZCodeParser.ImplideclContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 85
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 86
                self.implidecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 89
            self.nullablenewlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypdecl" ):
                return visitor.visitTypdecl(self)
            else:
                return visitor.visitChildren(self)




    def typdecl(self):

        localctx = ZCodeParser.TypdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.typ()
            self.state = 92
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.state = 93
                self.match(ZCodeParser.ASSIGN)
                self.state = 94
                self.expr()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
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


    class ImplideclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implivardecl(self):
            return self.getTypedRuleContext(ZCodeParser.ImplivardeclContext,0)


        def implidynadecl(self):
            return self.getTypedRuleContext(ZCodeParser.ImplidynadeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implidecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplidecl" ):
                return visitor.visitImplidecl(self)
            else:
                return visitor.visitChildren(self)




    def implidecl(self):

        localctx = ZCodeParser.ImplideclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_implidecl)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.implivardecl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.implidynadecl()
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


    class ImplivardeclContext(ParserRuleContext):
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implivardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplivardecl" ):
                return visitor.visitImplivardecl(self)
            else:
                return visitor.visitChildren(self)




    def implivardecl(self):

        localctx = ZCodeParser.ImplivardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implivardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ZCodeParser.VAR)
            self.state = 103
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 104
            self.match(ZCodeParser.ASSIGN)
            self.state = 105
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplidynadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implidynadecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplidynadecl" ):
                return visitor.visitImplidynadecl(self)
            else:
                return visitor.visitChildren(self)




    def implidynadecl(self):

        localctx = ZCodeParser.ImplidynadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implidynadecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ZCodeParser.DYNAMIC)
            self.state = 108
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.state = 109
                self.match(ZCodeParser.ASSIGN)
                self.state = 110
                self.expr()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
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

        def nullablenewlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NullablenewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,i)


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
        self.enterRule(localctx, 16, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ZCodeParser.FUNC)
            self.state = 115
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 116
            self.match(ZCodeParser.LRB)
            self.state = 117
            self.parameterlist()
            self.state = 118
            self.match(ZCodeParser.RRB)
            self.state = 119
            self.nullablenewlinelist()
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 120
                self.returnstate()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 121
                self.blockstate()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.nullablenewlinelist()
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
        self.enterRule(localctx, 18, self.RULE_funcdeclonly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ZCodeParser.FUNC)
            self.state = 128
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 129
            self.match(ZCodeParser.LRB)
            self.state = 130
            self.parameterlist()
            self.state = 131
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
        self.enterRule(localctx, 20, self.RULE_parameterlist)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
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
        self.enterRule(localctx, 22, self.RULE_parameterprime)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.param()
                self.state = 138
                self.match(ZCodeParser.CM)
                self.state = 139
                self.parameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.typ()
            self.state = 145
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
        self.enterRule(localctx, 26, self.RULE_newlinelist)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(ZCodeParser.NEWLINE)
                self.state = 148
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullablenewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullablenewlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullablenewlinelist" ):
                return visitor.visitNullablenewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def nullablenewlinelist(self):

        localctx = ZCodeParser.NullablenewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nullablenewlinelist)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(ZCodeParser.NEWLINE)
                self.state = 153
                self.nullablenewlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 30, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
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

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstate" ):
                return visitor.visitReturnstate(self)
            else:
                return visitor.visitChildren(self)




    def returnstate(self):

        localctx = ZCodeParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.RETURN)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.IDENTIFIER, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT]:
                self.state = 160
                self.expr()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
            self.newlinelist()
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

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = ZCodeParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.BEGIN)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.IDENTIFIER, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT]:
                self.state = 167
                self.expr()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.state = 168
                self.newlinelist()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 171
            self.match(ZCodeParser.END)
            self.state = 172
            self.newlinelist()
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
        self.enterRule(localctx, 36, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ZCodeParser.LSB)
            self.state = 175
            self.elementlist()
            self.state = 176
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self.enterRule(localctx, 38, self.RULE_elementlist)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.expr()
                self.state = 179
                self.match(ZCodeParser.CM)
                self.state = 180
                self.elementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def CMPRSTR(self):
            return self.getToken(ZCodeParser.CMPRSTR, 0)

        def DIFF(self):
            return self.getToken(ZCodeParser.DIFF, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = ZCodeParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.DIFF) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.CMPRSTR))) != 0)):
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


    class LogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = ZCodeParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = ZCodeParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
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


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = ZCodeParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MOD))) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.expr1()
                self.state = 194
                self.match(ZCodeParser.CONCAT)
                self.state = 195
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def relational(self):
            return self.getTypedRuleContext(ZCodeParser.RelationalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr1)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.expr2(0)
                self.state = 201
                self.relational()
                self.state = 202
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def logical(self):
            return self.getTypedRuleContext(ZCodeParser.LogicalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    self.logical()
                    self.state = 212
                    self.expr3(0) 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def adding(self):
            return self.getTypedRuleContext(ZCodeParser.AddingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    self.adding()
                    self.state = 224
                    self.expr4(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    self.multiplying()
                    self.state = 236
                    self.expr5() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr5)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(ZCodeParser.NOT)
                self.state = 244
                self.expr5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.IDENTIFIER, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr6)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(ZCodeParser.MINUS)
                self.state = 249
                self.expr6()
                pass
            elif token in [ZCodeParser.LRB, ZCodeParser.IDENTIFIER, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.expr7(0)
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    self.match(ZCodeParser.LSB)
                    self.state = 258
                    self.exprlist()
                    self.state = 259
                    self.match(ZCodeParser.RSB) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr8)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(ZCodeParser.LRB)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(ZCodeParser.RRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def arraytype(self):
            return self.getTypedRuleContext(ZCodeParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_literal)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(ZCodeParser.BOOLLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.arraytype()
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


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = ZCodeParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 281
            self.match(ZCodeParser.LSB)
            self.state = 282
            self.exprlist()
            self.state = 283
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprlist)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.expr()
                self.state = 286
                self.match(ZCodeParser.CM)
                self.state = 287
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expr2_sempred
        self._predicates[27] = self.expr3_sempred
        self._predicates[28] = self.expr4_sempred
        self._predicates[31] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




