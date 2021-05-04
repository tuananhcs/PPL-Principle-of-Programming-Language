import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Var:x[1][2][3];"""
        expect = Program([VarDecl(Id("x"), [1,2,3], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """
        Var:x, y[1][2][3];
        """
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"),[1,2,3], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """
        Var:x, z = 1, y[1][2][3];
        """
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("z"),[], IntLiteral(1)),VarDecl(Id("y"),[1,2,3], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """
        Var: y = 10., z = 10.e-7;
        """
        expect = Program([VarDecl(Id('y'),[],FloatLiteral(10.0)),VarDecl(Id('z'),[],FloatLiteral(1e-06))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """
        Var: z = True, y = 0xAF;
        """
        expect = Program([VarDecl(Id('z'),[],BooleanLiteral(True)),VarDecl(Id('y'),[],IntLiteral(175))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """
        Var:x, z = "abc \\t";
        """
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("z"),[], StringLiteral("abc \\t"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = """
        Var:x = {1,1.5e+7,"abc"};
        Var:y = {1,2,{3,4}};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),FloatLiteral(15000000.0),StringLiteral('abc')])),VarDecl(Id('y'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test8(self):
        input = """ Var: x, y;"""
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test9(self):
        input = """ Var: x;
        Var: y;"""
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test10(self):
        input = """
        Function: main
        Parameter: n, m[10]
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None),VarDecl(Id("m"),[10],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test11(self):
        input = """
        Function: main
        Body:
        Var: a = 5, b[1];
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[1],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test12(self):
        input = """
        Var: a = 5, b[1];
        Function: main
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[1],None),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test13(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test14(self):
        input = """
        Function: main
        Body:
        Var: x, y;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test15(self):
        input = """
        Function: main
        Body:
        Var: x, y[1][2];
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1,2],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test16(self):
        input = """
        Function: main
        Body:
        Continue;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test17(self):
        input = """
        Function: main
        Body:
        Break;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test18(self):
        input = """
        Function: main
        Body:
        Return ;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test19(self):
        input = """
        Function: main
        Body:
        Return a[1][2][3];
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Return(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test20(self):
        input = """
        Function: main
        Body:
        a[1][2+3] = 1;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(1),BinaryOp("+",IntLiteral(2),IntLiteral(3))]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test21(self):
        input = """
        Function: main
        Body:
        While 1 Do
        Continue;
        Return 1;
        EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(IntLiteral(1),([],[Continue(),Return(IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test22(self):
        input = """
        Function: main
        Body:
        For (a = 1, a < 10, 2) Do
        a = 1 + 2 > 3;
        Break;
        EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("a"),IntLiteral(1),BinaryOp("<",Id("a"),IntLiteral(10)),IntLiteral(2),([],[Assign(Id("a"),BinaryOp(">",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test23(self):
        input = """
        Function: main
        Body:
        a = foo();
        foo1();
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),CallExpr(Id("foo"),[])),CallStmt(Id("foo1"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test24(self):
        input = """
        Function: main
        Body:
        Do
        foo();
        Return;
        While 1 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[CallStmt(Id("foo"),[]),Return(None)]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test25(self):
        input = """
        Function: main
        Body:
        If 1 Then Return ;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[Return(None)])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        input = """
        Function: main
        Body:
        If 1 Then Return ;
        ElseIf 2 Then Continue;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[Return(None)]),(IntLiteral(2),[],[Continue()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test27(self):
        input = """
        Function: main
        Body:
        If 1 Then Return ;
        ElseIf 2 Then a=1;
        Else
        Break;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[Return(None)]),(IntLiteral(2),[],[Assign(Id("a"),IntLiteral(1))])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test28(self):
        input = r"""Function: iffull


            Parameter: themdauchamphay
            Body:
                If n == 0 Then
                    Return 1;
                ElseIf (n>0) Then
                    Return n * fact (n - 1);
                Else
                    Return n;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id("iffull"), [VarDecl(Id("themdauchamphay"), [], None)], ([], [If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]), (BinaryOp(">", Id("n"), IntLiteral(0)), [],[Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))])],([], [Return(Id("n"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        """Created automatically"""
        input = r"""Function: iflongnhau
        Parameter: a, b
        Body:
        Var: id[4412][867][9856][867], stringID[108] = "day la \\ 1 chuoi !!",literal = 120000e-1,  array[2][4] = {{867,445,987},{76,12,744}};
            If n > 10 Then
                If n <. 20.5 Then Return x;
                EndIf.
                printStrLn(arg);
            Else fact(x);
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("iflongnhau"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("id"),[4412,867,9856,867],None),VarDecl(Id("stringID"),[108],StringLiteral("day la \\\\ 1 chuoi !!")),VarDecl(Id("literal"),[],FloatLiteral(12000.0)),VarDecl(Id("array"),[2,4],ArrayLiteral([ArrayLiteral([IntLiteral(867),IntLiteral(445),IntLiteral(987)]),ArrayLiteral([IntLiteral(76),IntLiteral(12),IntLiteral(744)])]))],[If([(BinaryOp(">",Id("n"),IntLiteral(10)),[],[If([(BinaryOp("<.",Id("n"),FloatLiteral(20.5)),[],[Return(Id("x"))])],([],[])),CallStmt(Id("printStrLn"),[Id("arg")])])],([],[CallStmt(Id("fact"),[Id("x")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))


    ############### test ################

    def test_330(self):
        """Created automatically"""
        input = r"""Var: faji342F__324dADS;"""
        expect = Program([VarDecl(Id("faji342F__324dADS"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_331(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
        """
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5)), VarDecl(Id("b"), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]),ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), VarDecl(Id("c"), [], None),VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None),VarDecl(Id("f"), [], None), VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        """Created automatically"""
        input = r"""
        Var: decimal[108], hexadecimal[0X5456A][0x205F], octdecimal[0o413215][0O123];
        Var: array[5][13456];
        """
        expect = Program([VarDecl(Id("decimal"), [108], None), VarDecl(Id("hexadecimal"), [345450, 8287], None),VarDecl(Id("octdecimal"), [136845, 83], None), VarDecl(Id("array"), [5, 13456], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        """Created automatically"""
        input = r"""
        Var: dsa[432][0X364][0o35721], b = 20.e5, c = "mot con vit xoe ra 2 \n cai canh";
        """
        expect = Program([VarDecl(Id("dsa"), [432, 868, 15313], None), VarDecl(Id("b"), [], FloatLiteral(2000000.0)),VarDecl(Id("c"), [], StringLiteral("mot con vit xoe ra 2 \\n cai canh"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        """Created automatically"""
        input = r"""
        Var: x = {**comment trong array**{34221}, {"fsd\\h" **cmt**},2};
        """
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral([ArrayLiteral([IntLiteral(34221)]), ArrayLiteral([StringLiteral("fsd\\\\h")]), IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self):
        """Created automatically"""
        input = r"""
        Var **COMMENT**: ****id = 465632
        **dsfhfsdhjnc^#%#@@~!**;
    Var: sss;
        """
        expect = Program([VarDecl(Id("id"), [], IntLiteral(465632)), VarDecl(Id("sss"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        """Created automatically"""
        input = r"""
        Function: abc
        Parameter: global_var
        Body:
            dayLA1_teNbIen = 25+6-.2.5%3\100 ;
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc"), [VarDecl(Id("global_var"), [], None)], ([], [Assign(Id("dayLA1_teNbIen"), BinaryOp("-.", BinaryOp("+", IntLiteral(25), IntLiteral(6)),BinaryOp("\\", BinaryOp("%", FloatLiteral(2.5), IntLiteral(3)),IntLiteral(100))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        """Created automatically"""
        input = r""" Function: emptybody
        Parameter: var
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id("emptybody"), [VarDecl(Id("var"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        """Created automatically"""
        input = r"""
        Function: **comment chut da**cocomment
        Body:
            x=20;
                x=100.0;
        EndBody.
        """
        expect = Program([FuncDecl(Id("cocomment"), [],([], [Assign(Id("x"), IntLiteral(20)), Assign(Id("x"), FloatLiteral(100.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        """Created automatically"""
        input = r""" Function: if
        Body:
            If x==i Then Break;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if"), [], ([], [If([(BinaryOp("==", Id("x"), Id("i")), [], [Break()])], ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        """Created automatically"""
        input = r"""
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody."""
        expect = Program([VarDecl(Id("x"), [], None), FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([], [
            If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))])], ([], [
                Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]))])),
                          FuncDecl(Id("main"), [],
                                   ([], [Assign(Id("x"), IntLiteral(10)), CallStmt(Id("fact"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        """Created automatically"""
        input = r"""
        Function: parameter
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body:
            a=1;
        EndBody.
        """
        expect = Program([FuncDecl(Id("parameter"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None),
                                                     VarDecl(Id("c"), [123], None),
                                                     VarDecl(Id("d"), [123, 234, 0], None),
                                                     VarDecl(Id("e"), [], None)],
                                   ([], [Assign(Id("a"), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        """Created automatically"""
        input = r"""Function: iffull


        Parameter: themdauchamphay
        Body:
            If n == 0 Then
                Return 1;
            ElseIf (n>0) Then
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("iffull"), [VarDecl(Id("themdauchamphay"), [], None)], ([], [If(
            [(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]), (
            BinaryOp(">", Id("n"), IntLiteral(0)), [],
            [Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))])],
            ([], [Return(Id("n"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        """Created automatically"""
        input = r"""Function: initvalueparam
        Parameter: n, arr[5]
        Body:
            Var: r = 10., v;
        EndBody."""
        expect = Program([FuncDecl(Id("initvalueparam"),
                                   [VarDecl(Id("n"), [], None), VarDecl(Id("arr"), [5], None)],
                                   ([VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id("v"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        """Created automatically"""
        input = r"""Function: varinstmtlist
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                i = i + 1;
            While i <= 10
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("varinstmtlist"), [], ([VarDecl(Id("i"), [], IntLiteral(0))], [Dowhile(
            ([VarDecl(Id("k"), [], IntLiteral(10))], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]),
            BinaryOp("<=", Id("i"), IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        """Created automatically"""
        input = r"""
        Function: foroke
        Body:
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foroke"), [], ([], [
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2),
                ([], [CallStmt(Id("writeln"), [Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        """Created automatically"""
        input = r"""
        Function: forinitfail
        Parameter: n[5]
        Body:
            For (i = 0, i < 10, 1) Do
                n[i]=n+i;
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("forinitfail"), [VarDecl(Id("n"), [5], None)], ([], [
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(ArrayCell(Id("n"), [Id("i")]), BinaryOp("+", Id("n"), Id("i")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        """Created automatically"""
        input = r"""
        Function: formissing
        Body:
            For (i=12, i < k, i*i) Do
            goo();
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("formissing"), [], ([], [
            For(Id("i"), IntLiteral(12), BinaryOp("<", Id("i"), Id("k")), BinaryOp("*", Id("i"), Id("i")),
                ([], [CallStmt(Id("goo"), [])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        """Created automatically"""
        input = r"""
        Function: fornotendfor
        Body:
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("fornotendfor"), [], ([], [
            For(Id("i"), IntLiteral(1), BinaryOp("<=", Id("i"), BinaryOp("*", Id("x"), Id("x"))),
                BinaryOp("+.", BinaryOp("*", Id("i"), Id("i")), FloatLiteral(1.5)),
                ([], [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        """Created automatically"""
        input = r"""
        Function: forinfor
        Parameter: row,col,sum,arr[5][9]
        Body:
            Var: sum=0;
            For( i=0,i<=row,1) Do
                For(j=0,j<col,2) Do
                    sum=sum+arr[i][j];
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("forinfor"), [VarDecl(Id("row"), [], None), VarDecl(Id("col"), [], None),
                                                    VarDecl(Id("sum"), [], None), VarDecl(Id("arr"), [5, 9], None)], (
                                   [VarDecl(Id("sum"), [], IntLiteral(0))], [
                                       For(Id("i"), IntLiteral(0), BinaryOp("<=", Id("i"), Id("row")), IntLiteral(1), (
                                       [], [
                                           For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("col")), IntLiteral(2),
                                               ([], [Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"),
                                                                                                          [Id("i"), Id(
                                                                                                              "j")])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        """Created automatically"""
        input = r"""Function: whileoke
        Body:
            Var: i = 0,k=10;
            While i !=k Do
                a[i] = b + i +. 15.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("whileoke"), [], (
        [VarDecl(Id("i"), [], IntLiteral(0)), VarDecl(Id("k"), [], IntLiteral(10))], [
            While(BinaryOp("!=", Id("i"), Id("k")), ([], [Assign(ArrayCell(Id("a"), [Id("i")]),
                                                                 BinaryOp("+.", BinaryOp("+", Id("b"), Id("i")),
                                                                          FloatLiteral(15.0))),
                                                          Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        """Created automatically"""
        input = r"""Function: whileandif
        Body:
            Var: x=20;
            While True Do
                If x==0 Then Break;
                ElseIf x%2==0 Then
                    x=x\2;
                Else writeln(x);
                EndIf.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("whileandif"), [], ([VarDecl(Id("x"), [], IntLiteral(20))], [
            While(BooleanLiteral(True), ([], [If([(BinaryOp("==", Id("x"), IntLiteral(0)), [], [Break()]), (
            BinaryOp("==", BinaryOp("%", Id("x"), IntLiteral(2)), IntLiteral(0)), [],
            [Assign(Id("x"), BinaryOp("\\", Id("x"), IntLiteral(2)))])],
                                                 ([], [CallStmt(Id("writeln"), [Id("x")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        """Created automatically"""
        input = r"""Function: whilenullstmt
        Body:
            While i < 5 Do EndWhile.
        EndBody."""
        expect = Program(
            [FuncDecl(Id("whilenullstmt"), [], ([], [While(BinaryOp("<", Id("i"), IntLiteral(5)), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        """Created automatically"""
        input = r"""Function: whileinwhile
        Parameter: x
        Body:
            While (True) Do
                While (x>=0) Do
                    x = x+-1;
                EndWhile.
                If ((x<0)) Then Break; EndIf.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("whileinwhile"), [VarDecl(Id("x"), [], None)], ([], [While(BooleanLiteral(True), (
        [], [While(BinaryOp(">=", Id("x"), IntLiteral(0)),
                   ([], [Assign(Id("x"), BinaryOp("+", Id("x"), UnaryOp("-", IntLiteral(1))))])),
             If([(BinaryOp("<", Id("x"), IntLiteral(0)), [], [Break()])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        """Created automatically"""
        input = r"""Function: whilenotendwhile
        Parameter: n
        Body:
            While True Do
                Whilen>=1 Do
                    Whilen<.69.96 Do
                        While n%3==1 Do
                            n = n \ 5;
                        EndWhile
                    .EndWhile.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("whilenotendwhile"), [VarDecl(Id("n"), [], None)], ([], [
            While(BooleanLiteral(True), ([], [While(BinaryOp(">=", Id("n"), IntLiteral(1)), ([], [
                While(BinaryOp("<.", Id("n"), FloatLiteral(69.96)), ([], [
                    While(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(3)), IntLiteral(1)),
                          ([], [Assign(Id("n"), BinaryOp("\\", Id("n"), IntLiteral(5)))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            While True Do print("Hello World"); EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("main"), [], (
        [], [While(BooleanLiteral(True), ([], [CallStmt(Id("print"), [StringLiteral("Hello World")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        """Created automatically"""
        input = r"""Function: whileindowhile
        Parameter: x
        Body:
            Do
                While a<100 Do
                    a=a-30;
                EndWhile.
            While (a>1)
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("whileindowhile"), [VarDecl(Id("x"), [], None)], ([], [Dowhile(([], [
            While(BinaryOp("<", Id("a"), IntLiteral(100)),
                  ([], [Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(30)))]))]), BinaryOp(">", Id("a"),
                                                                                               IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        """Created automatically"""
        input = r"""Function: testdowhile
        Parameter: x,a,b
        Body:
            Do x = a + b;
            While(x<1000.e5)
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("testdowhile"),
                                   [VarDecl(Id("x"), [], None), VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                                   ([], [Dowhile(([], [Assign(Id("x"), BinaryOp("+", Id("a"), Id("b")))]),
                                                 BinaryOp("<", Id("x"), FloatLiteral(100000000.0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_358(self):
        """Created automatically"""
        input = r"""Function: notexpr
        Parameter: n
        Body:
            Do
                Return 1;
            While a =/= 2.2 EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("notexpr"), [VarDecl(Id("n"), [], None)], (
        [], [Dowhile(([], [Return(IntLiteral(1))]), BinaryOp("=/=", Id("a"), FloatLiteral(2.2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        """Created automatically"""
        input = r"""Function: breaktest
        Parameter: x
        Body:
            While x >= 1 Do
                If y<100 Then Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("breaktest"), [VarDecl(Id("x"), [], None)], ([], [
            While(BinaryOp(">=", Id("x"), IntLiteral(1)),
                  ([], [If([(BinaryOp("<", Id("y"), IntLiteral(100)), [], [Break()])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        """Created automatically"""
        input = r"""Function: break
        Body:
            For (i=0, i!=9, (i*.2.0)) Do
                If i>=10 Then Break;
                EndIf.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("break"), [], ([], [
            For(Id("i"), IntLiteral(0), BinaryOp("!=", Id("i"), IntLiteral(9)),
                BinaryOp("*.", Id("i"), FloatLiteral(2.0)),
                ([], [If([(BinaryOp(">=", Id("i"), IntLiteral(10)), [], [Break()])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        """Created automatically"""
        input = r"""Function: continue
        Body:
            For (i=0, i!=9, i) Do
                If i==10 Then Continue;
                EndIf.
                foo();
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("continue"), [], ([], [
            For(Id("i"), IntLiteral(0), BinaryOp("!=", Id("i"), IntLiteral(9)), Id("i"), (
            [], [If([(BinaryOp("==", Id("i"), IntLiteral(10)), [], [Continue()])], ([],[])), CallStmt(Id("foo"), [])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_362(self):
        """Created automatically"""
        input = r"""Function: breakandcontinuealone
        Body:
            Continue;
            Break;
        EndBody."""
        expect = Program([FuncDecl(Id("breakandcontinuealone"), [], ([], [Continue(), Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        """Created automatically"""
        input = r"""Function: callstmt
        Parameter: x,y
        Body:
            foo(2 + x, 4. \. y);
            goo();
        EndBody."""
        expect = Program([FuncDecl(Id("callstmt"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], ([], [
            CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\.", FloatLiteral(4.0), Id("y"))]),
            CallStmt(Id("goo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body:
            call(a,876,var*.65e-1,arr[3],True,"chuoi~~\n");
        EndBody."""
        expect = Program([FuncDecl(Id("callmore"), [], ([], [CallStmt(Id("call"), [Id("a"), IntLiteral(876),
                                                                                   BinaryOp("*.", Id("var"),
                                                                                            FloatLiteral(6.5)),
                                                                                   ArrayCell(Id("arr"),
                                                                                             [IntLiteral(3)]),
                                                                                   BooleanLiteral(True),
                                                                                   StringLiteral("chuoi~~\\n")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        """Created automatically"""
        input = r"""Var: callnotinfunction;
        Function: a
        Body:
            goo(x,y*2,z+3.00000003);
            EndBody."""
        expect = Program([VarDecl(Id("callnotinfunction"),[],None),FuncDecl(Id("a"),[],([],[CallStmt(Id("goo"),[Id("x"),BinaryOp("*",Id("y"),IntLiteral(2)),BinaryOp("+",Id("z"),FloatLiteral(3.00000003))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        """Created automatically"""
        input = r"""Function: callwithoutsemi
        Body:
            iden__TI_FIerOf_Function(a,b_,c+.3.e-2);
        EndBody."""
        expect = Program([FuncDecl(Id("callwithoutsemi"), [], ([], [CallStmt(Id("iden__TI_FIerOf_Function"),
                                                                             [Id("a"), Id("b_"), BinaryOp("+.", Id("c"),
                                                                                                          FloatLiteral(
                                                                                                              0.03))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_367(self):
        """Created automatically"""
        input = r"""Function: testreturn
        Parameter: n
        Body:
            Var: t=False;
            If n<100 Then t=True;
            EndIf.
            Return t;
        EndBody."""
        expect = Program([FuncDecl(Id("testreturn"), [VarDecl(Id("n"), [], None)], (
        [VarDecl(Id("t"), [], BooleanLiteral(False))],
        [If([(BinaryOp("<", Id("n"), IntLiteral(100)), [], [Assign(Id("t"), BooleanLiteral(True))])], ([],[])),
         Return(Id("t"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        """Created automatically"""
        input = r"""Function: returnnull
        Parameter: i
        Body:
            If i==0 Then Return;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("returnnull"), [VarDecl(Id("i"), [], None)],
                                   ([], [If([(BinaryOp("==", Id("i"), IntLiteral(0)), [], [Return(None)])], ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_369(self):
        """Created automatically"""
        input = r"""Function: returnstring
            Body:
                Return "String";
            EndBody."""
        expect = Program([FuncDecl(Id("returnstring"), [], ([], [Return(StringLiteral("String"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        """Created automatically"""
        input = r"""
            Function: returnboolean
            Body:
            If str == "Chung Xon" Then
                Return True;
            Else
                Return False;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id("returnboolean"), [], ([], [
            If([(BinaryOp("==", Id("str"), StringLiteral("Chung Xon")), [], [Return(BooleanLiteral(True))])],
               ([], [Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        """Created automatically"""
        input = r"""
        Function: funccallfail
        Body:
        foo=a+2;
        EndBody."""
        expect = Program(
            [FuncDecl(Id("funccallfail"), [], ([], [Assign(Id("foo"), BinaryOp("+", Id("a"), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        """Created automatically"""
        input = r"""Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody."""
        expect = Program([FuncDecl(Id("array"), [VarDecl(Id("x"), [123], None)], ([VarDecl(Id("i"), [], IntLiteral(0))],
                                                                                  [Assign(ArrayCell(Id("x"),
                                                                                                    [IntLiteral(123)]),
                                                                                          ArrayLiteral([IntLiteral(996),
                                                                                                        IntLiteral(712),
                                                                                                        IntLiteral(
                                                                                                            216)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        """Created automatically"""
        input = r"""Function: arrayinarray
                Parameter: x[2][3]
        Body:
            Var: i = 0;
            x[2][3]={{867,345,987},{76,12,744}};
        EndBody."""
        expect = Program([FuncDecl(Id("arrayinarray"), [VarDecl(Id("x"), [2, 3], None)], (
        [VarDecl(Id("i"), [], IntLiteral(0))], [Assign(ArrayCell(Id("x"), [IntLiteral(2), IntLiteral(3)]), ArrayLiteral(
            [ArrayLiteral([IntLiteral(867), IntLiteral(345), IntLiteral(987)]),
             ArrayLiteral([IntLiteral(76), IntLiteral(12), IntLiteral(744)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        """Created automatically"""
        input = r"""
        Var: stringinarray, x[123]={"STRING","aRraY1","Array2"};"""
        expect = Program([VarDecl(Id("stringinarray"), [], None), VarDecl(Id("x"), [123], ArrayLiteral(
            [StringLiteral("STRING"), StringLiteral("aRraY1"), StringLiteral("Array2")]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_375(self):
        """Created automatically"""
        input = r"""Function: arrayhavespace
        Body:
            Var  : x[123]={   20, 2   ,108  };
        EndBody."""
        expect = Program([FuncDecl(Id("arrayhavespace"), [], (
        [VarDecl(Id("x"), [123], ArrayLiteral([IntLiteral(20), IntLiteral(2), IntLiteral(108)]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_376(self):
        """Created automatically"""
        input = r"""Function: complexarray
            Body: x[123]={"duwat73\r \t", "@#&\n rwFEW54",54312,10.e13, 0.123, 543.0e-6  ,{"xe mau xanh"},"xe mau do"};
        EndBody."""
        expect = Program([FuncDecl(Id("complexarray"), [], ([], [Assign(ArrayCell(Id("x"), [IntLiteral(123)]),
                                                                        ArrayLiteral([StringLiteral("duwat73\\r \\t"),
                                                                                      StringLiteral("@#&\\n rwFEW54"),
                                                                                      IntLiteral(54312),
                                                                                      FloatLiteral(100000000000000.0),
                                                                                      FloatLiteral(0.123),
                                                                                      FloatLiteral(0.000543),
                                                                                      ArrayLiteral([StringLiteral(
                                                                                          "xe mau xanh")]),
                                                                                      StringLiteral("xe mau do")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        """Created automatically"""
        input = r"""Function: arraynull
        Body:
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody."""
        expect = Program([FuncDecl(Id("arraynull"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(12)]),ArrayLiteral([])),Assign(ArrayCell(Id("x"),[IntLiteral(45)]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_378(self):
        """Created automatically"""
        input = r"""Function: multicallstmt
        Body:
            a =-((func1(a)+23) * -func2(4)+arr[3])\. 0.5;
        EndBody."""
        expect = Program([FuncDecl(Id("multicallstmt"),[],([],[Assign(Id("a"),BinaryOp("\.",UnaryOp("-",BinaryOp("+",BinaryOp("*",BinaryOp("+",CallExpr(Id("func1"),[Id("a")]),IntLiteral(23)),UnaryOp("-",CallExpr(Id("func2"),[IntLiteral(4)]))),ArrayCell(Id("arr"),[IntLiteral(3)]))),FloatLiteral(0.5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_379(self):
        """Created automatically"""
        input = r"""Function: callincall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody."""
        expect = Program([FuncDecl(Id("callincall"), [], ([], [Assign(Id("a"), BinaryOp("-", BinaryOp("+", CallExpr(
            Id("func1"), [CallExpr(Id("foo"), [IntLiteral(3)])]), IntLiteral(23)), CallExpr(Id("func2"), [
            CallExpr(Id("goo"), [CallExpr(Id("foo"), [Id("a")])])])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_380(self):
        """Created automatically"""
        input = r"""Function: a Parameter: a Body: Var: a=False;EndBody. Function: b Body: EndBody.
Function: d**Here some too**Parameter: d Body: EndBody."""
        expect = Program(
            [FuncDecl(Id("a"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("a"), [], BooleanLiteral(False))], [])),
             FuncDecl(Id("b"), [], ([], [])), FuncDecl(Id("d"), [VarDecl(Id("d"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        """Created automatically"""
        input = r"""Function: foo
        Parameter: n
        Body:
            Var: i = 0;
            While i!=423 Do
                fact (i);
                i = i + 3; **cmt**
                If i==212 Then Break;
                a = (!(b && c)||!(a&&b));
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("!=",Id("i"),IntLiteral(423)),([],[CallStmt(Id("fact"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(3))),If([(BinaryOp("==",Id("i"),IntLiteral(212)),[],[Break(),Assign(Id("a"),BinaryOp("||",UnaryOp("!",BinaryOp("&&",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("&&",Id("a"),Id("b")))))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        """Created automatically"""
        input = r"""Function: mmmmm
        Body:
            Do
                While(1) Do
                foo (2 + x, 4. \. y);goo ();
            EndWhile.
            While(1)
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("mmmmm"), [], ([], [Dowhile(([], [While(IntLiteral(1), ([], [
            CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\.", FloatLiteral(4.0), Id("y"))]),
            CallStmt(Id("goo"), [])]))]), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        """Created automatically"""
        input = r"""Function: more1
        Parameter: a[5], b
        Body:
        Var: x = {{1,2,3}, **Comment here** "abc"};
        Var: i = 0;
        While (i < 5) Do
        If i == 3 ThenReturn 1;EndIf.
        i = i + 1;
        EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("more1"), [VarDecl(Id("a"), [5], None), VarDecl(Id("b"), [], None)], ([VarDecl(
            Id("x"), [],
            ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), StringLiteral("abc")])), VarDecl(
            Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(5)), ([], [
            If([(BinaryOp("==", Id("i"), IntLiteral(3)), [], [Return(IntLiteral(1))])], ([],[])),
            Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_384(self):
        """Created automatically"""
        input = r"""Function: factorialOfNumber
        Parameter: n
        Body:
        Var:factorial=1;
        print("Enter integer: ");
        read();
        For (i=0, i<=n, 1) Do
            factorial=factorial*i;
        EndFor.
        print(factorial);
        Return factorial;
        EndBody."""
        expect = Program([FuncDecl(Id("factorialOfNumber"), [VarDecl(Id("n"), [], None)], (
        [VarDecl(Id("factorial"), [], IntLiteral(1))],
        [CallStmt(Id("print"), [StringLiteral("Enter integer: ")]), CallStmt(Id("read"), []),
         For(Id("i"), IntLiteral(0), BinaryOp("<=", Id("i"), Id("n")), IntLiteral(1),
             ([], [Assign(Id("factorial"), BinaryOp("*", Id("factorial"), Id("i")))])),
         CallStmt(Id("print"), [Id("factorial")]), Return(Id("factorial"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_385(self):
        """Created automatically"""
        input = r"""Function: fibo
        Parameter: n
        Body:
            Var: n, t1 = 0, t2 = 1, nextTerm = 0;
            print("Enter the number of terms: ");
            getline(n);
            print("Fibonacci Series: ");
            For (i = 1, i <= n, 1) Do
                If(i == 1) Then
                print(" " + t1);
                Continue;
                EndIf.
            If(i == 2) Then
                print( t2+" ");
        Continue;
        EndIf.
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;

        print(nextTerm + " ");
    EndFor.
    Return 0;
    EndBody."""
        expect = Program([FuncDecl(Id("fibo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("n"),[],None),VarDecl(Id("t1"),[],IntLiteral(0)),VarDecl(Id("t2"),[],IntLiteral(1)),VarDecl(Id("nextTerm"),[],IntLiteral(0))],[CallStmt(Id("print"),[StringLiteral("Enter the number of terms: ")]),CallStmt(Id("getline"),[Id("n")]),CallStmt(Id("print"),[StringLiteral("Fibonacci Series: ")]),For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),IntLiteral(1)),[],[CallStmt(Id("print"),[BinaryOp("+",StringLiteral(" "),Id("t1"))]),Continue()])],([],[])),If([(BinaryOp("==",Id("i"),IntLiteral(2)),[],[CallStmt(Id("print"),[BinaryOp("+",Id("t2"),StringLiteral(" "))]),Continue()])],([],[])),Assign(Id("nextTerm"),BinaryOp("+",Id("t1"),Id("t2"))),Assign(Id("t1"),Id("t2")),Assign(Id("t2"),Id("nextTerm")),CallStmt(Id("print"),[BinaryOp("+",Id("nextTerm"),StringLiteral(" "))])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_386(self):
        """Created automatically"""
        input = r"""Function: octalToDecimal
        Parameter: octalNumber
        Body:
        Var: decimalNumber = 0, i = 0, rem;
        While (octalNumber != 0) Do
            rem = octalNumber % 10;
            octalNumber =octalNumber \ 10;
            decimalNumber =decimalNumber  + rem * pow(8,i);
            i=i+1;
        EndWhile.
    Return decimalNumber;
    EndBody."""
        expect = Program([FuncDecl(Id("octalToDecimal"),[VarDecl(Id("octalNumber"),[],None)],([VarDecl(Id("decimalNumber"),[],IntLiteral(0)),VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("rem"),[],None)],[While(BinaryOp("!=",Id("octalNumber"),IntLiteral(0)),([],[Assign(Id("rem"),BinaryOp("%",Id("octalNumber"),IntLiteral(10))),Assign(Id("octalNumber"),BinaryOp("\\",Id("octalNumber"),IntLiteral(10))),Assign(Id("decimalNumber"),BinaryOp("+",Id("decimalNumber"),BinaryOp("*",Id("rem"),CallExpr(Id("pow"),[IntLiteral(8),Id("i")])))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(Id("decimalNumber"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_387(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """
        expect = Program(
            [FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("x"), [], IntLiteral(2))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_388(self):
        """Created automatically"""
        input = r"""Function: ifOKE
        Body:
            If n == 0 Then
                Break;
            EndIf.
        EndBody."""
        expect = Program(
            [FuncDecl(Id("ifOKE"), [], ([], [If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Break()])], ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_389(self):
        """Created automatically"""
        input = r"""Function: ifOKE
        Body:
            If n == 0 Then
                x = 3;
            ElseIf x != 2 Then
                check = False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("ifOKE"), [], ([], [If(
            [(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Assign(Id("x"), IntLiteral(3))]),
             (BinaryOp("!=", Id("x"), IntLiteral(2)), [], [Assign(Id("check"), BooleanLiteral(False))])], ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_390(self):
        """Created automatically"""
        input = r"""Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then

                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func(123);
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("b"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[IntLiteral(123)])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_391(self):
        """Created automatically"""
        input = r"""** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("b"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_392(self):
        """Created automatically"""
        input = r"""Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
                Return a;
            ElseIf a == 6 Then
                a = a *. 2;
                Break;
            Else Continue;
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("*.",Id("a"),IntLiteral(2))),Break()])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_393(self):
        """Created automatically"""
        input = r"""Function: index
        Body:
            arr(a + bbb[61.2 *. (x + y)])[2] = b[2][3];
        EndBody."""
        expect = Program([FuncDecl(Id("index"),[],([],[Assign(ArrayCell(CallExpr(Id("arr"),[BinaryOp("+",Id("a"),ArrayCell(Id("bbb"),[BinaryOp("*.",FloatLiteral(61.2),BinaryOp("+",Id("x"),Id("y")))]))]),[IntLiteral(2)]),ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_394(self):
        """Created automatically"""
        input = r"""
            Function: print
            Parameter: n,x
            Body:
                Var: i;
                For (i = 0, i < sqrt(n), 2) Do
                    x = i + n;
                    print(x\2);
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("print"), [VarDecl(Id("n"), [], None), VarDecl(Id("x"), [], None)], (
        [VarDecl(Id("i"), [], None)], [
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), CallExpr(Id("sqrt"), [Id("n")])), IntLiteral(2), ([], [
                Assign(Id("x"), BinaryOp("+", Id("i"), Id("n"))),
                CallStmt(Id("print"), [BinaryOp("\\", Id("x"), IntLiteral(2))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        """Created automatically"""
        input = r"""Function: test1
        Body:
            m = test2(a,b) + test1 (x);
        EndBody.
        Function: test2
        Body:
            Do
                If(z == 1) Then
                    x = !a;
                EndIf.
            While x
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("test1"), [], ([], [Assign(Id("m"), BinaryOp("+", CallExpr(Id("test2"),
                                                                                                 [Id("a"), Id("b")]),
                                                                                   CallExpr(Id("test1"),
                                                                                            [Id("x")])))])),
                          FuncDecl(Id("test2"), [], ([], [Dowhile(([], [If(
                              [(BinaryOp("==", Id("z"), IntLiteral(1)), [], [Assign(Id("x"), UnaryOp("!", Id("a")))])],
                              ([],[]))]), Id("x"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_396(self):
        """Created automatically"""
        input = r"""Function: mix
        Body:
            While x>1 Do
                For (i = 100,True, i-1) Do
                    If a<3 Then
                        Break;
                    EndIf.
                    a = a -1;
                EndFor.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("mix"), [], ([], [While(BinaryOp(">", Id("x"), IntLiteral(1)), ([], [
            For(Id("i"), IntLiteral(100), BooleanLiteral(True), BinaryOp("-", Id("i"), IntLiteral(1)), ([], [
                If([(BinaryOp("<", Id("a"), IntLiteral(3)), [], [Break()])], ([],[])),
                Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        """Created automatically"""
        input = r"""Function: printchar
        Body:
            For (a = 1, a <= len(str),1 ) Do
                writeln(str[a]);
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("printchar"), [], ([], [
            For(Id("a"), IntLiteral(1), BinaryOp("<=", Id("a"), CallExpr(Id("len"), [Id("str")])), IntLiteral(1),
                ([], [CallStmt(Id("writeln"), [ArrayCell(Id("str"), [Id("a")])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_398(self):
        """Created automatically"""
        input = r"""Function: test
            Parameter: a,b
            Body:
                a = "string 1";
                b = "string 2";
                Return a+b;
            EndBody. """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([], [
            Assign(Id("a"), StringLiteral("string 1")), Assign(Id("b"), StringLiteral("string 2")),
            Return(BinaryOp("+", Id("a"), Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
        """Created automatically"""
        input = r"""Function: tinhtoansml
            Parameter: a,b
            Body:
                a[3 +. 10e2] = (foo(x) +. 12.e3) *. 0x123 - a[b[2][3]] + 4;
            EndBody. """
        expect = Program([FuncDecl(Id("tinhtoansml"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+.",IntLiteral(3),FloatLiteral(1000.0))]),BinaryOp("+",BinaryOp("-",BinaryOp("*.",BinaryOp("+.",CallExpr(Id("foo"),[Id("x")]),FloatLiteral(12000.0)),IntLiteral(291)),ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])])),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
        """Created automatically"""
        input = r"""
            Function: nhieuoilanhieu
            Body:
                Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                Var: b = True, c = False;
                For (i = 0, i < 10, 2) Do
                    For (i = 1, i < x*x , i + 1 ) Do
                        If(z == False) Then
                            x = haha();
                        EndIf.
                        For( j = 1, j < x*x ,j + 1) Do
                            Do
                                a = a * 1;
                            While( 1 )
                            EndDo.
                        EndFor.
                    EndFor.
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("nhieuoilanhieu"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("i"),IntLiteral(1)),([],[If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("haha"),[]))])],([],[])),For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("j"),IntLiteral(1)),([],[Dowhile(([],[Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(1)))]),IntLiteral(1))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

    def test401(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = "This is a string", y = "";
                Var: z = **comment** "This \\n is \t a '" string '"";
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], (
        [VarDecl(Id("x"), [], StringLiteral("This is a string")), VarDecl(Id("y"), [], StringLiteral("")),
         VarDecl(Id("z"), [], StringLiteral("This \\n is 	 a '\" string '\""))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 401))