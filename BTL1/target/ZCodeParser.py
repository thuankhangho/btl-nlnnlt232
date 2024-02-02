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
        buf.write("\u01a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3o\n\3\3\4\3\4\5\4s\n\4\3\5\3")
        buf.write("\5\5\5w\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0081")
        buf.write("\n\6\3\6\3\6\3\6\5\6\u0086\n\6\3\7\3\7\5\7\u008a\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a1\n\n\3\n\3")
        buf.write("\n\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00ae")
        buf.write("\n\f\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00b6\n\16\3\17\3")
        buf.write("\17\3\17\5\17\u00bb\n\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00c8\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u00dc\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u00e3\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\7\32\u00ec\n\32\f\32\16\32\u00ef\13\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u00f8\n\33\f\33\16")
        buf.write("\33\u00fb\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u0104\n\34\f\34\16\34\u0107\13\34\3\35\3\35\3\35\5\35")
        buf.write("\u010c\n\35\3\36\3\36\3\36\5\36\u0111\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\7\37\u011b\n\37\f\37\16\37")
        buf.write("\u011e\13\37\3 \3 \3 \3 \3 \3 \3 \5 \u0127\n \3!\3!\3")
        buf.write("!\3!\5!\u012d\n!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\5")
        buf.write("#\u0139\n#\3$\3$\5$\u013d\n$\3$\3$\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\5&\u014a\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u0155\n\'\3(\3(\3(\3(\3)\3)\3)\3)\5)\u015f\n)\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\5.\u017a\n.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\5\60\u0189\n\60\3\61\3\61\3")
        buf.write("\61\5\61\u018e\n\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u0197\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01a2\n\63\3\63\2\6\62\64\66<\64\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bd\2\7\3\2\5\7\5\2\36\36 $&&\3\2")
        buf.write("\27\30\3\2\31\32\3\2\33\35\2\u019f\2f\3\2\2\2\4n\3\2\2")
        buf.write("\2\6r\3\2\2\2\bv\3\2\2\2\nz\3\2\2\2\f\u0089\3\2\2\2\16")
        buf.write("\u008b\3\2\2\2\20\u0090\3\2\2\2\22\u0097\3\2\2\2\24\u00a6")
        buf.write("\3\2\2\2\26\u00ad\3\2\2\2\30\u00af\3\2\2\2\32\u00b5\3")
        buf.write("\2\2\2\34\u00ba\3\2\2\2\36\u00bc\3\2\2\2 \u00be\3\2\2")
        buf.write("\2\"\u00c7\3\2\2\2$\u00c9\3\2\2\2&\u00ce\3\2\2\2(\u00d0")
        buf.write("\3\2\2\2*\u00d2\3\2\2\2,\u00d4\3\2\2\2.\u00db\3\2\2\2")
        buf.write("\60\u00e2\3\2\2\2\62\u00e4\3\2\2\2\64\u00f0\3\2\2\2\66")
        buf.write("\u00fc\3\2\2\28\u010b\3\2\2\2:\u0110\3\2\2\2<\u0112\3")
        buf.write("\2\2\2>\u0126\3\2\2\2@\u012c\3\2\2\2B\u012e\3\2\2\2D\u0138")
        buf.write("\3\2\2\2F\u013c\3\2\2\2H\u0140\3\2\2\2J\u0145\3\2\2\2")
        buf.write("L\u014b\3\2\2\2N\u0156\3\2\2\2P\u015e\3\2\2\2R\u0160\3")
        buf.write("\2\2\2T\u0167\3\2\2\2V\u0170\3\2\2\2X\u0173\3\2\2\2Z\u0176")
        buf.write("\3\2\2\2\\\u017d\3\2\2\2^\u0188\3\2\2\2`\u018a\3\2\2\2")
        buf.write("b\u0196\3\2\2\2d\u01a1\3\2\2\2fg\5\34\17\2gh\5\4\3\2h")
        buf.write("i\7\2\2\3i\3\3\2\2\2jk\5\6\4\2kl\5\4\3\2lo\3\2\2\2mo\5")
        buf.write("\6\4\2nj\3\2\2\2nm\3\2\2\2o\5\3\2\2\2ps\5\22\n\2qs\5\b")
        buf.write("\5\2rp\3\2\2\2rq\3\2\2\2s\7\3\2\2\2tw\5\n\6\2uw\5\f\7")
        buf.write("\2vt\3\2\2\2vu\3\2\2\2wx\3\2\2\2xy\5\34\17\2y\t\3\2\2")
        buf.write("\2z{\5\36\20\2{\u0080\7\61\2\2|}\7)\2\2}~\7\61\2\2~\u0081")
        buf.write("\7*\2\2\177\u0081\3\2\2\2\u0080|\3\2\2\2\u0080\177\3\2")
        buf.write("\2\2\u0081\u0085\3\2\2\2\u0082\u0083\7\37\2\2\u0083\u0086")
        buf.write("\5.\30\2\u0084\u0086\3\2\2\2\u0085\u0082\3\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\13\3\2\2\2\u0087\u008a\5\16\b\2\u0088")
        buf.write("\u008a\5\20\t\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2")
        buf.write("\2\u008a\r\3\2\2\2\u008b\u008c\7\t\2\2\u008c\u008d\7\61")
        buf.write("\2\2\u008d\u008e\7\37\2\2\u008e\u008f\5.\30\2\u008f\17")
        buf.write("\3\2\2\2\u0090\u0091\7\n\2\2\u0091\u0095\7\61\2\2\u0092")
        buf.write("\u0093\7\37\2\2\u0093\u0096\5.\30\2\u0094\u0096\3\2\2")
        buf.write("\2\u0095\u0092\3\2\2\2\u0095\u0094\3\2\2\2\u0096\21\3")
        buf.write("\2\2\2\u0097\u0098\7\13\2\2\u0098\u0099\7\61\2\2\u0099")
        buf.write("\u009a\7\'\2\2\u009a\u009b\5\24\13\2\u009b\u009c\7(\2")
        buf.write("\2\u009c\u00a0\5\34\17\2\u009d\u00a1\5Z.\2\u009e\u00a1")
        buf.write("\5`\61\2\u009f\u00a1\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\5\34\17\2\u00a3\23\3\2\2\2\u00a4\u00a7\5")
        buf.write("\26\f\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a9\5\30\r\2\u00a9")
        buf.write("\u00aa\7+\2\2\u00aa\u00ab\5\26\f\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00ae\5\30\r\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\27\3\2\2\2\u00af\u00b0\5\36\20\2\u00b0")
        buf.write("\u00b1\7\61\2\2\u00b1\31\3\2\2\2\u00b2\u00b3\7,\2\2\u00b3")
        buf.write("\u00b6\5\32\16\2\u00b4\u00b6\7,\2\2\u00b5\u00b2\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\33\3\2\2\2\u00b7\u00b8\7")
        buf.write(",\2\2\u00b8\u00bb\5\34\17\2\u00b9\u00bb\3\2\2\2\u00ba")
        buf.write("\u00b7\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\35\3\2\2\2\u00bc")
        buf.write("\u00bd\t\2\2\2\u00bd\37\3\2\2\2\u00be\u00bf\7)\2\2\u00bf")
        buf.write("\u00c0\5\"\22\2\u00c0\u00c1\7*\2\2\u00c1!\3\2\2\2\u00c2")
        buf.write("\u00c3\5.\30\2\u00c3\u00c4\7+\2\2\u00c4\u00c5\5\"\22\2")
        buf.write("\u00c5\u00c8\3\2\2\2\u00c6\u00c8\5.\30\2\u00c7\u00c2\3")
        buf.write("\2\2\2\u00c7\u00c6\3\2\2\2\u00c8#\3\2\2\2\u00c9\u00ca")
        buf.write("\7\61\2\2\u00ca\u00cb\7\'\2\2\u00cb\u00cc\5^\60\2\u00cc")
        buf.write("\u00cd\7(\2\2\u00cd%\3\2\2\2\u00ce\u00cf\t\3\2\2\u00cf")
        buf.write("\'\3\2\2\2\u00d0\u00d1\t\4\2\2\u00d1)\3\2\2\2\u00d2\u00d3")
        buf.write("\t\5\2\2\u00d3+\3\2\2\2\u00d4\u00d5\t\6\2\2\u00d5-\3\2")
        buf.write("\2\2\u00d6\u00d7\5\60\31\2\u00d7\u00d8\7%\2\2\u00d8\u00d9")
        buf.write("\5\60\31\2\u00d9\u00dc\3\2\2\2\u00da\u00dc\5\60\31\2\u00db")
        buf.write("\u00d6\3\2\2\2\u00db\u00da\3\2\2\2\u00dc/\3\2\2\2\u00dd")
        buf.write("\u00de\5\62\32\2\u00de\u00df\5&\24\2\u00df\u00e0\5\62")
        buf.write("\32\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5\62\32\2\u00e2")
        buf.write("\u00dd\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\61\3\2\2\2\u00e4")
        buf.write("\u00e5\b\32\1\2\u00e5\u00e6\5\64\33\2\u00e6\u00ed\3\2")
        buf.write("\2\2\u00e7\u00e8\f\4\2\2\u00e8\u00e9\5(\25\2\u00e9\u00ea")
        buf.write("\5\64\33\2\u00ea\u00ec\3\2\2\2\u00eb\u00e7\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\63\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\b\33")
        buf.write("\1\2\u00f1\u00f2\5\66\34\2\u00f2\u00f9\3\2\2\2\u00f3\u00f4")
        buf.write("\f\4\2\2\u00f4\u00f5\5*\26\2\u00f5\u00f6\5\66\34\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f8\u00fb\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\65\3\2")
        buf.write("\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\b\34\1\2\u00fd\u00fe")
        buf.write("\58\35\2\u00fe\u0105\3\2\2\2\u00ff\u0100\f\4\2\2\u0100")
        buf.write("\u0101\5,\27\2\u0101\u0102\58\35\2\u0102\u0104\3\2\2\2")
        buf.write("\u0103\u00ff\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\67\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u0109\7\26\2\2\u0109\u010c\58\35\2\u010a")
        buf.write("\u010c\5:\36\2\u010b\u0108\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c9\3\2\2\2\u010d\u010e\7\32\2\2\u010e\u0111\5:\36")
        buf.write("\2\u010f\u0111\5<\37\2\u0110\u010d\3\2\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111;\3\2\2\2\u0112\u0113\b\37\1\2\u0113\u0114")
        buf.write("\5> \2\u0114\u011c\3\2\2\2\u0115\u0116\f\4\2\2\u0116\u0117")
        buf.write("\7)\2\2\u0117\u0118\5D#\2\u0118\u0119\7*\2\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0115\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d=\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0127\7\61\2\2\u0120\u0127\5@!\2")
        buf.write("\u0121\u0122\7\'\2\2\u0122\u0123\5.\30\2\u0123\u0124\7")
        buf.write("(\2\2\u0124\u0127\3\2\2\2\u0125\u0127\5$\23\2\u0126\u011f")
        buf.write("\3\2\2\2\u0126\u0120\3\2\2\2\u0126\u0121\3\2\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127?\3\2\2\2\u0128\u012d\7.\2\2\u0129")
        buf.write("\u012d\7/\2\2\u012a\u012d\7\60\2\2\u012b\u012d\5B\"\2")
        buf.write("\u012c\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3")
        buf.write("\2\2\2\u012c\u012b\3\2\2\2\u012dA\3\2\2\2\u012e\u012f")
        buf.write("\7\61\2\2\u012f\u0130\7)\2\2\u0130\u0131\5D#\2\u0131\u0132")
        buf.write("\7*\2\2\u0132C\3\2\2\2\u0133\u0134\5.\30\2\u0134\u0135")
        buf.write("\7+\2\2\u0135\u0136\5D#\2\u0136\u0139\3\2\2\2\u0137\u0139")
        buf.write("\5.\30\2\u0138\u0133\3\2\2\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("E\3\2\2\2\u013a\u013d\5\n\6\2\u013b\u013d\5\f\7\2\u013c")
        buf.write("\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013f\5\32\16\2\u013fG\3\2\2\2\u0140\u0141\5J&")
        buf.write("\2\u0141\u0142\7\37\2\2\u0142\u0143\5.\30\2\u0143\u0144")
        buf.write("\5\32\16\2\u0144I\3\2\2\2\u0145\u0149\7\61\2\2\u0146\u0147")
        buf.write("\7)\2\2\u0147\u0148\7.\2\2\u0148\u014a\7*\2\2\u0149\u0146")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014aK\3\2\2\2\u014b\u014c")
        buf.write("\7\21\2\2\u014c\u014d\7\'\2\2\u014d\u014e\5.\30\2\u014e")
        buf.write("\u014f\7(\2\2\u014f\u0150\5\34\17\2\u0150\u0154\5d\63")
        buf.write("\2\u0151\u0155\5N(\2\u0152\u0155\5P)\2\u0153\u0155\3\2")
        buf.write("\2\2\u0154\u0151\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155M\3\2\2\2\u0156\u0157\7\22\2\2\u0157\u0158")
        buf.write("\5d\63\2\u0158\u0159\5\32\16\2\u0159O\3\2\2\2\u015a\u015b")
        buf.write("\5R*\2\u015b\u015c\5P)\2\u015c\u015f\3\2\2\2\u015d\u015f")
        buf.write("\5R*\2\u015e\u015a\3\2\2\2\u015e\u015d\3\2\2\2\u015fQ")
        buf.write("\3\2\2\2\u0160\u0161\7\23\2\2\u0161\u0162\7\'\2\2\u0162")
        buf.write("\u0163\5.\30\2\u0163\u0164\7(\2\2\u0164\u0165\5\34\17")
        buf.write("\2\u0165\u0166\5d\63\2\u0166S\3\2\2\2\u0167\u0168\7\f")
        buf.write("\2\2\u0168\u0169\7\61\2\2\u0169\u016a\7\r\2\2\u016a\u016b")
        buf.write("\5.\30\2\u016b\u016c\7\16\2\2\u016c\u016d\5.\30\2\u016d")
        buf.write("\u016e\5\34\17\2\u016e\u016f\5d\63\2\u016fU\3\2\2\2\u0170")
        buf.write("\u0171\7\17\2\2\u0171\u0172\5\34\17\2\u0172W\3\2\2\2\u0173")
        buf.write("\u0174\7\20\2\2\u0174\u0175\5\34\17\2\u0175Y\3\2\2\2\u0176")
        buf.write("\u0179\7\b\2\2\u0177\u017a\5.\30\2\u0178\u017a\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u017c\5\32\16\2\u017c[\3\2\2\2\u017d\u017e")
        buf.write("\7\61\2\2\u017e\u017f\7\'\2\2\u017f\u0180\5^\60\2\u0180")
        buf.write("\u0181\7(\2\2\u0181\u0182\5\32\16\2\u0182]\3\2\2\2\u0183")
        buf.write("\u0184\5.\30\2\u0184\u0185\7+\2\2\u0185\u0186\5^\60\2")
        buf.write("\u0186\u0189\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0183\3")
        buf.write("\2\2\2\u0188\u0187\3\2\2\2\u0189_\3\2\2\2\u018a\u018d")
        buf.write("\7\24\2\2\u018b\u018e\5b\62\2\u018c\u018e\5\32\16\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0190\7\25\2\2\u0190\u0191\5\32\16\2\u0191a\3\2")
        buf.write("\2\2\u0192\u0193\5d\63\2\u0193\u0194\5b\62\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0192\3\2\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197c\3\2\2\2\u0198\u01a2\5F$\2\u0199")
        buf.write("\u01a2\5H%\2\u019a\u01a2\5L\'\2\u019b\u01a2\5T+\2\u019c")
        buf.write("\u01a2\5V,\2\u019d\u01a2\5X-\2\u019e\u01a2\5Z.\2\u019f")
        buf.write("\u01a2\5\\/\2\u01a0\u01a2\5`\61\2\u01a1\u0198\3\2\2\2")
        buf.write("\u01a1\u0199\3\2\2\2\u01a1\u019a\3\2\2\2\u01a1\u019b\3")
        buf.write("\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d\3\2\2\2\u01a1\u019e")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("e\3\2\2\2#nrv\u0080\u0085\u0089\u0095\u00a0\u00a6\u00ad")
        buf.write("\u00b5\u00ba\u00c7\u00db\u00e2\u00ed\u00f9\u0105\u010b")
        buf.write("\u0110\u011c\u0126\u012c\u0138\u013c\u0149\u0154\u015e")
        buf.write("\u0179\u0188\u018d\u0196\u01a1")
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
                      "LSB", "RSB", "CM", "NEWLINE", "LINECMT", "NUMLIT", 
                      "BOOLLIT", "STRINGLIT", "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", 
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
    RULE_parameterlist = 9
    RULE_parameterprime = 10
    RULE_param = 11
    RULE_newlinelist = 12
    RULE_nullablenewlinelist = 13
    RULE_typ = 14
    RULE_arraylit = 15
    RULE_elementlist = 16
    RULE_functioncall = 17
    RULE_relational = 18
    RULE_logical = 19
    RULE_adding = 20
    RULE_multiplying = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_expr7 = 29
    RULE_expr8 = 30
    RULE_literal = 31
    RULE_arraytype = 32
    RULE_exprlist = 33
    RULE_vardeclstate = 34
    RULE_assignstate = 35
    RULE_lhs = 36
    RULE_ifstate = 37
    RULE_elsestate = 38
    RULE_elifstatelist = 39
    RULE_elifstate = 40
    RULE_forstate = 41
    RULE_breakstate = 42
    RULE_continuestate = 43
    RULE_returnstate = 44
    RULE_functioncallstate = 45
    RULE_argumentlist = 46
    RULE_blockstate = 47
    RULE_stmtlist = 48
    RULE_stmt = 49

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "typdecl", 
                   "implidecl", "implivardecl", "implidynadecl", "funcdecl", 
                   "parameterlist", "parameterprime", "param", "newlinelist", 
                   "nullablenewlinelist", "typ", "arraylit", "elementlist", 
                   "functioncall", "relational", "logical", "adding", "multiplying", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "literal", "arraytype", "exprlist", 
                   "vardeclstate", "assignstate", "lhs", "ifstate", "elsestate", 
                   "elifstatelist", "elifstate", "forstate", "breakstate", 
                   "continuestate", "returnstate", "functioncallstate", 
                   "argumentlist", "blockstate", "stmtlist", "stmt" ]

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
    LINECMT=43
    NUMLIT=44
    BOOLLIT=45
    STRINGLIT=46
    IDENTIFIER=47
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

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


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
            self.state = 100
            self.nullablenewlinelist()
            self.state = 101
            self.decllist()
            self.state = 102
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
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.decl()
                self.state = 105
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 114
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 115
                self.implidecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 118
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


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.IDENTIFIER)
            else:
                return self.getToken(ZCodeParser.IDENTIFIER, i)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

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
            self.state = 120
            self.typ()
            self.state = 121
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSB]:
                self.state = 122
                self.match(ZCodeParser.LSB)
                self.state = 123
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 124
                self.match(ZCodeParser.RSB)
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.ASSIGN, ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.state = 128
                self.match(ZCodeParser.ASSIGN)
                self.state = 129
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
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.implivardecl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
            self.state = 137
            self.match(ZCodeParser.VAR)
            self.state = 138
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 139
            self.match(ZCodeParser.ASSIGN)
            self.state = 140
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
            self.state = 142
            self.match(ZCodeParser.DYNAMIC)
            self.state = 143
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.state = 144
                self.match(ZCodeParser.ASSIGN)
                self.state = 145
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
            self.state = 149
            self.match(ZCodeParser.FUNC)
            self.state = 150
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 151
            self.match(ZCodeParser.LRB)
            self.state = 152
            self.parameterlist()
            self.state = 153
            self.match(ZCodeParser.RRB)
            self.state = 154
            self.nullablenewlinelist()
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 155
                self.returnstate()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 156
                self.blockstate()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
            self.nullablenewlinelist()
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
        self.enterRule(localctx, 18, self.RULE_parameterlist)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
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
        self.enterRule(localctx, 20, self.RULE_parameterprime)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.param()
                self.state = 167
                self.match(ZCodeParser.CM)
                self.state = 168
                self.parameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.typ()
            self.state = 174
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
        self.enterRule(localctx, 24, self.RULE_newlinelist)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.NEWLINE)
                self.state = 177
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
        self.enterRule(localctx, 26, self.RULE_nullablenewlinelist)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(ZCodeParser.NEWLINE)
                self.state = 182
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
        self.enterRule(localctx, 28, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.LSB)
            self.state = 189
            self.elementlist()
            self.state = 190
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
        self.enterRule(localctx, 32, self.RULE_elementlist)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.expr()
                self.state = 193
                self.match(ZCodeParser.CM)
                self.state = 194
                self.elementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functioncall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = ZCodeParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 200
            self.match(ZCodeParser.LRB)
            self.state = 201
            self.argumentlist()
            self.state = 202
            self.match(ZCodeParser.RRB)
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
        self.enterRule(localctx, 36, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
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
        self.enterRule(localctx, 38, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
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
        self.enterRule(localctx, 40, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
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
        self.enterRule(localctx, 42, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
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
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.expr1()
                self.state = 213
                self.match(ZCodeParser.CONCAT)
                self.state = 214
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
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
        self.enterRule(localctx, 46, self.RULE_expr1)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.expr2(0)
                self.state = 220
                self.relational()
                self.state = 221
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    self.logical()
                    self.state = 231
                    self.expr3(0) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 241
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 242
                    self.adding()
                    self.state = 243
                    self.expr4(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    self.multiplying()
                    self.state = 255
                    self.expr5() 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_expr5)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(ZCodeParser.NOT)
                self.state = 263
                self.expr5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(ZCodeParser.MINUS)
                self.state = 268
                self.expr6()
                pass
            elif token in [ZCodeParser.LRB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    self.match(ZCodeParser.LSB)
                    self.state = 277
                    self.exprlist()
                    self.state = 278
                    self.match(ZCodeParser.RSB) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def functioncall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr8)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(ZCodeParser.LRB)
                self.state = 288
                self.expr()
                self.state = 289
                self.match(ZCodeParser.RRB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.functioncall()
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
        self.enterRule(localctx, 62, self.RULE_literal)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.BOOLLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
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
        self.enterRule(localctx, 64, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 301
            self.match(ZCodeParser.LSB)
            self.state = 302
            self.exprlist()
            self.state = 303
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
        self.enterRule(localctx, 66, self.RULE_exprlist)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.expr()
                self.state = 306
                self.match(ZCodeParser.CM)
                self.state = 307
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def typdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypdeclContext,0)


        def implidecl(self):
            return self.getTypedRuleContext(ZCodeParser.ImplideclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardeclstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclstate" ):
                return visitor.visitVardeclstate(self)
            else:
                return visitor.visitChildren(self)




    def vardeclstate(self):

        localctx = ZCodeParser.VardeclstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_vardeclstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 312
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 313
                self.implidecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 316
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstate" ):
                return visitor.visitAssignstate(self)
            else:
                return visitor.visitChildren(self)




    def assignstate(self):

        localctx = ZCodeParser.AssignstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.lhs()
            self.state = 319
            self.match(ZCodeParser.ASSIGN)
            self.state = 320
            self.expr()
            self.state = 321
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 324
                self.match(ZCodeParser.LSB)
                self.state = 325
                self.match(ZCodeParser.NUMLIT)
                self.state = 326
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elsestate(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestateContext,0)


        def elifstatelist(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstatelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstate" ):
                return visitor.visitIfstate(self)
            else:
                return visitor.visitChildren(self)




    def ifstate(self):

        localctx = ZCodeParser.IfstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.IF)
            self.state = 330
            self.match(ZCodeParser.LRB)
            self.state = 331
            self.expr()
            self.state = 332
            self.match(ZCodeParser.RRB)
            self.state = 333
            self.nullablenewlinelist()
            self.state = 334
            self.stmt()
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 335
                self.elsestate()
                pass

            elif la_ == 2:
                self.state = 336
                self.elifstatelist()
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestate" ):
                return visitor.visitElsestate(self)
            else:
                return visitor.visitChildren(self)




    def elsestate(self):

        localctx = ZCodeParser.ElsestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elsestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.ELSE)
            self.state = 341
            self.stmt()
            self.state = 342
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstatelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstate(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstateContext,0)


        def elifstatelist(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstatelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstatelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstatelist" ):
                return visitor.visitElifstatelist(self)
            else:
                return visitor.visitChildren(self)




    def elifstatelist(self):

        localctx = ZCodeParser.ElifstatelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elifstatelist)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.elifstate()
                self.state = 345
                self.elifstatelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.elifstate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstate" ):
                return visitor.visitElifstate(self)
            else:
                return visitor.visitChildren(self)




    def elifstate(self):

        localctx = ZCodeParser.ElifstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(ZCodeParser.ELIF)
            self.state = 351
            self.match(ZCodeParser.LRB)
            self.state = 352
            self.expr()
            self.state = 353
            self.match(ZCodeParser.RRB)
            self.state = 354
            self.nullablenewlinelist()
            self.state = 355
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstate" ):
                return visitor.visitForstate(self)
            else:
                return visitor.visitChildren(self)




    def forstate(self):

        localctx = ZCodeParser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.FOR)
            self.state = 358
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 359
            self.match(ZCodeParser.UNTIL)
            self.state = 360
            self.expr()
            self.state = 361
            self.match(ZCodeParser.BY)
            self.state = 362
            self.expr()
            self.state = 363
            self.nullablenewlinelist()
            self.state = 364
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstate" ):
                return visitor.visitBreakstate(self)
            else:
                return visitor.visitChildren(self)




    def breakstate(self):

        localctx = ZCodeParser.BreakstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.BREAK)
            self.state = 367
            self.nullablenewlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def nullablenewlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablenewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestate" ):
                return visitor.visitContinuestate(self)
            else:
                return visitor.visitChildren(self)




    def continuestate(self):

        localctx = ZCodeParser.ContinuestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(ZCodeParser.CONTINUE)
            self.state = 370
            self.nullablenewlinelist()
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
        self.enterRule(localctx, 88, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(ZCodeParser.RETURN)
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.state = 373
                self.expr()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 377
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functioncallstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncallstate" ):
                return visitor.visitFunctioncallstate(self)
            else:
                return visitor.visitChildren(self)




    def functioncallstate(self):

        localctx = ZCodeParser.FunctioncallstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_functioncallstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 380
            self.match(ZCodeParser.LRB)
            self.state = 381
            self.argumentlist()
            self.state = 382
            self.match(ZCodeParser.RRB)
            self.state = 383
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_argumentlist)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LRB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.expr()
                self.state = 386
                self.match(ZCodeParser.CM)
                self.state = 387
                self.argumentlist()
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


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = ZCodeParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ZCodeParser.BEGIN)
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.END, ZCodeParser.IDENTIFIER]:
                self.state = 393
                self.stmtlist()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.state = 394
                self.newlinelist()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 397
            self.match(ZCodeParser.END)
            self.state = 398
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmtlist)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.stmt()
                self.state = 401
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END]:
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclstate(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclstateContext,0)


        def assignstate(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstateContext,0)


        def ifstate(self):
            return self.getTypedRuleContext(ZCodeParser.IfstateContext,0)


        def forstate(self):
            return self.getTypedRuleContext(ZCodeParser.ForstateContext,0)


        def breakstate(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstateContext,0)


        def continuestate(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestateContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstateContext,0)


        def functioncallstate(self):
            return self.getTypedRuleContext(ZCodeParser.FunctioncallstateContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstateContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.vardeclstate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.assignstate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.ifstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.forstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 410
                self.breakstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 411
                self.continuestate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 412
                self.returnstate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 413
                self.functioncallstate()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 414
                self.blockstate()
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
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        self._predicates[29] = self.expr7_sempred
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
         




