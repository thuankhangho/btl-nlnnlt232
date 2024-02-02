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
        buf.write("\u018d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write(",\3,\3-\3-\3-\3-\7-\u011f\n-\f-\16-\u0122\13-\3-\5-\u0125")
        buf.write("\n-\3-\3-\3.\3.\5.\u012b\n.\3.\5.\u012e\n.\3/\6/\u0131")
        buf.write("\n/\r/\16/\u0132\3\60\3\60\7\60\u0137\n\60\f\60\16\60")
        buf.write("\u013a\13\60\3\61\3\61\5\61\u013e\n\61\3\61\6\61\u0141")
        buf.write("\n\61\r\61\16\61\u0142\3\62\3\62\7\62\u0147\n\62\f\62")
        buf.write("\16\62\u014a\13\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u015c")
        buf.write("\n\63\3\64\3\64\3\64\3\64\5\64\u0162\n\64\3\65\3\65\7")
        buf.write("\65\u0166\n\65\f\65\16\65\u0169\13\65\3\66\6\66\u016c")
        buf.write("\n\66\r\66\16\66\u016d\3\66\3\66\3\67\3\67\3\67\3\67\7")
        buf.write("\67\u0176\n\67\f\67\16\67\u0179\13\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\38\38\38\38\78\u0184\n8\f8\168\u0187\138\38\3")
        buf.write("8\39\39\39\3\u0120\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\60e\2g\2")
        buf.write("i\61k\62m\63o\64q\65\3\2\r\3\3\f\f\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\13\17\17\"\"\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\6\2")
        buf.write("\13\f\17\17$$^^\2\u019e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2c\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3u\3\2\2\2\5w\3\2\2\2\7")
        buf.write("|\3\2\2\2\t\u0082\3\2\2\2\13\u0089\3\2\2\2\r\u008e\3\2")
        buf.write("\2\2\17\u0095\3\2\2\2\21\u009c\3\2\2\2\23\u00a0\3\2\2")
        buf.write("\2\25\u00a8\3\2\2\2\27\u00ad\3\2\2\2\31\u00b1\3\2\2\2")
        buf.write("\33\u00b7\3\2\2\2\35\u00ba\3\2\2\2\37\u00c0\3\2\2\2!\u00c9")
        buf.write("\3\2\2\2#\u00cc\3\2\2\2%\u00d1\3\2\2\2\'\u00d6\3\2\2\2")
        buf.write(")\u00dc\3\2\2\2+\u00e0\3\2\2\2-\u00e4\3\2\2\2/\u00e8\3")
        buf.write("\2\2\2\61\u00eb\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef\3\2")
        buf.write("\2\2\67\u00f1\3\2\2\29\u00f3\3\2\2\2;\u00f5\3\2\2\2=\u00f7")
        buf.write("\3\2\2\2?\u00fa\3\2\2\2A\u00fd\3\2\2\2C\u00ff\3\2\2\2")
        buf.write("E\u0102\3\2\2\2G\u0104\3\2\2\2I\u0107\3\2\2\2K\u010b\3")
        buf.write("\2\2\2M\u010e\3\2\2\2O\u0110\3\2\2\2Q\u0112\3\2\2\2S\u0114")
        buf.write("\3\2\2\2U\u0116\3\2\2\2W\u0118\3\2\2\2Y\u011a\3\2\2\2")
        buf.write("[\u0128\3\2\2\2]\u0130\3\2\2\2_\u0134\3\2\2\2a\u013b\3")
        buf.write("\2\2\2c\u0144\3\2\2\2e\u015b\3\2\2\2g\u0161\3\2\2\2i\u0163")
        buf.write("\3\2\2\2k\u016b\3\2\2\2m\u0171\3\2\2\2o\u017f\3\2\2\2")
        buf.write("q\u018a\3\2\2\2sv\5\5\3\2tv\5\7\4\2us\3\2\2\2ut\3\2\2")
        buf.write("\2v\4\3\2\2\2wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7g\2\2{\6\3")
        buf.write("\2\2\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2")
        buf.write("\u0080\u0081\7g\2\2\u0081\b\3\2\2\2\u0082\u0083\7p\2\2")
        buf.write("\u0083\u0084\7w\2\2\u0084\u0085\7o\2\2\u0085\u0086\7d")
        buf.write("\2\2\u0086\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088\n\3\2")
        buf.write("\2\2\u0089\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\u008d\7n\2\2\u008d\f\3\2\2\2\u008e\u008f")
        buf.write("\7u\2\2\u008f\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092")
        buf.write("\7k\2\2\u0092\u0093\7p\2\2\u0093\u0094\7i\2\2\u0094\16")
        buf.write("\3\2\2\2\u0095\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7v\2\2\u0098\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7p\2\2\u009b\20\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7t\2\2\u009f\22\3\2\2\2\u00a0\u00a1")
        buf.write("\7f\2\2\u00a1\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7e\2\2\u00a7\24\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\26")
        buf.write("\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\30\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\32\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9")
        buf.write("\7{\2\2\u00b9\34\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7m\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7h\2\2\u00cb\"\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0$\3")
        buf.write("\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7h\2\2\u00d5&\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db(\3\2\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df*\3")
        buf.write("\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3,\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7f\2\2\u00e7.\3\2\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\60\3\2\2\2\u00eb\u00ec")
        buf.write("\7-\2\2\u00ec\62\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee\64\3")
        buf.write("\2\2\2\u00ef\u00f0\7,\2\2\u00f0\66\3\2\2\2\u00f1\u00f2")
        buf.write("\7\61\2\2\u00f28\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f4:\3")
        buf.write("\2\2\2\u00f5\u00f6\7?\2\2\u00f6<\3\2\2\2\u00f7\u00f8\7")
        buf.write(">\2\2\u00f8\u00f9\7/\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7")
        buf.write("#\2\2\u00fb\u00fc\7?\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7")
        buf.write(">\2\2\u00feB\3\2\2\2\u00ff\u0100\7>\2\2\u0100\u0101\7")
        buf.write("?\2\2\u0101D\3\2\2\2\u0102\u0103\7@\2\2\u0103F\3\2\2\2")
        buf.write("\u0104\u0105\7@\2\2\u0105\u0106\7?\2\2\u0106H\3\2\2\2")
        buf.write("\u0107\u0108\7\60\2\2\u0108\u0109\7\60\2\2\u0109\u010a")
        buf.write("\7\60\2\2\u010aJ\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010dL\3\2\2\2\u010e\u010f\7*\2\2\u010fN\3\2\2")
        buf.write("\2\u0110\u0111\7+\2\2\u0111P\3\2\2\2\u0112\u0113\7]\2")
        buf.write("\2\u0113R\3\2\2\2\u0114\u0115\7_\2\2\u0115T\3\2\2\2\u0116")
        buf.write("\u0117\7.\2\2\u0117V\3\2\2\2\u0118\u0119\7\f\2\2\u0119")
        buf.write("X\3\2\2\2\u011a\u011b\7%\2\2\u011b\u011c\7%\2\2\u011c")
        buf.write("\u0120\3\2\2\2\u011d\u011f\13\2\2\2\u011e\u011d\3\2\2")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u0121\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0125\t\2\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u0127\b-\2\2\u0127Z\3\2\2\2\u0128\u012a\5]/\2\u0129")
        buf.write("\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012d\3\2\2\2\u012c\u012e\5a\61\2\u012d\u012c\3")
        buf.write("\2\2\2\u012d\u012e\3\2\2\2\u012e\\\3\2\2\2\u012f\u0131")
        buf.write("\t\3\2\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133^\3\2\2\2\u0134")
        buf.write("\u0138\7\60\2\2\u0135\u0137\t\3\2\2\u0136\u0135\3\2\2")
        buf.write("\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139`\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u013d")
        buf.write("\t\4\2\2\u013c\u013e\t\5\2\2\u013d\u013c\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141\t\3\2\2")
        buf.write("\u0140\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143b\3\2\2\2\u0144\u0148")
        buf.write("\7$\2\2\u0145\u0147\5g\64\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\7")
        buf.write("$\2\2\u014c\u014d\b\62\3\2\u014dd\3\2\2\2\u014e\u014f")
        buf.write("\7^\2\2\u014f\u015c\7d\2\2\u0150\u0151\7^\2\2\u0151\u015c")
        buf.write("\7h\2\2\u0152\u0153\7^\2\2\u0153\u015c\7t\2\2\u0154\u0155")
        buf.write("\7^\2\2\u0155\u015c\7p\2\2\u0156\u0157\7^\2\2\u0157\u015c")
        buf.write("\7v\2\2\u0158\u015c\7)\2\2\u0159\u015a\7^\2\2\u015a\u015c")
        buf.write("\7^\2\2\u015b\u014e\3\2\2\2\u015b\u0150\3\2\2\2\u015b")
        buf.write("\u0152\3\2\2\2\u015b\u0154\3\2\2\2\u015b\u0156\3\2\2\2")
        buf.write("\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015cf\3\2\2")
        buf.write("\2\u015d\u0162\n\6\2\2\u015e\u0162\5e\63\2\u015f\u0160")
        buf.write("\7)\2\2\u0160\u0162\7$\2\2\u0161\u015d\3\2\2\2\u0161\u015e")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0162h\3\2\2\2\u0163\u0167")
        buf.write("\t\7\2\2\u0164\u0166\t\b\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168j\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\t\t\2")
        buf.write("\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\b\66\2\2\u0170l\3\2\2\2\u0171\u0177\7$\2\2\u0172")
        buf.write("\u0173\7^\2\2\u0173\u0176\t\n\2\2\u0174\u0176\n\13\2\2")
        buf.write("\u0175\u0172\3\2\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\7^\2\2\u017b")
        buf.write("\u017c\n\n\2\2\u017c\u017d\3\2\2\2\u017d\u017e\b\67\4")
        buf.write("\2\u017en\3\2\2\2\u017f\u0185\7$\2\2\u0180\u0181\7^\2")
        buf.write("\2\u0181\u0184\t\n\2\2\u0182\u0184\n\f\2\2\u0183\u0180")
        buf.write("\3\2\2\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0188\u0189\b8\5\2\u0189p\3\2\2\2")
        buf.write("\u018a\u018b\13\2\2\2\u018b\u018c\b9\6\2\u018cr\3\2\2")
        buf.write("\2\25\2u\u0120\u0124\u012a\u012d\u0132\u0138\u013d\u0142")
        buf.write("\u0148\u015b\u0161\u0167\u016d\u0175\u0177\u0183\u0185")
        buf.write("\7\b\2\2\3\62\2\3\67\3\38\4\39\5")
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
     


