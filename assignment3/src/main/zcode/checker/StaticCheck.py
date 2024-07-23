#Student ID: 2113481

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncSymbol(Zcode):
    def __init__(self, name = "", param = [], typ = None, body = False):
        self.name = name
        self.param = param #danh sách các type của các param
        self.typ = typ #type của hàm
        self.body = body #True nếu có body trong khai báo

class VarSymbol(Zcode):
    def __init__(self, name = "", typ = None):
        self.name = name
        self.typ = typ #type của biến

class ArraySymbol(Type):
    #* eleTypeList: List[Type] Type là Zcode hoặc ArrayZcode
    def __init__(self, eleTypeList):
        self.eleTypeList = eleTypeList

class CannotBeInferredSymbol(Type):
    def __init__(self, name = ""):
        self.name = name

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.numForIn = 0 #so vong for dang vao
        self.function = None #ham hien tai
        self.haveReturn = False #ham hien tai co return khong
        self.funcList = { #danh sach cac ham
                "readNumber" : FuncSymbol("readNumber", [], NumberType(), True),
                "readBool" : FuncSymbol("readBool", [], BoolType(), True),
                "readString" : FuncSymbol("readString", [], StringType(), True),
                "writeNumber" : FuncSymbol("writeNumber", [NumberType()], VoidType(), True),
                "writeBool" : FuncSymbol("writeBool", [BoolType()], VoidType(), True),
                "writeString" : FuncSymbol("writeString", [StringType()], VoidType(), True)
                }
        
    def check(self):
        self.visit(self.ast, [{}])
        return None    
    
    def arrayTypeCmp(self, typ1, typ2):
        if type(typ1.eleType) != type(typ2.eleType):
            return False
        elif type(typ1.eleType) is ArrayType:
            return self.arrayTypeCmp(typ1.eleType, typ2.eleType) and typ1.size == typ2.size
        return typ1.size == typ2.size
    
    def typeCmp(self, typ1, typ2):
        if type(typ1) is ArrayType and type(typ2) is ArrayType:
            return self.arrayTypeCmp(typ1, typ2)
        elif type(typ1) == type(typ2):
            return True
        return False   
    
    def listTypeCmp(self, listtyp1, listtyp2):
        if len(listtyp1) != len(listtyp2):
            return False   
        for typ1, typ2 in zip(listtyp1, listtyp2):
            if not self.typeCmp(typ1, typ2):
                return False
        return True
    
    def inferVar(self, scope_list, idname, typ, raiseAst = None):
        for oneScope in scope_list:
            if oneScope.get(idname):
                if oneScope[idname].typ is None or self.typeCmp(oneScope[idname].typ, typ):
                    oneScope[idname].typ = typ
                    return typ
                else:
                    raise TypeMismatchInExpression(raiseAst)
    
    def inferFunc(self, funcList, idname, typ, raiseAst = None):
        if self.funcList.get(idname):
            if funcList[idname].typ is None or self.typeCmp(funcList[idname].typ, typ):
                funcList[idname].typ = typ
                return typ
            else:
                raise TypeMismatchInExpression(raiseAst)
    
    def inferArray(self, typeArray, typeArraySymbol, typeArraySymbolAst, o, forSubExpr):
        if typeArray.size[0] != len(typeArraySymbol.eleTypeList):
            if forSubExpr:
                raise TypeMismatchInExpression(typeArraySymbolAst)
            else:
                return False
        if len(typeArray.size) == 1:
            for eleType in typeArraySymbol.eleTypeList:
                if type(eleType) is VarSymbol:
                    self.inferVar(o, eleType.name, typeArray.eleType, typeArraySymbolAst)
                elif type(eleType) is FuncSymbol:
                    self.inferFunc(self.funcList, eleType.name, typeArray.eleType, typeArraySymbolAst)
                elif type(eleType) is ArraySymbol:
                    return False
            return True
        else:
            for eleType in typeArraySymbol.eleTypeList:
                if type(eleType) is VarSymbol:
                    eleType.typ = self.inferVar(o, eleType.name, ArrayType(typeArray.size[1:], typeArray.eleType), typeArraySymbolAst)
                elif type(eleType) is FuncSymbol:
                    eleType.typ = self.inferFunc(self.funcList, eleType.name, ArrayType(typeArray.size[1:], typeArray.eleType), typeArraySymbolAst)
                elif type(eleType) is ArraySymbol:
                    if not self.inferArray(ArrayType(typeArray.size[1:], typeArray.eleType), eleType, typeArraySymbolAst, o, True):
                        return False
            return True
                
    def inferTypeForExpr(self, ast, ltyp, last, rtyp, rast, o):
        if type(ltyp) is CannotBeInferredSymbol or type(rtyp) is CannotBeInferredSymbol:
            return False
        if type(ltyp) in [VarSymbol, FuncSymbol, ArraySymbol] and type(rtyp) in [VarSymbol, FuncSymbol, ArraySymbol]:
            return False
        elif type(ltyp) is ArrayType and type(rtyp) is ArraySymbol:
            if self.inferArray(ltyp, rtyp, rast, o, True):
                return True
            else:
                raise TypeMismatchInExpression(ast)
        elif type(rtyp) is ArraySymbol:
            return False
        elif type(ltyp) is VarSymbol and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferVar(o, last.name, rtyp, rast)
        elif type(ltyp) is FuncSymbol and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferFunc(self.funcList, last.name.name, rtyp, rast)
        elif type(rtyp) is VarSymbol and type(ltyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferVar(o, rast.name, ltyp, last)
        elif type(rtyp) is FuncSymbol and type(ltyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferFunc(self.funcList, rast.name.name, ltyp, last)
        elif type(ltyp) in [NumberType, BoolType, StringType, ArrayType] and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            if self.typeCmp(ltyp, rtyp):
                return True
            else:
                raise TypeMismatchInExpression(ast)
        return True
    
    def inferTypeForStmt(self, ast, ltyp, last, rtyp, rast, o):
        if type(ltyp) is CannotBeInferredSymbol or type(rtyp) is CannotBeInferredSymbol:
            raise TypeCannotBeInferred(ast)
        if type(ltyp) in [VarSymbol, FuncSymbol, ArraySymbol] and type(rtyp) in [VarSymbol, FuncSymbol, ArraySymbol]:
            raise TypeCannotBeInferred(ast)
        elif type(ltyp) is ArrayType and type(rtyp) is ArraySymbol:
            if self.inferArray(ltyp, rtyp, rast, o, False):
                return
            else:
                raise TypeMismatchInStatement(ast)
        elif type(rtyp) is ArraySymbol:
            raise TypeCannotBeInferred(ast)
        elif type(ltyp) is VarSymbol and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferVar(o, last.name, rtyp, rast)
        elif type(ltyp) is FuncSymbol and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferFunc(self.funcList, last.name.name, rtyp, rast)
        elif type(rtyp) is VarSymbol and type(ltyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferVar(o, rast.name, ltyp, last)
        elif type(rtyp) is FuncSymbol and type(ltyp) in [NumberType, BoolType, StringType, ArrayType]:
            self.inferFunc(self.funcList, rast.name.name, ltyp, last)
        elif type(ltyp) in [NumberType, BoolType, StringType, ArrayType] and type(rtyp) in [NumberType, BoolType, StringType, ArrayType]:
            if self.typeCmp(ltyp, rtyp):
                return
            else:
                raise TypeMismatchInStatement(ast)     
                
    def visitProgram(self, ast, o):
        for onedecl in ast.decl: 
            self.visit(onedecl, o)
        
        for key, symbol in zip(self.funcList.keys(), self.funcList.values()):
            if type(symbol) is FuncSymbol:
                if not symbol.body:
                    raise NoDefinition(key)
 
        if not self.funcList.get("main"):
            raise NoEntryPoint()
        if type(self.funcList["main"]) is not FuncSymbol:
            raise NoEntryPoint()
        if len(self.funcList["main"].param) != 0:
            raise NoEntryPoint()
        if type(self.funcList["main"].typ) is not VoidType:
            raise NoEntryPoint()
                
    def visitVarDecl(self, ast, o):
        isParam = False
        if o[-1] == 'param':
            isParam = True
            o.remove('param')
        
        isCheckRedecl = True
        if o[-1] == 'noCheckParam':
            isCheckRedecl = False
            o.remove('noCheckParam')
        
        if o[0].get(ast.name.name):
            if isParam:
                raise Redeclared(Parameter(), ast.name.name)
            elif isCheckRedecl:
                raise Redeclared(Variable(), ast.name.name)
    
        o[0][ast.name.name] = VarSymbol(ast.name.name, ast.varType) 

        if ast.varInit: 
            rtype = self.visit(ast.varInit, o)
            if ast.varType is not None:
                ltype = ast.varType
            else:
                ltype = self.visit(ast.name, o)
            self.inferTypeForStmt(ast, ltype, ast.name, rtype, ast.varInit, o)
            
    def visitFuncDecl(self, ast, o):
        paramList = [{}]    
        if len(ast.param) != 0:
            for oneparam in ast.param:
                if ast.body is not None:
                    self.visit(oneparam, paramList + ['param'])
                else:
                    self.visit(oneparam, paramList + ['noCheckParam'])
                
        paramTypeList = []
        for oneparam in ast.param:
            paramTypeList.append(oneparam.varType)
        if self.funcList.get(ast.name.name):
            if self.funcList[ast.name.name].body == True:
                raise Redeclared(Function(), ast.name.name)
            if self.listTypeCmp(paramTypeList, self.funcList[ast.name.name].param):
                if ast.body is not None:
                    self.funcList[ast.name.name].body = True
                else:
                    raise Redeclared(Function(), ast.name.name)
            else:
                raise Redeclared(Function(), ast.name.name)
        else:
            body = True
            if ast.body is None:
                body = False
            self.funcList[ast.name.name] = FuncSymbol(ast.name.name, paramTypeList, None, body)
        
        self.function = self.funcList[ast.name.name], ast.name.name
        
        self.haveReturn = False 
        if ast.body is not None:
            self.visit(ast.body, paramList + o)
            if not self.haveReturn:
                if self.funcList[ast.name.name].typ is None:
                    self.funcList[ast.name.name].typ = VoidType()
                elif not self.typeCmp(self.funcList[ast.name.name].typ, VoidType()): 
                    raise TypeMismatchInStatement(Return(None))
        return

    def visitId(self, ast, o):
        find = False
        idType = None
        idExpr = None
        for oneScope in o:
            if oneScope.get(ast.name):
                idExpr = oneScope[ast.name]
                idType = oneScope[ast.name].typ
                find = True
                break
        if find == False:
            raise Undeclared(Identifier(), ast.name)
        if idType is not None:
            return idType
        else:
            return idExpr

    def visitBinaryOp(self, ast, o):
        ltype = self.visit(ast.left, o)
        if ast.op in ['+', '-', '*', '/', '%']:
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", ltype, ast.left, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", ltype, ast.left, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['and', 'or']:
            canInfered = self.inferTypeForExpr(ast, BoolType(), "", ltype, ast.left, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['==']:
            canInfered = self.inferTypeForExpr(ast, StringType(), "", ltype, ast.left, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['...']:
            canInfered = self.inferTypeForExpr(ast, StringType(), "", ltype, ast.left, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        
        rtype = self.visit(ast.right, o)
        if ast.op in ['+', '-', '*', '/', '%']:
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", rtype, ast.right, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", rtype, ast.right, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['and', 'or']:
            canInfered = self.inferTypeForExpr(ast, BoolType(), "", rtype, ast.right, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['==']:
            canInfered = self.inferTypeForExpr(ast, StringType(), "", rtype, ast.right, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        elif ast.op in ['...']:
            canInfered = self.inferTypeForExpr(ast, StringType(), "", rtype, ast.right, o)
            if not canInfered:
                return CannotBeInferredSymbol()
        if ast.op in ['+', '-', '*', '/', '%']:
            return NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            return BoolType()
        elif ast.op in ['and', 'or']:
            return BoolType()
        elif ast.op in ['==']:
            return BoolType()
        elif ast.op in ['...']:
            return StringType()

    def visitUnaryOp(self, ast, o):
        otype = self.visit(ast.operand, o)
        if ast.op in ['-']:
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", otype, ast.operand, o)
            if not canInfered:
                return CannotBeInferredSymbol()
            return NumberType()
        elif ast.op in ['not']:
            canInfered = self.inferTypeForExpr(ast, BoolType(), "", otype, ast.operand, o)
            if not canInfered:
                return CannotBeInferredSymbol()
            return BoolType()

    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if type(arr) in [BoolType, StringType, NumberType]:
            raise TypeMismatchInExpression(ast)
        elif type(arr) is not ArrayType:
            return CannotBeInferredSymbol()
          
        for ele in ast.idx:
            eleType = self.visit(ele, o)
            canInfered = self.inferTypeForExpr(ast, NumberType(), "", eleType, ele, o)
            if not canInfered:
                return CannotBeInferredSymbol()

        if len(arr.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx):
            return arr.eleType
        else:
            sub = len(arr.size) - len(ast.idx)
            newSize = arr.size[len(arr.size) - sub:]
            return ArrayType(newSize, arr.eleType)

    def visitCallExpr(self, ast, o):
        argList = [self.visit(onearg, o) for onearg in ast.args]
        if self.funcList.get(ast.name.name):
            paramList =  self.funcList[ast.name.name].param
            if len(argList) != len(paramList):
                raise TypeMismatchInExpression(ast)
            i = 0
            for onearg, oneparam in zip(argList, paramList):
                canInfered = self.inferTypeForExpr(ast, oneparam, "", onearg, ast.args[i], o)
                if not canInfered:
                    return CannotBeInferredSymbol()
                i+=1
            if self.funcList[ast.name.name].typ is None:
                return self.funcList[ast.name.name]
            elif self.typeCmp(self.funcList[ast.name.name].typ, VoidType()):
                raise TypeMismatchInExpression(ast)
            else:
                return self.funcList[ast.name.name].typ
        else:
            raise Undeclared(Function(), ast.name.name)
        
    def visitAssign(self, ast, o):
        rtype = self.visit(ast.rhs, o)
        ltype = self.visit(ast.lhs, o)
        self.inferTypeForStmt(ast, ltype, ast.lhs, rtype, ast.rhs, o)            
        
    def visitIf(self, ast, o): 
        exprTyp = self.visit(ast.expr, o)
        self.inferTypeForStmt(ast, BoolType(), "", exprTyp, ast.expr, o)
        self.visit(ast.thenStmt, o)
          
        for oneElif in ast.elifStmt:
            exprTyp = self.visit(oneElif[0], o)
            self.inferTypeForStmt(ast, BoolType(), "", exprTyp, oneElif[0], o)
            self.visit(oneElif[1], o)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)
    
    def visitFor(self, ast, o): 
        idTyp = self.visit(ast.name, o)
        self.inferTypeForStmt(ast, NumberType(), "", idTyp, ast.name, o)
        condExprTyp = self.visit(ast.condExpr, o)
        self.inferTypeForStmt(ast, BoolType(), "", condExprTyp, ast.condExpr, o)
        updExprTyp = self.visit(ast.updExpr, o)
        self.inferTypeForStmt(ast, NumberType(), "", updExprTyp, ast.updExpr, o)
        
        self.numForIn += 1 
        self.visit(ast.body, o)
        self.numForIn -= 1 
    
    def visitBreak(self, ast, o):
        if self.numForIn == 0: 
            raise MustInLoop(ast)
        return None

    def visitContinue(self, ast, o):
        if self.numForIn == 0: 
            raise MustInLoop(ast)
        return None
    
    def visitReturn(self, ast, o):
        self.haveReturn = True

        if ast.expr is None:
            funcType = self.function[0].typ
            if funcType is None:
                self.function[0].typ = VoidType()
                self.funcList[self.function[1]].typ = VoidType()
                return
            else:
                if type(funcType) is not VoidType:
                    raise TypeMismatchInStatement(ast) 
        else:   
            returnExp = self.visit(ast.expr, o)
            funcType = self.function[0].typ
            if type(returnExp) in [FuncSymbol, VarSymbol, ArraySymbol, CannotBeInferredSymbol] and funcType is None:
                raise TypeCannotBeInferred(ast)
            if type(funcType) in [NumberType, BoolType, StringType, ArrayType]:
                if type(returnExp) is FuncSymbol:
                    self.inferFunc(self.funcList, ast.expr.name.name, funcType, ast.expr)
                    return
                elif type(returnExp) is VarSymbol:
                    self.inferVar(o, ast.expr.name, funcType, ast.expr)
                    return
                elif type(returnExp) is ArraySymbol:
                    if type(funcType) in [NumberType, BoolType, StringType]:
                        raise TypeMismatchInStatement(ast)
                    elif type(funcType) is ArrayType:
                        if self.inferArray(funcType, returnExp, ast.expr, o, False):
                            return
                        else:
                            raise TypeMismatchInStatement(ast)
                elif not self.typeCmp(returnExp, funcType):
                    raise TypeMismatchInStatement(ast)  
            elif type(funcType) is VoidType:
                raise TypeMismatchInStatement(ast)   
            else:
                self.function[0].typ = returnExp
                self.funcList[self.function[1]].typ = returnExp
                return
    
    def visitCallStmt(self, ast, o):
        argList = [self.visit(onearg, o) for onearg in ast.args]
        if self.funcList.get(ast.name.name):
            paramList =  self.funcList[ast.name.name].param
            if len(argList) != len(paramList):
                raise TypeMismatchInStatement(ast)
            i = 0
            for onearg, oneparam in zip(argList, paramList):
                self.inferTypeForStmt(ast, oneparam, "", onearg, ast.args[i], o)
                i+=1
            if self.funcList[ast.name.name].typ is None:
                self.funcList[ast.name.name].typ = VoidType()
                return self.funcList[ast.name.name]
            elif not self.typeCmp(self.funcList[ast.name.name].typ, VoidType()):
                raise TypeMismatchInStatement(ast)
            else:
                return self.funcList[ast.name.name].typ
        else:
            raise Undeclared(Function(), ast.name.name)

    def visitBlock(self, ast, o):
        oNew = [{}] + o 
        for onestmt in ast.stmt: 
            self.visit(onestmt, oNew)   

    def visitNumberType(self, ast, o): 
        return ast
    
    def visitBoolType(self, ast, o): 
        return ast
    
    def visitStringType(self, ast, o): 
        return ast
    
    def visitArrayType(self, ast, o): 
        return ast
    
    def visitNumberLiteral(self, ast, o): 
        return NumberType()
    
    def visitBooleanLiteral(self, ast, o): 
        return BoolType()
    
    def visitStringLiteral(self, ast, o): 
        return StringType()
    
    def visitArrayLiteral(self, ast, o):
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, o)
            if typ is None and type(checkTyp) in [BoolType, StringType, NumberType, ArrayType]:
                typ = checkTyp
            elif type(checkTyp) is CannotBeInferredSymbol:
                return CannotBeInferredSymbol()
            
        if typ is None:
            return ArraySymbol([self.visit(item, o) for item in ast.value])
        elif type(typ) in [StringType, BoolType, NumberType]:
            for item in ast.value:
                checkTyp = self.visit(item, o)
                if self.typeCmp(typ, checkTyp):  
                    continue
                elif type(checkTyp) is VarSymbol:
                    self.inferVar(o, item.name, typ, item)
                elif type(checkTyp) is FuncSymbol:
                    self.inferFunc(self.funcList, item.name.name, typ, item)
                elif type(checkTyp) is ArraySymbol:
                    return CannotBeInferredSymbol()
                else:
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)], typ)
        else:
            for item in ast.value:
                checkTyp = self.visit(item, o)
                if self.typeCmp(typ, checkTyp):  
                    continue
                elif type(checkTyp) is VarSymbol:
                    self.inferVar(o, item.name, typ, item)
                elif type(checkTyp) is FuncSymbol:
                    self.inferFunc(self.funcList, item.name.name, typ, item)
                elif type(checkTyp) is ArraySymbol:
                    if self.inferArray(typ, checkTyp, item, o, False):
                        continue
                    else:
                        raise TypeMismatchInExpression(ast) 
                else:
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)] + typ.size, typ.eleType)