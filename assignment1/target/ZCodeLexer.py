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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\5\2z\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\7,\u011f\n,\f,\16,\u0122\13,\3-\6")
        buf.write("-\u0125\n-\r-\16-\u0126\3.\3.\7.\u012b\n.\f.\16.\u012e")
        buf.write("\13.\3/\3/\5/\u0132\n/\3/\6/\u0135\n/\r/\16/\u0136\3\60")
        buf.write("\3\60\5\60\u013b\n\60\3\60\5\60\u013e\n\60\3\61\3\61\3")
        buf.write("\61\3\61\5\61\u0144\n\61\3\62\3\62\3\62\3\63\3\63\7\63")
        buf.write("\u014b\n\63\f\63\16\63\u014e\13\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c")
        buf.write("\13\65\3\65\3\65\3\66\6\66\u0161\n\66\r\66\16\66\u0162")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\78\u016d\n8\f8\16")
        buf.write("8\u0170\138\38\38\38\58\u0175\n8\38\38\39\39\39\3:\3:")
        buf.write("\7:\u017e\n:\f:\16:\u0181\13:\3:\3:\3:\3;\3;\3;\2\2<\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y\2[\2]\2_.a\2c\2e/g\60i\61k\62m\63o\64q\2s\65u")
        buf.write("\66\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv\4\2\f\f\16")
        buf.write("\17\5\2\n\13\16\16\"\"\3\3\f\f\2\u0191\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\3y\3\2\2\2\5{\3\2\2\2\7\u0080\3\2\2\2\t\u0086\3\2\2")
        buf.write("\2\13\u008d\3\2\2\2\r\u0092\3\2\2\2\17\u0099\3\2\2\2\21")
        buf.write("\u00a0\3\2\2\2\23\u00a4\3\2\2\2\25\u00ac\3\2\2\2\27\u00b1")
        buf.write("\3\2\2\2\31\u00b5\3\2\2\2\33\u00bb\3\2\2\2\35\u00be\3")
        buf.write("\2\2\2\37\u00c4\3\2\2\2!\u00cd\3\2\2\2#\u00d0\3\2\2\2")
        buf.write("%\u00d5\3\2\2\2\'\u00da\3\2\2\2)\u00e0\3\2\2\2+\u00e4")
        buf.write("\3\2\2\2-\u00e6\3\2\2\2/\u00e8\3\2\2\2\61\u00ea\3\2\2")
        buf.write("\2\63\u00ec\3\2\2\2\65\u00ee\3\2\2\2\67\u00f2\3\2\2\2")
        buf.write("9\u00f6\3\2\2\2;\u00f9\3\2\2\2=\u00fb\3\2\2\2?\u00fe\3")
        buf.write("\2\2\2A\u0101\3\2\2\2C\u0103\3\2\2\2E\u0106\3\2\2\2G\u0108")
        buf.write("\3\2\2\2I\u010b\3\2\2\2K\u010f\3\2\2\2M\u0112\3\2\2\2")
        buf.write("O\u0114\3\2\2\2Q\u0116\3\2\2\2S\u0118\3\2\2\2U\u011a\3")
        buf.write("\2\2\2W\u011c\3\2\2\2Y\u0124\3\2\2\2[\u0128\3\2\2\2]\u012f")
        buf.write("\3\2\2\2_\u0138\3\2\2\2a\u0143\3\2\2\2c\u0145\3\2\2\2")
        buf.write("e\u0148\3\2\2\2g\u0152\3\2\2\2i\u0154\3\2\2\2k\u0160\3")
        buf.write("\2\2\2m\u0166\3\2\2\2o\u016a\3\2\2\2q\u0178\3\2\2\2s\u017b")
        buf.write("\3\2\2\2u\u0185\3\2\2\2wz\5\5\3\2xz\5\7\4\2yw\3\2\2\2")
        buf.write("yx\3\2\2\2z\4\3\2\2\2{|\7v\2\2|}\7t\2\2}~\7w\2\2~\177")
        buf.write("\7g\2\2\177\6\3\2\2\2\u0080\u0081\7h\2\2\u0081\u0082\7")
        buf.write("c\2\2\u0082\u0083\7n\2\2\u0083\u0084\7u\2\2\u0084\u0085")
        buf.write("\7g\2\2\u0085\b\3\2\2\2\u0086\u0087\7p\2\2\u0087\u0088")
        buf.write("\7w\2\2\u0088\u0089\7o\2\2\u0089\u008a\7d\2\2\u008a\u008b")
        buf.write("\7g\2\2\u008b\u008c\7t\2\2\u008c\n\3\2\2\2\u008d\u008e")
        buf.write("\7d\2\2\u008e\u008f\7q\2\2\u008f\u0090\7q\2\2\u0090\u0091")
        buf.write("\7n\2\2\u0091\f\3\2\2\2\u0092\u0093\7u\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7t\2\2\u0095\u0096\7k\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\u0098\7i\2\2\u0098\16\3\2\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7g\2\2\u009b\u009c\7v\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7t\2\2\u009e\u009f\7p\2\2\u009f\20")
        buf.write("\3\2\2\2\u00a0\u00a1\7x\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\22\3\2\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6")
        buf.write("\7{\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9")
        buf.write("\7o\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7e\2\2\u00ab\24")
        buf.write("\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7e\2\2\u00b0\26\3\2\2\2\u00b1\u00b2")
        buf.write("\7h\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7t\2\2\u00b4\30")
        buf.write("\3\2\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7n\2\2\u00ba\32")
        buf.write("\3\2\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd\7{\2\2\u00bd\34")
        buf.write("\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\36")
        buf.write("\3\2\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7g\2\2\u00cc \3")
        buf.write("\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf\"\3")
        buf.write("\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7g\2\2\u00d4$\3\2\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9&\3\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7i\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df(\3\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7f\2\2\u00e3*\3\2\2\2\u00e4\u00e5")
        buf.write("\7-\2\2\u00e5,\3\2\2\2\u00e6\u00e7\7/\2\2\u00e7.\3\2\2")
        buf.write("\2\u00e8\u00e9\7,\2\2\u00e9\60\3\2\2\2\u00ea\u00eb\7\61")
        buf.write("\2\2\u00eb\62\3\2\2\2\u00ec\u00ed\7\'\2\2\u00ed\64\3\2")
        buf.write("\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\66\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7f\2\2\u00f58\3\2\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7t\2\2\u00f8:\3\2\2\2\u00f9\u00fa")
        buf.write("\7?\2\2\u00fa<\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc\u00fd")
        buf.write("\7/\2\2\u00fd>\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100@\3\2\2\2\u0101\u0102\7>\2\2\u0102B\3\2\2")
        buf.write("\2\u0103\u0104\7>\2\2\u0104\u0105\7?\2\2\u0105D\3\2\2")
        buf.write("\2\u0106\u0107\7@\2\2\u0107F\3\2\2\2\u0108\u0109\7@\2")
        buf.write("\2\u0109\u010a\7?\2\2\u010aH\3\2\2\2\u010b\u010c\7\60")
        buf.write("\2\2\u010c\u010d\7\60\2\2\u010d\u010e\7\60\2\2\u010eJ")
        buf.write("\3\2\2\2\u010f\u0110\7?\2\2\u0110\u0111\7?\2\2\u0111L")
        buf.write("\3\2\2\2\u0112\u0113\7*\2\2\u0113N\3\2\2\2\u0114\u0115")
        buf.write("\7+\2\2\u0115P\3\2\2\2\u0116\u0117\7]\2\2\u0117R\3\2\2")
        buf.write("\2\u0118\u0119\7_\2\2\u0119T\3\2\2\2\u011a\u011b\7.\2")
        buf.write("\2\u011bV\3\2\2\2\u011c\u0120\t\2\2\2\u011d\u011f\t\3")
        buf.write("\2\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121X\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0123\u0125\t\4\2\2\u0124\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127Z\3\2\2\2\u0128\u012c\7\60\2\2\u0129\u012b\t\4\2")
        buf.write("\2\u012a\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\\\3\2\2\2\u012e\u012c")
        buf.write("\3\2\2\2\u012f\u0131\t\5\2\2\u0130\u0132\t\6\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u0135\t\4\2\2\u0134\u0133\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137^")
        buf.write("\3\2\2\2\u0138\u013a\5Y-\2\u0139\u013b\5[.\2\u013a\u0139")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c")
        buf.write("\u013e\5]/\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("`\3\2\2\2\u013f\u0144\n\7\2\2\u0140\u0144\5c\62\2\u0141")
        buf.write("\u0142\7)\2\2\u0142\u0144\7$\2\2\u0143\u013f\3\2\2\2\u0143")
        buf.write("\u0140\3\2\2\2\u0143\u0141\3\2\2\2\u0144b\3\2\2\2\u0145")
        buf.write("\u0146\7^\2\2\u0146\u0147\t\b\2\2\u0147d\3\2\2\2\u0148")
        buf.write("\u014c\7$\2\2\u0149\u014b\5a\61\2\u014a\u0149\3\2\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150")
        buf.write("\7$\2\2\u0150\u0151\b\63\2\2\u0151f\3\2\2\2\u0152\u0153")
        buf.write("\7\f\2\2\u0153h\3\2\2\2\u0154\u0155\7%\2\2\u0155\u0156")
        buf.write("\7%\2\2\u0156\u015a\3\2\2\2\u0157\u0159\n\t\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015a\3")
        buf.write("\2\2\2\u015d\u015e\b\65\3\2\u015ej\3\2\2\2\u015f\u0161")
        buf.write("\t\n\2\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0165\b\66\3\2\u0165l\3\2\2\2\u0166\u0167\7\17")
        buf.write("\2\2\u0167\u0168\3\2\2\2\u0168\u0169\b\67\3\2\u0169n\3")
        buf.write("\2\2\2\u016a\u016e\7$\2\2\u016b\u016d\5a\61\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0174\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0171\u0175\t\13\2\2\u0172\u0173\7\17\2\2\u0173\u0175")
        buf.write("\7\f\2\2\u0174\u0171\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0177\b8\4\2\u0177p\3\2\2\2\u0178")
        buf.write("\u0179\7^\2\2\u0179\u017a\n\b\2\2\u017ar\3\2\2\2\u017b")
        buf.write("\u017f\7$\2\2\u017c\u017e\5a\61\2\u017d\u017c\3\2\2\2")
        buf.write("\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183")
        buf.write("\5q9\2\u0183\u0184\b:\5\2\u0184t\3\2\2\2\u0185\u0186\13")
        buf.write("\2\2\2\u0186\u0187\b;\6\2\u0187v\3\2\2\2\22\2y\u0120\u0126")
        buf.write("\u012c\u0131\u0136\u013a\u013d\u0143\u014c\u015a\u0162")
        buf.write("\u016e\u0174\u017f\7\3\63\2\b\2\2\38\3\3:\4\3;\5")
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
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    NOT = 26
    AND = 27
    OR = 28
    EQUAL = 29
    ASSIGN = 30
    DIFF = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    CONCAT = 36
    COMPARE = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    COMMA = 42
    ID = 43
    NUMBER_LIT = 44
    STR_LIT = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    CR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
            "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'", 
            "'\r'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "DIFF", "LT", 
            "LTE", "GT", "GTE", "CONCAT", "COMPARE", "LP", "RP", "LSB", 
            "RSB", "COMMA", "ID", "NUMBER_LIT", "STR_LIT", "NEWLINE", "COMMENTS", 
            "WS", "CR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOL_LIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "DIFF", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "COMPARE", "LP", "RP", "LSB", "RSB", "COMMA", "ID", "INTERGER", 
                  "DECIMAL", "EXPONENT", "NUMBER_LIT", "STR_CHAR", "ESC_SEQ", 
                  "STR_LIT", "NEWLINE", "COMMENTS", "WS", "CR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESC", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[49] = self.STR_LIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            if self.text[-1] == '\n':
            	if self.text[-2] == '\r':
            		raise UncloseString(self.text[1:-2]);
            	else:
            		raise UncloseString(self.text[1:-1]);
            else:
            	raise UncloseString(self.text[1:]);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


