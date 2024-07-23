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
        buf.write("\u0199\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\7\2^\n\2\f\2\16\2a\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3j\n\3\3\4\3\4\3\4\3\4\5\4p\n\4\3\5\3\5\3\5\5\5u\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7~\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008e")
        buf.write("\n\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u0097\n\n\3\13\3")
        buf.write("\13\5\13\u009b\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00a9\n\16\3\16\3\16\5\16\u00ad")
        buf.write("\n\16\3\16\3\16\5\16\u00b1\n\16\3\16\3\16\5\16\u00b5\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\5\17\u00bc\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00c3\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u00ca\n\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00d2\n\22\f\22\16\22\u00d5\13\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\7\23\u00dd\n\23\f\23\16\23\u00e0\13\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\7\24\u00e8\n\24\f\24\16\24\u00eb")
        buf.write("\13\24\3\25\3\25\3\25\5\25\u00f0\n\25\3\26\3\26\3\26\5")
        buf.write("\26\u00f5\n\26\3\27\3\27\5\27\u00f9\n\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0100\n\27\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u0107\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0110\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0117\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u0122")
        buf.write("\n\34\3\35\3\35\3\35\5\35\u0127\n\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0134\n\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\5!\u0140\n!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u014c\n#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\5$\u0156\n$\3%\3%\3%\3%\3%\5%\u015d\n%\3")
        buf.write("%\3%\3&\3&\5&\u0163\n&\3&\3&\5&\u0167\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u0170\n\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\5*\u017c\n*\3*\3*\3+\3+\3+\5+\u0183\n+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\5-\u0192\n-\3.\6.\u0195")
        buf.write("\n.\r.\16.\u0196\3.\2\5\"$&/\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2")
        buf.write("\7\3\2\5\7\5\2\36\36 $&&\3\2\34\35\3\2\26\27\3\2\30\32")
        buf.write("\2\u01a1\2_\3\2\2\2\4i\3\2\2\2\6o\3\2\2\2\bt\3\2\2\2\n")
        buf.write("v\3\2\2\2\f}\3\2\2\2\16\177\3\2\2\2\20\u0087\3\2\2\2\22")
        buf.write("\u0096\3\2\2\2\24\u009a\3\2\2\2\26\u009c\3\2\2\2\30\u009f")
        buf.write("\3\2\2\2\32\u00a4\3\2\2\2\34\u00bb\3\2\2\2\36\u00c2\3")
        buf.write("\2\2\2 \u00c9\3\2\2\2\"\u00cb\3\2\2\2$\u00d6\3\2\2\2&")
        buf.write("\u00e1\3\2\2\2(\u00ef\3\2\2\2*\u00f4\3\2\2\2,\u00ff\3")
        buf.write("\2\2\2.\u0106\3\2\2\2\60\u010f\3\2\2\2\62\u0116\3\2\2")
        buf.write("\2\64\u0118\3\2\2\2\66\u0121\3\2\2\28\u0123\3\2\2\2:\u0133")
        buf.write("\3\2\2\2<\u0135\3\2\2\2>\u0138\3\2\2\2@\u013f\3\2\2\2")
        buf.write("B\u0141\3\2\2\2D\u0146\3\2\2\2F\u0155\3\2\2\2H\u0157\3")
        buf.write("\2\2\2J\u0166\3\2\2\2L\u0168\3\2\2\2N\u0173\3\2\2\2P\u0176")
        buf.write("\3\2\2\2R\u0179\3\2\2\2T\u017f\3\2\2\2V\u0187\3\2\2\2")
        buf.write("X\u0191\3\2\2\2Z\u0194\3\2\2\2\\^\7/\2\2]\\\3\2\2\2^a")
        buf.write("\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3\2\2\2bc\5\4")
        buf.write("\3\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4\2fg\5\4\3\2gj\3\2\2")
        buf.write("\2hj\5\6\4\2ie\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kp\5\32\16")
        buf.write("\2lm\5\b\5\2mn\5Z.\2np\3\2\2\2ok\3\2\2\2ol\3\2\2\2p\7")
        buf.write("\3\2\2\2qu\5\n\6\2ru\5\f\7\2su\5\24\13\2tq\3\2\2\2tr\3")
        buf.write("\2\2\2ts\3\2\2\2u\t\3\2\2\2vw\7\t\2\2wx\7,\2\2xy\7\37")
        buf.write("\2\2yz\5\36\20\2z\13\3\2\2\2{~\5\16\b\2|~\5\20\t\2}{\3")
        buf.write("\2\2\2}|\3\2\2\2~\r\3\2\2\2\177\u0080\t\2\2\2\u0080\u0085")
        buf.write("\7,\2\2\u0081\u0082\7)\2\2\u0082\u0083\5\22\n\2\u0083")
        buf.write("\u0084\7*\2\2\u0084\u0086\3\2\2\2\u0085\u0081\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\17\3\2\2\2\u0087\u0088\t\2")
        buf.write("\2\2\u0088\u008d\7,\2\2\u0089\u008a\7)\2\2\u008a\u008b")
        buf.write("\5\22\n\2\u008b\u008c\7*\2\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("\u0089\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\7\37\2\2\u0090\u0091\5\36\20\2\u0091\21\3")
        buf.write("\2\2\2\u0092\u0097\7-\2\2\u0093\u0094\7-\2\2\u0094\u0095")
        buf.write("\7+\2\2\u0095\u0097\5\22\n\2\u0096\u0092\3\2\2\2\u0096")
        buf.write("\u0093\3\2\2\2\u0097\23\3\2\2\2\u0098\u009b\5\30\r\2\u0099")
        buf.write("\u009b\5\26\f\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2")
        buf.write("\2\u009b\25\3\2\2\2\u009c\u009d\7\n\2\2\u009d\u009e\7")
        buf.write(",\2\2\u009e\27\3\2\2\2\u009f\u00a0\7\n\2\2\u00a0\u00a1")
        buf.write("\7,\2\2\u00a1\u00a2\7\37\2\2\u00a2\u00a3\5\36\20\2\u00a3")
        buf.write("\31\3\2\2\2\u00a4\u00a5\7\13\2\2\u00a5\u00a6\7,\2\2\u00a6")
        buf.write("\u00a8\7\'\2\2\u00a7\u00a9\5\34\17\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b4")
        buf.write("\7(\2\2\u00ab\u00ad\5Z.\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b5\5R*\2\u00af\u00b1")
        buf.write("\5Z.\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b5\5V,\2\u00b3\u00b5\5Z.\2\u00b4\u00ac")
        buf.write("\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\33\3\2\2\2\u00b6\u00b7\5\16\b\2\u00b7\u00b8\7+\2\2\u00b8")
        buf.write("\u00b9\5\34\17\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\5\16")
        buf.write("\b\2\u00bb\u00b6\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\35")
        buf.write("\3\2\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\7%\2\2\u00bf")
        buf.write("\u00c0\5 \21\2\u00c0\u00c3\3\2\2\2\u00c1\u00c3\5 \21\2")
        buf.write("\u00c2\u00bd\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\37\3\2")
        buf.write("\2\2\u00c4\u00c5\5\"\22\2\u00c5\u00c6\t\3\2\2\u00c6\u00c7")
        buf.write("\5\"\22\2\u00c7\u00ca\3\2\2\2\u00c8\u00ca\5\"\22\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca!\3\2\2\2\u00cb")
        buf.write("\u00cc\b\22\1\2\u00cc\u00cd\5$\23\2\u00cd\u00d3\3\2\2")
        buf.write("\2\u00ce\u00cf\f\4\2\2\u00cf\u00d0\t\4\2\2\u00d0\u00d2")
        buf.write("\5$\23\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4#\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d7\b\23\1\2\u00d7\u00d8\5&\24")
        buf.write("\2\u00d8\u00de\3\2\2\2\u00d9\u00da\f\4\2\2\u00da\u00db")
        buf.write("\t\5\2\2\u00db\u00dd\5&\24\2\u00dc\u00d9\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df%\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\b\24\1")
        buf.write("\2\u00e2\u00e3\5(\25\2\u00e3\u00e9\3\2\2\2\u00e4\u00e5")
        buf.write("\f\4\2\2\u00e5\u00e6\t\6\2\2\u00e6\u00e8\5(\25\2\u00e7")
        buf.write("\u00e4\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\'\3\2\2\2\u00eb\u00e9\3\2\2")
        buf.write("\2\u00ec\u00ed\7\33\2\2\u00ed\u00f0\5(\25\2\u00ee\u00f0")
        buf.write("\5*\26\2\u00ef\u00ec\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write(")\3\2\2\2\u00f1\u00f2\7\27\2\2\u00f2\u00f5\5*\26\2\u00f3")
        buf.write("\u00f5\5,\27\2\u00f4\u00f1\3\2\2\2\u00f4\u00f3\3\2\2\2")
        buf.write("\u00f5+\3\2\2\2\u00f6\u00f9\7,\2\2\u00f7\u00f9\58\35\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3")
        buf.write("\2\2\2\u00fa\u00fb\7)\2\2\u00fb\u00fc\5.\30\2\u00fc\u00fd")
        buf.write("\7*\2\2\u00fd\u0100\3\2\2\2\u00fe\u0100\5\60\31\2\u00ff")
        buf.write("\u00f8\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100-\3\2\2\2\u0101")
        buf.write("\u0107\5\36\20\2\u0102\u0103\5\36\20\2\u0103\u0104\7+")
        buf.write("\2\2\u0104\u0105\5.\30\2\u0105\u0107\3\2\2\2\u0106\u0101")
        buf.write("\3\2\2\2\u0106\u0102\3\2\2\2\u0107/\3\2\2\2\u0108\u0110")
        buf.write("\7,\2\2\u0109\u0110\5\62\32\2\u010a\u010b\7\'\2\2\u010b")
        buf.write("\u010c\5\36\20\2\u010c\u010d\7(\2\2\u010d\u0110\3\2\2")
        buf.write("\2\u010e\u0110\58\35\2\u010f\u0108\3\2\2\2\u010f\u0109")
        buf.write("\3\2\2\2\u010f\u010a\3\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("\61\3\2\2\2\u0111\u0117\7-\2\2\u0112\u0117\7.\2\2\u0113")
        buf.write("\u0117\7\3\2\2\u0114\u0117\7\4\2\2\u0115\u0117\5\64\33")
        buf.write("\2\u0116\u0111\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0113")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write("\63\3\2\2\2\u0118\u0119\7)\2\2\u0119\u011a\5\66\34\2\u011a")
        buf.write("\u011b\7*\2\2\u011b\65\3\2\2\2\u011c\u011d\5\36\20\2\u011d")
        buf.write("\u011e\7+\2\2\u011e\u011f\5\66\34\2\u011f\u0122\3\2\2")
        buf.write("\2\u0120\u0122\5\36\20\2\u0121\u011c\3\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\67\3\2\2\2\u0123\u0124\7,\2\2\u0124\u0126")
        buf.write("\7\'\2\2\u0125\u0127\5.\30\2\u0126\u0125\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\7(\2\2")
        buf.write("\u01299\3\2\2\2\u012a\u0134\5<\37\2\u012b\u0134\5> \2")
        buf.write("\u012c\u0134\5D#\2\u012d\u0134\5L\'\2\u012e\u0134\5N(")
        buf.write("\2\u012f\u0134\5P)\2\u0130\u0134\5R*\2\u0131\u0134\5T")
        buf.write("+\2\u0132\u0134\5V,\2\u0133\u012a\3\2\2\2\u0133\u012b")
        buf.write("\3\2\2\2\u0133\u012c\3\2\2\2\u0133\u012d\3\2\2\2\u0133")
        buf.write("\u012e\3\2\2\2\u0133\u012f\3\2\2\2\u0133\u0130\3\2\2\2")
        buf.write("\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134;\3\2\2")
        buf.write("\2\u0135\u0136\5\b\5\2\u0136\u0137\5Z.\2\u0137=\3\2\2")
        buf.write("\2\u0138\u0139\5@!\2\u0139\u013a\7\37\2\2\u013a\u013b")
        buf.write("\5\36\20\2\u013b\u013c\5Z.\2\u013c?\3\2\2\2\u013d\u0140")
        buf.write("\7,\2\2\u013e\u0140\5B\"\2\u013f\u013d\3\2\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140A\3\2\2\2\u0141\u0142\7,\2\2\u0142\u0143")
        buf.write("\7)\2\2\u0143\u0144\5.\30\2\u0144\u0145\7*\2\2\u0145C")
        buf.write("\3\2\2\2\u0146\u0147\7\21\2\2\u0147\u0148\7\'\2\2\u0148")
        buf.write("\u0149\5\36\20\2\u0149\u014b\7(\2\2\u014a\u014c\5Z.\2")
        buf.write("\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014e\5:\36\2\u014e\u014f\5F$\2\u014f\u0150")
        buf.write("\5J&\2\u0150E\3\2\2\2\u0151\u0152\5H%\2\u0152\u0153\5")
        buf.write("F$\2\u0153\u0156\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0151")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156G\3\2\2\2\u0157\u0158")
        buf.write("\7\23\2\2\u0158\u0159\7\'\2\2\u0159\u015a\5\36\20\2\u015a")
        buf.write("\u015c\7(\2\2\u015b\u015d\5Z.\2\u015c\u015b\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\5:\36\2")
        buf.write("\u015fI\3\2\2\2\u0160\u0162\7\22\2\2\u0161\u0163\5Z.\2")
        buf.write("\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3")
        buf.write("\2\2\2\u0164\u0167\5:\36\2\u0165\u0167\3\2\2\2\u0166\u0160")
        buf.write("\3\2\2\2\u0166\u0165\3\2\2\2\u0167K\3\2\2\2\u0168\u0169")
        buf.write("\7\f\2\2\u0169\u016a\7,\2\2\u016a\u016b\7\r\2\2\u016b")
        buf.write("\u016c\5\36\20\2\u016c\u016d\7\16\2\2\u016d\u016f\5\36")
        buf.write("\20\2\u016e\u0170\5Z.\2\u016f\u016e\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\5:\36\2\u0172")
        buf.write("M\3\2\2\2\u0173\u0174\7\17\2\2\u0174\u0175\5Z.\2\u0175")
        buf.write("O\3\2\2\2\u0176\u0177\7\20\2\2\u0177\u0178\5Z.\2\u0178")
        buf.write("Q\3\2\2\2\u0179\u017b\7\b\2\2\u017a\u017c\5\36\20\2\u017b")
        buf.write("\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\5Z.\2\u017eS\3\2\2\2\u017f\u0180\7,\2\2\u0180")
        buf.write("\u0182\7\'\2\2\u0181\u0183\5.\30\2\u0182\u0181\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\7")
        buf.write("(\2\2\u0185\u0186\5Z.\2\u0186U\3\2\2\2\u0187\u0188\7\24")
        buf.write("\2\2\u0188\u0189\5Z.\2\u0189\u018a\5X-\2\u018a\u018b\7")
        buf.write("\25\2\2\u018b\u018c\5Z.\2\u018cW\3\2\2\2\u018d\u018e\5")
        buf.write(":\36\2\u018e\u018f\5X-\2\u018f\u0192\3\2\2\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("Y\3\2\2\2\u0193\u0195\7/\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197[\3\2\2\2*_iot}\u0085\u008d\u0096\u009a\u00a8\u00ac")
        buf.write("\u00b0\u00b4\u00bb\u00c2\u00c9\u00d3\u00de\u00e9\u00ef")
        buf.write("\u00f4\u00f8\u00ff\u0106\u010f\u0116\u0121\u0126\u0133")
        buf.write("\u013f\u014b\u0155\u015c\u0162\u0166\u016f\u017b\u0182")
        buf.write("\u0191\u0196")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'", "<INVALID>", 
                     "<INVALID>", "'\r'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                      "OR", "EQUAL", "ASSIGN", "DIFF", "LT", "LTE", "GT", 
                      "GTE", "CONCAT", "COMPARE", "LP", "RP", "LSB", "RSB", 
                      "COMMA", "ID", "NUMBER_LIT", "STR_LIT", "NEWLINE", 
                      "COMMENTS", "WS", "CR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_name_of_type = 5
    RULE_name_of_type_noass = 6
    RULE_name_of_type_ass = 7
    RULE_list_size = 8
    RULE_implicit_dynamic = 9
    RULE_implicit_dynamic_noass = 10
    RULE_implicit_dynamic_ass = 11
    RULE_function = 12
    RULE_func_paralist = 13
    RULE_exp = 14
    RULE_exp0 = 15
    RULE_exp1 = 16
    RULE_exp2 = 17
    RULE_exp3 = 18
    RULE_exp4 = 19
    RULE_exp5 = 20
    RULE_exp6 = 21
    RULE_index_operators = 22
    RULE_operand = 23
    RULE_literal = 24
    RULE_arr_lit = 25
    RULE_list_exp = 26
    RULE_func_call = 27
    RULE_stmt = 28
    RULE_var_dec_stmt = 29
    RULE_assign_stmt = 30
    RULE_lhs = 31
    RULE_index_exp = 32
    RULE_if_stmt = 33
    RULE_elif_stmtlist = 34
    RULE_elif_stmt = 35
    RULE_elsestmt = 36
    RULE_for_stmt = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_func_call_stmt = 41
    RULE_block_stmt = 42
    RULE_liststmt = 43
    RULE_some_endl = 44

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "name_of_type", "name_of_type_noass", 
                   "name_of_type_ass", "list_size", "implicit_dynamic", 
                   "implicit_dynamic_noass", "implicit_dynamic_ass", "function", 
                   "func_paralist", "exp", "exp0", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "index_operators", "operand", 
                   "literal", "arr_lit", "list_exp", "func_call", "stmt", 
                   "var_dec_stmt", "assign_stmt", "lhs", "index_exp", "if_stmt", 
                   "elif_stmtlist", "elif_stmt", "elsestmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "func_call_stmt", 
                   "block_stmt", "liststmt", "some_endl" ]

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
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    NOT=25
    AND=26
    OR=27
    EQUAL=28
    ASSIGN=29
    DIFF=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    CONCAT=35
    COMPARE=36
    LP=37
    RP=38
    LSB=39
    RSB=40
    COMMA=41
    ID=42
    NUMBER_LIT=43
    STR_LIT=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    CR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
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

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 90
                self.match(ZCodeParser.NEWLINE)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.list_declared()
            self.state = 97
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.declared()
                self.state = 100
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.variables()
                self.state = 107
                self.some_endl()
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


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def name_of_type(self):
            return self.getTypedRuleContext(ZCodeParser.Name_of_typeContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.name_of_type()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.implicit_dynamic()
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


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ZCodeParser.VAR)
            self.state = 117
            self.match(ZCodeParser.ID)
            self.state = 118
            self.match(ZCodeParser.ASSIGN)
            self.state = 119
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_of_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_of_type_noass(self):
            return self.getTypedRuleContext(ZCodeParser.Name_of_type_noassContext,0)


        def name_of_type_ass(self):
            return self.getTypedRuleContext(ZCodeParser.Name_of_type_assContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_name_of_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_of_type" ):
                return visitor.visitName_of_type(self)
            else:
                return visitor.visitChildren(self)




    def name_of_type(self):

        localctx = ZCodeParser.Name_of_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_name_of_type)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.name_of_type_noass()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.name_of_type_ass()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_of_type_noassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def list_size(self):
            return self.getTypedRuleContext(ZCodeParser.List_sizeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_name_of_type_noass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_of_type_noass" ):
                return visitor.visitName_of_type_noass(self)
            else:
                return visitor.visitChildren(self)




    def name_of_type_noass(self):

        localctx = ZCodeParser.Name_of_type_noassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_name_of_type_noass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self.match(ZCodeParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 127
                self.match(ZCodeParser.LSB)
                self.state = 128
                self.list_size()
                self.state = 129
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_of_type_assContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def list_size(self):
            return self.getTypedRuleContext(ZCodeParser.List_sizeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_name_of_type_ass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_of_type_ass" ):
                return visitor.visitName_of_type_ass(self)
            else:
                return visitor.visitChildren(self)




    def name_of_type_ass(self):

        localctx = ZCodeParser.Name_of_type_assContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_name_of_type_ass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 135
                self.match(ZCodeParser.LSB)
                self.state = 136
                self.list_size()
                self.state = 137
                self.match(ZCodeParser.RSB)


            self.state = 141
            self.match(ZCodeParser.ASSIGN)
            self.state = 142
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_size(self):
            return self.getTypedRuleContext(ZCodeParser.List_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_size" ):
                return visitor.visitList_size(self)
            else:
                return visitor.visitChildren(self)




    def list_size(self):

        localctx = ZCodeParser.List_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_size)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 146
                self.match(ZCodeParser.COMMA)
                self.state = 147
                self.list_size()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_dynamic_ass(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamic_assContext,0)


        def implicit_dynamic_noass(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamic_noassContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_implicit_dynamic)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.implicit_dynamic_ass()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.implicit_dynamic_noass()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamic_noassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic_noass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic_noass" ):
                return visitor.visitImplicit_dynamic_noass(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic_noass(self):

        localctx = ZCodeParser.Implicit_dynamic_noassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_implicit_dynamic_noass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.DYNAMIC)
            self.state = 155
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamic_assContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic_ass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic_ass" ):
                return visitor.visitImplicit_dynamic_ass(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic_ass(self):

        localctx = ZCodeParser.Implicit_dynamic_assContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_implicit_dynamic_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ZCodeParser.DYNAMIC)
            self.state = 158
            self.match(ZCodeParser.ID)
            self.state = 159
            self.match(ZCodeParser.ASSIGN)
            self.state = 160
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def func_paralist(self):
            return self.getTypedRuleContext(ZCodeParser.Func_paralistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ZCodeParser.FUNC)
            self.state = 163
            self.match(ZCodeParser.ID)
            self.state = 164
            self.match(ZCodeParser.LP)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 165
                self.func_paralist()


            self.state = 168
            self.match(ZCodeParser.RP)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 169
                    self.some_endl()


                self.state = 172
                self.return_stmt()
                pass

            elif la_ == 2:
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 173
                    self.some_endl()


                self.state = 176
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 177
                self.some_endl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paralistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_of_type_noass(self):
            return self.getTypedRuleContext(ZCodeParser.Name_of_type_noassContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def func_paralist(self):
            return self.getTypedRuleContext(ZCodeParser.Func_paralistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_paralist" ):
                return visitor.visitFunc_paralist(self)
            else:
                return visitor.visitChildren(self)




    def func_paralist(self):

        localctx = ZCodeParser.Func_paralistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_paralist)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.name_of_type_noass()
                self.state = 181
                self.match(ZCodeParser.COMMA)
                self.state = 182
                self.func_paralist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.name_of_type_noass()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp0Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp0Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.exp0()

                self.state = 188
                self.match(ZCodeParser.CONCAT)
                self.state = 189
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def COMPARE(self):
            return self.getToken(ZCodeParser.COMPARE, 0)

        def DIFF(self):
            return self.getToken(ZCodeParser.DIFF, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = ZCodeParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp0)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.exp1(0)
                self.state = 195
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.DIFF) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.COMPARE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(ZCodeParser.Exp1Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 206
                    self.exp2(0) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 217
                    self.exp3(0) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 226
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 227
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 228
                    self.exp4() 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = ZCodeParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp4)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(ZCodeParser.NOT)
                self.state = 235
                self.exp4()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.exp5()
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


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp5)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(ZCodeParser.SUB)
                self.state = 240
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp6)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 244
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 245
                    self.func_call()
                    pass


                self.state = 248
                self.match(ZCodeParser.LSB)
                self.state = 249
                self.index_operators()
                self.state = 250
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_index_operators)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.exp()
                self.state = 257
                self.match(ZCodeParser.COMMA)
                self.state = 258
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operand)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(ZCodeParser.LP)
                self.state = 265
                self.exp()
                self.state = 266
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.func_call()
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

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.arr_lit()
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


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def list_exp(self):
            return self.getTypedRuleContext(ZCodeParser.List_expContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = ZCodeParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.LSB)
            self.state = 279
            self.list_exp()
            self.state = 280
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_exp(self):
            return self.getTypedRuleContext(ZCodeParser.List_expContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = ZCodeParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_exp)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.exp()
                self.state = 283
                self.match(ZCodeParser.COMMA)
                self.state = 284
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.ID)
            self.state = 290
            self.match(ZCodeParser.LP)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 291
                self.index_operators()


            self.state = 294
            self.match(ZCodeParser.RP)
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

        def var_dec_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Var_dec_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.var_dec_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 301
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 302
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 304
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_dec_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec_stmt" ):
                return visitor.visitVar_dec_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_dec_stmt(self):

        localctx = ZCodeParser.Var_dec_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_var_dec_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.variables()
            self.state = 308
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.lhs()
            self.state = 311
            self.match(ZCodeParser.ASSIGN)
            self.state = 312
            self.exp()
            self.state = 313
            self.some_endl()
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

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.index_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = ZCodeParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.ID)
            self.state = 320
            self.match(ZCodeParser.LSB)
            self.state = 321
            self.index_operators()
            self.state = 322
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtlistContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.IF)
            self.state = 325
            self.match(ZCodeParser.LP)
            self.state = 326
            self.exp()
            self.state = 327
            self.match(ZCodeParser.RP)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 328
                self.some_endl()


            self.state = 331
            self.stmt()
            self.state = 332
            self.elif_stmtlist()
            self.state = 333
            self.elsestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmtlist" ):
                return visitor.visitElif_stmtlist(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmtlist(self):

        localctx = ZCodeParser.Elif_stmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elif_stmtlist)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.elif_stmt()
                self.state = 336
                self.elif_stmtlist()
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


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.ELIF)
            self.state = 342
            self.match(ZCodeParser.LP)
            self.state = 343
            self.exp()
            self.state = 344
            self.match(ZCodeParser.RP)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 345
                self.some_endl()


            self.state = 348
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(ZCodeParser.ELSE)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 351
                    self.some_endl()


                self.state = 354
                self.stmt()
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


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.FOR)
            self.state = 359
            self.match(ZCodeParser.ID)
            self.state = 360
            self.match(ZCodeParser.UNTIL)
            self.state = 361
            self.exp()
            self.state = 362
            self.match(ZCodeParser.BY)
            self.state = 363
            self.exp()
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 364
                self.some_endl()


            self.state = 367
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(ZCodeParser.BREAK)
            self.state = 370
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(ZCodeParser.CONTINUE)
            self.state = 373
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(ZCodeParser.RETURN)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 376
                self.exp()


            self.state = 379
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def some_endl(self):
            return self.getTypedRuleContext(ZCodeParser.Some_endlContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.ID)
            self.state = 382
            self.match(ZCodeParser.LP)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 383
                self.index_operators()


            self.state = 386
            self.match(ZCodeParser.RP)
            self.state = 387
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def some_endl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Some_endlContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Some_endlContext,i)


        def liststmt(self):
            return self.getTypedRuleContext(ZCodeParser.ListstmtContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.BEGIN)
            self.state = 390
            self.some_endl()
            self.state = 391
            self.liststmt()
            self.state = 392
            self.match(ZCodeParser.END)
            self.state = 393
            self.some_endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def liststmt(self):
            return self.getTypedRuleContext(ZCodeParser.ListstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_liststmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListstmt" ):
                return visitor.visitListstmt(self)
            else:
                return visitor.visitChildren(self)




    def liststmt(self):

        localctx = ZCodeParser.ListstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_liststmt)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt()
                self.state = 396
                self.liststmt()
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


    class Some_endlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_some_endl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSome_endl" ):
                return visitor.visitSome_endl(self)
            else:
                return visitor.visitChildren(self)




    def some_endl(self):

        localctx = ZCodeParser.Some_endlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_some_endl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 401
                self.match(ZCodeParser.NEWLINE)
                self.state = 404 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

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
        self._predicates[16] = self.exp1_sempred
        self._predicates[17] = self.exp2_sempred
        self._predicates[18] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




