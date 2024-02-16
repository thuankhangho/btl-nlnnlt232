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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\7,\u0119")
        buf.write("\n,\f,\16,\u011c\13,\3,\5,\u011f\n,\3,\3,\3-\3-\5-\u0125")
        buf.write("\n-\3-\5-\u0128\n-\3.\6.\u012b\n.\r.\16.\u012c\3/\3/\7")
        buf.write("/\u0131\n/\f/\16/\u0134\13/\3\60\3\60\5\60\u0138\n\60")
        buf.write("\3\60\6\60\u013b\n\60\r\60\16\60\u013c\3\61\3\61\7\61")
        buf.write("\u0141\n\61\f\61\16\61\u0144\13\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\5\62\u0156\n\62\3\63\3\63\3\63\3\63\5\63\u015c\n")
        buf.write("\63\3\64\3\64\7\64\u0160\n\64\f\64\16\64\u0163\13\64\3")
        buf.write("\65\6\65\u0166\n\65\r\65\16\65\u0167\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\66\7\66\u0170\n\66\f\66\16\66\u0173\13\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\7\67\u017e")
        buf.write("\n\67\f\67\16\67\u0181\13\67\3\67\3\67\38\38\38\3\u011a")
        buf.write("\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[\2]\2_\2a/c\2e\2g\60i\61k\62m\63o\64\3")
        buf.write("\2\r\3\3\f\f\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$$^")
        buf.write("^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\13\17\17\"\"\t\2))")
        buf.write("^^ddhhppttvv\6\2\f\f\17\17$$^^\6\2\13\f\17\17$$^^\2\u0197")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2g\3\2")
        buf.write("\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3")
        buf.write("\2\2\2\5v\3\2\2\2\7|\3\2\2\2\t\u0083\3\2\2\2\13\u0088")
        buf.write("\3\2\2\2\r\u008f\3\2\2\2\17\u0096\3\2\2\2\21\u009a\3\2")
        buf.write("\2\2\23\u00a2\3\2\2\2\25\u00a7\3\2\2\2\27\u00ab\3\2\2")
        buf.write("\2\31\u00b1\3\2\2\2\33\u00b4\3\2\2\2\35\u00ba\3\2\2\2")
        buf.write("\37\u00c3\3\2\2\2!\u00c6\3\2\2\2#\u00cb\3\2\2\2%\u00d0")
        buf.write("\3\2\2\2\'\u00d6\3\2\2\2)\u00da\3\2\2\2+\u00de\3\2\2\2")
        buf.write("-\u00e2\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9")
        buf.write("\3\2\2\2\65\u00eb\3\2\2\2\67\u00ed\3\2\2\29\u00ef\3\2")
        buf.write("\2\2;\u00f1\3\2\2\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00fc\3\2\2\2E\u00fe\3\2\2\2G\u0101\3\2\2\2")
        buf.write("I\u0105\3\2\2\2K\u0108\3\2\2\2M\u010a\3\2\2\2O\u010c\3")
        buf.write("\2\2\2Q\u010e\3\2\2\2S\u0110\3\2\2\2U\u0112\3\2\2\2W\u0114")
        buf.write("\3\2\2\2Y\u0122\3\2\2\2[\u012a\3\2\2\2]\u012e\3\2\2\2")
        buf.write("_\u0135\3\2\2\2a\u013e\3\2\2\2c\u0155\3\2\2\2e\u015b\3")
        buf.write("\2\2\2g\u015d\3\2\2\2i\u0165\3\2\2\2k\u016b\3\2\2\2m\u0179")
        buf.write("\3\2\2\2o\u0184\3\2\2\2qr\7v\2\2rs\7t\2\2st\7w\2\2tu\7")
        buf.write("g\2\2u\4\3\2\2\2vw\7h\2\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z")
        buf.write("{\7g\2\2{\6\3\2\2\2|}\7p\2\2}~\7w\2\2~\177\7o\2\2\177")
        buf.write("\u0080\7d\2\2\u0080\u0081\7g\2\2\u0081\u0082\7t\2\2\u0082")
        buf.write("\b\3\2\2\2\u0083\u0084\7d\2\2\u0084\u0085\7q\2\2\u0085")
        buf.write("\u0086\7q\2\2\u0086\u0087\7n\2\2\u0087\n\3\2\2\2\u0088")
        buf.write("\u0089\7u\2\2\u0089\u008a\7v\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\u008c\7k\2\2\u008c\u008d\7p\2\2\u008d\u008e\7i\2\2\u008e")
        buf.write("\f\3\2\2\2\u008f\u0090\7t\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7w\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7p\2\2\u0095\16\3\2\2\2\u0096\u0097\7x\2\2\u0097")
        buf.write("\u0098\7c\2\2\u0098\u0099\7t\2\2\u0099\20\3\2\2\2\u009a")
        buf.write("\u009b\7f\2\2\u009b\u009c\7{\2\2\u009c\u009d\7p\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7o\2\2\u009f\u00a0\7k\2\2\u00a0")
        buf.write("\u00a1\7e\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6")
        buf.write("\24\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7q\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\26\3\2\2\2\u00ab\u00ac\7w\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7n\2\2\u00b0\30\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2")
        buf.write("\u00b3\7{\2\2\u00b3\32\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8")
        buf.write("\u00b9\7m\2\2\u00b9\34\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\36\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write("\u00c5\7h\2\2\u00c5 \3\2\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\"\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7n\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf$\3\2\2\2\u00d0")
        buf.write("\u00d1\7d\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7i\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5&\3\2\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7f\2\2\u00d9")
        buf.write("(\3\2\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7q\2\2\u00dc")
        buf.write("\u00dd\7v\2\2\u00dd*\3\2\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write("\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1,\3\2\2\2\u00e2")
        buf.write("\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4.\3\2\2\2\u00e5")
        buf.write("\u00e6\7-\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8")
        buf.write("\62\3\2\2\2\u00e9\u00ea\7,\2\2\u00ea\64\3\2\2\2\u00eb")
        buf.write("\u00ec\7\61\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\7\'\2\2\u00ee")
        buf.write("8\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0:\3\2\2\2\u00f1\u00f2")
        buf.write("\7>\2\2\u00f2\u00f3\7/\2\2\u00f3<\3\2\2\2\u00f4\u00f5")
        buf.write("\7#\2\2\u00f5\u00f6\7?\2\2\u00f6>\3\2\2\2\u00f7\u00f8")
        buf.write("\7>\2\2\u00f8@\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fbB\3\2\2\2\u00fc\u00fd\7@\2\2\u00fdD\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ff\u0100\7?\2\2\u0100F\3\2\2")
        buf.write("\2\u0101\u0102\7\60\2\2\u0102\u0103\7\60\2\2\u0103\u0104")
        buf.write("\7\60\2\2\u0104H\3\2\2\2\u0105\u0106\7?\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107J\3\2\2\2\u0108\u0109\7*\2\2\u0109L\3\2\2")
        buf.write("\2\u010a\u010b\7+\2\2\u010bN\3\2\2\2\u010c\u010d\7]\2")
        buf.write("\2\u010dP\3\2\2\2\u010e\u010f\7_\2\2\u010fR\3\2\2\2\u0110")
        buf.write("\u0111\7.\2\2\u0111T\3\2\2\2\u0112\u0113\7\f\2\2\u0113")
        buf.write("V\3\2\2\2\u0114\u0115\7%\2\2\u0115\u0116\7%\2\2\u0116")
        buf.write("\u011a\3\2\2\2\u0117\u0119\13\2\2\2\u0118\u0117\3\2\2")
        buf.write("\2\u0119\u011c\3\2\2\2\u011a\u011b\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u011f\t\2\2\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0121\b,\2\2\u0121X\3\2\2\2\u0122\u0124\5[.\2\u0123")
        buf.write("\u0125\5]/\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0127\3\2\2\2\u0126\u0128\5_\60\2\u0127\u0126\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128Z\3\2\2\2\u0129\u012b\t\3\2")
        buf.write("\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\\\3\2\2\2\u012e\u0132")
        buf.write("\7\60\2\2\u012f\u0131\t\3\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133^\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\t\4\2")
        buf.write("\2\u0136\u0138\t\5\2\2\u0137\u0136\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\t\3\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d`\3\2\2\2\u013e\u0142\7$\2\2")
        buf.write("\u013f\u0141\5e\63\2\u0140\u013f\3\2\2\2\u0141\u0144\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\7$\2\2\u0146")
        buf.write("\u0147\b\61\3\2\u0147b\3\2\2\2\u0148\u0149\7^\2\2\u0149")
        buf.write("\u0156\7d\2\2\u014a\u014b\7^\2\2\u014b\u0156\7h\2\2\u014c")
        buf.write("\u014d\7^\2\2\u014d\u0156\7t\2\2\u014e\u014f\7^\2\2\u014f")
        buf.write("\u0156\7p\2\2\u0150\u0151\7^\2\2\u0151\u0156\7v\2\2\u0152")
        buf.write("\u0156\7)\2\2\u0153\u0154\7^\2\2\u0154\u0156\7^\2\2\u0155")
        buf.write("\u0148\3\2\2\2\u0155\u014a\3\2\2\2\u0155\u014c\3\2\2\2")
        buf.write("\u0155\u014e\3\2\2\2\u0155\u0150\3\2\2\2\u0155\u0152\3")
        buf.write("\2\2\2\u0155\u0153\3\2\2\2\u0156d\3\2\2\2\u0157\u015c")
        buf.write("\n\6\2\2\u0158\u015c\5c\62\2\u0159\u015a\7)\2\2\u015a")
        buf.write("\u015c\7$\2\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015cf\3\2\2\2\u015d\u0161\t\7\2")
        buf.write("\2\u015e\u0160\t\b\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("h\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\t\t\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b")
        buf.write("\65\2\2\u016aj\3\2\2\2\u016b\u0171\7$\2\2\u016c\u016d")
        buf.write("\7^\2\2\u016d\u0170\t\n\2\2\u016e\u0170\n\13\2\2\u016f")
        buf.write("\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0176")
        buf.write("\n\n\2\2\u0176\u0177\3\2\2\2\u0177\u0178\b\66\4\2\u0178")
        buf.write("l\3\2\2\2\u0179\u017f\7$\2\2\u017a\u017b\7^\2\2\u017b")
        buf.write("\u017e\t\n\2\2\u017c\u017e\n\f\2\2\u017d\u017a\3\2\2\2")
        buf.write("\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0183\b\67\5\2\u0183n\3\2\2\2\u0184\u0185")
        buf.write("\13\2\2\2\u0185\u0186\b8\6\2\u0186p\3\2\2\2\24\2\u011a")
        buf.write("\u011e\u0124\u0127\u012c\u0132\u0137\u013c\u0142\u0155")
        buf.write("\u015b\u0161\u0167\u016f\u0171\u017d\u017f\7\b\2\2\3\61")
        buf.write("\2\3\66\3\3\67\4\38\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    PLUS = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE = 26
    MOD = 27
    EQUAL = 28
    ASSIGN = 29
    DIFF = 30
    LT = 31
    LE = 32
    GT = 33
    GE = 34
    CONCAT = 35
    CMPRSTR = 36
    LRB = 37
    RRB = 38
    LSB = 39
    RSB = 40
    CM = 41
    NEWLINE = 42
    LINECMT = 43
    NUMLIT = 44
    STRINGLIT = 45
    IDENTIFIER = 46
    WS = 47
    ILLEGAL_ESCAPE = 48
    UNCLOSE_STRING = 49
    ERROR_CHAR = 50

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
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MOD", "EQUAL", "ASSIGN", "DIFF", 
            "LT", "LE", "GT", "GE", "CONCAT", "CMPRSTR", "LRB", "RRB", "LSB", 
            "RSB", "CM", "NEWLINE", "LINECMT", "NUMLIT", "STRINGLIT", "IDENTIFIER", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", 
                  "EQUAL", "ASSIGN", "DIFF", "LT", "LE", "GT", "GE", "CONCAT", 
                  "CMPRSTR", "LRB", "RRB", "LSB", "RSB", "CM", "NEWLINE", 
                  "LINECMT", "NUMLIT", "INTEGER", "DECIMAL", "EXPONENT", 
                  "STRINGLIT", "ESCAPESEQ", "CHARSEQ", "IDENTIFIER", "WS", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[47] = self.STRINGLIT_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ERROR_CHAR_action 
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
     


