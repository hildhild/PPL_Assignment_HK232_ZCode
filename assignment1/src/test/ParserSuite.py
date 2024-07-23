import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## &>P:tB>(j~FYhv? wsU:
func Uo (string xKY[5.285,74,27.620])
	begin
	end
## CUIKJfV8=%[XnSqQ,
string sxw <- dBl
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
func oI (var Qb)	return W4(ldn("K)3'"" and "]'"'"'"H") % FB)[QFNp, Y2]
number S2zh[189,34.702]
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
dynamic lhhC ## gSyp{m 
func T0EM (string oj[76.850e-71,69E31])	begin
		bool JQ <- 0.237 ## |he%D
		CD9(52.115, 20)
		return
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
func p5e (dynamic oe[7.350e+91,1.314])
	return 928.031E66
## QJ/A 
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
## X5<
## gI[|vWe,(.E
## R~qH<v-p}V
## bp/%8ZiM
## ~Vw11ek(vU#%
'''
		expect = '''Error on line 7 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
bool K_SH
func bQ (dynamic RC)	begin
		Mur(fBk, 23)
		dynamic nr[5.593E-66,2] <- pK ## ?a:15Nys[r
	end

func wgkm (number W9[15])	return "t"

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
bool np[57.204e-19,7,3.460] ## "F^RxK Q%n"E
## DpE:u.j
dynamic qD <- false ## _%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
func a5jM ()	begin
		## y
		## 3o
	end
## H!-|o`lr0nh9
dynamic Sq <- false
## Eqkx/|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
var ZCZF[340.693e-29,935]
## =:x6T-3<wU
func tV ()
	begin
		## 1W`"NGCM hL/@
		## (i#D`83ztdW=$
		continue
	end
func k7 ()	return

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
func wW ()
	begin
	end

string u4NW <- "f'"w"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
## dQXj`qCFv=`::*KL
string FQ[4.862,856.991E44,547] ## vDyRGZBAp
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
number HdU[4.354E-85,5.807e-48,38E43] ## ynM^;s}&eqj~fG?
## acVOu=^sx
func cnZG (dynamic LZ[7,86.069,2E-42], string YG8, dynamic Gf[1.906])	return
dynamic RG[72] <- 317.826e+19 ## m|[|
func AjRr (string ZLbD[152])	return
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
## !BwZPXo
number aZx <- true
string bNS[25]
func V1C (var OAvp)
	begin
		## 4Du
	end

'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
number RaVP
func pk (string mb[623,51,17], var EbZ, number WwwV)
	begin
		## |bF|=?)?XvBEv(Voo
	end

'''
		expect = '''Error on line 3 col 31: var'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
## 4DAgmMy
## 1Kc@!E&]8v~a`O]1p-zQ
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func i1 (number lfJD)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## z]P)]2?lYk.s
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
var otqC[7E+13,468.481]
func Sx (bool dd)
	begin
		if (ZZ)
		Qjn(true)
		elif (true) break
		elif (true)
		dynamic cD[70,6.556E50,43] <- 25
		else if ("%") if (bihq) return
		elif ("]mY") var mnx0[253,75.785e18,421E-61] ## v1{;KbeGIK%TmR
		elif (lUUe)
		return
		elif ("y'"%") number Y_UL ## !n)|`UsVR+Z=<o&+o%p
		else continue
		elif (false)
		break
		elif ("'";G'"")
		oh(rMl, 2.972E+62, 4)
		elif (jsgH) BxtR(false, true, false)
		else for Os until true by ">'""
			continue
	end
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
## kpRqvZsz^3@W&/T
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
func JD (dynamic sLLm)
	begin
		break
	end
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
dynamic wBL[8.155E-33,98,9.931] <- 804 ## |R
## !spl[<YJz|x++J4K,u}b
func N4 (number bN[9.533])	return 8
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
## tL
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
func YnI (string Es, var Nt)
	return
func X7n ()	return true
bool OUYC[29.727,73.315]
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
func lRv (dynamic dXBj[818,9.956e95,14E+29], bool jnA_[51.050,7e-91,77])
	return 1

var aQRd
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
string Ia[16e11,32] <- true ## {qfP[P`@Jzujek2!J]gy
func Xpc (dynamic zv9o)
	return

func yQ (number Vq)	return false
dynamic YW[65.794E-40] <- MWOQ
func mgQ7 ()
	return "5U'"z'""
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
number OUhM[357.741]
var S7mb <- false ## b:50&i
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
bool Kmq <- true ## j
string LAn3[542.538e+95,7.689] <- 984.647 ##  mWS>rB*KY
var erHV[4E16,1.136] ## b@QM
var wveq[2.681] <- 558 ## !x%ZmF+E{;W/P=JF#r6z
## ."B
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
number Uui_ <- "'"'"N'""
## 8&7E
string xHZs[5.361,41] ## ^z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## dj8~Fr{Mi>(J]4_:
func kdSU (number yiX, var yW[0.888e83,7.250])
	return

number t7Xm <- 64.884e18 ## .&}d!S_ruoseA39
dynamic SBK[7.300] <- 94.527
'''
		expect = '''Error on line 3 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
string gX[8.737E-30] <- false
bool eXcg[57.670] ## ?SWC:-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
## $8;
func yA (number hrPR, var Xxu[800.796E-71])	return
'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
## .% on^i
func vHg (number BKE, bool lZmd)	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
func jT (number qJ, var V5r[31.161,46.674E+20,642E+71])	return "'"'""
func Rh ()
	return

func RS (number qy)	return
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
## x]1X6}!bo|o8 1^Wxy
func l0 (dynamic Djd, var x9, string J9[83E-10,3e56,5])	begin
		## [z[g
	end

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
string ky ##  CljeyjEQXun^7{
## fFHM~`
func uj (dynamic Rpa[427], dynamic mMXA[769])	return
func t6 ()
	return
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
dynamic bIC <- HR
## ]E
## dDSP~UfnD4U/Mr
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
func Vi_p (string ePT[275E29,27E82,797])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
bool D0b[919]
func PZ0 (dynamic ze[703E08,17,45.170])
	begin
		## vay"#2p{$<|f.~]RfVq
		## u0k;fM;R;]>`
	end

var w6 <- true
func aAbH (number Qud[56,18.331])
	begin
		break
	end

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
func muo (bool Fkav)
	return 3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
string d9 ## x]Yr&j%%c|^eO/ILQ
func pf ()	return g8

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
number PLW[64.813e+76] <- false ## V%eRZCJGw;oJ8{+u
number obMr[7.900E18,544.908,303.623]
## El^*r{+{>+6FBT
string Ta <- true
string tb <- "'"'"" ## WLBt
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
## {du8pjGmw{?Lac}MRjH
func xoM ()	return "'"('""
dynamic my[82.492e+06,59]
'''
		expect = '''Error on line 4 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func wAO (dynamic sk3Q, number bTxR)	begin
	end
number ZK2r[2]
## {f7meJ7/<MA~
string Abt7
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
number Degm <- "'"'""
string aK <- false ## U
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
func bZ ()
	return
dynamic VPJ4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
func vZ (bool Vgj)	return
dynamic rZ[4.679e-17] <- O0
func gCj (var aOM)
	return
func rDZP (dynamic J5ai, bool B6P[76e54,99E15,33])	begin
	end

func kaeg (string w33R[112.066,2.450E+92])
	return

'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func dyMX ()
	return false
## Qj,9utk7L}%IYrR:k
## 9,x]%o:5-.cLYl
func nb (number fE)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
var Aop5 <- 7.305 ## +-bVT.
func J5 (dynamic B2A8[639.392e38,8.433], var tjCJ)
	begin
		continue
		## mYB;3Xw_12=__Q5hWn
	end
number b2
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
string aI[329E+02,953] <- false
number rh <- false
func F7r ()	begin
		## ppsWRA)
	end

bool tpHL[648e+18,404.363e53,3]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
## {_utl
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
func id (bool bp)
	return "7'"'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
number Keb ## }V[U:}
string n1l[75E+21,1.622,33.701e-81] <- 295.504E-77
func BPp (number BbG[0.165E05,289.979E+37])	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
dynamic ce <- 453e-99
func LE5 ()	return
func tKu (number MX[16.391], bool uE)	begin
		## z=+rcOKpcJXbn;KoCfvk
		begin
		end
	end
## [~})Kxh$RS
## ?
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
## ]KQs6xcbwB_Dp2`OYM
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
string GpZ[520] <- true ## T p,KF
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
## ~SA?cKj_$cp{@
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 256))
	
	def test_257(self):
		input = '''
## QwSX YcF?z4yK~Q+MO+w
## w=g,b
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
## ~If
func Qr (string yEkp, number TSuz[8,973E+42], var NGm[80e+60,6e+11,806.639e-31])
	begin
		Thy["^9'"G", oW] <- true
	end

'''
		expect = '''Error on line 3 col 46: var'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
## ^;@upWm#F_eA1jw
func Jak (string IoB, dynamic a0m, dynamic qL)
	return

'''
		expect = '''Error on line 3 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
func KtR (var OvSC[678,2.199], bool ujw[65.340])	return
func un (string yo, number Q737, string kjgF)	return "'"8W'""

func zt (string AVJ[232,870,0.982e+00], bool cTT)	begin
	end

func cqYZ (string NQ[2.218E-65], number LYnR[76.271])
	begin
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
func TM (number Js9[0,735.254], bool Rn8)	begin
		var L4Al <- 788.007
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
## L;)kD+r
func JH ()
	begin
		## &I.i>#GT
		break
		## *
	end
number zr ## gcWDsQ(Q)7>
## 7o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
var Ou
number SR[7E-23] <- "/'"'"'"'"" ## }CAV50)/Lul?
func Bgz (dynamic qH7[421.670,997,11e+84], string ZHrV[30.067,798.867e-13,0e-01])
	begin
		## f+r6+:yWiKtZ>`IOy
		if (xm)
		for EdPg until false by "P"
			IFB()
		elif (15E-30) continue
		elif (67E-95) if ("'"'"'"'"p") H3J <- "Wc=d'""
		elif (false) for in until false by "/'"B'"'""
			bool ypE[3.231,5.359,6] <- 198E-42
		## f
	end
func I8j (var w0i, bool JM, bool yaO)
	return WcH
'''
		expect = '''Error on line 2 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## N&$G9
string D6 <- 53E87
func QPa9 ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
func Aa ()	return Upj

dynamic iH[68.056e+29,2] <- a22 ## ,!x./CbrU^brg``N#
## o:)
'''
		expect = '''Error on line 4 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func yn7S (dynamic Es, bool oX)
	return
func GT (var hPsj[572e+18,122e28,673.245E51], dynamic Qv[190.937E01,926.593E31,868.895E+34])	return
string hy <- false
var E4E[460.970,499e+11,4E00]
## XC5u~3-
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
## o"_qG0cL
string zc3Z[9.609E30,202,262.231] ## On*#*O{P8&v.oyr
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
func aTk (string YBg[4.395e+52], dynamic PDbJ)
	return "m'""

func EPt ()
	begin
		## gMC5}yq?
		V0Pn()
	end
func skwk (var HyLg, number EshT, var jM)
	return "'"'"'"'""

number sHB[290.427] <- true ## zi(O<WQ<7yb&Q;!u!W7
'''
		expect = '''Error on line 2 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
func HZ (dynamic OFNp, number XS[8.572E+36,906.669])	return 8e+63

func MFT ()	return false

dynamic Gz <- oT
number RpS[956,764.345] <- "`.'"'""
number hB0[59.664,195] <- true ## rlW(_.)*n92u
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
## V_IFK#
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
##  -8
## (Qx$)!qhCT[B!H
string d6[154.564,48.039e-28] <- "d(U'"'"" ## +7Au0$omhbO`o(T"}%d
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
func bl7 (string sbXK, bool kG81[772e-77,9])	return
## 6/Kq`)%4S17,X=fFF
## W$/)~zwg_B{KJ7t>U0~
func G0jl (bool RyK8)	return AK
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
var VM6 ## aV
## A 0jsD,5e#N
'''
		expect = '''Error on line 2 col 14: 
'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
bool id_[64.606,161.310,1.632] <- 9.710
number cBKW[907]
## 08i$?
## [y>0u
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
## :N}.,V?D0qt
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
func gi (string a7, bool hA, bool o88Y[9.999e-34])	return
## VCeH
## 6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
## .?GJ8/
number h6 <- 949
## M+LjO}TbEx-lq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
bool Khe[459.494E-71] ## iU~5*T
## @E`yp2*OI_Cq25h![Z^Q
func r27 (var YdB[3.031E-62])	return
number HK6[8.369e49,1e+23] ## F=zT
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
bool SMgB ## 9t8MBUpy{*F
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
## Xt> qu}i;M3c
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
## +{]#1]p~Q
func Ge (bool WXK)
	begin
		## px8fah$<$r@4U&EB&~
	end
func Q3c (dynamic wz)	return 6e98

func Xoe (string l336)
	return

'''
		expect = '''Error on line 7 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## ,&)T^*DQau fEW4o^Jy
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func fj (dynamic t__[961.109e-73,68.111E+68,9], number lP8k, string w7pK)
	begin
		## LV?vU05MJ<7Pg
		number TnZo[594,54E+78,0.491e-62] <- 7.997e16
		for j0nT until U3 by rmch
			begin
			end
	end
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
bool iMal[657] <- true ## %3jngsh4fECq@=
dynamic xh98[655,1e+43,4E+78] ## {jBKQv$N+Y?ahu<=k1 
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
func OaxH (bool Bfd)
	return

func WOsg (number JP, dynamic rb, number TPTB[9.586])
	return 10e+05

func Ei1 (number uMV, number m1Y, string yK94)
	return true
number pBg <- 51.466 ## [
dynamic B0Rs[9.051E-28,63.704,9] ## N_Z?|C:H&5P
'''
		expect = '''Error on line 5 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
func j2oP ()	begin
		## $|@>Au.UV
	end

## _o|
var woM ## vj(
dynamic dh0[447e-00,0.040] <- r1V
'''
		expect = '''Error on line 7 col 15: 
'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
func WFyz ()
	return "]:?b|"
dynamic EZb <- false ## U-B
func sSMO (bool qfR7, bool nJ[384.740,361.873E-90,3.183E+37], bool h0)	return true
dynamic a2[91.760,258E+86,951.440e35] <- false ## vAl
'''
		expect = '''Error on line 6 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
bool uiN <- zp
dynamic Se[352,59E-37,8e+87] <- false ## B(#S9%v5IX3*
string d14[528.596e+84,2.891,5.543] <- WGg ## &@3P8vX|%Nk4ovIE
## N
func p8T ()
	return
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
number fqZ
## +UC|R<OL#94SeI=
var Ij1
func oh (string dD9l[335.937,25.300])	return "p"

'''
		expect = '''Error on line 4 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
## Pzp6
number Ab[1] ## ;Owz,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
## k
string FQe ## A,8_zDF0g0O3
## 6
func xNl ()
	return false

func mXLY (bool f8)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
## NB{=@gql"xnad)uz~I{G
## I,
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
func AwP (bool Zl)
	return

## hsOETfH6-!~Y;CZ09
var qTnH[63.366] <- true ## N
## 9GnbFq0F3`{;nCd`
'''
		expect = '''Error on line 6 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
func Ja (dynamic sY)	begin
	end
func jPMi (dynamic Hsu, number pV7)
	begin
		## !rD$
		## xK]Fjx
		break
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## Tb
func vJdO (number vE[3E-18,39.321E+17], string OoVl, string CT)
	begin
		## T)B)$Yw*c-
		bool oT9d ## /IVIUX%fa$0q~.A_%
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## ]d+Xh2x
string V2[882.454e+79,86E-13] ## p:,4Xe[
func iU1i (string qbY[72E02])
	begin
		if (440)
		JK <- ey
		elif ("X'"")
		for mDs until 46.051e-08 by "yYby"
			var u2[0] ## N~fbH`qX=xT.Tsh4`26f
		elif ("'"'"") hz(Jhga)
	end

var chcv ## :&M:ox_$_Fl.8;pI}T
'''
		expect = '''Error on line 10 col 9: ['''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
func nX (string Jhk, var jvN4)
	begin
	end
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## /(N
string TQW <- rVwi
string oUt <- mCCv ## >$EHvg]:VD,wQ=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
func LJt1 (string Mep[77.946e+45,9e-15,26.134E+40])	return
## (eZBH_>Pz{g2.3+)?t
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
func TJ (number FB[0.043e+49], number LlT)	begin
		wDfo()
		bool Qir <- "'"'"'"'"o" ## <96DVNLVu1<^CI"
	end

func rr4 (bool UUS[157], bool Ga)
	begin
		SBWX <- Y9
		##  <>yr|jdKHB
		break
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 300))