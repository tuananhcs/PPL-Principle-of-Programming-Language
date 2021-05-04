#1811442
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(self.visit(ctx.many_var_declare())+ self.visit(ctx.many_func_declare()))
    def visitMany_var_declare(self, ctx: BKITParser.Many_var_declareContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.one_var_declare())
        else:
            return self.visit(ctx.one_var_declare()) + self.visit(ctx.many_var_declare())
    def visitOne_var_declare(self, ctx: BKITParser.One_var_declareContext):
        return self.visit(ctx.id_list())
    def visitId_list(self, ctx: BKITParser.Id_listContext):
        if ctx.id_list():
            return self.visit(ctx.id_list_element()) + self.visit(ctx.id_list())
        else:
            return self.visit(ctx.id_list_element())
    def visitId_list_element(self, ctx: BKITParser.Id_list_elementContext):
        id = Id(ctx.ID().getText())
        if ctx.composit():
            dimen = self.visit(ctx.composit())
        else: dimen = []
        if ctx.ASSIGN():
            if ctx.array_literal():
                literal = self.visit(ctx.array_literal())
            else:
                literal = self.visit(ctx.literal())
        else: literal = []
        return [VarDecl(id,dimen,literal)]


    def visitComposit(self,ctx:BKITParser.CompositContext):
        intlist = ctx.INT_LITERAL()
        lst = []
        for j in intlist:
            i = j.getText()
            x = i.find('x')
            X = i.find('X')
            o = i.find('o')
            O = i.find('O')
            if (x != -1 or X != -1):
                lst += [str(int(i, 16))]
            elif (o != -1 or O != -1):
                lst += [str(int(i, 8))]
            else:
                lst += [i]
        dimen = list(map(lambda x: int(x), lst))
        return dimen

    def visitMany_func_declare(self, ctx: BKITParser.Many_func_declareContext):
        if ctx.one_func_declare():
            if ctx.many_func_declare():
                return self.visit(ctx.one_func_declare()) +  self.visit(ctx.many_func_declare())
            return self.visit(ctx.one_func_declare())
        else: return []
    def visitOne_func_declare(self, ctx: BKITParser.One_func_declareContext):
        func_name = Id(ctx.ID().getText())
        if ctx.parameter_name():
            param_list = self.visit(ctx.parameter_name())
        else:
            param_list = []
        var_list = self.visit(ctx.many_var_declare())
        stm_list = self.visit(ctx.many_stm())
        body = tuple([var_list] + [stm_list])
        return [FuncDecl(func_name, param_list,body)]
    def visitParameter_name(self, ctx: BKITParser.Parameter_nameContext):
        if ctx.parameter_name():
            return self.visit(ctx.param_list_element()) + self.visit(ctx.parameter_name())
        else:
            return self.visit(ctx.param_list_element())
    def visitParam_list_element(self,ctx: BKITParser.Param_list_elementContext):
        id = Id(ctx.ID().getText())
        dimen=[]
        if ctx.composit():
            dimen = self.visit(ctx.composit())
        return [VarDecl(id, dimen, None)]


    def visitMany_stm(self, ctx: BKITParser.Many_stmContext):
        if ctx.stm():
            if ctx.many_stm():
                return self.visit(ctx.stm()) + self.visit(ctx.many_stm())
            return self.visit(ctx.stm())
        return []

    def visitStm(self, ctx: BKITParser.StmContext):
        if ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        if ctx.call_stm():
            return self.visit(ctx.call_stm())
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.if_stm():
            return self.visit(ctx.if_stm())
        if ctx.break_stm():
            return self.visit(ctx.break_stm())
        if ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        if ctx.while_stm():
            return self.visit(ctx.while_stm())
        if ctx.do_while_stm():
            return self.visit(ctx.do_while_stm())
        if ctx.for_stm():
            return self.visit(ctx.for_stm())

    def visitAssign_stm(self, ctx: BKITParser.Assign_stmContext):
        lhs = []
        rhs = []
        if (ctx.array_cell()):
            lhs = self.visit(ctx.array_cell())
        else:
            lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.exp())
        return [Assign(lhs, rhs)]

    def visitCall_stm(self, ctx: BKITParser.Call_stmContext):
        id = Id(ctx.ID().getText())
        lst = []
        if ctx.exp():
            for i in range(len(ctx.exp())):
                lst += [self.visit(ctx.exp(i))]
        else:
            lst = []

        return [CallStmt(id, lst)]

    def visitCall_exp(self, ctx: BKITParser.Call_expContext):
        id = Id(ctx.ID().getText())
        param = []
        if ctx.exp():
            for i in range(len(ctx.exp())):
                param += [self.visit(ctx.exp(i))]
        else:
            param = []

        return CallExpr(id, param)



    def visitReturn_stm(self, ctx: BKITParser.Return_stmContext):
        if ctx.exp():
            return [Return(self.visit(ctx.exp()))]
        else:
            return [Return(None)]

    def visitBreak_stm(self,ctx:BKITParser.Break_stmContext):
        return [Break()]

    def visitContinue_stm(self,ctx:BKITParser.Continue_stmContext):
        return [Continue()]

    def visitIf_stm(self, ctx: BKITParser.If_stmContext):
        manyelseif = []
        if ctx.many_elseif():

            for i in range(len(ctx.many_elseif())):

                manyelseif += [self.visit(ctx.many_elseif(i))]
            ifthenStm = [self.visit(ctx.if_then())] + manyelseif
        else:
            ifthenStm = [self.visit(ctx.if_then())]
        if ctx.else_part():
            elseStm = self.visit(ctx.else_part())
        else:
            elseStm = ([],[])

        return [If(ifthenStm, elseStm)]
    def visitIf_then(self, ctx: BKITParser.If_thenContext):
        exp = self.visit(ctx.exp())
        list_var_decleare = self.visit(ctx.many_var_declare())
        list_stm = self.visit(ctx.many_stm())
        return (exp, list_var_decleare, list_stm)
    def visitMany_elseif(self, ctx: BKITParser.Many_elseifContext):
        exp = self.visit(ctx.exp())
        list_var_decleare = self.visit(ctx.many_var_declare())
        list_stm = self.visit(ctx.many_stm())
        return (exp, list_var_decleare, list_stm)
    def visitElse_part(self, ctx: BKITParser.Else_partContext):
        return (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))


    def visitWhile_stm(self, ctx: BKITParser.While_stmContext):
        exp = self.visit(ctx.exp())
        sl = (self.visit(ctx.many_var_declare()) , self.visit(ctx.many_stm()))
        return [While(exp,sl)]

    def visitDo_while_stm(self, ctx: BKITParser.Do_while_stmContext):
        sl = (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))
        exp = self.visit(ctx.exp())
        return [Dowhile(sl,exp)]

    def visitFor_stm(self, ctx: BKITParser.For_stmContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        loop = (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))
        return [For(id,expr1,expr2,expr3,loop)]

    def visitExp(self, ctx: BKITParser.ExpContext):
        # BinaryOP:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        else:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        return UnaryOp(ctx.NEGATION().getText(), self.visit(ctx.exp4()))
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp5()))
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.call_exp():
            return self.visit(ctx.call_exp())
        if ctx.array_cell():
            return self.visit(ctx.array_cell())
        if ctx.exp():
            return self.visit(ctx.exp())
    def visitArray_cell(self, ctx: BKITParser.Array_cellContext):
        lelf = []
        if ctx.ID():
            lelf = Id(ctx.ID().getText())
        if ctx.call_exp():
            lelf = self.visit(ctx.call_exp())
        if ctx.exp():
            lelf = self.visit(ctx.exp())
        return ArrayCell(lelf, self.visit(ctx.index_op()))
    def visitIndex_op(self, ctx: BKITParser.Index_opContext):
        if ctx.index_op():
            return [self.visit(ctx.exp())] + self.visit(ctx.index_op())
        else:
            return [self.visit(ctx.exp())]


    # LITERAL_______________________________________________________________________
    def visitArray_literal(self, ctx: BKITParser.Array_literalContext):
        lst = []
        for i in range(len(ctx.array_literal_element())):
            lst += self.visit(ctx.array_literal_element(i))
        return ArrayLiteral(lst)
    def visitArray_literal_element(self, ctx: BKITParser.Array_literal_elementContext):
        if ctx.literal():
            return [self.visit(ctx.literal())]
        else:
            return [self.visit(ctx.array_literal())]
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INT_LITERAL():
            i = ctx.INT_LITERAL().getText()
            x = i.find('x')
            X = i.find('X')
            o = i.find('o')
            O = i.find('O')
            if (x != -1 or X != -1):
                cvert = int(i, 16)
            elif (o != -1 or O != -1):
                cvert = int(i, 8)
            else:
                cvert = int(i)
            return IntLiteral(cvert)
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())











