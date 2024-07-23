import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
func gp ()	return - (- vX())

func wA0b ()	begin
		continue
		if (- "U") return true
		elif ("MMScz")
		var vj <- 55.05
		elif (false) if (87.18) thHT <- 22.17
		elif (46.55) for UC until 75.16 by true
			string oBD[70.12,6.46,14.4]
		else ifu <- Hqpk
		elif ("D") for W6_n until "Tyi" by false
			continue
		if (SY) return
		elif ("L") ATrn()
		elif (66.95)
		if (true) if (9.73) bool drCu <- 3.91
		elif (xml)
		break
		elif (false)
		U7J0()
		elif (30.21)
		A8 <- 40.51
		elif (91.21)
		if (HQ2)
		number gW[49.89,78.69] <- "uwZw"
		elif (36.48) if (x5)
		for Sj until false by "cNtm"
			continue
		elif ("sc")
		break
		elif (39.9)
		xco0(false, sCs9, rYiY)
		else Uf3(true)
		elif (true)
		for gNO until "GO" by true
			break
		elif ("QO") fO(BL3F, "Rfak")
		elif (true) for A3VK until true by true
			if (94.02)
			continue
			elif (rZ) for AA until true by "gzQ"
				bool D4cd
			elif (tb6)
			begin
				rA <- "gGtqk"
				qoMS(71.79, 65.76, true)
			end
			elif (true) break
			elif (M4m) for G_B_ until "pYU" by ja6
				begin
					continue
					bcQ8[aeR, 25.05] <- false
					begin
						Mxv6("no", 57.82, true)
					end
				end
			elif (7.11) break
		elif (24.9)
		break
		elif ("GtPT") return "JsnJz"
		else return true
		elif (true) continue
		else begin
		end
		elif (false) qv(s0x9, "c", "KzY")
		elif (40.4) break
		elif (false) g2["IokRm"] <- jJyB
	end

bool A51[81.2,89.8]
func gr ()
	return
func Puil (number BaU)
	begin
		begin
			break
		end
		begin
		end
		return 55.74
	end
'''
		expect = '''Program([FuncDecl(Id(gp), [], Return(UnaryOp(-, UnaryOp(-, CallExpr(Id(vX), []))))), FuncDecl(Id(wA0b), [], Block([Continue, If((UnaryOp(-, StringLit(U)), Return(BooleanLit(True))), [(StringLit(MMScz), VarDecl(Id(vj), None, var, NumLit(55.05))), (BooleanLit(False), If((NumLit(87.18), AssignStmt(Id(thHT), NumLit(22.17))), [(NumLit(46.55), For(Id(UC), NumLit(75.16), BooleanLit(True), VarDecl(Id(oBD), ArrayType([70.12, 6.46, 14.4], StringType), None, None)))], AssignStmt(Id(ifu), Id(Hqpk)))), (StringLit(D), For(Id(W6_n), StringLit(Tyi), BooleanLit(False), Continue))], None), If((Id(SY), Return()), [(StringLit(L), CallStmt(Id(ATrn), [])), (NumLit(66.95), If((BooleanLit(True), If((NumLit(9.73), VarDecl(Id(drCu), BoolType, None, NumLit(3.91))), [(Id(xml), Break), (BooleanLit(False), CallStmt(Id(U7J0), [])), (NumLit(30.21), AssignStmt(Id(A8), NumLit(40.51))), (NumLit(91.21), If((Id(HQ2), VarDecl(Id(gW), ArrayType([49.89, 78.69], NumberType), None, StringLit(uwZw))), [(NumLit(36.48), If((Id(x5), For(Id(Sj), BooleanLit(False), StringLit(cNtm), Continue)), [(StringLit(sc), Break), (NumLit(39.9), CallStmt(Id(xco0), [BooleanLit(False), Id(sCs9), Id(rYiY)]))], CallStmt(Id(Uf3), [BooleanLit(True)]))), (BooleanLit(True), For(Id(gNO), StringLit(GO), BooleanLit(True), Break)), (StringLit(QO), CallStmt(Id(fO), [Id(BL3F), StringLit(Rfak)])), (BooleanLit(True), For(Id(A3VK), BooleanLit(True), BooleanLit(True), If((NumLit(94.02), Continue), [(Id(rZ), For(Id(AA), BooleanLit(True), StringLit(gzQ), VarDecl(Id(D4cd), BoolType, None, None))), (Id(tb6), Block([AssignStmt(Id(rA), StringLit(gGtqk)), CallStmt(Id(qoMS), [NumLit(71.79), NumLit(65.76), BooleanLit(True)])])), (BooleanLit(True), Break), (Id(M4m), For(Id(G_B_), StringLit(pYU), Id(ja6), Block([Continue, AssignStmt(ArrayCell(Id(bcQ8), [Id(aeR), NumLit(25.05)]), BooleanLit(False)), Block([CallStmt(Id(Mxv6), [StringLit(no), NumLit(57.82), BooleanLit(True)])])]))), (NumLit(7.11), Break), (NumLit(24.9), Break), (StringLit(GtPT), Return(StringLit(JsnJz)))], Return(BooleanLit(True))))), (BooleanLit(True), Continue)], Block([]))), (BooleanLit(False), CallStmt(Id(qv), [Id(s0x9), StringLit(c), StringLit(KzY)])), (NumLit(40.4), Break), (BooleanLit(False), AssignStmt(ArrayCell(Id(g2), [StringLit(IokRm)]), Id(jJyB)))], None)), [], None))], None)])), VarDecl(Id(A51), ArrayType([81.2, 89.8], BoolType), None, None), FuncDecl(Id(gr), [], Return()), FuncDecl(Id(Puil), [VarDecl(Id(BaU), NumberType, None, None)], Block([Block([Break]), Block([]), Return(NumLit(55.74))]))])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
func y0 (number CN)
	return S3Il
string du[53.22,93.37] <- true
func awfc (string Pb1Q)	begin
		for khl until "XY" by false
			return
		cJYX(zMe)
	end
string AUN[59.92,42.68]
'''
		expect = '''Program([FuncDecl(Id(y0), [VarDecl(Id(CN), NumberType, None, None)], Return(Id(S3Il))), VarDecl(Id(du), ArrayType([53.22, 93.37], StringType), None, BooleanLit(True)), FuncDecl(Id(awfc), [VarDecl(Id(Pb1Q), StringType, None, None)], Block([For(Id(khl), StringLit(XY), BooleanLit(False), Return()), CallStmt(Id(cJYX), [Id(zMe)])])), VarDecl(Id(AUN), ArrayType([59.92, 42.68], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
string xt_
string QH2N <- true
var cOk5 <- 95.74
dynamic qbny
func mf ()
	return "rbaNF"

'''
		expect = '''Program([VarDecl(Id(xt_), StringType, None, None), VarDecl(Id(QH2N), StringType, None, BooleanLit(True)), VarDecl(Id(cOk5), None, var, NumLit(95.74)), VarDecl(Id(qbny), None, dynamic, None), FuncDecl(Id(mf), [], Return(StringLit(rbaNF)))])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
bool OA <- false
func la (string gl)	return
string VPn
func q5 (string Ok[84.33,39.29], bool sBm)	return true

'''
		expect = '''Program([VarDecl(Id(OA), BoolType, None, BooleanLit(False)), FuncDecl(Id(la), [VarDecl(Id(gl), StringType, None, None)], Return()), VarDecl(Id(VPn), StringType, None, None), FuncDecl(Id(q5), [VarDecl(Id(Ok), ArrayType([84.33, 39.29], StringType), None, None), VarDecl(Id(sBm), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
bool D2vI[10.25,15.69] <- false
func tda (bool iK, bool pQ, bool HX3)	return

'''
		expect = '''Program([VarDecl(Id(D2vI), ArrayType([10.25, 15.69], BoolType), None, BooleanLit(False)), FuncDecl(Id(tda), [VarDecl(Id(iK), BoolType, None, None), VarDecl(Id(pQ), BoolType, None, None), VarDecl(Id(HX3), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
bool eV <- 4.56
'''
		expect = '''Program([VarDecl(Id(eV), BoolType, None, NumLit(4.56))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
bool o9[82.35,54.7,80.73]
string PC1[41.51,72.53] <- "gsmgY"
'''
		expect = '''Program([VarDecl(Id(o9), ArrayType([82.35, 54.7, 80.73], BoolType), None, None), VarDecl(Id(PC1), ArrayType([41.51, 72.53], StringType), None, StringLit(gsmgY))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
string lGuw
func NFB ()	begin
		continue
		for tDfl until kr by GT5
			QxW <- "mCxK"
		for Jj until false by "AOd"
			continue
	end

string T2 <- "bd"
bool Ov_o <- iFF
number lH[5.39,13.03] <- "j"
'''
		expect = '''Program([VarDecl(Id(lGuw), StringType, None, None), FuncDecl(Id(NFB), [], Block([Continue, For(Id(tDfl), Id(kr), Id(GT5), AssignStmt(Id(QxW), StringLit(mCxK))), For(Id(Jj), BooleanLit(False), StringLit(AOd), Continue)])), VarDecl(Id(T2), StringType, None, StringLit(bd)), VarDecl(Id(Ov_o), BoolType, None, Id(iFF)), VarDecl(Id(lH), ArrayType([5.39, 13.03], NumberType), None, StringLit(j))])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
func YUw (number m9F[71.28,95.81], number LaH)
	return oKe

var m1 <- true
number T_br <- "IOcBD"
var v5D <- "iSXn"
func Qadg (number Ba[55.18,28.64], bool bulk[96.55,96.75])	return
'''
		expect = '''Program([FuncDecl(Id(YUw), [VarDecl(Id(m9F), ArrayType([71.28, 95.81], NumberType), None, None), VarDecl(Id(LaH), NumberType, None, None)], Return(Id(oKe))), VarDecl(Id(m1), None, var, BooleanLit(True)), VarDecl(Id(T_br), NumberType, None, StringLit(IOcBD)), VarDecl(Id(v5D), None, var, StringLit(iSXn)), FuncDecl(Id(Qadg), [VarDecl(Id(Ba), ArrayType([55.18, 28.64], NumberType), None, None), VarDecl(Id(bulk), ArrayType([96.55, 96.75], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
func ugYK (string dGc[60.26,39.28], number g3Q[96.21,65.34,29.67], number Iy7[13.99,18.33,93.08])
	return
number Sp2 <- 17.36
func L7t ()
	return
bool nY2
dynamic rQ
'''
		expect = '''Program([FuncDecl(Id(ugYK), [VarDecl(Id(dGc), ArrayType([60.26, 39.28], StringType), None, None), VarDecl(Id(g3Q), ArrayType([96.21, 65.34, 29.67], NumberType), None, None), VarDecl(Id(Iy7), ArrayType([13.99, 18.33, 93.08], NumberType), None, None)], Return()), VarDecl(Id(Sp2), NumberType, None, NumLit(17.36)), FuncDecl(Id(L7t), [], Return()), VarDecl(Id(nY2), BoolType, None, None), VarDecl(Id(rQ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
func hacm (number jfwc[67.43,89.64,73.32], number rzQW[31.8,35.35], string UX)	return

func PTTG ()	return "WtX"
'''
		expect = '''Program([FuncDecl(Id(hacm), [VarDecl(Id(jfwc), ArrayType([67.43, 89.64, 73.32], NumberType), None, None), VarDecl(Id(rzQW), ArrayType([31.8, 35.35], NumberType), None, None), VarDecl(Id(UX), StringType, None, None)], Return()), FuncDecl(Id(PTTG), [], Return(StringLit(WtX)))])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
func eF7V (string zZE)
	return

'''
		expect = '''Program([FuncDecl(Id(eF7V), [VarDecl(Id(zZE), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
number KGrC[18.56,6.01,86.9]
'''
		expect = '''Program([VarDecl(Id(KGrC), ArrayType([18.56, 6.01, 86.9], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
string RdP[59.24,10.42,81.82]
number QsFv <- 64.97
bool X9OC <- 86.16
string LEC
'''
		expect = '''Program([VarDecl(Id(RdP), ArrayType([59.24, 10.42, 81.82], StringType), None, None), VarDecl(Id(QsFv), NumberType, None, NumLit(64.97)), VarDecl(Id(X9OC), BoolType, None, NumLit(86.16)), VarDecl(Id(LEC), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
number jVlk[22.36,75.74] <- G8Zy
'''
		expect = '''Program([VarDecl(Id(jVlk), ArrayType([22.36, 75.74], NumberType), None, Id(G8Zy))])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = '''
string T3Z <- hN
func ZRTk ()	begin
		continue
		qz("ZZVR")
		continue
	end

func LL6 (bool dDs, number OJE[59.57])	begin
	end
bool I7 <- "fnv"
bool x70s[14.88,7.23] <- lhpx
'''
		expect = '''Program([VarDecl(Id(T3Z), StringType, None, Id(hN)), FuncDecl(Id(ZRTk), [], Block([Continue, CallStmt(Id(qz), [StringLit(ZZVR)]), Continue])), FuncDecl(Id(LL6), [VarDecl(Id(dDs), BoolType, None, None), VarDecl(Id(OJE), ArrayType([59.57], NumberType), None, None)], Block([])), VarDecl(Id(I7), BoolType, None, StringLit(fnv)), VarDecl(Id(x70s), ArrayType([14.88, 7.23], BoolType), None, Id(lhpx))])'''
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = '''
func vNe (string KVv4[92.97,49.5], bool uo)
	begin
		return
	end

'''
		expect = '''Program([FuncDecl(Id(vNe), [VarDecl(Id(KVv4), ArrayType([92.97, 49.5], StringType), None, None), VarDecl(Id(uo), BoolType, None, None)], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
func Gug (string nwF[66.07,54.91,16.18], bool IsOH, bool Ryo6)	return "DnF"

func xh (string YU)
	return true

func Umx (bool an_[3.43,75.41], number KL, string Exl[92.8])	return true

bool SAf[97.84,25.75] <- false
func g0 (bool Sc8[38.98,11.04], bool w3[97.1,87.44,46.44], string I5Y[18.36,40.24,44.03])	return false
'''
		expect = '''Program([FuncDecl(Id(Gug), [VarDecl(Id(nwF), ArrayType([66.07, 54.91, 16.18], StringType), None, None), VarDecl(Id(IsOH), BoolType, None, None), VarDecl(Id(Ryo6), BoolType, None, None)], Return(StringLit(DnF))), FuncDecl(Id(xh), [VarDecl(Id(YU), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(Umx), [VarDecl(Id(an_), ArrayType([3.43, 75.41], BoolType), None, None), VarDecl(Id(KL), NumberType, None, None), VarDecl(Id(Exl), ArrayType([92.8], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(SAf), ArrayType([97.84, 25.75], BoolType), None, BooleanLit(False)), FuncDecl(Id(g0), [VarDecl(Id(Sc8), ArrayType([38.98, 11.04], BoolType), None, None), VarDecl(Id(w3), ArrayType([97.1, 87.44, 46.44], BoolType), None, None), VarDecl(Id(I5Y), ArrayType([18.36, 40.24, 44.03], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
number lo[89.27,56.69] <- raT
number PzN[29.58] <- 48.75
string Liu[70.65,3.41,72.47]
string Ru <- 31.85
'''
		expect = '''Program([VarDecl(Id(lo), ArrayType([89.27, 56.69], NumberType), None, Id(raT)), VarDecl(Id(PzN), ArrayType([29.58], NumberType), None, NumLit(48.75)), VarDecl(Id(Liu), ArrayType([70.65, 3.41, 72.47], StringType), None, None), VarDecl(Id(Ru), StringType, None, NumLit(31.85))])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
bool Go50[33.28] <- 47.87
func dqN ()	begin
		continue
		d7g["Xbzxw", 42.7] <- alD
		return "U"
	end

func xS ()
	return fYL
'''
		expect = '''Program([VarDecl(Id(Go50), ArrayType([33.28], BoolType), None, NumLit(47.87)), FuncDecl(Id(dqN), [], Block([Continue, AssignStmt(ArrayCell(Id(d7g), [StringLit(Xbzxw), NumLit(42.7)]), Id(alD)), Return(StringLit(U))])), FuncDecl(Id(xS), [], Return(Id(fYL)))])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
func ZA (number WL, string d7[59.37,0.58,65.69])	begin
	end

bool mLK[39.29,85.58] <- Lp
func vkA (string XJw[45.13,89.32])	begin
		if (32.92) cwwH(wL)
		string AAwN <- true
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(ZA), [VarDecl(Id(WL), NumberType, None, None), VarDecl(Id(d7), ArrayType([59.37, 0.58, 65.69], StringType), None, None)], Block([])), VarDecl(Id(mLK), ArrayType([39.29, 85.58], BoolType), None, Id(Lp)), FuncDecl(Id(vkA), [VarDecl(Id(XJw), ArrayType([45.13, 89.32], StringType), None, None)], Block([If((NumLit(32.92), CallStmt(Id(cwwH), [Id(wL)])), [], None), VarDecl(Id(AAwN), StringType, None, BooleanLit(True)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''
bool qCEh[56.25,75.75,40.66] <- 11.44
'''
		expect = '''Program([VarDecl(Id(qCEh), ArrayType([56.25, 75.75, 40.66], BoolType), None, NumLit(11.44))])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
number rdiT[62.32,54.71,49.88] <- YeAV
func igRG (string wuJ[92.38,95.23], number ooUp[98.9])	return ZT
func QWh (string R9wB[29.22], number BL)	return "I"

'''
		expect = '''Program([VarDecl(Id(rdiT), ArrayType([62.32, 54.71, 49.88], NumberType), None, Id(YeAV)), FuncDecl(Id(igRG), [VarDecl(Id(wuJ), ArrayType([92.38, 95.23], StringType), None, None), VarDecl(Id(ooUp), ArrayType([98.9], NumberType), None, None)], Return(Id(ZT))), FuncDecl(Id(QWh), [VarDecl(Id(R9wB), ArrayType([29.22], StringType), None, None), VarDecl(Id(BL), NumberType, None, None)], Return(StringLit(I)))])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
func th (string HjjL[75.35], bool PPh[56.62,19.57], string VAMJ[91.8,67.9])
	begin
		for r3Tx until 85.56 by "uqqIl"
			continue
		begin
		end
	end
string ri
func oXi (number Ih2)	return 78.66
func GB (string U5_d, bool PoC)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(th), [VarDecl(Id(HjjL), ArrayType([75.35], StringType), None, None), VarDecl(Id(PPh), ArrayType([56.62, 19.57], BoolType), None, None), VarDecl(Id(VAMJ), ArrayType([91.8, 67.9], StringType), None, None)], Block([For(Id(r3Tx), NumLit(85.56), StringLit(uqqIl), Continue), Block([])])), VarDecl(Id(ri), StringType, None, None), FuncDecl(Id(oXi), [VarDecl(Id(Ih2), NumberType, None, None)], Return(NumLit(78.66))), FuncDecl(Id(GB), [VarDecl(Id(U5_d), StringType, None, None), VarDecl(Id(PoC), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
string uHh7 <- 87.98
func PS8 (bool f2)	return

'''
		expect = '''Program([VarDecl(Id(uHh7), StringType, None, NumLit(87.98)), FuncDecl(Id(PS8), [VarDecl(Id(f2), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
func Mnp3 ()
	return R1w

dynamic Uj <- false
func kGmg (bool xX[36.91,93.5], string wI)
	begin
		IEO()
		continue
		for dHT until "p" by "Z"
			dA[zw, Yit, true] <- RzoN
	end
'''
		expect = '''Program([FuncDecl(Id(Mnp3), [], Return(Id(R1w))), VarDecl(Id(Uj), None, dynamic, BooleanLit(False)), FuncDecl(Id(kGmg), [VarDecl(Id(xX), ArrayType([36.91, 93.5], BoolType), None, None), VarDecl(Id(wI), StringType, None, None)], Block([CallStmt(Id(IEO), []), Continue, For(Id(dHT), StringLit(p), StringLit(Z), AssignStmt(ArrayCell(Id(dA), [Id(zw), Id(Yit), BooleanLit(True)]), Id(RzoN)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
func dEG (bool TI[69.92], string zcsJ)
	begin
		for kl until 93.13 by 38.08
			string LjBs[66.16]
		if (false)
		return
		elif (false) bool WQL[39.72,30.83] <- 1.5
		elif (false) mg8("SuEhG", liw)
		elif ("pMrU") begin
		end
		elif ("Lw")
		r7(false)
		if (false)
		begin
			r4In <- 53.02
		end
		elif ("Ycw") if (false)
		return false
		else string lus[2.83]
		elif (false)
		ayK(34.41)
	end

'''
		expect = '''Program([FuncDecl(Id(dEG), [VarDecl(Id(TI), ArrayType([69.92], BoolType), None, None), VarDecl(Id(zcsJ), StringType, None, None)], Block([For(Id(kl), NumLit(93.13), NumLit(38.08), VarDecl(Id(LjBs), ArrayType([66.16], StringType), None, None)), If((BooleanLit(False), Return()), [(BooleanLit(False), VarDecl(Id(WQL), ArrayType([39.72, 30.83], BoolType), None, NumLit(1.5))), (BooleanLit(False), CallStmt(Id(mg8), [StringLit(SuEhG), Id(liw)])), (StringLit(pMrU), Block([])), (StringLit(Lw), CallStmt(Id(r7), [BooleanLit(False)]))], None), If((BooleanLit(False), Block([AssignStmt(Id(r4In), NumLit(53.02))])), [(StringLit(Ycw), If((BooleanLit(False), Return(BooleanLit(False))), [], VarDecl(Id(lus), ArrayType([2.83], StringType), None, None))), (BooleanLit(False), CallStmt(Id(ayK), [NumLit(34.41)]))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
string bT0[63.36,38.64] <- 15.7
func um6J (string NHU[77.57,77.25], string xD[35.86])	return "o"
string a3[14.6,26.27,30.21]
'''
		expect = '''Program([VarDecl(Id(bT0), ArrayType([63.36, 38.64], StringType), None, NumLit(15.7)), FuncDecl(Id(um6J), [VarDecl(Id(NHU), ArrayType([77.57, 77.25], StringType), None, None), VarDecl(Id(xD), ArrayType([35.86], StringType), None, None)], Return(StringLit(o))), VarDecl(Id(a3), ArrayType([14.6, 26.27, 30.21], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
func o877 (string L5G, number CB[69.89,66.0,70.84], string VD[12.03,27.92])	return
dynamic Uf1
'''
		expect = '''Program([FuncDecl(Id(o877), [VarDecl(Id(L5G), StringType, None, None), VarDecl(Id(CB), ArrayType([69.89, 66.0, 70.84], NumberType), None, None), VarDecl(Id(VD), ArrayType([12.03, 27.92], StringType), None, None)], Return()), VarDecl(Id(Uf1), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
func uWL7 (bool EMve[3.61,19.29,21.2], bool nQOL, bool I4P[17.96,96.49,57.75])
	return

func id (number ZZ, bool g4V, bool wfe)
	begin
		b_c <- 91.05
		q4bV[qF] <- 85.96
		for GxUo until "c" by 76.9
			return "zCH"
	end
bool o8[62.71] <- Y4
'''
		expect = '''Program([FuncDecl(Id(uWL7), [VarDecl(Id(EMve), ArrayType([3.61, 19.29, 21.2], BoolType), None, None), VarDecl(Id(nQOL), BoolType, None, None), VarDecl(Id(I4P), ArrayType([17.96, 96.49, 57.75], BoolType), None, None)], Return()), FuncDecl(Id(id), [VarDecl(Id(ZZ), NumberType, None, None), VarDecl(Id(g4V), BoolType, None, None), VarDecl(Id(wfe), BoolType, None, None)], Block([AssignStmt(Id(b_c), NumLit(91.05)), AssignStmt(ArrayCell(Id(q4bV), [Id(qF)]), NumLit(85.96)), For(Id(GxUo), StringLit(c), NumLit(76.9), Return(StringLit(zCH)))])), VarDecl(Id(o8), ArrayType([62.71], BoolType), None, Id(Y4))])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
number A4LT[67.8,24.15]
func kC ()	return
bool ApZH[15.91,77.78,47.6] <- zb
func liG (string Pv0[49.86,25.96,43.2], number X2EI)
	return

func UvZ9 (string Gh[75.7,67.27], bool ayb[92.19,27.34], string AG[23.02,55.26,37.74])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(A4LT), ArrayType([67.8, 24.15], NumberType), None, None), FuncDecl(Id(kC), [], Return()), VarDecl(Id(ApZH), ArrayType([15.91, 77.78, 47.6], BoolType), None, Id(zb)), FuncDecl(Id(liG), [VarDecl(Id(Pv0), ArrayType([49.86, 25.96, 43.2], StringType), None, None), VarDecl(Id(X2EI), NumberType, None, None)], Return()), FuncDecl(Id(UvZ9), [VarDecl(Id(Gh), ArrayType([75.7, 67.27], StringType), None, None), VarDecl(Id(ayb), ArrayType([92.19, 27.34], BoolType), None, None), VarDecl(Id(AG), ArrayType([23.02, 55.26, 37.74], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
func NH (number pXUa[37.27,60.87,73.7], string R_E[46.6,1.02,90.64])
	return

'''
		expect = '''Program([FuncDecl(Id(NH), [VarDecl(Id(pXUa), ArrayType([37.27, 60.87, 73.7], NumberType), None, None), VarDecl(Id(R_E), ArrayType([46.6, 1.02, 90.64], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
bool PBN[52.43,51.63] <- true
number oe[82.16,66.49,32.81] <- 27.92
func nTp (string VQ[31.43,52.72,76.8])
	begin
	end
string Kfu
'''
		expect = '''Program([VarDecl(Id(PBN), ArrayType([52.43, 51.63], BoolType), None, BooleanLit(True)), VarDecl(Id(oe), ArrayType([82.16, 66.49, 32.81], NumberType), None, NumLit(27.92)), FuncDecl(Id(nTp), [VarDecl(Id(VQ), ArrayType([31.43, 52.72, 76.8], StringType), None, None)], Block([])), VarDecl(Id(Kfu), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
string bkSs
bool aY[15.97,49.45,88.04] <- false
'''
		expect = '''Program([VarDecl(Id(bkSs), StringType, None, None), VarDecl(Id(aY), ArrayType([15.97, 49.45, 88.04], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
number vof <- "paCC"
'''
		expect = '''Program([VarDecl(Id(vof), NumberType, None, StringLit(paCC))])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
var Jqy_ <- false
func pU (number emut)
	begin
		ZWO5(20.62, false, "Lk")
	end

dynamic ak3J <- "fc"
func BzxU ()
	return

'''
		expect = '''Program([VarDecl(Id(Jqy_), None, var, BooleanLit(False)), FuncDecl(Id(pU), [VarDecl(Id(emut), NumberType, None, None)], Block([CallStmt(Id(ZWO5), [NumLit(20.62), BooleanLit(False), StringLit(Lk)])])), VarDecl(Id(ak3J), None, dynamic, StringLit(fc)), FuncDecl(Id(BzxU), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
func pdK (bool C2vr[34.79,75.53,73.02], string XDZv[39.0,18.51], bool rezZ)
	return xjo
'''
		expect = '''Program([FuncDecl(Id(pdK), [VarDecl(Id(C2vr), ArrayType([34.79, 75.53, 73.02], BoolType), None, None), VarDecl(Id(XDZv), ArrayType([39.0, 18.51], StringType), None, None), VarDecl(Id(rezZ), BoolType, None, None)], Return(Id(xjo)))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
dynamic lRF9
string FRf9 <- 71.08
string VC
func Qgm9 (number N_Y[35.76], number va1[46.97,49.27])	return true
bool rZ[47.04,3.05] <- ocRw
'''
		expect = '''Program([VarDecl(Id(lRF9), None, dynamic, None), VarDecl(Id(FRf9), StringType, None, NumLit(71.08)), VarDecl(Id(VC), StringType, None, None), FuncDecl(Id(Qgm9), [VarDecl(Id(N_Y), ArrayType([35.76], NumberType), None, None), VarDecl(Id(va1), ArrayType([46.97, 49.27], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(rZ), ArrayType([47.04, 3.05], BoolType), None, Id(ocRw))])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
string be8
number PKDf[85.79]
number lcA <- "fXKC"
'''
		expect = '''Program([VarDecl(Id(be8), StringType, None, None), VarDecl(Id(PKDf), ArrayType([85.79], NumberType), None, None), VarDecl(Id(lcA), NumberType, None, StringLit(fXKC))])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
number lJ7[30.97,30.97] <- 39.25
func V1 (string T2j[84.69,5.69], number q2y)	return
'''
		expect = '''Program([VarDecl(Id(lJ7), ArrayType([30.97, 30.97], NumberType), None, NumLit(39.25)), FuncDecl(Id(V1), [VarDecl(Id(T2j), ArrayType([84.69, 5.69], StringType), None, None), VarDecl(Id(q2y), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
func TNk (bool LSd[25.08,37.11,11.54])	return

'''
		expect = '''Program([FuncDecl(Id(TNk), [VarDecl(Id(LSd), ArrayType([25.08, 37.11, 11.54], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
number C4[27.64,63.71,86.09] <- DlF
'''
		expect = '''Program([VarDecl(Id(C4), ArrayType([27.64, 63.71, 86.09], NumberType), None, Id(DlF))])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
func Iw (string TG, number Y9[16.19,58.58,91.66])
	return

func sJ (string Mmf, bool SNGN)	begin
		begin
		end
		continue
		if (false) continue
		elif ("PU") continue
		elif (34.45)
		tJv0 <- ouA
		elif (true) continue
		elif ("OxYz") number SSPN[65.91]
		elif (X732) for MLZM until 18.87 by "qS"
			break
	end

'''
		expect = '''Program([FuncDecl(Id(Iw), [VarDecl(Id(TG), StringType, None, None), VarDecl(Id(Y9), ArrayType([16.19, 58.58, 91.66], NumberType), None, None)], Return()), FuncDecl(Id(sJ), [VarDecl(Id(Mmf), StringType, None, None), VarDecl(Id(SNGN), BoolType, None, None)], Block([Block([]), Continue, If((BooleanLit(False), Continue), [(StringLit(PU), Continue), (NumLit(34.45), AssignStmt(Id(tJv0), Id(ouA))), (BooleanLit(True), Continue), (StringLit(OxYz), VarDecl(Id(SSPN), ArrayType([65.91], NumberType), None, None)), (Id(X732), For(Id(MLZM), NumLit(18.87), StringLit(qS), Break))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
var a8 <- true
bool Om[89.54]
number pbO[93.66,63.15] <- ALi
func vz4f (string Ng, bool ac[71.56,72.96], bool klAF[27.69,23.69,38.73])	return

'''
		expect = '''Program([VarDecl(Id(a8), None, var, BooleanLit(True)), VarDecl(Id(Om), ArrayType([89.54], BoolType), None, None), VarDecl(Id(pbO), ArrayType([93.66, 63.15], NumberType), None, Id(ALi)), FuncDecl(Id(vz4f), [VarDecl(Id(Ng), StringType, None, None), VarDecl(Id(ac), ArrayType([71.56, 72.96], BoolType), None, None), VarDecl(Id(klAF), ArrayType([27.69, 23.69, 38.73], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
func jAh (number W6M[3.35,50.52,26.61], bool qJ[3.56], string BE)
	return "aYQ"
var MXC <- "R"
func mp (number Tk, bool dyKf[48.99,22.35,52.75])	begin
		L8["u", false] <- 13.14
	end

string WYl[30.51]
'''
		expect = '''Program([FuncDecl(Id(jAh), [VarDecl(Id(W6M), ArrayType([3.35, 50.52, 26.61], NumberType), None, None), VarDecl(Id(qJ), ArrayType([3.56], BoolType), None, None), VarDecl(Id(BE), StringType, None, None)], Return(StringLit(aYQ))), VarDecl(Id(MXC), None, var, StringLit(R)), FuncDecl(Id(mp), [VarDecl(Id(Tk), NumberType, None, None), VarDecl(Id(dyKf), ArrayType([48.99, 22.35, 52.75], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(L8), [StringLit(u), BooleanLit(False)]), NumLit(13.14))])), VarDecl(Id(WYl), ArrayType([30.51], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
bool nPVr[51.41] <- B2
number bl <- "a"
func fYfp (bool KCW, string I2S2[7.49])
	return

var uVW <- 15.77
'''
		expect = '''Program([VarDecl(Id(nPVr), ArrayType([51.41], BoolType), None, Id(B2)), VarDecl(Id(bl), NumberType, None, StringLit(a)), FuncDecl(Id(fYfp), [VarDecl(Id(KCW), BoolType, None, None), VarDecl(Id(I2S2), ArrayType([7.49], StringType), None, None)], Return()), VarDecl(Id(uVW), None, var, NumLit(15.77))])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
func loDz (string TR2[16.04,7.97])	return

func noQ ()
	begin
		D_G(74.19)
		for O3 until u8 by 34.76
			Zsp("cXhw")
	end
func OEAM (number zGg, string puD, string fthF[14.71,25.88,69.76])
	begin
		continue
		RpG()
	end

bool eef9[29.23,17.84] <- "a"
'''
		expect = '''Program([FuncDecl(Id(loDz), [VarDecl(Id(TR2), ArrayType([16.04, 7.97], StringType), None, None)], Return()), FuncDecl(Id(noQ), [], Block([CallStmt(Id(D_G), [NumLit(74.19)]), For(Id(O3), Id(u8), NumLit(34.76), CallStmt(Id(Zsp), [StringLit(cXhw)]))])), FuncDecl(Id(OEAM), [VarDecl(Id(zGg), NumberType, None, None), VarDecl(Id(puD), StringType, None, None), VarDecl(Id(fthF), ArrayType([14.71, 25.88, 69.76], StringType), None, None)], Block([Continue, CallStmt(Id(RpG), [])])), VarDecl(Id(eef9), ArrayType([29.23, 17.84], BoolType), None, StringLit(a))])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
number gG[39.23,64.57,99.49] <- 52.82
string pgep[22.2] <- "T"
func sGss ()	begin
		AQG(false, true, false)
		continue
		string VzIy[96.15]
	end
'''
		expect = '''Program([VarDecl(Id(gG), ArrayType([39.23, 64.57, 99.49], NumberType), None, NumLit(52.82)), VarDecl(Id(pgep), ArrayType([22.2], StringType), None, StringLit(T)), FuncDecl(Id(sGss), [], Block([CallStmt(Id(AQG), [BooleanLit(False), BooleanLit(True), BooleanLit(False)]), Continue, VarDecl(Id(VzIy), ArrayType([96.15], StringType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
func Je_ (bool Fr[42.15,93.6,5.24])	return
func xh (number L2T, bool ypz7[30.32])	return

func rb42 ()	begin
		continue
	end
bool oL[98.03] <- false
func Qxwm (string cjxK, bool ovBr)
	return

'''
		expect = '''Program([FuncDecl(Id(Je_), [VarDecl(Id(Fr), ArrayType([42.15, 93.6, 5.24], BoolType), None, None)], Return()), FuncDecl(Id(xh), [VarDecl(Id(L2T), NumberType, None, None), VarDecl(Id(ypz7), ArrayType([30.32], BoolType), None, None)], Return()), FuncDecl(Id(rb42), [], Block([Continue])), VarDecl(Id(oL), ArrayType([98.03], BoolType), None, BooleanLit(False)), FuncDecl(Id(Qxwm), [VarDecl(Id(cjxK), StringType, None, None), VarDecl(Id(ovBr), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
func MX (string X8SA, number cZ[82.08], string d3r[8.5])	begin
		return
		pamb(true)
	end

func xsBx ()
	return

func cR (bool ZzHO)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(MX), [VarDecl(Id(X8SA), StringType, None, None), VarDecl(Id(cZ), ArrayType([82.08], NumberType), None, None), VarDecl(Id(d3r), ArrayType([8.5], StringType), None, None)], Block([Return(), CallStmt(Id(pamb), [BooleanLit(True)])])), FuncDecl(Id(xsBx), [], Return()), FuncDecl(Id(cR), [VarDecl(Id(ZzHO), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
func qt (number Vz[80.8,91.62], number uor[15.58], number mx)
	begin
		break
		break
	end

func wa (string jDQ[48.8,93.16])	return
'''
		expect = '''Program([FuncDecl(Id(qt), [VarDecl(Id(Vz), ArrayType([80.8, 91.62], NumberType), None, None), VarDecl(Id(uor), ArrayType([15.58], NumberType), None, None), VarDecl(Id(mx), NumberType, None, None)], Block([Break, Break])), FuncDecl(Id(wa), [VarDecl(Id(jDQ), ArrayType([48.8, 93.16], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
string S2K[41.42,57.78,53.46] <- "Tgev"
func noLe (bool izyC[68.73,47.95])	return

'''
		expect = '''Program([VarDecl(Id(S2K), ArrayType([41.42, 57.78, 53.46], StringType), None, StringLit(Tgev)), FuncDecl(Id(noLe), [VarDecl(Id(izyC), ArrayType([68.73, 47.95], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
number ZHhr[49.51]
func LV7t (number hsz7)
	return
func U_Uj (number Ue0, string j7AD)
	return

func lx ()	return
'''
		expect = '''Program([VarDecl(Id(ZHhr), ArrayType([49.51], NumberType), None, None), FuncDecl(Id(LV7t), [VarDecl(Id(hsz7), NumberType, None, None)], Return()), FuncDecl(Id(U_Uj), [VarDecl(Id(Ue0), NumberType, None, None), VarDecl(Id(j7AD), StringType, None, None)], Return()), FuncDecl(Id(lx), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
bool ch[55.13,6.11,75.29] <- true
number rAu
func lM (bool bt5[29.78,2.94])	return

'''
		expect = '''Program([VarDecl(Id(ch), ArrayType([55.13, 6.11, 75.29], BoolType), None, BooleanLit(True)), VarDecl(Id(rAu), NumberType, None, None), FuncDecl(Id(lM), [VarDecl(Id(bt5), ArrayType([29.78, 2.94], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
number Q1 <- d9q
string a_[22.02,3.13,95.14]
string sW[54.7] <- "F"
string wOf0
'''
		expect = '''Program([VarDecl(Id(Q1), NumberType, None, Id(d9q)), VarDecl(Id(a_), ArrayType([22.02, 3.13, 95.14], StringType), None, None), VarDecl(Id(sW), ArrayType([54.7], StringType), None, StringLit(F)), VarDecl(Id(wOf0), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
func VehA (string dDws, string Dt, bool QVj_)
	begin
		TZh[dc0, "tuOVo"] <- "ig"
		if ("xv")
		for iA until true by 53.58
			number BXS0[52.09,12.01] <- "Fs"
		elif (55.55) continue
		elif (false)
		for qC until 83.44 by "w"
			l0kn[2.81] <- "p"
		CCiA(true, Qm)
	end
var IEXA <- "dBm"
'''
		expect = '''Program([FuncDecl(Id(VehA), [VarDecl(Id(dDws), StringType, None, None), VarDecl(Id(Dt), StringType, None, None), VarDecl(Id(QVj_), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(TZh), [Id(dc0), StringLit(tuOVo)]), StringLit(ig)), If((StringLit(xv), For(Id(iA), BooleanLit(True), NumLit(53.58), VarDecl(Id(BXS0), ArrayType([52.09, 12.01], NumberType), None, StringLit(Fs)))), [(NumLit(55.55), Continue), (BooleanLit(False), For(Id(qC), NumLit(83.44), StringLit(w), AssignStmt(ArrayCell(Id(l0kn), [NumLit(2.81)]), StringLit(p))))], None), CallStmt(Id(CCiA), [BooleanLit(True), Id(Qm)])])), VarDecl(Id(IEXA), None, var, StringLit(dBm))])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''
func Wtz (number BPO7[40.85])	return
'''
		expect = '''Program([FuncDecl(Id(Wtz), [VarDecl(Id(BPO7), ArrayType([40.85], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
bool ByY[3.48,52.91] <- "N"
string jXl <- "KdXt"
'''
		expect = '''Program([VarDecl(Id(ByY), ArrayType([3.48, 52.91], BoolType), None, StringLit(N)), VarDecl(Id(jXl), StringType, None, StringLit(KdXt))])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
func fsW (number Ly[47.93], number Ddn, string Ez)	return IIeI
func znO6 (number rB[43.67,70.41], number A8t[92.19,42.9,97.0])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(fsW), [VarDecl(Id(Ly), ArrayType([47.93], NumberType), None, None), VarDecl(Id(Ddn), NumberType, None, None), VarDecl(Id(Ez), StringType, None, None)], Return(Id(IIeI))), FuncDecl(Id(znO6), [VarDecl(Id(rB), ArrayType([43.67, 70.41], NumberType), None, None), VarDecl(Id(A8t), ArrayType([92.19, 42.9, 97.0], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
number dnY1[85.62] <- "TF"
dynamic xd <- true
bool rK <- "k"
'''
		expect = '''Program([VarDecl(Id(dnY1), ArrayType([85.62], NumberType), None, StringLit(TF)), VarDecl(Id(xd), None, dynamic, BooleanLit(True)), VarDecl(Id(rK), BoolType, None, StringLit(k))])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
dynamic NW <- true
'''
		expect = '''Program([VarDecl(Id(NW), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
func X6D (number RM4N[15.49,68.95,13.68])
	begin
		if (SR06)
		Oal(false)
		elif (52.99) continue
		elif (75.57)
		if (true) return false
		elif (false) begin
			DrRn(I1, "pm", 59.8)
			continue
		end
		elif (gX) begin
		end
		elif (false) begin
			string Ga3r[48.76,38.34,69.59] <- true
			begin
				number lYY <- "u"
				number fKP <- 18.38
			end
			continue
		end
		elif (true)
		continue
		else if ("mPBF") h2w <- false
		elif (true)
		begin
		end
		elif (98.63)
		j5 <- "q"
		elif (79.89)
		begin
			bool Lo[33.28,96.74]
		end
		else eQ <- 36.05
		elif (I1g) begin
			PD("oeM", 80.45)
			continue
			continue
		end
		elif (90.96) break
		else if (ngX1)
		string E04[19.68,89.47,60.64]
		else GxMk(31.56)
	end
number im76[86.88,19.7] <- GBf
func t34 (bool OxL)
	return HDBD

func OioL (bool KX[75.81,29.67,18.87], string w03)
	return g88

'''
		expect = '''Program([FuncDecl(Id(X6D), [VarDecl(Id(RM4N), ArrayType([15.49, 68.95, 13.68], NumberType), None, None)], Block([If((Id(SR06), CallStmt(Id(Oal), [BooleanLit(False)])), [(NumLit(52.99), Continue), (NumLit(75.57), If((BooleanLit(True), Return(BooleanLit(False))), [(BooleanLit(False), Block([CallStmt(Id(DrRn), [Id(I1), StringLit(pm), NumLit(59.8)]), Continue])), (Id(gX), Block([])), (BooleanLit(False), Block([VarDecl(Id(Ga3r), ArrayType([48.76, 38.34, 69.59], StringType), None, BooleanLit(True)), Block([VarDecl(Id(lYY), NumberType, None, StringLit(u)), VarDecl(Id(fKP), NumberType, None, NumLit(18.38))]), Continue])), (BooleanLit(True), Continue)], If((StringLit(mPBF), AssignStmt(Id(h2w), BooleanLit(False))), [(BooleanLit(True), Block([])), (NumLit(98.63), AssignStmt(Id(j5), StringLit(q))), (NumLit(79.89), Block([VarDecl(Id(Lo), ArrayType([33.28, 96.74], BoolType), None, None)]))], AssignStmt(Id(eQ), NumLit(36.05))))), (Id(I1g), Block([CallStmt(Id(PD), [StringLit(oeM), NumLit(80.45)]), Continue, Continue])), (NumLit(90.96), Break)], If((Id(ngX1), VarDecl(Id(E04), ArrayType([19.68, 89.47, 60.64], StringType), None, None)), [], CallStmt(Id(GxMk), [NumLit(31.56)])))])), VarDecl(Id(im76), ArrayType([86.88, 19.7], NumberType), None, Id(GBf)), FuncDecl(Id(t34), [VarDecl(Id(OxL), BoolType, None, None)], Return(Id(HDBD))), FuncDecl(Id(OioL), [VarDecl(Id(KX), ArrayType([75.81, 29.67, 18.87], BoolType), None, None), VarDecl(Id(w03), StringType, None, None)], Return(Id(g88)))])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
string Av <- true
func GHYG ()
	begin
		break
		if (9.63)
		continue
		elif ("y")
		begin
		end
		elif (K9K) QOK(84.2, true, true)
		elif (G1IY) continue
		elif (false) if (86.12)
		Jv <- true
		else begin
			begin
				begin
					continue
					dynamic cIl9 <- "nN"
				end
				ND5 <- 7.56
				break
			end
		end
	end

bool AIL[19.35,0.17] <- 76.65
func LFt (bool BZW5[6.37], string AP[58.93])	begin
		bool uFf <- NE
	end

func TR_ ()	begin
		if (true)
		return "XUX"
		elif ("ci") XRsP()
		elif ("Klm") continue
		elif (false)
		q6 <- true
		elif ("j") MSM("N", "G")
		elif (80.57) for dS until 78.47 by 73.77
			begin
			end
		y9h()
	end
'''
		expect = '''Program([VarDecl(Id(Av), StringType, None, BooleanLit(True)), FuncDecl(Id(GHYG), [], Block([Break, If((NumLit(9.63), Continue), [(StringLit(y), Block([])), (Id(K9K), CallStmt(Id(QOK), [NumLit(84.2), BooleanLit(True), BooleanLit(True)])), (Id(G1IY), Continue), (BooleanLit(False), If((NumLit(86.12), AssignStmt(Id(Jv), BooleanLit(True))), [], Block([Block([Block([Continue, VarDecl(Id(cIl9), None, dynamic, StringLit(nN))]), AssignStmt(Id(ND5), NumLit(7.56)), Break])])))], None)])), VarDecl(Id(AIL), ArrayType([19.35, 0.17], BoolType), None, NumLit(76.65)), FuncDecl(Id(LFt), [VarDecl(Id(BZW5), ArrayType([6.37], BoolType), None, None), VarDecl(Id(AP), ArrayType([58.93], StringType), None, None)], Block([VarDecl(Id(uFf), BoolType, None, Id(NE))])), FuncDecl(Id(TR_), [], Block([If((BooleanLit(True), Return(StringLit(XUX))), [(StringLit(ci), CallStmt(Id(XRsP), [])), (StringLit(Klm), Continue), (BooleanLit(False), AssignStmt(Id(q6), BooleanLit(True))), (StringLit(j), CallStmt(Id(MSM), [StringLit(N), StringLit(G)])), (NumLit(80.57), For(Id(dS), NumLit(78.47), NumLit(73.77), Block([])))], None), CallStmt(Id(y9h), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
string ol <- 37.63
number G1R <- false
var vnEw <- GU
'''
		expect = '''Program([VarDecl(Id(ol), StringType, None, NumLit(37.63)), VarDecl(Id(G1R), NumberType, None, BooleanLit(False)), VarDecl(Id(vnEw), None, var, Id(GU))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func cWG ()
	begin
		uT("j", "gomn")
		M3ye <- 38.85
	end
func IwyZ ()	begin
		s4U <- 35.17
		kCG5()
	end

number Rd
func wZo ()	return
'''
		expect = '''Program([FuncDecl(Id(cWG), [], Block([CallStmt(Id(uT), [StringLit(j), StringLit(gomn)]), AssignStmt(Id(M3ye), NumLit(38.85))])), FuncDecl(Id(IwyZ), [], Block([AssignStmt(Id(s4U), NumLit(35.17)), CallStmt(Id(kCG5), [])])), VarDecl(Id(Rd), NumberType, None, None), FuncDecl(Id(wZo), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
func UG3 (number fiE[75.99,76.12], number jJP, bool db[88.26,38.15,30.9])	return

'''
		expect = '''Program([FuncDecl(Id(UG3), [VarDecl(Id(fiE), ArrayType([75.99, 76.12], NumberType), None, None), VarDecl(Id(jJP), NumberType, None, None), VarDecl(Id(db), ArrayType([88.26, 38.15, 30.9], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
func Cm (number R9[95.17], bool Ms4H, bool lR[95.45])	begin
		for DWRQ until EuG by 11.31
			return 52.9
	end

'''
		expect = '''Program([FuncDecl(Id(Cm), [VarDecl(Id(R9), ArrayType([95.17], NumberType), None, None), VarDecl(Id(Ms4H), BoolType, None, None), VarDecl(Id(lR), ArrayType([95.45], BoolType), None, None)], Block([For(Id(DWRQ), Id(EuG), NumLit(11.31), Return(NumLit(52.9)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
func TYQ3 (string zT5y[42.31,72.66], bool XX[24.98], string T8dG[94.19])
	return "okhI"

string Ct[87.08,32.66]
string m53E
bool uLJe[91.69,96.36,88.73] <- "Ob"
'''
		expect = '''Program([FuncDecl(Id(TYQ3), [VarDecl(Id(zT5y), ArrayType([42.31, 72.66], StringType), None, None), VarDecl(Id(XX), ArrayType([24.98], BoolType), None, None), VarDecl(Id(T8dG), ArrayType([94.19], StringType), None, None)], Return(StringLit(okhI))), VarDecl(Id(Ct), ArrayType([87.08, 32.66], StringType), None, None), VarDecl(Id(m53E), StringType, None, None), VarDecl(Id(uLJe), ArrayType([91.69, 96.36, 88.73], BoolType), None, StringLit(Ob))])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
dynamic cvf8
'''
		expect = '''Program([VarDecl(Id(cvf8), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func Dg ()
	return ln0

func ztj ()
	return false

string eOd[70.69,60.27,54.69] <- true
func b42 ()
	return

func sJ ()	return XOCI
'''
		expect = '''Program([FuncDecl(Id(Dg), [], Return(Id(ln0))), FuncDecl(Id(ztj), [], Return(BooleanLit(False))), VarDecl(Id(eOd), ArrayType([70.69, 60.27, 54.69], StringType), None, BooleanLit(True)), FuncDecl(Id(b42), [], Return()), FuncDecl(Id(sJ), [], Return(Id(XOCI)))])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
func XzJJ (bool e8SI[64.25,23.15], string PhIm)	return
func P6W (string d1lu[32.63,58.78,72.25], string uu[88.25], number Xbim[15.85,93.73])
	return true
'''
		expect = '''Program([FuncDecl(Id(XzJJ), [VarDecl(Id(e8SI), ArrayType([64.25, 23.15], BoolType), None, None), VarDecl(Id(PhIm), StringType, None, None)], Return()), FuncDecl(Id(P6W), [VarDecl(Id(d1lu), ArrayType([32.63, 58.78, 72.25], StringType), None, None), VarDecl(Id(uu), ArrayType([88.25], StringType), None, None), VarDecl(Id(Xbim), ArrayType([15.85, 93.73], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
func OyBp ()	return
func rYD (string Ad, string BXG0[4.0,70.96], bool vvf)
	return "raWI"
dynamic Vnr
'''
		expect = '''Program([FuncDecl(Id(OyBp), [], Return()), FuncDecl(Id(rYD), [VarDecl(Id(Ad), StringType, None, None), VarDecl(Id(BXG0), ArrayType([4.0, 70.96], StringType), None, None), VarDecl(Id(vvf), BoolType, None, None)], Return(StringLit(raWI))), VarDecl(Id(Vnr), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
bool Ug4o[95.67,27.27,6.14] <- "gYy"
func j52F (number Cm[1.74,44.36])
	return true

func y2R (string AlI, bool b1[18.16,8.88,8.16], bool DO7[35.06,61.6,44.43])
	return

'''
		expect = '''Program([VarDecl(Id(Ug4o), ArrayType([95.67, 27.27, 6.14], BoolType), None, StringLit(gYy)), FuncDecl(Id(j52F), [VarDecl(Id(Cm), ArrayType([1.74, 44.36], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(y2R), [VarDecl(Id(AlI), StringType, None, None), VarDecl(Id(b1), ArrayType([18.16, 8.88, 8.16], BoolType), None, None), VarDecl(Id(DO7), ArrayType([35.06, 61.6, 44.43], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
func U0w (string psm[10.58,71.99,29.16], string n4aL, string WNJR)	return 47.76

dynamic pc <- dHQ
func AKh (string ctUM[64.57,56.82,21.79], bool tJET[17.98,85.82,25.73], bool Aq1c)	return true
number Kz[89.84,79.34] <- "sWtr"
'''
		expect = '''Program([FuncDecl(Id(U0w), [VarDecl(Id(psm), ArrayType([10.58, 71.99, 29.16], StringType), None, None), VarDecl(Id(n4aL), StringType, None, None), VarDecl(Id(WNJR), StringType, None, None)], Return(NumLit(47.76))), VarDecl(Id(pc), None, dynamic, Id(dHQ)), FuncDecl(Id(AKh), [VarDecl(Id(ctUM), ArrayType([64.57, 56.82, 21.79], StringType), None, None), VarDecl(Id(tJET), ArrayType([17.98, 85.82, 25.73], BoolType), None, None), VarDecl(Id(Aq1c), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Kz), ArrayType([89.84, 79.34], NumberType), None, StringLit(sWtr))])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
string qmg[31.32,21.61,93.26] <- false
number Aa[31.06,90.65] <- 83.4
var acgq <- 35.06
func km7 (number mn5x[15.76,94.34], number FVN[90.34,17.8], number Zs[81.74])	begin
		for g_l until 80.19 by "SNV"
			bool CN[65.88] <- true
	end

'''
		expect = '''Program([VarDecl(Id(qmg), ArrayType([31.32, 21.61, 93.26], StringType), None, BooleanLit(False)), VarDecl(Id(Aa), ArrayType([31.06, 90.65], NumberType), None, NumLit(83.4)), VarDecl(Id(acgq), None, var, NumLit(35.06)), FuncDecl(Id(km7), [VarDecl(Id(mn5x), ArrayType([15.76, 94.34], NumberType), None, None), VarDecl(Id(FVN), ArrayType([90.34, 17.8], NumberType), None, None), VarDecl(Id(Zs), ArrayType([81.74], NumberType), None, None)], Block([For(Id(g_l), NumLit(80.19), StringLit(SNV), VarDecl(Id(CN), ArrayType([65.88], BoolType), None, BooleanLit(True)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
func L2 ()
	begin
		if (JU) break
		elif ("H")
		break
		elif ("WtA")
		JD2p(false)
		number qyKo <- 29.44
		Lq[xra] <- "mw"
	end
func hZ (string r6gF, number egp)
	begin
	end
var FC0 <- false
'''
		expect = '''Program([FuncDecl(Id(L2), [], Block([If((Id(JU), Break), [(StringLit(H), Break), (StringLit(WtA), CallStmt(Id(JD2p), [BooleanLit(False)]))], None), VarDecl(Id(qyKo), NumberType, None, NumLit(29.44)), AssignStmt(ArrayCell(Id(Lq), [Id(xra)]), StringLit(mw))])), FuncDecl(Id(hZ), [VarDecl(Id(r6gF), StringType, None, None), VarDecl(Id(egp), NumberType, None, None)], Block([])), VarDecl(Id(FC0), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
func Tz ()	begin
		begin
			for E2Vl until false by 14.87
				var PNvg <- "X"
			cTA()
			return false
		end
		QX9[true] <- 65.93
	end
func zwIr (number X1[78.51,15.5])	begin
		Swo(MOoz, "o", true)
		return
		begin
			break
		end
	end
func VgGC (string Llr[35.69,59.53,49.16])
	begin
		Una()
		begin
		end
	end
number Ul <- 63.75
'''
		expect = '''Program([FuncDecl(Id(Tz), [], Block([Block([For(Id(E2Vl), BooleanLit(False), NumLit(14.87), VarDecl(Id(PNvg), None, var, StringLit(X))), CallStmt(Id(cTA), []), Return(BooleanLit(False))]), AssignStmt(ArrayCell(Id(QX9), [BooleanLit(True)]), NumLit(65.93))])), FuncDecl(Id(zwIr), [VarDecl(Id(X1), ArrayType([78.51, 15.5], NumberType), None, None)], Block([CallStmt(Id(Swo), [Id(MOoz), StringLit(o), BooleanLit(True)]), Return(), Block([Break])])), FuncDecl(Id(VgGC), [VarDecl(Id(Llr), ArrayType([35.69, 59.53, 49.16], StringType), None, None)], Block([CallStmt(Id(Una), []), Block([])])), VarDecl(Id(Ul), NumberType, None, NumLit(63.75))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
func i6z ()
	return "Q"

dynamic db_4 <- 48.85
'''
		expect = '''Program([FuncDecl(Id(i6z), [], Return(StringLit(Q))), VarDecl(Id(db_4), None, dynamic, NumLit(48.85))])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
number vtc[60.67] <- S_
string LNA <- "NLno"
'''
		expect = '''Program([VarDecl(Id(vtc), ArrayType([60.67], NumberType), None, Id(S_)), VarDecl(Id(LNA), StringType, None, StringLit(NLno))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
func WD2h (bool tdQ, number nsK[76.59,2.9,47.5], number zt)	return
bool XkA[59.27,69.3] <- lDgN
number pnRV[61.78] <- false
'''
		expect = '''Program([FuncDecl(Id(WD2h), [VarDecl(Id(tdQ), BoolType, None, None), VarDecl(Id(nsK), ArrayType([76.59, 2.9, 47.5], NumberType), None, None), VarDecl(Id(zt), NumberType, None, None)], Return()), VarDecl(Id(XkA), ArrayType([59.27, 69.3], BoolType), None, Id(lDgN)), VarDecl(Id(pnRV), ArrayType([61.78], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
func X2F (bool Eu[3.1,0.87,2.05])	return
func C_ ()
	return
bool zx[51.31,74.53,78.34] <- 41.42
func mtb (string PNA[69.37,70.1,73.96], string Jc[1.03], string w7b[82.71])
	begin
	end
number M0a
'''
		expect = '''Program([FuncDecl(Id(X2F), [VarDecl(Id(Eu), ArrayType([3.1, 0.87, 2.05], BoolType), None, None)], Return()), FuncDecl(Id(C_), [], Return()), VarDecl(Id(zx), ArrayType([51.31, 74.53, 78.34], BoolType), None, NumLit(41.42)), FuncDecl(Id(mtb), [VarDecl(Id(PNA), ArrayType([69.37, 70.1, 73.96], StringType), None, None), VarDecl(Id(Jc), ArrayType([1.03], StringType), None, None), VarDecl(Id(w7b), ArrayType([82.71], StringType), None, None)], Block([])), VarDecl(Id(M0a), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
dynamic qoZ7 <- 86.32
'''
		expect = '''Program([VarDecl(Id(qoZ7), None, dynamic, NumLit(86.32))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
func qIhK (bool R5, string Xm[5.09,52.07])
	return OBxn
func ACy1 ()	return
func jw ()
	return

number tU[67.07,81.17,71.01] <- true
'''
		expect = '''Program([FuncDecl(Id(qIhK), [VarDecl(Id(R5), BoolType, None, None), VarDecl(Id(Xm), ArrayType([5.09, 52.07], StringType), None, None)], Return(Id(OBxn))), FuncDecl(Id(ACy1), [], Return()), FuncDecl(Id(jw), [], Return()), VarDecl(Id(tU), ArrayType([67.07, 81.17, 71.01], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
string ut <- false
'''
		expect = '''Program([VarDecl(Id(ut), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
func eO (number ghh, number RMx, number JPuj[80.83])
	return uVa

string PIP[9.28] <- 93.17
func O6 (number aUCL[10.99], number Vw[18.53,83.55,28.23])	return
func Q6 (bool IV38[10.89,50.47,36.7])	begin
		begin
			break
			VFe3 <- "Jaa"
		end
	end

func CGh (number xzs[43.15], string y70)	return false
'''
		expect = '''Program([FuncDecl(Id(eO), [VarDecl(Id(ghh), NumberType, None, None), VarDecl(Id(RMx), NumberType, None, None), VarDecl(Id(JPuj), ArrayType([80.83], NumberType), None, None)], Return(Id(uVa))), VarDecl(Id(PIP), ArrayType([9.28], StringType), None, NumLit(93.17)), FuncDecl(Id(O6), [VarDecl(Id(aUCL), ArrayType([10.99], NumberType), None, None), VarDecl(Id(Vw), ArrayType([18.53, 83.55, 28.23], NumberType), None, None)], Return()), FuncDecl(Id(Q6), [VarDecl(Id(IV38), ArrayType([10.89, 50.47, 36.7], BoolType), None, None)], Block([Block([Break, AssignStmt(Id(VFe3), StringLit(Jaa))])])), FuncDecl(Id(CGh), [VarDecl(Id(xzs), ArrayType([43.15], NumberType), None, None), VarDecl(Id(y70), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
func Li9U (number ab)	return

dynamic ka6R <- OV5
string Osj[9.67,61.88,31.74]
func xS (string foLt[7.84,60.83,37.64], string FyF, bool kVR[57.6])
	return

'''
		expect = '''Program([FuncDecl(Id(Li9U), [VarDecl(Id(ab), NumberType, None, None)], Return()), VarDecl(Id(ka6R), None, dynamic, Id(OV5)), VarDecl(Id(Osj), ArrayType([9.67, 61.88, 31.74], StringType), None, None), FuncDecl(Id(xS), [VarDecl(Id(foLt), ArrayType([7.84, 60.83, 37.64], StringType), None, None), VarDecl(Id(FyF), StringType, None, None), VarDecl(Id(kVR), ArrayType([57.6], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
func m5Z_ (bool bnC[68.83,56.1,29.54])	return
string w3TN
func AoVc (bool Elk_[1.59], number m_, string m41T[85.9,52.67,3.71])
	return
number mijX
func nLY5 ()
	return
'''
		expect = '''Program([FuncDecl(Id(m5Z_), [VarDecl(Id(bnC), ArrayType([68.83, 56.1, 29.54], BoolType), None, None)], Return()), VarDecl(Id(w3TN), StringType, None, None), FuncDecl(Id(AoVc), [VarDecl(Id(Elk_), ArrayType([1.59], BoolType), None, None), VarDecl(Id(m_), NumberType, None, None), VarDecl(Id(m41T), ArrayType([85.9, 52.67, 3.71], StringType), None, None)], Return()), VarDecl(Id(mijX), NumberType, None, None), FuncDecl(Id(nLY5), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
number O7S4[34.14,34.87]
func tcy3 ()
	begin
		continue
		dSc("CbOm", 34.01)
		continue
	end

func SKR (string lj, string IaP[41.76,55.45,48.7], string Ou)	begin
		continue
		begin
			break
			IAN[true] <- "kU"
		end
		begin
			if (80.73)
			Qe[false, "ie", "PKdD"] <- false
			elif (p9YK)
			return 25.12
			elif (swD) break
			elif (true) WBFU[true] <- Ut
			elif (68.9) LY8Y()
			else begin
				Sv9("YdkAk", "g")
				begin
					Ey0 <- "WNU"
				end
				SGU("CD", true)
			end
			kjD(false, LM3, "gMOz")
			string H799 <- W4Or
		end
	end

'''
		expect = '''Program([VarDecl(Id(O7S4), ArrayType([34.14, 34.87], NumberType), None, None), FuncDecl(Id(tcy3), [], Block([Continue, CallStmt(Id(dSc), [StringLit(CbOm), NumLit(34.01)]), Continue])), FuncDecl(Id(SKR), [VarDecl(Id(lj), StringType, None, None), VarDecl(Id(IaP), ArrayType([41.76, 55.45, 48.7], StringType), None, None), VarDecl(Id(Ou), StringType, None, None)], Block([Continue, Block([Break, AssignStmt(ArrayCell(Id(IAN), [BooleanLit(True)]), StringLit(kU))]), Block([If((NumLit(80.73), AssignStmt(ArrayCell(Id(Qe), [BooleanLit(False), StringLit(ie), StringLit(PKdD)]), BooleanLit(False))), [(Id(p9YK), Return(NumLit(25.12))), (Id(swD), Break), (BooleanLit(True), AssignStmt(ArrayCell(Id(WBFU), [BooleanLit(True)]), Id(Ut))), (NumLit(68.9), CallStmt(Id(LY8Y), []))], Block([CallStmt(Id(Sv9), [StringLit(YdkAk), StringLit(g)]), Block([AssignStmt(Id(Ey0), StringLit(WNU))]), CallStmt(Id(SGU), [StringLit(CD), BooleanLit(True)])])), CallStmt(Id(kjD), [BooleanLit(False), Id(LM3), StringLit(gMOz)]), VarDecl(Id(H799), StringType, None, Id(W4Or))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
func YMjD (bool v4)	begin
		if (wrC)
		E2s(gpM, UDy8, true)
		elif (true) for n4M5 until "fS" by LK
			for l4g6 until false by true
				MyM("WS", eo, "ipXry")
		continue
		if (2.28) break
		elif (i31) continue
		elif ("BstrP")
		for ph until true by 86.47
			Dbm <- "pVO"
		elif (GwzS) return 10.05
	end
'''
		expect = '''Program([FuncDecl(Id(YMjD), [VarDecl(Id(v4), BoolType, None, None)], Block([If((Id(wrC), CallStmt(Id(E2s), [Id(gpM), Id(UDy8), BooleanLit(True)])), [(BooleanLit(True), For(Id(n4M5), StringLit(fS), Id(LK), For(Id(l4g6), BooleanLit(False), BooleanLit(True), CallStmt(Id(MyM), [StringLit(WS), Id(eo), StringLit(ipXry)]))))], None), Continue, If((NumLit(2.28), Break), [(Id(i31), Continue), (StringLit(BstrP), For(Id(ph), BooleanLit(True), NumLit(86.47), AssignStmt(Id(Dbm), StringLit(pVO)))), (Id(GwzS), Return(NumLit(10.05)))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
string Dze[43.24] <- false
string A7
'''
		expect = '''Program([VarDecl(Id(Dze), ArrayType([43.24], StringType), None, BooleanLit(False)), VarDecl(Id(A7), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
func rnF0 (number LjD[31.72,97.03,39.24], number tI[78.54])
	return
'''
		expect = '''Program([FuncDecl(Id(rnF0), [VarDecl(Id(LjD), ArrayType([31.72, 97.03, 39.24], NumberType), None, None), VarDecl(Id(tI), ArrayType([78.54], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
string O2
func uD (bool wO[1.48])
	begin
		return
	end

string Uc
string a2o <- 1.53
string OM2_
'''
		expect = '''Program([VarDecl(Id(O2), StringType, None, None), FuncDecl(Id(uD), [VarDecl(Id(wO), ArrayType([1.48], BoolType), None, None)], Block([Return()])), VarDecl(Id(Uc), StringType, None, None), VarDecl(Id(a2o), StringType, None, NumLit(1.53)), VarDecl(Id(OM2_), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
number r7XA[45.63,28.29,42.15]
string ATm
func BXuL (number vae8, bool BhsY)
	return 64.43
'''
		expect = '''Program([VarDecl(Id(r7XA), ArrayType([45.63, 28.29, 42.15], NumberType), None, None), VarDecl(Id(ATm), StringType, None, None), FuncDecl(Id(BXuL), [VarDecl(Id(vae8), NumberType, None, None), VarDecl(Id(BhsY), BoolType, None, None)], Return(NumLit(64.43)))])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
string nedF[64.62] <- false
string tMA[12.26,27.66] <- dTuF
number NpB[63.01,10.12] <- true
bool TtQ6[29.46,21.97]
'''
		expect = '''Program([VarDecl(Id(nedF), ArrayType([64.62], StringType), None, BooleanLit(False)), VarDecl(Id(tMA), ArrayType([12.26, 27.66], StringType), None, Id(dTuF)), VarDecl(Id(NpB), ArrayType([63.01, 10.12], NumberType), None, BooleanLit(True)), VarDecl(Id(TtQ6), ArrayType([29.46, 21.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
func IR_9 (bool mTBX)
	return "nRF"
'''
		expect = '''Program([FuncDecl(Id(IR_9), [VarDecl(Id(mTBX), BoolType, None, None)], Return(StringLit(nRF)))])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
func NP2 (bool lPuN[31.27,48.48,66.54], bool Fh[82.61,49.0])	return

bool XDKR[14.21,57.28]
var li <- "f"
'''
		expect = '''Program([FuncDecl(Id(NP2), [VarDecl(Id(lPuN), ArrayType([31.27, 48.48, 66.54], BoolType), None, None), VarDecl(Id(Fh), ArrayType([82.61, 49.0], BoolType), None, None)], Return()), VarDecl(Id(XDKR), ArrayType([14.21, 57.28], BoolType), None, None), VarDecl(Id(li), None, var, StringLit(f))])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
func yt (number L7e[85.06], bool WK, number tQEM[76.93,99.59])
	return

string M8R <- false
bool g0 <- "PScUI"
func A291 (bool hw1[65.78,97.96,39.72])	begin
		return
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(yt), [VarDecl(Id(L7e), ArrayType([85.06], NumberType), None, None), VarDecl(Id(WK), BoolType, None, None), VarDecl(Id(tQEM), ArrayType([76.93, 99.59], NumberType), None, None)], Return()), VarDecl(Id(M8R), StringType, None, BooleanLit(False)), VarDecl(Id(g0), BoolType, None, StringLit(PScUI)), FuncDecl(Id(A291), [VarDecl(Id(hw1), ArrayType([65.78, 97.96, 39.72], BoolType), None, None)], Block([Return(), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
bool uurj
func LjV_ (string RMxq, bool cQu0, number dxQm[92.66])
	return

func Cbd (string b8o[7.6,36.31,73.6])
	return

func JIX (string tHH[31.95,79.59], number iv)	return false

number XmCg[3.34,16.97,14.55]
'''
		expect = '''Program([VarDecl(Id(uurj), BoolType, None, None), FuncDecl(Id(LjV_), [VarDecl(Id(RMxq), StringType, None, None), VarDecl(Id(cQu0), BoolType, None, None), VarDecl(Id(dxQm), ArrayType([92.66], NumberType), None, None)], Return()), FuncDecl(Id(Cbd), [VarDecl(Id(b8o), ArrayType([7.6, 36.31, 73.6], StringType), None, None)], Return()), FuncDecl(Id(JIX), [VarDecl(Id(tHH), ArrayType([31.95, 79.59], StringType), None, None), VarDecl(Id(iv), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(XmCg), ArrayType([3.34, 16.97, 14.55], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
string zkIq[32.08]
string P_x[95.67,38.09] <- AFf
func EWU (bool n_j, number zPo[77.51], string dWLg[58.5])	begin
		bool gO
		Pd_(true, 31.24, "di")
	end
'''
		expect = '''Program([VarDecl(Id(zkIq), ArrayType([32.08], StringType), None, None), VarDecl(Id(P_x), ArrayType([95.67, 38.09], StringType), None, Id(AFf)), FuncDecl(Id(EWU), [VarDecl(Id(n_j), BoolType, None, None), VarDecl(Id(zPo), ArrayType([77.51], NumberType), None, None), VarDecl(Id(dWLg), ArrayType([58.5], StringType), None, None)], Block([VarDecl(Id(gO), BoolType, None, None), CallStmt(Id(Pd_), [BooleanLit(True), NumLit(31.24), StringLit(di)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
func MerN (bool MDNC)	return

'''
		expect = '''Program([FuncDecl(Id(MerN), [VarDecl(Id(MDNC), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 400))
