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
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3")
        buf.write(",\7,\u011b\n,\f,\16,\u011e\13,\3,\5,\u0121\n,\3,\3,\3")
        buf.write("-\3-\5-\u0127\n-\3-\5-\u012a\n-\3.\6.\u012d\n.\r.\16.")
        buf.write("\u012e\3/\3/\7/\u0133\n/\f/\16/\u0136\13/\3\60\3\60\5")
        buf.write("\60\u013a\n\60\3\60\6\60\u013d\n\60\r\60\16\60\u013e\3")
        buf.write("\61\3\61\5\61\u0143\n\61\3\62\3\62\7\62\u0147\n\62\f\62")
        buf.write("\16\62\u014a\13\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u015c")
        buf.write("\n\63\3\64\3\64\3\64\3\64\5\64\u0162\n\64\3\65\3\65\7")
        buf.write("\65\u0166\n\65\f\65\16\65\u0169\13\65\3\66\6\66\u016c")
        buf.write("\n\66\r\66\16\66\u016d\3\66\3\66\3\67\3\67\3\67\3\67\7")
        buf.write("\67\u0176\n\67\f\67\16\67\u0179\13\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\38\38\38\38\38\38\78\u0186\n8\f8\168\u0189\13")
        buf.write("8\38\38\39\39\39\3\u011c\2:\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\60e\2")
        buf.write("g\2i\61k\62m\63o\64q\65\3\2\r\3\3\f\f\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\13\17\17\"\"\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^")
        buf.write("^\6\2\13\f\17\17$$^^\2\u01a1\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5x\3\2\2\2")
        buf.write("\7~\3\2\2\2\t\u0085\3\2\2\2\13\u008a\3\2\2\2\r\u0091\3")
        buf.write("\2\2\2\17\u0098\3\2\2\2\21\u009c\3\2\2\2\23\u00a4\3\2")
        buf.write("\2\2\25\u00a9\3\2\2\2\27\u00ad\3\2\2\2\31\u00b3\3\2\2")
        buf.write("\2\33\u00b6\3\2\2\2\35\u00bc\3\2\2\2\37\u00c5\3\2\2\2")
        buf.write("!\u00c8\3\2\2\2#\u00cd\3\2\2\2%\u00d2\3\2\2\2\'\u00d8")
        buf.write("\3\2\2\2)\u00dc\3\2\2\2+\u00e0\3\2\2\2-\u00e4\3\2\2\2")
        buf.write("/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb\3\2\2\2\65\u00ed")
        buf.write("\3\2\2\2\67\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f3\3\2\2")
        buf.write("\2=\u00f6\3\2\2\2?\u00f9\3\2\2\2A\u00fb\3\2\2\2C\u00fe")
        buf.write("\3\2\2\2E\u0100\3\2\2\2G\u0103\3\2\2\2I\u0107\3\2\2\2")
        buf.write("K\u010a\3\2\2\2M\u010c\3\2\2\2O\u010e\3\2\2\2Q\u0110\3")
        buf.write("\2\2\2S\u0112\3\2\2\2U\u0114\3\2\2\2W\u0116\3\2\2\2Y\u0124")
        buf.write("\3\2\2\2[\u012c\3\2\2\2]\u0130\3\2\2\2_\u0137\3\2\2\2")
        buf.write("a\u0142\3\2\2\2c\u0144\3\2\2\2e\u015b\3\2\2\2g\u0161\3")
        buf.write("\2\2\2i\u0163\3\2\2\2k\u016b\3\2\2\2m\u0171\3\2\2\2o\u017f")
        buf.write("\3\2\2\2q\u018c\3\2\2\2st\7v\2\2tu\7t\2\2uv\7w\2\2vw\7")
        buf.write("g\2\2w\4\3\2\2\2xy\7h\2\2yz\7c\2\2z{\7n\2\2{|\7u\2\2|")
        buf.write("}\7g\2\2}\6\3\2\2\2~\177\7p\2\2\177\u0080\7w\2\2\u0080")
        buf.write("\u0081\7o\2\2\u0081\u0082\7d\2\2\u0082\u0083\7g\2\2\u0083")
        buf.write("\u0084\7t\2\2\u0084\b\3\2\2\2\u0085\u0086\7d\2\2\u0086")
        buf.write("\u0087\7q\2\2\u0087\u0088\7q\2\2\u0088\u0089\7n\2\2\u0089")
        buf.write("\n\3\2\2\2\u008a\u008b\7u\2\2\u008b\u008c\7v\2\2\u008c")
        buf.write("\u008d\7t\2\2\u008d\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f")
        buf.write("\u0090\7i\2\2\u0090\f\3\2\2\2\u0091\u0092\7t\2\2\u0092")
        buf.write("\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095\7w\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\u0097\7p\2\2\u0097\16\3\2\2\2\u0098")
        buf.write("\u0099\7x\2\2\u0099\u009a\7c\2\2\u009a\u009b\7t\2\2\u009b")
        buf.write("\20\3\2\2\2\u009c\u009d\7f\2\2\u009d\u009e\7{\2\2\u009e")
        buf.write("\u009f\7p\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7o\2\2\u00a1")
        buf.write("\u00a2\7k\2\2\u00a2\u00a3\7e\2\2\u00a3\22\3\2\2\2\u00a4")
        buf.write("\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7")
        buf.write("\u00a8\7e\2\2\u00a8\24\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa")
        buf.write("\u00ab\7q\2\2\u00ab\u00ac\7t\2\2\u00ac\26\3\2\2\2\u00ad")
        buf.write("\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write("\u00b1\7k\2\2\u00b1\u00b2\7n\2\2\u00b2\30\3\2\2\2\u00b3")
        buf.write("\u00b4\7d\2\2\u00b4\u00b5\7{\2\2\u00b5\32\3\2\2\2\u00b6")
        buf.write("\u00b7\7d\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9")
        buf.write("\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb\34\3\2\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2")
        buf.write("\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4\36\3\2\2\2\u00c5")
        buf.write("\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7 \3\2\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb")
        buf.write("\u00cc\7g\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce")
        buf.write("\u00cf\7n\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7h\2\2\u00d1")
        buf.write("$\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write("\u00d5\7i\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("&\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7p\2\2\u00da")
        buf.write("\u00db\7f\2\2\u00db(\3\2\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df*\3\2\2\2\u00e0")
        buf.write("\u00e1\7c\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7f\2\2\u00e3")
        buf.write(",\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write(".\3\2\2\2\u00e7\u00e8\7-\2\2\u00e8\60\3\2\2\2\u00e9\u00ea")
        buf.write("\7/\2\2\u00ea\62\3\2\2\2\u00eb\u00ec\7,\2\2\u00ec\64\3")
        buf.write("\2\2\2\u00ed\u00ee\7\61\2\2\u00ee\66\3\2\2\2\u00ef\u00f0")
        buf.write("\7\'\2\2\u00f08\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2:\3\2")
        buf.write("\2\2\u00f3\u00f4\7>\2\2\u00f4\u00f5\7/\2\2\u00f5<\3\2")
        buf.write("\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8\7?\2\2\u00f8>\3\2")
        buf.write("\2\2\u00f9\u00fa\7>\2\2\u00fa@\3\2\2\2\u00fb\u00fc\7>")
        buf.write("\2\2\u00fc\u00fd\7?\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7@")
        buf.write("\2\2\u00ffD\3\2\2\2\u0100\u0101\7@\2\2\u0101\u0102\7?")
        buf.write("\2\2\u0102F\3\2\2\2\u0103\u0104\7\60\2\2\u0104\u0105\7")
        buf.write("\60\2\2\u0105\u0106\7\60\2\2\u0106H\3\2\2\2\u0107\u0108")
        buf.write("\7?\2\2\u0108\u0109\7?\2\2\u0109J\3\2\2\2\u010a\u010b")
        buf.write("\7*\2\2\u010bL\3\2\2\2\u010c\u010d\7+\2\2\u010dN\3\2\2")
        buf.write("\2\u010e\u010f\7]\2\2\u010fP\3\2\2\2\u0110\u0111\7_\2")
        buf.write("\2\u0111R\3\2\2\2\u0112\u0113\7.\2\2\u0113T\3\2\2\2\u0114")
        buf.write("\u0115\7\f\2\2\u0115V\3\2\2\2\u0116\u0117\7%\2\2\u0117")
        buf.write("\u0118\7%\2\2\u0118\u011c\3\2\2\2\u0119\u011b\13\2\2\2")
        buf.write("\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011c\u011a\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0121\t\2\2\2\u0120\u011f\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\b,\2\2\u0123X\3\2\2\2\u0124")
        buf.write("\u0126\5[.\2\u0125\u0127\5]/\2\u0126\u0125\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u012a\5_\60\2")
        buf.write("\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012aZ\3\2\2")
        buf.write("\2\u012b\u012d\t\3\2\2\u012c\u012b\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\\\3\2\2\2\u0130\u0134\7\60\2\2\u0131\u0133\t\3\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135^\3\2\2\2\u0136\u0134\3\2\2")
        buf.write("\2\u0137\u0139\t\4\2\2\u0138\u013a\t\5\2\2\u0139\u0138")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u013d\t\3\2\2\u013c\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f`\3\2\2")
        buf.write("\2\u0140\u0143\5\3\2\2\u0141\u0143\5\5\3\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143b\3\2\2\2\u0144\u0148")
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
        buf.write("\2\u017en\3\2\2\2\u017f\u0187\7$\2\2\u0180\u0181\7)\2")
        buf.write("\2\u0181\u0186\7$\2\2\u0182\u0183\7^\2\2\u0183\u0186\t")
        buf.write("\n\2\2\u0184\u0186\n\f\2\2\u0185\u0180\3\2\2\2\u0185\u0182")
        buf.write("\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u018a\u018b\b8\5\2\u018bp\3\2\2\2")
        buf.write("\u018c\u018d\13\2\2\2\u018d\u018e\b9\6\2\u018er\3\2\2")
        buf.write("\2\25\2\u011c\u0120\u0126\u0129\u012e\u0134\u0139\u013e")
        buf.write("\u0142\u0148\u015b\u0161\u0167\u016d\u0175\u0177\u0185")
        buf.write("\u0187\7\b\2\2\3\62\2\3\67\3\38\4\39\5")
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
    BOOLLIT = 45
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
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MOD", "EQUAL", "ASSIGN", "DIFF", 
            "LT", "LE", "GT", "GE", "CONCAT", "CMPRSTR", "LRB", "RRB", "LSB", 
            "RSB", "CM", "NEWLINE", "LINECMT", "NUMLIT", "BOOLLIT", "STRINGLIT", 
            "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", 
                  "EQUAL", "ASSIGN", "DIFF", "LT", "LE", "GT", "GE", "CONCAT", 
                  "CMPRSTR", "LRB", "RRB", "LSB", "RSB", "CM", "NEWLINE", 
                  "LINECMT", "NUMLIT", "INTEGER", "DECIMAL", "EXPONENT", 
                  "BOOLLIT", "STRINGLIT", "ESCAPESEQ", "CHARSEQ", "IDENTIFIER", 
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
     


