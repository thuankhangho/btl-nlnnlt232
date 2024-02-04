# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\5\2v\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3-\7-\u011f\n-\f-\16-\u0122\13-\3-\3-\3")
        buf.write(".\3.\5.\u0128\n.\3.\5.\u012b\n.\3/\6/\u012e\n/\r/\16/")
        buf.write("\u012f\3\60\3\60\7\60\u0134\n\60\f\60\16\60\u0137\13\60")
        buf.write("\3\61\3\61\5\61\u013b\n\61\3\61\6\61\u013e\n\61\r\61\16")
        buf.write("\61\u013f\3\62\3\62\7\62\u0144\n\62\f\62\16\62\u0147\13")
        buf.write("\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0159\n\63\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u015f\n\64\3\65\3\65\7\65\u0163\n\65")
        buf.write("\f\65\16\65\u0166\13\65\3\66\6\66\u0169\n\66\r\66\16\66")
        buf.write("\u016a\3\66\3\66\3\67\3\67\3\67\3\67\7\67\u0173\n\67\f")
        buf.write("\67\16\67\u0176\13\67\3\67\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\78\u0181\n8\f8\168\u0184\138\38\38\39\39\39\2\2:")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\2_\2a\2c\60e\2g\2i\61k\62m\63o\64q\65\3")
        buf.write("\2\r\4\2\f\f\16\17\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16")
        buf.write("\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\13\17\17\"\"")
        buf.write("\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\6\2\13\f\17\17$$")
        buf.write("^^\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2c\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\3u\3\2\2\2\5w\3\2\2\2\7|\3\2\2\2\t")
        buf.write("\u0082\3\2\2\2\13\u0089\3\2\2\2\r\u008e\3\2\2\2\17\u0095")
        buf.write("\3\2\2\2\21\u009c\3\2\2\2\23\u00a0\3\2\2\2\25\u00a8\3")
        buf.write("\2\2\2\27\u00ad\3\2\2\2\31\u00b1\3\2\2\2\33\u00b7\3\2")
        buf.write("\2\2\35\u00ba\3\2\2\2\37\u00c0\3\2\2\2!\u00c9\3\2\2\2")
        buf.write("#\u00cc\3\2\2\2%\u00d1\3\2\2\2\'\u00d6\3\2\2\2)\u00dc")
        buf.write("\3\2\2\2+\u00e0\3\2\2\2-\u00e4\3\2\2\2/\u00e8\3\2\2\2")
        buf.write("\61\u00eb\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef\3\2\2\2\67")
        buf.write("\u00f1\3\2\2\29\u00f3\3\2\2\2;\u00f5\3\2\2\2=\u00f7\3")
        buf.write("\2\2\2?\u00fa\3\2\2\2A\u00fd\3\2\2\2C\u00ff\3\2\2\2E\u0102")
        buf.write("\3\2\2\2G\u0104\3\2\2\2I\u0107\3\2\2\2K\u010b\3\2\2\2")
        buf.write("M\u010e\3\2\2\2O\u0110\3\2\2\2Q\u0112\3\2\2\2S\u0114\3")
        buf.write("\2\2\2U\u0116\3\2\2\2W\u0118\3\2\2\2Y\u011a\3\2\2\2[\u0125")
        buf.write("\3\2\2\2]\u012d\3\2\2\2_\u0131\3\2\2\2a\u0138\3\2\2\2")
        buf.write("c\u0141\3\2\2\2e\u0158\3\2\2\2g\u015e\3\2\2\2i\u0160\3")
        buf.write("\2\2\2k\u0168\3\2\2\2m\u016e\3\2\2\2o\u017c\3\2\2\2q\u0187")
        buf.write("\3\2\2\2sv\5\5\3\2tv\5\7\4\2us\3\2\2\2ut\3\2\2\2v\4\3")
        buf.write("\2\2\2wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7g\2\2{\6\3\2\2\2")
        buf.write("|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080")
        buf.write("\u0081\7g\2\2\u0081\b\3\2\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\u0084\7w\2\2\u0084\u0085\7o\2\2\u0085\u0086\7d\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088\n\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7n\2\2\u008d\f\3\2\2\2\u008e\u008f\7u\2\2\u008f")
        buf.write("\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092\7k\2\2\u0092")
        buf.write("\u0093\7p\2\2\u0093\u0094\7i\2\2\u0094\16\3\2\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\20\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7f\2\2\u00a1")
        buf.write("\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7e\2\2\u00a7")
        buf.write("\24\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7w\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\26\3\2\2\2\u00ad")
        buf.write("\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\30\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7n\2\2\u00b6")
        buf.write("\32\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7{\2\2\u00b9")
        buf.write("\34\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7t\2\2\u00bc")
        buf.write("\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7m\2\2\u00bf")
        buf.write("\36\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7q\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7k\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write(" \3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write("\"\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce")
        buf.write("\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0$\3\2\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5&\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db(\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df*\3\2\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7v\2\2\u00e3")
        buf.write(",\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7f\2\2\u00e7.\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\60\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec")
        buf.write("\62\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee\64\3\2\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\66\3\2\2\2\u00f1\u00f2\7\61\2\2\u00f2")
        buf.write("8\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f4:\3\2\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6<\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9")
        buf.write("\7/\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7#\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7>\2\2\u00feB\3\2\2")
        buf.write("\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101D\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103F\3\2\2\2\u0104\u0105\7@\2")
        buf.write("\2\u0105\u0106\7?\2\2\u0106H\3\2\2\2\u0107\u0108\7\60")
        buf.write("\2\2\u0108\u0109\7\60\2\2\u0109\u010a\7\60\2\2\u010aJ")
        buf.write("\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d\7?\2\2\u010dL")
        buf.write("\3\2\2\2\u010e\u010f\7*\2\2\u010fN\3\2\2\2\u0110\u0111")
        buf.write("\7+\2\2\u0111P\3\2\2\2\u0112\u0113\7]\2\2\u0113R\3\2\2")
        buf.write("\2\u0114\u0115\7_\2\2\u0115T\3\2\2\2\u0116\u0117\7.\2")
        buf.write("\2\u0117V\3\2\2\2\u0118\u0119\7\f\2\2\u0119X\3\2\2\2\u011a")
        buf.write("\u011b\7%\2\2\u011b\u011c\7%\2\2\u011c\u0120\3\2\2\2\u011d")
        buf.write("\u011f\n\2\2\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\b-\2\2\u0124Z\3")
        buf.write("\2\2\2\u0125\u0127\5]/\2\u0126\u0128\5_\60\2\u0127\u0126")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u012b\5a\61\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\\\3\2\2\2\u012c\u012e\t\3\2\2\u012d\u012c\3\2\2")
        buf.write("\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130^\3\2\2\2\u0131\u0135\7\60\2\2\u0132\u0134")
        buf.write("\t\3\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136`\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u013a\t\4\2\2\u0139\u013b\t\5\2\2")
        buf.write("\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3")
        buf.write("\2\2\2\u013c\u013e\t\3\2\2\u013d\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("b\3\2\2\2\u0141\u0145\7$\2\2\u0142\u0144\5g\64\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0148\u0149\7$\2\2\u0149\u014a\b\62\3\2\u014ad")
        buf.write("\3\2\2\2\u014b\u014c\7^\2\2\u014c\u0159\7d\2\2\u014d\u014e")
        buf.write("\7^\2\2\u014e\u0159\7h\2\2\u014f\u0150\7^\2\2\u0150\u0159")
        buf.write("\7t\2\2\u0151\u0152\7^\2\2\u0152\u0159\7p\2\2\u0153\u0154")
        buf.write("\7^\2\2\u0154\u0159\7v\2\2\u0155\u0159\7)\2\2\u0156\u0157")
        buf.write("\7^\2\2\u0157\u0159\7^\2\2\u0158\u014b\3\2\2\2\u0158\u014d")
        buf.write("\3\2\2\2\u0158\u014f\3\2\2\2\u0158\u0151\3\2\2\2\u0158")
        buf.write("\u0153\3\2\2\2\u0158\u0155\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0159f\3\2\2\2\u015a\u015f\n\6\2\2\u015b\u015f\5e\63")
        buf.write("\2\u015c\u015d\7)\2\2\u015d\u015f\7$\2\2\u015e\u015a\3")
        buf.write("\2\2\2\u015e\u015b\3\2\2\2\u015e\u015c\3\2\2\2\u015fh")
        buf.write("\3\2\2\2\u0160\u0164\t\7\2\2\u0161\u0163\t\b\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165j\3\2\2\2\u0166\u0164\3\2\2")
        buf.write("\2\u0167\u0169\t\t\2\2\u0168\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\b\66\2\2\u016dl\3\2\2\2\u016e")
        buf.write("\u0174\7$\2\2\u016f\u0170\7^\2\2\u0170\u0173\t\n\2\2\u0171")
        buf.write("\u0173\n\13\2\2\u0172\u016f\3\2\2\2\u0172\u0171\3\2\2")
        buf.write("\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0178\7^\2\2\u0178\u0179\n\n\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017b\b\67\4\2\u017bn\3\2\2\2\u017c\u0182\7$\2")
        buf.write("\2\u017d\u017e\7^\2\2\u017e\u0181\t\n\2\2\u017f\u0181")
        buf.write("\n\f\2\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0185\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\b")
        buf.write("8\5\2\u0186p\3\2\2\2\u0187\u0188\13\2\2\2\u0188\u0189")
        buf.write("\b9\6\2\u0189r\3\2\2\2\24\2u\u0120\u0127\u012a\u012f\u0135")
        buf.write("\u013a\u013f\u0145\u0158\u015e\u0164\u016a\u0172\u0174")
        buf.write("\u0180\u0182\7\b\2\2\3\62\2\3\67\3\38\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    NOT = 21
    AND = 22
    OR = 23
    PLUS = 24
    MINUS = 25
    MULTIPLY = 26
    DIVIDE = 27
    MOD = 28
    EQUAL = 29
    ASSIGN = 30
    DIFF = 31
    LT = 32
    LE = 33
    GT = 34
    GE = 35
    CONCAT = 36
    CMPRSTR = 37
    LRB = 38
    RRB = 39
    LSB = 40
    RSB = 41
    CM = 42
    NEWLINE = 43
    LINECMT = 44
    NUMLIT = 45
    STRINGLIT = 46
    IDENTIFIER = 47
    WS = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MOD", "EQUAL", "ASSIGN", "DIFF", 
            "LT", "LE", "GT", "GE", "CONCAT", "CMPRSTR", "LRB", "RRB", "LSB", 
            "RSB", "CM", "NEWLINE", "LINECMT", "NUMLIT", "STRINGLIT", "IDENTIFIER", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "BOOLLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MOD", "EQUAL", "ASSIGN", "DIFF", "LT", "LE", "GT", "GE", 
                  "CONCAT", "CMPRSTR", "LRB", "RRB", "LSB", "RSB", "CM", 
                  "NEWLINE", "LINECMT", "NUMLIT", "INTEGER", "DECIMAL", 
                  "EXPONENT", "STRINGLIT", "ESCAPESEQ", "CHARSEQ", "IDENTIFIER", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRINGLIT_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


