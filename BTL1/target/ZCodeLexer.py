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
        buf.write("\u0180\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\7")
        buf.write("-\u0119\n-\f-\16-\u011c\13-\3.\3.\3.\3.\3.\3.\7.\u0124")
        buf.write("\n.\f.\16.\u0127\13.\3.\3.\3.\3/\3/\5/\u012e\n/\3/\5/")
        buf.write("\u0131\n/\3\60\6\60\u0134\n\60\r\60\16\60\u0135\3\61\3")
        buf.write("\61\7\61\u013a\n\61\f\61\16\61\u013d\13\61\3\62\3\62\5")
        buf.write("\62\u0141\n\62\3\62\6\62\u0144\n\62\r\62\16\62\u0145\3")
        buf.write("\63\3\63\3\63\3\63\7\63\u014c\n\63\f\63\16\63\u014f\13")
        buf.write("\63\3\63\3\63\3\64\6\64\u0154\n\64\r\64\16\64\u0155\3")
        buf.write("\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\7\66\u0163\n\66\f\66\16\66\u0166\13\66\3\66\3\66\3\66")
        buf.write("\5\66\u016b\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u0175\n\67\f\67\16\67\u0178\13\67\3\67\3\67\3")
        buf.write("\67\5\67\u017d\n\67\3\67\3\67\2\28\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\2a\2c\2e\61g\62i\63k\64m\65\3\2\r\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\4\2\f\f\16\17\5\2\n\13\16\17\"\"\3\3\f")
        buf.write("\f\3\2\16\17\2\u0191\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\3q\3\2\2\2\5s\3\2\2\2\7x\3\2")
        buf.write("\2\2\t~\3\2\2\2\13\u0085\3\2\2\2\r\u008a\3\2\2\2\17\u0091")
        buf.write("\3\2\2\2\21\u0098\3\2\2\2\23\u009c\3\2\2\2\25\u00a4\3")
        buf.write("\2\2\2\27\u00a9\3\2\2\2\31\u00ad\3\2\2\2\33\u00b3\3\2")
        buf.write("\2\2\35\u00b6\3\2\2\2\37\u00bc\3\2\2\2!\u00c5\3\2\2\2")
        buf.write("#\u00c8\3\2\2\2%\u00cd\3\2\2\2\'\u00d2\3\2\2\2)\u00d8")
        buf.write("\3\2\2\2+\u00dc\3\2\2\2-\u00e0\3\2\2\2/\u00e4\3\2\2\2")
        buf.write("\61\u00e7\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67")
        buf.write("\u00ed\3\2\2\29\u00ef\3\2\2\2;\u00f1\3\2\2\2=\u00f3\3")
        buf.write("\2\2\2?\u00f6\3\2\2\2A\u00f9\3\2\2\2C\u00fb\3\2\2\2E\u00fe")
        buf.write("\3\2\2\2G\u0100\3\2\2\2I\u0103\3\2\2\2K\u0107\3\2\2\2")
        buf.write("M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e\3\2\2\2S\u0110\3")
        buf.write("\2\2\2U\u0112\3\2\2\2W\u0114\3\2\2\2Y\u0116\3\2\2\2[\u011d")
        buf.write("\3\2\2\2]\u012b\3\2\2\2_\u0133\3\2\2\2a\u0137\3\2\2\2")
        buf.write("c\u013e\3\2\2\2e\u0147\3\2\2\2g\u0153\3\2\2\2i\u0159\3")
        buf.write("\2\2\2k\u015c\3\2\2\2m\u016e\3\2\2\2or\5\5\3\2pr\5\7\4")
        buf.write("\2qo\3\2\2\2qp\3\2\2\2r\4\3\2\2\2st\7v\2\2tu\7t\2\2uv")
        buf.write("\7w\2\2vw\7g\2\2w\6\3\2\2\2xy\7h\2\2yz\7c\2\2z{\7n\2\2")
        buf.write("{|\7u\2\2|}\7g\2\2}\b\3\2\2\2~\177\7p\2\2\177\u0080\7")
        buf.write("w\2\2\u0080\u0081\7o\2\2\u0081\u0082\7d\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\u0084\7t\2\2\u0084\n\3\2\2\2\u0085\u0086")
        buf.write("\7d\2\2\u0086\u0087\7q\2\2\u0087\u0088\7q\2\2\u0088\u0089")
        buf.write("\7n\2\2\u0089\f\3\2\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e\7k\2\2\u008e\u008f")
        buf.write("\7p\2\2\u008f\u0090\7i\2\2\u0090\16\3\2\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097\7p\2\2\u0097\20")
        buf.write("\3\2\2\2\u0098\u0099\7x\2\2\u0099\u009a\7c\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\22\3\2\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7{\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7o\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7e\2\2\u00a3\24")
        buf.write("\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\26\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7t\2\2\u00ac\30")
        buf.write("\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7n\2\2\u00b2\32")
        buf.write("\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7{\2\2\u00b5\34")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb\36")
        buf.write("\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4 \3")
        buf.write("\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\"\3")
        buf.write("\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7g\2\2\u00cc$\3\2\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1&\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7(\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7f\2\2\u00db*\3\2\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df,\3")
        buf.write("\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3.\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7-\2\2\u00e8\62\3")
        buf.write("\2\2\2\u00e9\u00ea\7/\2\2\u00ea\64\3\2\2\2\u00eb\u00ec")
        buf.write("\7,\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\7\61\2\2\u00ee8\3")
        buf.write("\2\2\2\u00ef\u00f0\7\'\2\2\u00f0:\3\2\2\2\u00f1\u00f2")
        buf.write("\7?\2\2\u00f2<\3\2\2\2\u00f3\u00f4\7>\2\2\u00f4\u00f5")
        buf.write("\7/\2\2\u00f5>\3\2\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8@\3\2\2\2\u00f9\u00fa\7>\2\2\u00faB\3\2\2")
        buf.write("\2\u00fb\u00fc\7>\2\2\u00fc\u00fd\7?\2\2\u00fdD\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ffF\3\2\2\2\u0100\u0101\7@\2")
        buf.write("\2\u0101\u0102\7?\2\2\u0102H\3\2\2\2\u0103\u0104\7\60")
        buf.write("\2\2\u0104\u0105\7\60\2\2\u0105\u0106\7\60\2\2\u0106J")
        buf.write("\3\2\2\2\u0107\u0108\7?\2\2\u0108\u0109\7?\2\2\u0109L")
        buf.write("\3\2\2\2\u010a\u010b\7]\2\2\u010bN\3\2\2\2\u010c\u010d")
        buf.write("\7_\2\2\u010dP\3\2\2\2\u010e\u010f\7*\2\2\u010fR\3\2\2")
        buf.write("\2\u0110\u0111\7+\2\2\u0111T\3\2\2\2\u0112\u0113\7.\2")
        buf.write("\2\u0113V\3\2\2\2\u0114\u0115\7\f\2\2\u0115X\3\2\2\2\u0116")
        buf.write("\u011a\t\2\2\2\u0117\u0119\t\3\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011bZ\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u0125")
        buf.write("\7$\2\2\u011e\u0124\n\4\2\2\u011f\u0120\7^\2\2\u0120\u0124")
        buf.write("\t\5\2\2\u0121\u0122\7)\2\2\u0122\u0124\7$\2\2\u0123\u011e")
        buf.write("\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0121\3\2\2\2\u0124")
        buf.write("\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7")
        buf.write("$\2\2\u0129\u012a\b.\2\2\u012a\\\3\2\2\2\u012b\u012d\5")
        buf.write("_\60\2\u012c\u012e\5a\61\2\u012d\u012c\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131\5c\62\2\u0130")
        buf.write("\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131^\3\2\2\2\u0132")
        buf.write("\u0134\t\6\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136`\3\2\2")
        buf.write("\2\u0137\u013b\7\60\2\2\u0138\u013a\t\6\2\2\u0139\u0138")
        buf.write("\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013cb\3\2\2\2\u013d\u013b\3\2\2\2\u013e")
        buf.write("\u0140\t\7\2\2\u013f\u0141\t\b\2\2\u0140\u013f\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0144\t")
        buf.write("\6\2\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146d\3\2\2\2\u0147\u0148")
        buf.write("\7%\2\2\u0148\u0149\7%\2\2\u0149\u014d\3\2\2\2\u014a\u014c")
        buf.write("\n\t\2\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2")
        buf.write("\u014f\u014d\3\2\2\2\u0150\u0151\b\63\3\2\u0151f\3\2\2")
        buf.write("\2\u0152\u0154\t\n\2\2\u0153\u0152\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0158\b\64\3\2\u0158h\3\2\2\2\u0159")
        buf.write("\u015a\13\2\2\2\u015a\u015b\b\65\4\2\u015bj\3\2\2\2\u015c")
        buf.write("\u0164\7$\2\2\u015d\u0163\n\4\2\2\u015e\u015f\7^\2\2\u015f")
        buf.write("\u0163\t\5\2\2\u0160\u0161\7)\2\2\u0161\u0163\7$\2\2\u0162")
        buf.write("\u015d\3\2\2\2\u0162\u015e\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u016a\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\7\17\2\2\u0168\u016b\7\f\2\2\u0169\u016b\t\13\2\2\u016a")
        buf.write("\u0167\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\b\66\5\2\u016dl\3\2\2\2\u016e\u0176\7$\2")
        buf.write("\2\u016f\u0175\n\4\2\2\u0170\u0171\7^\2\2\u0171\u0175")
        buf.write("\t\5\2\2\u0172\u0173\7)\2\2\u0173\u0175\7$\2\2\u0174\u016f")
        buf.write("\3\2\2\2\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u017c\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017d\t")
        buf.write("\f\2\2\u017a\u017b\7^\2\2\u017b\u017d\n\5\2\2\u017c\u0179")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017f\b\67\6\2\u017fn\3\2\2\2\25\2q\u011a\u0123\u0125")
        buf.write("\u012d\u0130\u0135\u013b\u0140\u0145\u014d\u0155\u0162")
        buf.write("\u0164\u016a\u0174\u0176\u017c\7\3.\2\b\2\2\3\65\3\3\66")
        buf.write("\4\3\67\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
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
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQUAL = 29
    ASSIGNINIT = 30
    DIFF = 31
    LESS = 32
    LESSEQUAL = 33
    GREATER = 34
    GREATEREQUAL = 35
    CONCAT = 36
    DOUBlEEQUAL = 37
    LBRACKET = 38
    RBRACKET = 39
    LPAREN = 40
    RPAREN = 41
    COMMA = 42
    NEWLINE = 43
    ID = 44
    STRING_LIT = 45
    NUMBER_LIT = 46
    COMMENTS = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'['", "']'", "'('", "')'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGNINIT", "DIFF", "LESS", 
            "LESSEQUAL", "GREATER", "GREATEREQUAL", "CONCAT", "DOUBlEEQUAL", 
            "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", "COMMA", "NEWLINE", 
            "ID", "STRING_LIT", "NUMBER_LIT", "COMMENTS", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOL_LIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQUAL", "ASSIGNINIT", "DIFF", "LESS", "LESSEQUAL", "GREATER", 
                  "GREATEREQUAL", "CONCAT", "DOUBlEEQUAL", "LBRACKET", "RBRACKET", 
                  "LPAREN", "RPAREN", "COMMA", "NEWLINE", "ID", "STRING_LIT", 
                  "NUMBER_LIT", "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", 
                  "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[44] = self.STRING_LIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1];

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


