#StudentID: 2113481

from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, needInferType = False):
        self.frame = frame #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.needInferType = needInferType  #* kiểm có sai không, cần suy diễn-True, không cần-False

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        
        self.funcList = []
        self.function = None
        self.Return = False
        self.arrayCell = None 
    
    def infer(self, lhs, rhs, o):
        _, rtype = self.visit(rhs, Access(o.frame, o.symbol, False, True))
        _, ltype = self.visit(lhs, Access(o.frame, o.symbol, True, True))
        if type(ltype) in [FuncSymbol, VarSymbol]:
            ltype.typ = rtype
            self.emit.setType(ltype) #* cập nhật lại type vì trước đó type là None
        elif type(rtype) in [FuncSymbol, VarSymbol]:
           rtype.typ = ltype
           self.emit.setType(rtype) #* cập nhật lại type vì trước đó type là None
    
    def defaultValue(self, typ_): #khởi tạo giá trị mặc định
        varType = type(typ_)
        if varType is NumberType:
            return NumberLiteral(0.0)
        elif varType is StringType:
            return StringLiteral("")
        elif varType is BoolType:
            return BooleanLiteral(False)
        elif varType is ArrayType:
            expr = []
            if len(typ_.size) == 1:
                for x in range(typ_.size[0]):
                    expr += [self.defaultValue(typ_.typ)]
                return ArrayLiteral(expr)
            else:
                dimen = typ_.size
                for x in range(dimen[0]):
                    temp = self.defaultValue(ArrayType(dimen[1:], typ_.eleType))
                    expr += [temp]
                return ArrayLiteral(expr)
    
    def visitProgram(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        Symbol = [[]]
        Main = None #hàm main
        function = None #hàm hiện tại
        for onedecl in ast.decl:
            if type(onedecl) is FuncDecl and onedecl.body is not None:
                self.funcList += [FuncSymbol(onedecl.name.name, None, [i.varType for i in onedecl.param])]
                if onedecl.name.name == "main":
                    function = self.funcList[-1]
                    Main = onedecl
            elif type(onedecl) is VarDecl: #bien toan cuc
                Symbol[0] += [VarSymbol(onedecl.name.name, onedecl.varType, -1, True if onedecl.varInit else False)]
                self.emit.printout(self.emit.emitATTRIBUTE(onedecl.name.name, onedecl.varType if onedecl.varType else Symbol[0][-1], False, self.className))
                Symbol[0][-1].line = self.emit.newIndex()
        
        #* hàm khởi tạo trong Zcode (contructor bắt buộc)
        frame = Frame("<init>", VoidType)
        initCode = self.emit.emitMETHOD(lexeme="<init>", in_ = FuncSymbol("init", VoidType(), []), isStatic=False, frame=frame)
        frame.enterScope(True)
        initCode += self.emit.emitLABEL(frame.getStartLabel(), frame)
        initCode += self.emit.emitVAR(frame.getNewIndex(), "this", Zcode(), frame.getStartLabel(), frame.getEndLabel(), frame)
        initCode += self.emit.emitREADVAR("this", self.className, 0, frame)
        initCode += self.emit.emitINVOKESPECIAL(frame)
        initCode += self.emit.emitRETURN(VoidType(), frame)
        initCode += self.emit.emitLABEL(frame.getEndLabel(), frame)
        initCode += self.emit.emitENDMETHOD(frame)
        self.emit.printout(initCode)
        frame.exitScope()

        #* hàm khởi tạo biến static Zcode (contructor cho static)
        frame = Frame("<clinit>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncSymbol("clinit", VoidType(), []), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        #* có 2 TH là khởi tạo và khởi tạo array
        for onedecl in ast.decl:
            if type(onedecl) is VarDecl and onedecl.varInit is not None:
                self.visit(Assign(onedecl.name, onedecl.varInit), Access(frame, Symbol, False)) ,
            elif type(onedecl) is VarDecl and type(onedecl.varType) is ArrayType:
                if len(onedecl.varType.size) == 1:
                    self.emit.printout(self.visit(NumberLiteral(onedecl.varType.size[0]), Access(frame, Symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitNEWARRAY(onedecl.varType.eleType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + onedecl.name.name, onedecl.varType, frame))
                else:
                    for i in onedecl.varType.size:
                        self.emit.printout(self.visit(NumberLiteral(i), Access(frame, Symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(onedecl.varType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + onedecl.name.name, onedecl.varType, frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    

        #* khởi tạo các hàm static
        i = 0
        for onedecl in ast.decl:
            if type(onedecl) is FuncDecl and onedecl.name.name != "main" and onedecl.body is not None:
                self.function = self.funcList[i]
                self.visit(onedecl, Symbol)
            if type(onedecl) is FuncDecl and onedecl.body is not None:
                i += 1
        
        #* khởi tạo hàm main
        frame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_= FuncSymbol("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        index = frame.getNewIndex()
        paramList = [VarSymbol("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(Main.body, Access(frame, [paramList] + Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o): #biến cục bộ
        index = o.frame.getNewIndex()    
        self.emit.printout(self.emit.emitVAR(index, ast.name.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        ret_code = ""
        if ast.varInit is not None: #duoc khoi tao
            o.symbol[0] += [VarSymbol(ast.name.name, ast.varType, index, True)]
            o.symbol[0][-1].line = self.emit.newIndex()
            self.visit(Assign(ast.name, ast.varInit), o) 
        elif type(ast.varType) is ArrayType:
            if len(ast.varType.size) == 1:
                lit_code, typ = self.visit(NumberLiteral(ast.varType.size[0]), o)
                ret_code += lit_code + self.emit.emitF2I(o.frame) + self.emit.emitNEWARRAY(ast.varType.eleType, o.frame) + self.emit.emitWRITEVAR(ast.name, ast.varType, index, o.frame)
            else:
                for x in ast.varType.size:
                    lit_code, typ = self.visit(NumberLiteral(x), o)
                    ret_code += lit_code + self.emit.emitF2I(o.frame)
                ret_code += self.emit.emitMULTIANEWARRAY(ast.varType, o.frame) + self.emit.emitWRITEVAR(ast.name, ast.varType, index, o.frame)
            o.symbol[0] += [VarSymbol(ast.name.name, ast.varType, index, False)]
            o.symbol[0][-1].line = self.emit.newIndex()
        else:
            if ast.varType is not None:
                ret_code += self.visit(self.defaultValue(ast.varType), Access(o.frame, o.symbol, False))[0]
                ret_code += self.emit.emitWRITEVAR(ast.name, ast.varType, index, o.frame)
            o.symbol[0] += [VarSymbol(ast.name.name, ast.varType, index, False)]
            o.symbol[0][-1].line = self.emit.newIndex()      
        self.emit.printout(ret_code)
        return o.symbol[0][-1]      
                              
    def visitFuncDecl(self, ast, Symbol):
        self.Return = False
        function = None
        for item in self.funcList:
            if item.name == ast.name.name:
                function = item
                break
        frame = Frame(function.name, function.typ)
        self.emit.printout(self.emit.emitMETHOD(lexeme=function.name, in_= function, isStatic=True, frame=frame))
        function.line = self.emit.newIndex()
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        paramList = []
        for oneparam in ast.param:
            index =  frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, oneparam.name.name, oneparam.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            paramList += [VarSymbol(oneparam.name.name, oneparam.varType, index, oneparam.varInit)]
        index = frame.getNewIndex()
        paramList += [VarSymbol("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(ast.body, Access(frame, [paramList] + Symbol, False))
        if not self.Return:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            function.typ = VoidType()
            self.emit.setType(function)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()  
     
    def visitId(self, ast, o):
        Symbol = o.symbol
        if o.needInferType:
            for onescope in Symbol:
                for onesym in onescope:
                    if onesym.name == ast.name:
                        return None, onesym.typ if onesym.typ else onesym
        sym = None
        found = False
        for onescope in Symbol:
            for onesym in onescope:
                if onesym.name == ast.name:
                    sym = onesym
                    found = True
                    break
            if found:
                break   
        if sym:
            if o.isLeft:
                if sym.index != -1:
                    return self.emit.emitWRITEVAR(sym.name, sym.typ, sym.index, o.frame), sym.typ
                elif sym.index == -1:
                    return self.emit.emitPUTSTATIC(self.className + "." + sym.name, sym.typ, o.frame), sym.typ
            else:
                if sym.index != -1:
                    return self.emit.emitREADVAR(sym.name, sym.typ, sym.index, o.frame), sym.typ
                elif sym.index == -1:
                    return self.emit.emitGETSTATIC(self.className + "." + sym.name, sym.typ, o.frame), sym.typ                               

    def visitCallExpr(self, ast, o):
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber": 
                if o.needInferType: return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncSymbol(ast.name.name, NumberType(), []), o.frame), NumberType
            elif ast.name.name == "readBool": 
                if o.needInferType: return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncSymbol(ast.name.name, BoolType(), []), o.frame), NumberType
            elif ast.name.name == "readString": 
                if o.needInferType: return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncSymbol(ast.name.name, StringType(), []), o.frame), NumberType

        function = None
        for item in self.funcList:
            if item.name == ast.name.name:
                function = item
                
        if o.needInferType:
            for i in range(len(function.param)):
                self.infer(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function            
            
        for onearg in ast.args:
            argCode, argType = self.visit(onearg, o)
            self.emit.printout(argCode)
        return self.emit.emitINVOKESTATIC(self.className+ '/' + ast.name.name, function , o.frame), function.typ

    def visitBinaryOp(self, ast, o):
        if o.needInferType:
            if ast.op in ['+', '-', '*', '/', '%']:
                self.infer(ast.left, NumberType(), o)
                self.infer(ast.right, NumberType(), o)
                return None, NumberType()
            elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
                self.infer(ast.left, NumberType(), o)
                self.infer(ast.right, NumberType(), o)
                return None, BoolType()
            elif ast.op in ['and', 'or']:
                self.infer(ast.left, BoolType(), o)
                self.infer(ast.right, BoolType(), o)
                return None, BoolType()
            elif ast.op in ['==']:
                self.infer(ast.left, StringType(), o)
                self.infer(ast.right, StringType(), o)
                return None, BoolType()
            elif ast.op in ['...']:
                self.infer(ast.left, StringType(), o)
                self.infer(ast.right, StringType(), o)
                return None, StringType()
        
        lcode, ltype = self.visit(ast.left, o)
        rcode, rtype = self.visit(ast.right, o)
        rt = ltype
        if ast.op in ['+','-']:
            op = self.emit.emitADDOP(ast.op, ltype, o.frame)
        elif ast.op in ['*','/']:
            op = self.emit.emitMULOP(ast.op, ltype, o.frame)
        elif ast.op in ['=', '>', '<', '>=', '<=', '!=']:
            op = self.emit.emitREOP(ast.op, ltype, o.frame)
            rt = BoolType()
        elif ast.op in ['and']:
            op = self.emit.emitANDOP(o.frame)
        elif ast.op in ['or']:
            op = self.emit.emitOROP(o.frame)
        elif ast.op in ['...']:
            op = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", FuncSymbol('concat', StringType(), [StringType()]), o.frame)
        elif ast.op in ['==']:
            op = self.emit.emitINVOKEVIRTUAL("java/lang/Object/equals", FuncSymbol('equals', BoolType(), [None]), o.frame)
            rt = BoolType()
        elif ast.op in ['%']:
            op = self.emit.emitMOD(o.frame)
        return lcode + rcode + op, rt
       
    def visitUnaryOp(self, ast, o):
        if o.needInferType:
            if ast.op in ['-']:
                self.infer(ast.operand, NumberType(), o)
                return None, NumberType()
            elif ast.op in ['not']:
                self.infer(ast.operand, BoolType(), o)
                return None, BoolType()
        opcode, optype = self.visit(ast.operand, o)
        if ast.op in ['not']:
            op = self.emit.emitNOT(optype, o.frame)
        elif ast.op in ['-']:
            op = self.emit.emitNEGOP(optype, o.frame)
        return opcode + op, optype
    
    def visitArrayLiteral(self, ast, o):
        if o.needInferType:
            mainTyp = None
            for item in ast.value:
                _, checkTyp = self.visit(item, o)
                if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                    mainTyp = checkTyp
                    break
            for item in ast.value:
                self.infer(mainTyp, item, o)
            if isinstance(mainTyp, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], mainTyp)
            return None, ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)

        code = self.emit.emitPUSHCONST(str(len(ast.value)), NumberType(), o.frame)
        code += self.emit.emitF2I(o.frame)
        _, valType = self.visit(ast.value[0], o)
        if type(valType) is ArrayType:
            code += self.emit.emitANEWARRAY(valType, o.frame)
        else:
            code += self.emit.emitNEWARRAY(valType, o.frame)
        if type(ast.value[0]) is not ArrayLiteral:
            for x in range(len(ast.value)):
                code += self.emit.emitDUP(o.frame)
                code += self.emit.emitPUSHCONST(str(x), NumberType(), o.frame)
                code += self.emit.emitF2I(o.frame)
                e1c, e1t = self.visit(ast.value[x], o)
                code += e1c + self.emit.emitASTORE(e1t, o.frame)
            return code, ArrayType([len(ast.value)], valType)
        else:
            rt = None
            for x in range(len(ast.value)):
                code += self.emit.emitDUP(o.frame)
                e1c, e1t = self.visit(ast.value[x], o)
                rt = e1t
                code += self.emit.emitPUSHCONST(str(x), NumberType(), o.frame)
                code += self.emit.emitF2I(o.frame)
                code += e1c + self.emit.emitASTORE(e1t, o.frame)
            return code, ArrayType([len(ast.value)] + rt.size, rt.eleType)
       
    def visitArrayCell(self, ast, o):
        if o.needInferType:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.infer(NumberType(), i, o)
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   
        sym = None
        for onescope in o.symbol:
            found = False
            for onesym in onescope:
                if onesym.name == ast.arr.name:
                    sym = onesym
                    found = True
                    break
            if found == True:
                break
        code = None
        
        if sym.index == -1:
            code = self.emit.emitGETSTATIC(self.className + "." + sym.name, sym.typ, o.frame)
        else:
            code = self.emit.emitREADVAR(sym.name, sym.typ, sym.index, o.frame)
        dimension = sym.typ.size
        max_dimension = dimension
        for i in range(len(ast.idx)):
            dimension = dimension[1:]
            e1c, e1t = self.visit(ast.idx[i], Access(o.frame, o.symbol, False, False))
            code += e1c + self.emit.emitF2I(o.frame)
            if o.isLeft and i == len(ast.idx) - 1:
                break
            if i < len(max_dimension) - 1:
                code += self.emit.emitALOAD(ArrayType(dimension, e1t), o.frame)
            else:
                code += self.emit.emitALOAD(sym.typ.eleType, o.frame)
        if dimension == []:
            if o.isLeft:
                self.arrayCell = sym.typ.eleType
            return code, sym.typ.eleType
        else:
            if o.isLeft:
                self.arrayCell = ArrayType(dimension, sym.typ.eleType)
            return code, ArrayType(dimension, sym.typ.eleType)

    def visitReturn(self, ast, o):
        self.infer(self.function, ast.expr if ast.expr else VoidType(),o)
        self.Return = True #* đã có return
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        else:
            expCode, expType = self.visit(ast.expr, Access(o.frame, o.symbol, False))
            self.emit.printout(expCode + self.emit.emitRETURN(expType, o.frame))

    def visitAssign(self, ast, o):
        self.infer(ast.lhs, ast.rhs, o)
        rcode, _ = self.visit(ast.rhs, Access(o.frame, o.symbol, False))
        lcode, _ = self.visit(ast.lhs, Access(o.frame, o.symbol, True))
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lcode + rcode + self.emit.emitASTORE(self.arrayCell, o.frame))
        else:
            self.emit.printout(rcode + lcode)
    
    def visitCallStmt(self, ast, o):
        #* phần io
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": 
                self.infer(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool": 
                self.infer(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString": 
                self.infer(StringType(), ast.args[0], o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncSymbol(ast.name.name, VoidType(), [argsType]), o.frame))
            return
        function = None
        for item in self.funcList:
            if item.name == ast.name.name:
                function = item
                
        if o.needInferType:
            for i in range(len(function.param)):
                self.infer(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function            
        
        for onearg in ast.args:
            argCode, argType = self.visit(onearg, o)
            self.emit.printout(argCode)
        self.emit.printout(self.emit.emitINVOKESTATIC(self.className + '/' + ast.name.name, function , o.frame))
       
    def visitIf(self, ast, o):
        #* CHECK TYPE     
        self.infer(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.infer(BoolType(), item[0], o)   
       
        exitLabel = o.frame.getNewLabel()
        exprCode, exprTyp = self.visit(ast.expr, Access(o.frame, o.symbol, False))
        if ast.elifStmt: 
            elifLabel = []
            if ast.elseStmt: #có cả 3
                elseLabel = o.frame.getNewLabel()
                self.emit.printout(exprCode)
                elifLabel += [o.frame.getNewLabel()]
                self.emit.printout(self.emit.emitIFFALSE(elifLabel[0], o.frame))
                self.visit(ast.thenStmt, o)
                self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
                i = 0
                for oneElif in ast.elifStmt:
                    elifCondCode, elifCondTyp = self.visit(oneElif[0], Access(o.frame, o.symbol, False))
                    elifLabel += [o.frame.getNewLabel()]
                    self.emit.printout(self.emit.emitLABEL(elifLabel[i], o.frame))
                    self.emit.printout(elifCondCode)
                    if i == len(ast.elifStmt) - 1:
                        self.emit.printout(self.emit.emitIFFALSE(elseLabel, o.frame))
                    else:
                        self.emit.printout(self.emit.emitIFFALSE(elifLabel[i+1], o.frame))
                    self.visit(oneElif[1], o)
                    self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
                    i += 1
                self.emit.printout(self.emit.emitLABEL(elseLabel, o.frame))
                self.visit(ast.elseStmt, o)
            else: #chỉ if, elifelifLabel[0] = o.frame.getNewLabel()
                self.emit.printout(exprCode)
                elifLabel += [o.frame.getNewLabel()]
                self.emit.printout(self.emit.emitIFFALSE(elifLabel[0], o.frame))
                self.visit(ast.thenStmt, o)
                self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
                i = 0
                for oneElif in ast.elifStmt:
                    elifCondCode, elifCondTyp = self.visit(oneElif[0], Access(o.frame, o.symbol, False))
                    elifLabel += [o.frame.getNewLabel()]
                    self.emit.printout(self.emit.emitLABEL(elifLabel[i], o.frame))
                    self.emit.printout(elifCondCode)
                    if i == len(ast.elifStmt) - 1:
                        self.emit.printout(self.emit.emitIFFALSE(exitLabel, o.frame))
                    else:
                        self.emit.printout(self.emit.emitIFFALSE(elifLabel[i+1], o.frame))
                    self.visit(oneElif[1], o)
                    self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
                    i += 1
        elif ast.elseStmt: #chỉ if, else
            elseLabel = o.frame.getNewLabel()
            self.emit.printout(exprCode)
            self.emit.printout(self.emit.emitIFFALSE(elseLabel, o.frame))
            self.visit(ast.thenStmt, o)
            self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
            self.emit.printout(self.emit.emitLABEL(elseLabel, o.frame))
            self.visit(ast.elseStmt, o)
        else: #chỉ if
            self.emit.printout(exprCode)
            self.emit.printout(self.emit.emitIFFALSE(exitLabel, o.frame))
            self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))  
        
    def visitFor(self, ast, o):      
        self.infer(NumberType(), ast.name, o)         
        self.infer(BoolType(), ast.condExpr, o)        
        self.infer(NumberType(), ast.updExpr, o) 
        self.visit(ast.name, o)
        self.visit(Assign(Id("for"), ast.name), o)
        o.frame.enterLoop()
        loopLabel = o.frame.getNewLabel()
        continueLabel = o.frame.getContinueLabel()
        exitLabel = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(loopLabel, o.frame))
        condCode, condType = self.visit(ast.condExpr, Access(o.frame, o.symbol, False))
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFTRUE(exitLabel, o.frame))
        self.visit(ast.body, o)
        self.emit.printout(self.emit.emitLABEL(continueLabel, o.frame))
        self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        self.emit.printout(self.emit.emitGOTO(loopLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))
        o.frame.exitLoop()
        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        
    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol #! tăng tầm vực
        o.frame.enterScope(False) #* tầm vực mới, vì biến khởi tạo sẽ được xóa khi kết thúc tầm vực nên cần scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame)) #* đánh số tầm vực mới
        for onestmt in ast.stmt: 
            self.visit(onestmt, Access(o.frame, symbolnew, False))   
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame)) #* đánh số tầm vực mới
        o.frame.exitScope()  #* kết thức tầm vực
        
    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if not o.needInferType else None, NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if not o.needInferType else None, BoolType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if not o.needInferType else None, StringType()
    
    def visitArrayType(self, ast, param): 
        return None, ast
    
    def visitNumberType(self, ast, param): 
        return None, NumberType()
    
    def visitVoidType(self, ast, param): 
        return None, VoidType()
    
    def visitBoolType(self, ast, param): 
        return None, BoolType()
    
    def visitStringType(self, ast, param): 
        return None, StringType()
    
    def visitFuncSymbol(self, ast, param): 
        return None, ast.typ if ast.typ else ast
    
    def visitVarZcode(self, ast, param): 
        return None, ast.typ if ast.typ else ast
