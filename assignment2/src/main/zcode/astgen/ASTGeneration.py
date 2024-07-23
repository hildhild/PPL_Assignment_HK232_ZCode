#Student ID: 2113481

from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    # program: (NEWLINE)* list_declared EOF;
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))

    # list_declared:  declared list_declared |  declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]
    
    # declared: function | variables some_endl;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.variables())

    # variables: implicit_var | name_of_type | implicit_dynamic; 
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.name_of_type():
            return self.visit(ctx.name_of_type())
        return self.visit(ctx.implicit_dynamic())
    
    # implicit_var: VAR ID ASSIGN exp;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.ID().getText()), None, "var", self.visit(ctx.exp())) 
    
    # name_of_type: name_of_type_noass | name_of_type_ass;
    def visitName_of_type(self, ctx:ZCodeParser.Name_of_typeContext):
        if ctx.name_of_type_noass():
            return self.visit(ctx.name_of_type_noass())
        return self.visit(ctx.name_of_type_ass())
    
    # name_of_type_noass: (NUMBER | STRING | BOOL) ID (LSB list_size RSB)?;
    def visitName_of_type_noass(self, ctx:ZCodeParser.Name_of_type_noassContext):
        varType = ''
        if ctx.NUMBER():
            varType = NumberType()
        elif ctx.STRING():
            varType = StringType()
        else:
            varType = BoolType()
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), varType, None, None)
        arrType = ArrayType(self.visit(ctx.list_size()),varType)
        return VarDecl(Id(ctx.ID().getText()), arrType, None, None)
    
    # name_of_type_ass: (NUMBER | STRING | BOOL) ID (LSB list_size RSB)? ASSIGN exp;
    def visitName_of_type_ass(self, ctx:ZCodeParser.Name_of_type_assContext):
        varType = ''
        if ctx.NUMBER():
            varType = NumberType()
        elif ctx.STRING():
            varType = StringType()
        else:
            varType = BoolType()
        if ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.ID().getText()), varType, None, self.visit(ctx.exp()))
        arrType = ArrayType(self.visit(ctx.list_size()),varType)
        return VarDecl(Id(ctx.ID().getText()), arrType, None, self.visit(ctx.exp()))
    
    # list_size: NUMBER_LIT | NUMBER_LIT COMMA list_size;
    def visitList_size(self, ctx:ZCodeParser.List_sizeContext):
        if ctx.list_size():
            return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.list_size())
        return [float(ctx.NUMBER_LIT().getText())]
    
    # implicit_dynamic: implicit_dynamic_ass | implicit_dynamic_noass;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.implicit_dynamic_ass():
            return self.visit(ctx.implicit_dynamic_ass())
        return self.visit(ctx.implicit_dynamic_noass())
    
    # implicit_dynamic_noass: DYNAMIC ID;
    def visitImplicit_dynamic_noass(self, ctx:ZCodeParser.Implicit_dynamic_noassContext):
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic", None)
    
    # implicit_dynamic_ass: DYNAMIC ID ASSIGN exp;
    def visitImplicit_dynamic_ass(self, ctx:ZCodeParser.Implicit_dynamic_assContext):
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic", self.visit(ctx.exp()))

    # function: FUNC ID LP func_paralist? RP (some_endl? return_stmt |some_endl? block_stmt | some_endl); //10 case
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        if ctx.func_paralist():
            if (ctx.getChildCount() == 6) and ctx.some_endl(): #1
                return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.func_paralist()), None)
            elif ctx.return_stmt(): #2
                return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.func_paralist()), self.visit(ctx.return_stmt()))
            elif ctx.block_stmt(): #2
                return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.func_paralist()), self.visit(ctx.block_stmt()))       
        if (ctx.getChildCount() == 5) and ctx.some_endl(): #1
            return FuncDecl(Id(ctx.ID().getText()), [], None)
        elif ctx.return_stmt(): #2
            return FuncDecl(Id(ctx.ID().getText()), [], self.visit(ctx.return_stmt()))
        elif ctx.block_stmt(): #2
            return FuncDecl(Id(ctx.ID().getText()), [], self.visit(ctx.block_stmt()))
        
    # func_paralist: name_of_type_noass COMMA func_paralist | name_of_type_noass;
    def visitFunc_paralist(self, ctx:ZCodeParser.Func_paralistContext):
        if ctx.func_paralist():
            return [self.visit(ctx.name_of_type_noass())] + self.visit(ctx.func_paralist())
        return [self.visit(ctx.name_of_type_noass())]

    # exp: exp0 (CONCAT) exp0 | exp0;
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp0()[0])
        op = ctx.CONCAT().getText()
        left = self.visit(ctx.exp0()[0])
        right = self.visit(ctx.exp0()[1])
        return BinaryOp(op, left, right)

    # exp0: exp1 (EQUAL | COMPARE | DIFF | LT | GT | LTE | GTE) exp1 | exp1;
    def visitExp0(self, ctx:ZCodeParser.Exp0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1()[0])
        op = ''
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.COMPARE():
            op = ctx.COMPARE().getText()
        elif ctx.DIFF():
            op = ctx.DIFF().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()
        left = self.visit(ctx.exp1()[0])
        right = self.visit(ctx.exp1()[1])
        return BinaryOp(op, left, right)
    
    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp2())
        return BinaryOp(op, left, right)

    # exp2: exp2 (ADD | SUB) exp3 | exp3;
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        return BinaryOp(op, left, right)

    # exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        return BinaryOp(op, left, right)

    # exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        op = ctx.NOT().getText()
        operand = self.visit(ctx.exp4())
        return UnaryOp(op, operand)

    # exp5: SUB exp5 | exp6; 
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        op = ctx.SUB().getText()
        operand = self.visit(ctx.exp5())
        return UnaryOp(op, operand)

    # exp6: (ID | func_call) LSB index_operators RSB | operand; 
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        elif ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.index_operators()))
        elif ctx.func_call():
            return ArrayCell(self.visit(ctx.func_call()),self.visit(ctx.index_operators()))

    # index_operators: exp | exp COMMA index_operators;
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        if ctx.index_operators():
            return [self.visit(ctx.exp())] + self.visit(ctx.index_operators())
        return [self.visit(ctx.exp())]

    # operand: ID | literal | LP exp RP | func_call;
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.ID():
            return Id(ctx.ID().getText())

    # literal: NUMBER_LIT | STR_LIT | TRUE | FALSE | arr_lit;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        return ArrayLiteral(self.visit(ctx.arr_lit()))

    # arr_lit: LSB list_exp RSB;
    def visitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        return self.visit(ctx.list_exp())
    
    # list_exp: exp COMMA list_exp | exp;
    def visitList_exp(self, ctx:ZCodeParser.List_expContext):
        if ctx.list_exp():
            return [self.visit(ctx.exp())] + self.visit(ctx.list_exp())
        return [self.visit(ctx.exp())]

    # func_call: ID LP index_operators? RP;
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        if ctx.index_operators():
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        return CallExpr(Id(ctx.ID().getText()), [])

    # stmt: 
    # 	var_dec_stmt 
    # 	| assign_stmt
    # 	| if_stmt
    # 	| for_stmt 
    # 	| break_stmt
    # 	| continue_stmt
    # 	| return_stmt
    # 	| func_call_stmt 
    # 	| block_stmt;
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.var_dec_stmt():
            return self.visit(ctx.var_dec_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.func_call_stmt():
            return self.visit(ctx.func_call_stmt())
        return self.visit(ctx.block_stmt())

    # var_dec_stmt: variables some_endl;
    def visitVar_dec_stmt(self, ctx:ZCodeParser.Var_dec_stmtContext):
        return self.visit(ctx.variables())

    # assign_stmt: lhs ASSIGN exp some_endl;
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.exp()))
    
    # lhs: ID | index_exp; // Left hand side
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.index_exp():
            return self.visit(ctx.index_exp())
        return Id(ctx.ID().getText())

    # index_exp: ID LSB index_operators RSB;
    def visitIndex_exp(self, ctx:ZCodeParser.Index_expContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))

    # if_stmt: IF LP exp RP some_endl? stmt elif_stmtlist elsestmt;
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return If(self.visit(ctx.exp()), self.visit(ctx.stmt()), self.visit(ctx.elif_stmtlist()), self.visit(ctx.elsestmt()))
    
    # elif_stmtlist: elif_stmt elif_stmtlist |;
    def visitElif_stmtlist(self, ctx:ZCodeParser.Elif_stmtlistContext):
        if ctx.elif_stmtlist():
            return [self.visit(ctx.elif_stmt())] + self.visit(ctx.elif_stmtlist())
        return []
    
    # elif_stmt: ELIF LP exp RP some_endl? stmt;
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visit(ctx.exp()), self.visit(ctx.stmt())
    
    # elsestmt: ELSE some_endl? stmt|;
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.stmt())  

    # for_stmt: FOR ID UNTIL exp BY exp some_endl? stmt;
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.exp()[0]), self.visit(ctx.exp()[1]), self.visit(ctx.stmt()))

    # break_stmt: BREAK some_endl;
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE some_endl;
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()

    # return_stmt: RETURN exp? some_endl;
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return(None)

    #func_call_stmt: ID LP index_operators? RP some_endl;
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):  
        if ctx.index_operators():
            return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        return CallStmt(Id(ctx.ID().getText()), [])

    # block_stmt: BEGIN some_endl liststmt END some_endl;
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.liststmt()))
    
    # liststmt: stmt liststmt | ;
    def visitListstmt(self, ctx:ZCodeParser.ListstmtContext):
        if ctx.liststmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.liststmt())
        return []

    # some_endl: NEWLINE+;
    def visitSome_endl(self, ctx:ZCodeParser.Some_endlContext):
        return None
    