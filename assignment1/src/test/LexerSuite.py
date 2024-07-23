import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("277.548e65", "277.548e65,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("76E-85", "76E-85,<EOF>", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''## 6(7}Yo(<`zJUe_j''', '''<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("3.056E44", "3.056E44,<EOF>", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''";'"'"'"'" ''', '''Unclosed String: ;'"'"'"'" ''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("860", "860,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("U&RF4Hba", "U,Error Token &", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''"'"'"&"''', '''\'"'"&,<EOF>''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("36E-36", "36E-36,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''## g,7u7k_hOvr6X9:=''', '''<EOF>''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test('''## 2061D''', '''<EOF>''', 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("0.686", "0.686,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''"'"'"\\s:b"''', '''Illegal Escape In String: '"'"\\s''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''## sv+qY(/-r:{3Kn''', '''<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''## xzGs1N''', '''<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''";"''', ''';,<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''## G''', '''<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''## h};-?(bO1:{{''', '''<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("7.598", "7.598,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''"\\x'""''', '''Illegal Escape In String: \\x''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("L1lJ^WhMS", "L1lJ,Error Token ^", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''"D
(+='""''', '''Unclosed String: D''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test('''## "K''', '''<EOF>''', 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"'"6
k"''', '''Unclosed String: '"6''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("7.907e-89", "7.907e-89,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("7.054", "7.054,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## %m-6@=CCH{6MXYUIvZ''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''## SJ/IDB9"#jP_*1''', '''<EOF>''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''"\\c'"#b'""''', '''Illegal Escape In String: \\c''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test("555e77", "555e77,<EOF>", 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("YBEW", "YBEW,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("910", "910,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''"(K
Q"''', '''Unclosed String: (K''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''## 2C}6L5}lu~x}FpO*''', '''<EOF>''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''"lL"''', '''lL,<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("184.787e+16", "184.787e+16,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("1.302", "1.302,<EOF>", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"
]"''', '''Unclosed String: ''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''## |0~S#mE~f.D<''', '''<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test('''## w]}[.*!s1i"9Z5AX''', '''<EOF>''', 145))

	def test_146(self):
		self.assertTrue(TestLexer.test('''"T'"'" ''', '''Unclosed String: T'"'" ''', 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("5.112", "5.112,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("3.888", "3.888,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("lYI@uItg", "lYI,Error Token @", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("O5b7Oi", "O5b7Oi,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''## KT9mqpl''', '''<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''## [''', '''<EOF>''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''## 9d;EdLn&U^%JcQZEO''', '''<EOF>''', 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''## h7vcg''', '''<EOF>''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''"?\\xE"''', '''Illegal Escape In String: ?\\x''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''## ${Cc<6Cm''', '''<EOF>''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''## U"uo}74N8Dzt''', '''<EOF>''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("74.728E+18", "74.728E+18,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## |%#oE^:c$X}3{ty0Hbg''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("8E", "8,E,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''"'"
s'""''', '''Unclosed String: '"''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("CaYX9Om^bc", "CaYX9Om,Error Token ^", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("E88vI0i", "E88vI0i,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("gQ", "gQ,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("AJvGc", "AJvGc,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("367.344e+44", "367.344e+44,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''"mY ''', '''Unclosed String: mY ''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''## o0qa2v.^<a90uzs=+''', '''<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("#", "Error Token #", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''## Ub7*''', '''<EOF>''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("aO#AT", "aO,Error Token #", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("vZ@j7B", "vZ,Error Token @", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("9.421", "9.421,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("967", "967,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test('''## 8Z p~qTCH}K''', '''<EOF>''', 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''## ;S[''', '''<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''"'"\\oV>'""''', '''Illegal Escape In String: '"\\o''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''## 8Fc`h*)eY:rVl]u*''', '''<EOF>''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## f`]<5bE9[}V]c[ZhVa''', '''<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''"'"'"'"2"''', '''\'"'"'"2,<EOF>''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"'"d@]"''', '''\'"d@],<EOF>''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("MtyKSWd4fV", "MtyKSWd4fV,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test("Z8rDeTc", "Z8rDeTc,<EOF>", 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''## "''', '''<EOF>''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''"l'"'"'""''', '''l'"'"'",<EOF>''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("255.894", "255.894,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("36.399", "36.399,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''## W?f2''', '''<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## Fp<.''', '''<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("L9v4r", "L9v4r,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''"'"."''', '''\'".,<EOF>''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''"'"'"\\a'""''', '''Illegal Escape In String: '"'"\\a''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("L6", "L6,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("62.475E-07", "62.475E-07,<EOF>", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test('''"
K"''', '''Unclosed String: ''', 200))