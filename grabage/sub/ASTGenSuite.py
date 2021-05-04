#1811442
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_var_declare(self):
        """Simple var:  """
        input = """Var: x;"""
        expect=Program([VarDecl(Id('x'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_var_declare_with_assign(self):
        """Simple var: """
        input = """Var: x = 10;"""
        expect=Program([VarDecl(Id('x'),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_var_declare_with_assign_and_dimen(self):
        """Simple var: """
        input = """Var: x[10] = 10;"""
        expect=Program([VarDecl(Id('x'),[10],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_var_composit_var(self):
        """Simple var: """
        input = """Var: a, b;"""
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_var_ele_arr(self):
        """Simple var: """
        input = """Var: bi[5];"""
        expect=Program([VarDecl(Id('bi'),[5],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_double_var(self):
        """Simple var: """
        input = """Var: a; 
                    Var: bi[5];"""
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('bi'),[5],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_double_var_composit(self):
        """Simple var: """
        input = """Var: a, b = "Neu"; 
                    Var: foo[5];"""

        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],StringLiteral('Neu')),VarDecl(Id('foo'),[5],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_var_boolean(self):
        """Simple var: """
        input = """Var: a = False;"""
        expect=Program([VarDecl(Id('a'),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_var_composit_with_str(self):
        """Simple var: """
        input = """Var: a = False, b = True;
                Var: w ="www.google.com.vn";"""
        expect=Program([VarDecl(Id('a'),[],BooleanLiteral(False)),VarDecl(Id('b'),[],BooleanLiteral(True)),VarDecl(Id('w'),[],StringLiteral('www.google.com.vn'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_var_with_empty_arr(self):
        """Simple var: """
        input = """Var: a = {};"""
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_var_with_arr(self):
        """Simple var: """
        input = """Var: a = {1};"""
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_var_with_arr_many_dimen(self):
        """Simple var: """
        input = """Var: a = {1,2,{4,5}};"""
            
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(4),IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_var_with_ele_and_arr(self):
        """Simple var: """
        input = """Var: a[4][8] = {1,2,6};"""
        expect=Program([VarDecl(Id('a'),[4,8],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(6)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_var_with_ele_and_arr_many_dimen(self):
        """Simple var: """
        input = """Var: bias[4][5] = {1,2,{4,5,6}};"""
            
        expect=Program([VarDecl(Id('bias'),[4,5],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_int_lit(self):
        """Simple var: """
        input = """Var: a = 0xFF;"""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(255))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    

    def test_int_lit2(self):
        """Simple var: """
        input = """Var: a = 0xFF, b = 0o4547;"""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(255)),VarDecl(Id('b'),[],IntLiteral(2407))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_int_float(self):
        """Simple var: """
        input = """Var: bias = 0e0, bi = 000e4, range = 0.12e+9;"""
        expect=Program([VarDecl(Id('bias'),[],FloatLiteral(0.0)),VarDecl(Id('bi'),[],FloatLiteral(0.0)),VarDecl(Id('range'),[],FloatLiteral(120000000.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_string_float(self):
        """Simple var: """
        input = """Var: foo[5][80][80] = "string", b = "float" ;"""
        expect=Program([VarDecl(Id('foo'),[5,80,80],StringLiteral('string')),VarDecl(Id('b'),[],StringLiteral('float'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_compsose_lit(self):
        """Simple var: """
        input = """Var: a[5]= "True", b = True, c = False, d = 0xABDF, e = {1,5,{True,False}}, f, g = {};"""
        expect=Program([VarDecl(Id('a'),[5],StringLiteral('True')),VarDecl(Id('b'),[],BooleanLiteral(True)),VarDecl(Id('c'),[],BooleanLiteral(False)),VarDecl(Id('d'),[],IntLiteral(43999)),VarDecl(Id('e'),[],ArrayLiteral([IntLiteral(1),IntLiteral(5),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)])])),VarDecl(Id('f'),[],None),VarDecl(Id('g'),[],ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test_simple_program_var_decl_null_Param_null_stm(self):
        """Simple program """
        input = """Var: a = 100, b = True; 
        Function: main
        Body:
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(100)),VarDecl(Id('b'),[],BooleanLiteral(True)),FuncDecl(Id('main'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_simple_program_null_param_null_stm(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        EndBody."""
        expect=Program([FuncDecl(Id('main'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_simple_program_param(self):
        """Simple program:"""
        input = """Function: chill
        Parameter: a[5], b, u
        Body:
        EndBody."""
        expect=Program([FuncDecl(Id('chill'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None),VarDecl(Id('u'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    
    def test_simple_program_with_many_var_param(self):
        """Simple program:"""
        input = """
        Var: tuan, thu, bao = {10, 0.e7, 00000e10};
        Var: xuan, ha, thu, dong, pPL;
        Function: chill
        Parameter: a[5], b, u
        Body:
        EndBody."""
        expect=Program([VarDecl(Id('tuan'),[],None),VarDecl(Id('thu'),[],None),VarDecl(Id('bao'),[],ArrayLiteral([IntLiteral(10),FloatLiteral(0.0),FloatLiteral(0.0)])),VarDecl(Id('xuan'),[],None),VarDecl(Id('ha'),[],None),VarDecl(Id('thu'),[],None),VarDecl(Id('dong'),[],None),VarDecl(Id('pPL'),[],None),FuncDecl(Id('chill'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None),VarDecl(Id('u'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_assign_stm(self):
        """Simple program:"""
        input = """
        Var: m, n = 0.5;
        Function: main
        Parameter: x,y,a[5]
        Body:
            x = x +1; 
        EndBody.
        """
        expect=Program([VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],FloatLiteral(0.5)),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('a'),[5],None)],([],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_assign_stm1(self):
        """Simple program:"""
        input = """
        Var: a;
        Function: foo
        Parameter: a,b[4]
        Body:
            b = {1,2,3};
            c[2] = {{1,2,3},{1,2,3}};
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[Assign(Id('b'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id('c'),[IntLiteral(2)]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_assign_stm2(self):
        input = """
        Var: a;
        Function: x
        Parameter: y
        Body:
            a = a == (b != c);
            a = a && b || c;
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('x'),[VarDecl(Id('y'),[],None)],([],[Assign(Id('a'),BinaryOp('==',Id('a'),BinaryOp('!=',Id('b'),Id('c')))),Assign(Id('a'),BinaryOp('||',BinaryOp('&&',Id('a'),Id('b')),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_assign_stm3(self):
        input = """
        Function: foo
        Body:
            modern = a && c - e * a \ d != -a - hello(b)[2][a && b[4]];
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(Id('modern'),BinaryOp('!=',BinaryOp('&&',Id('a'),BinaryOp('-',Id('c'),BinaryOp('\\',BinaryOp('*',Id('e'),Id('a')),Id('d')))),BinaryOp('-',UnaryOp('-',Id('a')),ArrayCell(CallExpr(Id('hello'),[Id('b')]),[IntLiteral(2),BinaryOp('&&',Id('a'),ArrayCell(Id('b'),[IntLiteral(4)]))]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_callExp(self):
        input = """
        Var: a;
        Function: foo
        Parameter: a,b[4]
        Body:
            Var: a[2] = {1,2};
            inout = foo(a,{1,2,6},b,c,d[2]);
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([VarDecl(Id('a'),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[Assign(Id('inout'),CallExpr(Id('foo'),[Id('a'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(6)]),Id('b'),Id('c'),ArrayCell(Id('d'),[IntLiteral(2)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_callExp_1(self):
        input = """
        Var: a;
        Function: giaitich2
        Parameter: x,y,z,t
        Body:       
            k[foo(2)*3] = {1.5,9};
            vl[10+foo(2)%2][5] =  a(9);  
            foo(2); 
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('giaitich2'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),VarDecl(Id('t'),[],None)],([],[Assign(ArrayCell(Id('k'),[BinaryOp('*',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(3))]),ArrayLiteral([FloatLiteral(1.5),IntLiteral(9)])),Assign(ArrayCell(Id('vl'),[BinaryOp('+',IntLiteral(10),BinaryOp('%',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(2))),IntLiteral(5)]),CallExpr(Id('a'),[IntLiteral(9)])),CallStmt(Id('foo'),[IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_callExp_2(self):
        input = """
        Var: a;
        Function: foo
        Parameter: a,b[4]
        Body:       
        EndBody.
        Function: main
        Body:
            foo(8 - 5 \ 5 - 7 * (3 && a),a[foo(a+2,b[7*i])]);
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[])),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('-',BinaryOp('-',IntLiteral(8),BinaryOp('\\',IntLiteral(5),IntLiteral(5))),BinaryOp('*',IntLiteral(7),BinaryOp('&&',IntLiteral(3),Id('a')))),ArrayCell(Id('a'),[CallExpr(Id('foo'),[BinaryOp('+',Id('a'),IntLiteral(2)),ArrayCell(Id('b'),[BinaryOp('*',IntLiteral(7),Id('i'))])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_call_stm(self):
        """"""
        input = """
        Var: a = 8;
        Function: chill
        Parameter: a[5], b, u
        Body:
            foo(8); 
            foo(8+9); 
            foo(100); 
            foo(foo(foo()));
            foo[5][100] = 8 ;
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),FuncDecl(Id('chill'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None),VarDecl(Id('u'),[],None)],([],[CallStmt(Id('foo'),[IntLiteral(8)]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(8),IntLiteral(9))]),CallStmt(Id('foo'),[IntLiteral(100)]),CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]),Assign(ArrayCell(Id('foo'),[IntLiteral(5),IntLiteral(100)]),IntLiteral(8))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_break_stm(self):
        """"""
        input = """
        Var: a = 8;
        Function: chill
        Parameter: a[5], b, u
        Body:
            foo(8); 
            foo(8+9); 
            If a Then 
                Break; 
                Continue;
            EndIf.
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),FuncDecl(Id('chill'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None),VarDecl(Id('u'),[],None)],([],[CallStmt(Id('foo'),[IntLiteral(8)]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(8),IntLiteral(9))]),If([(Id('a'),[],[Break(),Continue()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_if_stm_noelseif(self):
        """"""
        input = """
        Var: a;
        Function: holiwook
        Parameter: a, m , n
        Body:
            foo(a);
            If a Then 
                Break;
                foo(a);  
                Continue;
            Else
            EndIf.
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('holiwook'),[VarDecl(Id('a'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([],[CallStmt(Id('foo'),[Id('a')]),If([(Id('a'),[],[Break(),CallStmt(Id('foo'),[Id('a')]),Continue()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_IfStmt_3(self):
        input = """
            Var: j,i;
            Function: intmain
            Body:
                If (c() < arr) Then
                    c();
                EndIf.
            EndBody.
        """
        expect=Program([VarDecl(Id('j'),[],None),VarDecl(Id('i'),[],None),FuncDecl(Id('intmain'),[],([],[If([(BinaryOp('<',CallExpr(Id('c'),[]),Id('arr')),[],[CallStmt(Id('c'),[])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_if_stm_elseif(self):
        """"""
        input = """
        Var: a;
        Function: holiwook
        Parameter: a, m , n
        Body:
            foo(a);
            If a Then 
                Break;
                foo(a);  
                Continue;
            ElseIf a Then 
                a = a % 10; 
                foo(9); 
            Else
            EndIf.
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('holiwook'),[VarDecl(Id('a'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([],[CallStmt(Id('foo'),[Id('a')]),If([(Id('a'),[],[Break(),CallStmt(Id('foo'),[Id('a')]),Continue()]),(Id('a'),[],[Assign(Id('a'),BinaryOp('%',Id('a'),IntLiteral(10))),CallStmt(Id('foo'),[IntLiteral(9)])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_if_stm_elseif_else(self):
        """"""
        input = """
        Var: a;
        Function: ok
        Parameter: ispring
        Body:
            Var: int, float; 
            foo(a);
            If a Then 
                Break;
                foo(a);  
                Return; 
            ElseIf a Then 
                a = a % 10; 
                foo(9); 
            ElseIf b Then
            Else
                p = -p;
            EndIf.
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('ok'),[VarDecl(Id('ispring'),[],None)],([VarDecl(Id('int'),[],None),VarDecl(Id('float'),[],None)],[CallStmt(Id('foo'),[Id('a')]),If([(Id('a'),[],[Break(),CallStmt(Id('foo'),[Id('a')]),Return(None)]),(Id('a'),[],[Assign(Id('a'),BinaryOp('%',Id('a'),IntLiteral(10))),CallStmt(Id('foo'),[IntLiteral(9)])]),(Id('b'),[],[])],([],[Assign(Id('p'),UnaryOp('-',Id('p')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_if_longnhau(self):
        """"""
        input = """
        Function: loop
        Body:
        If 2 Then i = 0; EndIf.
        readln();
        Return a;
        If 2 Then i = 0; EndIf.
        Break;
        If i % 2 Then 
            write(i);
            dem = dem + 1 ; 
            While t(1) Do 
                Return t(1) + t(n-1); 
                Break;
            EndWhile.
        EndIf.  
        Return a;
        Continue; 
        EndBody. 
        """
        expect=Program([FuncDecl(Id('loop'),[],([],[If([(IntLiteral(2),[],[Assign(Id('i'),IntLiteral(0))])],([],[])),CallStmt(Id('readln'),[]),Return(Id('a')),If([(IntLiteral(2),[],[Assign(Id('i'),IntLiteral(0))])],([],[])),Break(),If([(BinaryOp('%',Id('i'),IntLiteral(2)),[],[CallStmt(Id('write'),[Id('i')]),Assign(Id('dem'),BinaryOp('+',Id('dem'),IntLiteral(1))),While(CallExpr(Id('t'),[IntLiteral(1)]),([],[Return(BinaryOp('+',CallExpr(Id('t'),[IntLiteral(1)]),CallExpr(Id('t'),[BinaryOp('-',Id('n'),IntLiteral(1))]))),Break()]))])],([],[])),Return(Id('a')),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_function_call0(self):
        """Simple program:  """
        input = """
            Var: a = 8, b, c = {10};
            Function: tuananh_1811442
            Body:
            a = foo(2)[0];
            foo(2);
            foo(2)[3] = a+1;
            a=foo(2);
            EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],ArrayLiteral([IntLiteral(10)])),FuncDecl(Id('tuananh_1811442'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(0)])),CallStmt(Id('foo'),[IntLiteral(2)]),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp('+',Id('a'),IntLiteral(1))),Assign(Id('a'),CallExpr(Id('foo'),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_manyfunction(self):
        input = """
            Var: a = 8, b, c = {10};
            Function: test
            Body:
            Do
            a = a \. 2;
            c[5][5] = foo(3+foo(2)) + True; 
            a[5] = True || False; 
            m = True-.True;
            While a && True
            EndDo.
            EndBody.
            Function: tuananh_1811442
            Body:
            a = foo(2)[0];
            foo(2);
            foo(2)[3] = a+1;
            a=foo(2);
            EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],ArrayLiteral([IntLiteral(10)])),FuncDecl(Id('test'),[],([],[Dowhile(([],[Assign(Id('a'),BinaryOp('\\.',Id('a'),IntLiteral(2))),Assign(ArrayCell(Id('c'),[IntLiteral(5),IntLiteral(5)]),BinaryOp('+',CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BooleanLiteral(True))),Assign(ArrayCell(Id('a'),[IntLiteral(5)]),BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False))),Assign(Id('m'),BinaryOp('-.',BooleanLiteral(True),BooleanLiteral(True)))]),BinaryOp('&&',Id('a'),BooleanLiteral(True)))])),FuncDecl(Id('tuananh_1811442'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(0)])),CallStmt(Id('foo'),[IntLiteral(2)]),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp('+',Id('a'),IntLiteral(1))),Assign(Id('a'),CallExpr(Id('foo'),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_DSA(self):
        input = """
            Var: a = 8, b, c = {10};
            Function: main
            Parameter: y,z,a
            Body:
            While fun() == True Do process(currentNode); 
            EndWhile.
            If currentNode_left == null Then enqueue(bfQueue, currentNode_left);
            EndIf.
            If currentNode_right != null Then enqueue(bfQueue, currentNode_right);
            EndIf.
            EndBody."""
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],ArrayLiteral([IntLiteral(10)])),FuncDecl(Id('main'),[VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),VarDecl(Id('a'),[],None)],([],[While(BinaryOp('==',CallExpr(Id('fun'),[]),BooleanLiteral(True)),([],[CallStmt(Id('process'),[Id('currentNode')])])),If([(BinaryOp('==',Id('currentNode_left'),Id('null')),[],[CallStmt(Id('enqueue'),[Id('bfQueue'),Id('currentNode_left')])])],([],[])),If([(BinaryOp('!=',Id('currentNode_right'),Id('null')),[],[CallStmt(Id('enqueue'),[Id('bfQueue'),Id('currentNode_right')])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_manystm(self):
        input = """
            Var: a = 8, b, c = {10};
            Function: square
            Parameter: d, r
            Body: 
                Return a; 
                write("a" =/= 8);
                Return b; 
                write("b" + b);
                Return square == a * b ; 
                write(square); 
            EndBody.
            Function: tuan
            Body:
                a = foo(2)[0];
                foo(2);
                foo(2)[3] = a+1;
                a=foo(2);
            EndBody.
            Function: swap_a_b
            Parameter: a,b 
            Body: 
                If a>b Then
                tmp=a;
                a=b;
                b=tmp;
                EndIf.
            EndBody.
            
            """
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],ArrayLiteral([IntLiteral(10)])),FuncDecl(Id('square'),[VarDecl(Id('d'),[],None),VarDecl(Id('r'),[],None)],([],[Return(Id('a')),CallStmt(Id('write'),[BinaryOp('=/=',StringLiteral('a'),IntLiteral(8))]),Return(Id('b')),CallStmt(Id('write'),[BinaryOp('+',StringLiteral('b'),Id('b'))]),Return(BinaryOp('==',Id('square'),BinaryOp('*',Id('a'),Id('b')))),CallStmt(Id('write'),[Id('square')])])),FuncDecl(Id('tuan'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(0)])),CallStmt(Id('foo'),[IntLiteral(2)]),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp('+',Id('a'),IntLiteral(1))),Assign(Id('a'),CallExpr(Id('foo'),[IntLiteral(2)]))])),FuncDecl(Id('swap_a_b'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[If([(BinaryOp('>',Id('a'),Id('b')),[],[Assign(Id('tmp'),Id('a')),Assign(Id('a'),Id('b')),Assign(Id('b'),Id('tmp'))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_for_stm(self):
        input = """
        Var: root,left = 4,a;
        Function: id
        Parameter: n,a,b
        Body: 
            For (i=1, i<100, i+2) Do
                Continue; 

                If a>b Then
                tmp=a;
                a=b;
                b=tmp;
                EndIf.
                doo(5);
            EndFor.
            Return ; 
            Return b; 
        EndBody.
            
            """
        expect=Program([VarDecl(Id('root'),[],None),VarDecl(Id('left'),[],IntLiteral(4)),VarDecl(Id('a'),[],None),FuncDecl(Id('id'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('i'),IntLiteral(2)),([],[Continue(),If([(BinaryOp('>',Id('a'),Id('b')),[],[Assign(Id('tmp'),Id('a')),Assign(Id('a'),Id('b')),Assign(Id('b'),Id('tmp'))])],([],[])),CallStmt(Id('doo'),[IntLiteral(5)])])),Return(None),Return(Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_for_stm_longnhau(self):
        input = """
            Var: root,left = 4,a;
            Function: id
            Parameter: n,a,b
            Body: 
                For (i=1, i<100, i+2) Do
                    Continue; 
                    Break; 
                    Break; 
                    For(i = 0, i < 10, 1) Do
                        Continue;
                    EndFor.
                    Return (n -1)*2;
                    a = a * i; 
                    b = b - i; 
                    n = a + b; 
                    Break;
                    Continue; 
                    Break;
                EndFor.
                Return ; 
                Return b; 
            EndBody.
                
                """
        expect=Program([VarDecl(Id('root'),[],None),VarDecl(Id('left'),[],IntLiteral(4)),VarDecl(Id('a'),[],None),FuncDecl(Id('id'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('i'),IntLiteral(2)),([],[Continue(),Break(),Break(),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[Continue()])),Return(BinaryOp('*',BinaryOp('-',Id('n'),IntLiteral(1)),IntLiteral(2))),Assign(Id('a'),BinaryOp('*',Id('a'),Id('i'))),Assign(Id('b'),BinaryOp('-',Id('b'),Id('i'))),Assign(Id('n'),BinaryOp('+',Id('a'),Id('b'))),Break(),Continue(),Break()])),Return(None),Return(Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_while_stm_longnhau(self):
        input = """
            Function: test
        Body:
            Var: guard = 0;
            While guard Do
                a = b +. 1.;
                If i % 2 Then
                    Do
                        x = test() + 8;
                    While (a >=. b) EndDo.
                ElseIf i Then
                    test()[123] = 123;
                EndIf.
            EndWhile.
        EndBody.
                """
        expect=Program([FuncDecl(Id('test'),[],([VarDecl(Id('guard'),[],IntLiteral(0))],[While(Id('guard'),([],[Assign(Id('a'),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),If([(BinaryOp('%',Id('i'),IntLiteral(2)),[],[Dowhile(([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('test'),[]),IntLiteral(8)))]),BinaryOp('>=.',Id('a'),Id('b')))]),(Id('i'),[],[Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(123)]),IntLiteral(123))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_do_while_stm_longnhau(self):
        input = """
            Function: test
        Body:
            Var: guard = 0;
            While guard Do
                a = b +. 1.;
                If i % 2 Then
                    Do
                        x = test() + 8;
                        Do
                        x = test() + 8;
                    While (a >=. b) EndDo.
                    While (a >=. b) EndDo.
                ElseIf i Then
                    test()[123] = 123;
                EndIf.
            EndWhile.
        EndBody.
                """
        expect=Program([FuncDecl(Id('test'),[],([VarDecl(Id('guard'),[],IntLiteral(0))],[While(Id('guard'),([],[Assign(Id('a'),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),If([(BinaryOp('%',Id('i'),IntLiteral(2)),[],[Dowhile(([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('test'),[]),IntLiteral(8))),Dowhile(([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('test'),[]),IntLiteral(8)))]),BinaryOp('>=.',Id('a'),Id('b')))]),BinaryOp('>=.',Id('a'),Id('b')))]),(Id('i'),[],[Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(123)]),IntLiteral(123))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_basic(self):
        input = """
            Function: fibo
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
    EndBody.
                """
        expect=Program([FuncDecl(Id('fibo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('n'),[],None),VarDecl(Id('t1'),[],IntLiteral(0)),VarDecl(Id('t2'),[],IntLiteral(1)),VarDecl(Id('nextTerm'),[],IntLiteral(0))],[CallStmt(Id('print'),[StringLiteral('Enter the number of terms: ')]),CallStmt(Id('getline'),[Id('n')]),CallStmt(Id('print'),[StringLiteral('Fibonacci Series: ')]),For(Id('i'),IntLiteral(1),BinaryOp('<=',Id('i'),Id('n')),IntLiteral(1),([],[If([(BinaryOp('==',Id('i'),IntLiteral(1)),[],[CallStmt(Id('print'),[BinaryOp('+',StringLiteral(' '),Id('t1'))]),Continue()])],([],[])),If([(BinaryOp('==',Id('i'),IntLiteral(2)),[],[CallStmt(Id('print'),[BinaryOp('+',Id('t2'),StringLiteral(' '))]),Continue()])],([],[])),Assign(Id('nextTerm'),BinaryOp('+',Id('t1'),Id('t2'))),Assign(Id('t1'),Id('t2')),Assign(Id('t2'),Id('nextTerm')),CallStmt(Id('print'),[BinaryOp('+',Id('nextTerm'),StringLiteral(' '))])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_exp0(self):
        input = """
        Function: sign
        Body:
        a = a \. 2 + 8;
        a[m] = True || False; 
        m = True-.True;
        EndBody.
        """
        expect=Program([FuncDecl(Id('sign'),[],([],[Assign(Id('a'),BinaryOp('+',BinaryOp('\\.',Id('a'),IntLiteral(2)),IntLiteral(8))),Assign(ArrayCell(Id('a'),[Id('m')]),BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False))),Assign(Id('m'),BinaryOp('-.',BooleanLiteral(True),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_exp(self):
        input = """
        Function: exp
        Body:
        foo[8]= True ||  -False; 
        m = a[100];
        EndBody.
        """
        expect=Program([FuncDecl(Id('exp'),[],([],[Assign(ArrayCell(Id('foo'),[IntLiteral(8)]),BinaryOp('||',BooleanLiteral(True),UnaryOp('-',BooleanLiteral(False)))),Assign(Id('m'),ArrayCell(Id('a'),[IntLiteral(100)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_exp1(self):
        input = """
        Function: exp
        Body:
            Var: int_of_string; 
            Var: a[10], b = {}; 
            f = f + 2; 
            k = (k == k) + k[5] ;
            foo(f());
        EndBody.
        """
        expect=Program([FuncDecl(Id('exp'),[],([VarDecl(Id('int_of_string'),[],None),VarDecl(Id('a'),[10],None),VarDecl(Id('b'),[],ArrayLiteral([]))],[Assign(Id('f'),BinaryOp('+',Id('f'),IntLiteral(2))),Assign(Id('k'),BinaryOp('+',BinaryOp('==',Id('k'),Id('k')),ArrayCell(Id('k'),[IntLiteral(5)]))),CallStmt(Id('foo'),[CallExpr(Id('f'),[])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_exp2(self):
        input = """
        Function: foo
        Body:
            x = (5 + f() * 3 + a[10])[2] * 5 \ 8;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(Id('x'),BinaryOp('\\',BinaryOp('*',ArrayCell(BinaryOp('+',BinaryOp('+',IntLiteral(5),BinaryOp('*',CallExpr(Id('f'),[]),IntLiteral(3))),ArrayCell(Id('a'),[IntLiteral(10)])),[IntLiteral(2)]),IntLiteral(5)),IntLiteral(8)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_exp3(self):
        input = """
        Var: int;
        Function: int_literal
        Parameter: a
        Body:
            Var: a[2] = {1,False};
            inout = 158 ;
        EndBody.
        """
        expect=Program([VarDecl(Id('int'),[],None),FuncDecl(Id('int_literal'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[2],ArrayLiteral([IntLiteral(1),BooleanLiteral(False)]))],[Assign(Id('inout'),IntLiteral(158))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_exp4(self):
        input = """
        Var: in_out;
        Function: int_literal
        Parameter: a
        Body:
            Var: a[2][3] = {1,{}};
            input = 158 ;
            a = {} + foo(2);
            foo(8,{});
            Return output; 
        EndBody.
        """
        expect=Program([VarDecl(Id('in_out'),[],None),FuncDecl(Id('int_literal'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[2,3],ArrayLiteral([IntLiteral(1),ArrayLiteral([])]))],[Assign(Id('input'),IntLiteral(158)),Assign(Id('a'),BinaryOp('+',ArrayLiteral([]),CallExpr(Id('foo'),[IntLiteral(2)]))),CallStmt(Id('foo'),[IntLiteral(8),ArrayLiteral([])]),Return(Id('output'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_exp5(self):
        input = """
        Var: in_out;
        Function: check
        Parameter: a
        Body:
            Var: a[2][3] = {1,{}};
            z[foo(2)*3] = {1.5,9};
            (-1+4)[(a)] = 5;
            (foo(8))[10+foo(2)][8] =  a(9); 
            Return output; 
        EndBody.
        """
        expect=Program([VarDecl(Id('in_out'),[],None),FuncDecl(Id('check'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[2,3],ArrayLiteral([IntLiteral(1),ArrayLiteral([])]))],[Assign(ArrayCell(Id('z'),[BinaryOp('*',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(3))]),ArrayLiteral([FloatLiteral(1.5),IntLiteral(9)])),Assign(ArrayCell(BinaryOp('+',UnaryOp('-',IntLiteral(1)),IntLiteral(4)),[Id('a')]),IntLiteral(5)),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(8)]),[BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)])),IntLiteral(8)]),CallExpr(Id('a'),[IntLiteral(9)])),Return(Id('output'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_callstm_0(self):
        input = """
        Var: a;
        Function: foo
        Parameter: a,b[4]
        Body:       
        EndBody.
        Function: main
        Body:
            foo(8 - 5 \ 5 - 7 * (3 && a),a[foo(a+2,b[7*i])]);
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[])),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('-',BinaryOp('-',IntLiteral(8),BinaryOp('\\',IntLiteral(5),IntLiteral(5))),BinaryOp('*',IntLiteral(7),BinaryOp('&&',IntLiteral(3),Id('a')))),ArrayCell(Id('a'),[CallExpr(Id('foo'),[BinaryOp('+',Id('a'),IntLiteral(2)),ArrayCell(Id('b'),[BinaryOp('*',IntLiteral(7),Id('i'))])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_array_cell(self):
        input = """
        Var: foo[7];
        Function: test
        Parameter: a,b[4]
        Body:  
            foo[0xFF] = 1;
            foo[True]["a"] = foo(foo[5],(-1)[8]); 
            foo[foo() +. foo(5) - -a] = a * 8 -{True,False,0o77};
        EndBody.
        """
        expect=Program([VarDecl(Id('foo'),[7],None),FuncDecl(Id('test'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[Assign(ArrayCell(Id('foo'),[IntLiteral(255)]),IntLiteral(1)),Assign(ArrayCell(Id('foo'),[BooleanLiteral(True),StringLiteral('a')]),CallExpr(Id('foo'),[ArrayCell(Id('foo'),[IntLiteral(5)]),ArrayCell(UnaryOp('-',IntLiteral(1)),[IntLiteral(8)])])),Assign(ArrayCell(Id('foo'),[BinaryOp('-',BinaryOp('+.',CallExpr(Id('foo'),[]),CallExpr(Id('foo'),[IntLiteral(5)])),UnaryOp('-',Id('a')))]),BinaryOp('-',BinaryOp('*',Id('a'),IntLiteral(8)),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),IntLiteral(63)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_arr_cell1(self):
        input = """
        Function: funcall
        Body:
            Return; 
            Continue; 
            Break; 
            a [8 + 100 + True % 3 - 1] = {4,8,{}};
            (-foo())[4][t+t] = {}; 
        EndBody.
        Function: main
        Body:
            fibo(); 
        EndBody.
                """
        expect=Program([FuncDecl(Id('funcall'),[],([],[Return(None),Continue(),Break(),Assign(ArrayCell(Id('a'),[BinaryOp('-',BinaryOp('+',BinaryOp('+',IntLiteral(8),IntLiteral(100)),BinaryOp('%',BooleanLiteral(True),IntLiteral(3))),IntLiteral(1))]),ArrayLiteral([IntLiteral(4),IntLiteral(8),ArrayLiteral([])])),Assign(ArrayCell(UnaryOp('-',CallExpr(Id('foo'),[])),[IntLiteral(4),BinaryOp('+',Id('t'),Id('t'))]),ArrayLiteral([]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('fibo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_arr_cell2(self):
        input = """
        Function: arraycell
        Body:
            (fibo() +. True == False)[5] = p; 
        EndBody.
        Function: main
        Body:
            fibo(); 
        EndBody.
                """
        expect=Program([FuncDecl(Id('arraycell'),[],([],[Assign(ArrayCell(BinaryOp('==',BinaryOp('+.',CallExpr(Id('fibo'),[]),BooleanLiteral(True)),BooleanLiteral(False)),[IntLiteral(5)]),Id('p'))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('fibo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_call(self):
        input = """
        Function: foo
        Parameter: a,b[4]
        Body:       
        EndBody.
        Function: main
        Body:
            foo(8 - 5 \ 5 - 7 * (3 && a),a[foo(a+2,b[7*i])]);
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[])),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('-',BinaryOp('-',IntLiteral(8),BinaryOp('\\',IntLiteral(5),IntLiteral(5))),BinaryOp('*',IntLiteral(7),BinaryOp('&&',IntLiteral(3),Id('a')))),ArrayCell(Id('a'),[CallExpr(Id('foo'),[BinaryOp('+',Id('a'),IntLiteral(2)),ArrayCell(Id('b'),[BinaryOp('*',IntLiteral(7),Id('i'))])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_callstm_1(self):
        input = """
        Var: a;
        Function: foo
        Parameter: a,b[4]
        Body:       
        EndBody.
        Function: main
        Body:
            foo(foo(2),foo(foo(a)));
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[4],None)],([],[])),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(2)]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[Id('a')])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_for_and_while_longnhau(self):
        input = """
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
        expect=Program([FuncDecl(Id('nhieuoilanhieu'),[],([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),VarDecl(Id('b'),[],BooleanLiteral(True)),VarDecl(Id('c'),[],BooleanLiteral(False))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),BinaryOp('*',Id('x'),Id('x'))),BinaryOp('+',Id('i'),IntLiteral(1)),([],[If([(BinaryOp('==',Id('z'),BooleanLiteral(False)),[],[Assign(Id('x'),CallExpr(Id('haha'),[]))])],([],[])),For(Id('j'),IntLiteral(1),BinaryOp('<',Id('j'),BinaryOp('*',Id('x'),Id('x'))),BinaryOp('+',Id('j'),IntLiteral(1)),([],[Dowhile(([],[Assign(Id('a'),BinaryOp('*',Id('a'),IntLiteral(1)))]),IntLiteral(1))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_return(self):
        input = """
        Function: return
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func();
            Return a + d ;
            Return foo(2, foo(3) + 8);
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
                """
        expect=Program([FuncDecl(Id('return'),[],([],[If([(BinaryOp('||',BinaryOp('&&',BinaryOp('+',Id('a'),IntLiteral(5)),BinaryOp('-',Id('j'),IntLiteral(6))),BinaryOp('*',Id('k'),IntLiteral(7))),[],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('b'),BinaryOp('-',BinaryOp('-.',BinaryOp('-',Id('i'),BinaryOp('*',Id('b'),Id('a'))),BinaryOp('\\',Id('b'),Id('c'))),UnaryOp('-.',Id('d'))))])],([],[])),Return(BinaryOp('+',Id('a'),CallExpr(Id('func'),[]))),Return(BinaryOp('+',Id('a'),Id('d'))),Return(CallExpr(Id('foo'),[IntLiteral(2),BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(3)]),IntLiteral(8))]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_funcall_many_param(self):
        input = """
        Function: funcall
        Body:
            If foo({1,5,6}) \ 100 + {4,5,8} + True 
            Then 
                (-2+5)[8] = True;
                f()[10][100] = 0;
            EndIf.
        EndBody.
        Function: main
        Body:
            func(8 + 100);
            Return a+func();
            Return a + d ;
            Return foo(2, foo(3) + 8);
            Return 0;
        EndBody.
                """
        expect=Program([FuncDecl(Id('funcall'),[],([],[If([(BinaryOp('+',BinaryOp('+',BinaryOp('\\',CallExpr(Id('foo'),[ArrayLiteral([IntLiteral(1),IntLiteral(5),IntLiteral(6)])]),IntLiteral(100)),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(8)])),BooleanLiteral(True)),[],[Assign(ArrayCell(BinaryOp('+',UnaryOp('-',IntLiteral(2)),IntLiteral(5)),[IntLiteral(8)]),BooleanLiteral(True)),Assign(ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(10),IntLiteral(100)]),IntLiteral(0))])],([],[]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[BinaryOp('+',IntLiteral(8),IntLiteral(100))]),Return(BinaryOp('+',Id('a'),CallExpr(Id('func'),[]))),Return(BinaryOp('+',Id('a'),Id('d'))),Return(CallExpr(Id('foo'),[IntLiteral(2),BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(3)]),IntLiteral(8))])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
   
    def test_if_else_long_for(self):
        input = """
        Function: if_for
        Body:
            If bool_of_string ("True") Then
                
                For(i = 0, i < 10, 1) Do
                Continue;
                EndFor.
            ElseIf a == 5 Then
                a = max(123);
                Return a;
            ElseIf a == 100 Then
                a = a \ 2;
                Break;
            Else Continue;
            EndIf.
        EndBody.
                """
        expect=Program([FuncDecl(Id('if_for'),[],([],[If([(CallExpr(Id('bool_of_string'),[StringLiteral('True')]),[],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[Continue()]))]),(BinaryOp('==',Id('a'),IntLiteral(5)),[],[Assign(Id('a'),CallExpr(Id('max'),[IntLiteral(123)])),Return(Id('a'))]),(BinaryOp('==',Id('a'),IntLiteral(100)),[],[Assign(Id('a'),BinaryOp('\\',Id('a'),IntLiteral(2))),Break()])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_for_long_if_else(self):
        input = """
        Function: if_for
        Body:
            For(i = 0, i < 10, 1) Do
            If string ("True") Then
                
                Continue;
                foo(10); 
            ElseIf a == 5 Then
                arr = {1,2,3};
                Return arr;
            ElseIf a == 100 Then
                a = a \. 2;
                Break;
            Else Continue;
            
            EndIf.
            EndFor.
        EndBody.
                """
        expect=Program([FuncDecl(Id('if_for'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[If([(CallExpr(Id('string'),[StringLiteral('True')]),[],[Continue(),CallStmt(Id('foo'),[IntLiteral(10)])]),(BinaryOp('==',Id('a'),IntLiteral(5)),[],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Return(Id('arr'))]),(BinaryOp('==',Id('a'),IntLiteral(100)),[],[Assign(Id('a'),BinaryOp('\\.',Id('a'),IntLiteral(2))),Break()])],([],[Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_if_else_long_while(self):
        input = """
        Function: if_for
        Body:
                If (a + 0xFF) Then running(root); EndIf.
                While foo(9 + a[10]) Do 
                    If (a + 0xFF) Then running(root);  
                    EndIf.**if staement**
                EndWhile.
        EndBody.
                """
        expect=Program([FuncDecl(Id('if_for'),[],([],[If([(BinaryOp('+',Id('a'),IntLiteral(255)),[],[CallStmt(Id('running'),[Id('root')])])],([],[])),While(CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(9),ArrayCell(Id('a'),[IntLiteral(10)]))]),([],[If([(BinaryOp('+',Id('a'),IntLiteral(255)),[],[CallStmt(Id('running'),[Id('root')])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_while_long_if_else(self):
        input = """
        Function: if_for
        Body:
                While foo(9 + a[10]) Do 
                If (a + 0o77) Then runby(root_ref); 
                ElseIf (a + 0e0) **body staement** Then runby(root_ref); 
                Else Return; 
                EndIf.
                EndWhile.
        EndBody.
                """
        expect=Program([FuncDecl(Id('if_for'),[],([],[While(CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(9),ArrayCell(Id('a'),[IntLiteral(10)]))]),([],[If([(BinaryOp('+',Id('a'),IntLiteral(63)),[],[CallStmt(Id('runby'),[Id('root_ref')])]),(BinaryOp('+',Id('a'),FloatLiteral(0.0)),[],[CallStmt(Id('runby'),[Id('root_ref')])])],([],[Return(None)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_basic_else(self):
        input = """
        Function: ppl_2
        Body:
            Var: x,check;
            If x<2 Then
                x = foo();
            ElseIf x==2 Then
                
                Break;
            Else 
                check=True;
                Return 0;
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('ppl_2'),[],([VarDecl(Id('x'),[],None),VarDecl(Id('check'),[],None)],[If([(BinaryOp('<',Id('x'),IntLiteral(2)),[],[Assign(Id('x'),CallExpr(Id('foo'),[]))]),(BinaryOp('==',Id('x'),IntLiteral(2)),[],[Break()])],([],[Assign(Id('check'),BooleanLiteral(True)),Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    def test_complex_exp(self):
        input = """
        Function: main
        **main ne**
        Parameter: x,y,z
        **Param**
        Body:
        If foo(2) Then x = x + 2; EndIf.
        a[3 + foo(2)] = {1,2,0};
        a = (a+b*foo(8));
        a = "uit";
        go("a"); 
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[If([(CallExpr(Id('foo'),[IntLiteral(2)]),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(2)))])],([],[])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(0)])),Assign(Id('a'),BinaryOp('+',Id('a'),BinaryOp('*',Id('b'),CallExpr(Id('foo'),[IntLiteral(8)])))),Assign(Id('a'),StringLiteral('uit')),CallStmt(Id('go'),[StringLiteral('a')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_simple_program1(self):
        """ """
        input = """
            Function: m
            Body:
            While d
            Do
                foo(5); 
                a = 8;
            EndWhile.
            EndBody."""
        expect=Program([FuncDecl(Id('m'),[],([],[While(Id('d'),([],[CallStmt(Id('foo'),[IntLiteral(5)]),Assign(Id('a'),IntLiteral(8))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_simple_program2(self):
        """"""
        input = """
            Function: m
            Body:
            While d
            Do
                Var: a = 10;
                foo(10+5);
            EndWhile.
            EndBody."""
        expect=Program([FuncDecl(Id('m'),[],([],[While(Id('d'),([VarDecl(Id('a'),[],IntLiteral(10))],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(10),IntLiteral(5))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_cmt(self):
        """ """
        input = """
        Var: a = {1,2,0xFF} , b = \"**hi\", c ;
        Function: main
        **main ne**
        Parameter: x,y,z
        **Param **
        Body:
        ** null stm **
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(255)])),VarDecl(Id('b'),[],StringLiteral('**hi')),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_many_program2(self):
        """ """
        input = """
        Var: a = {1,2};
        Function: main
        Parameter: a
        Body:
        EndBody.
        Function : abc
        Body:
            foo(6); 
            taller = true;
            Return root; 
            Break;
            Continue; 
        EndBody."""
        
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[])),FuncDecl(Id('abc'),[],([],[CallStmt(Id('foo'),[IntLiteral(6)]),Assign(Id('taller'),Id('true')),Return(Id('root')),Break(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_full_program(self):
        """ """
        input = """
        Var: a,b,c,cv,dt,p=8;
        Function: square
        Parameter: d, r
        Body: 
            Return a; 
            write(\"a\" =/= 8);
            Return b; 
            write(\"b\" + b);
            Return square == a * b ; 
            write(square); 
        EndBody."""
        
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('cv'),[],None),VarDecl(Id('dt'),[],None),VarDecl(Id('p'),[],IntLiteral(8)),FuncDecl(Id('square'),[VarDecl(Id('d'),[],None),VarDecl(Id('r'),[],None)],([],[Return(Id('a')),CallStmt(Id('write'),[BinaryOp('=/=',StringLiteral('a'),IntLiteral(8))]),Return(Id('b')),CallStmt(Id('write'),[BinaryOp('+',StringLiteral('b'),Id('b'))]),Return(BinaryOp('==',Id('square'),BinaryOp('*',Id('a'),Id('b')))),CallStmt(Id('write'),[Id('square')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_many_var_in_func(self):
        """ """
        input = """
        Var: a[10][5];
        Function: square
        Parameter: d, r
        Body: 
            Var: a = {};
            Var: b = True; 
            a = a + 1;  
        EndBody."""
        
        expect=Program([VarDecl(Id('a'),[10,5],None),FuncDecl(Id('square'),[VarDecl(Id('d'),[],None),VarDecl(Id('r'),[],None)],([VarDecl(Id('a'),[],ArrayLiteral([])),VarDecl(Id('b'),[],BooleanLiteral(True))],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_many_vardecl_in_func(self):
        """ """
        input = """
        Var: a[10][5];
        Function: square
        Parameter: d, r
        Body: 
            Var: a = {};
            Var: b = True; 
            a = a + 1;  
        EndBody."""
        
        expect=Program([VarDecl(Id('a'),[10,5],None),FuncDecl(Id('square'),[VarDecl(Id('d'),[],None),VarDecl(Id('r'),[],None)],([VarDecl(Id('a'),[],ArrayLiteral([])),VarDecl(Id('b'),[],BooleanLiteral(True))],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_too_so_much_loop(self):
        """ """
        input = """
            Function: test
        Parameter:  highfunction
        Body:
            Var: min, max;
            For(i = 1, i < 5, low) Do
                For(j = 0, j < i, 1) Do
                    If arr[j] < min Then
                        min = arr[j];
                    ElseIf arr[j] > max Then
                        max = arr[j];
                    Else
                    EndIf.
                    While min == max Do
                        Var: temperature;
                        For(i = low, i < high, 1) Do
                            If arr[j] < min Then
                            min = arr[j];
                            ElseIf arr[j] > max Then
                            max = arr[j];
                            Else
                            EndIf.
                        EndFor.
                    EndWhile.
                EndFor.
            EndFor.
        EndBody."""
        expect=Program([FuncDecl(Id('test'),[VarDecl(Id('highfunction'),[],None)],([VarDecl(Id('min'),[],None),VarDecl(Id('max'),[],None)],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(5)),Id('low'),([],[For(Id('j'),IntLiteral(0),BinaryOp('<',Id('j'),Id('i')),IntLiteral(1),([],[If([(BinaryOp('<',ArrayCell(Id('arr'),[Id('j')]),Id('min')),[],[Assign(Id('min'),ArrayCell(Id('arr'),[Id('j')]))]),(BinaryOp('>',ArrayCell(Id('arr'),[Id('j')]),Id('max')),[],[Assign(Id('max'),ArrayCell(Id('arr'),[Id('j')]))])],([],[])),While(BinaryOp('==',Id('min'),Id('max')),([VarDecl(Id('temperature'),[],None)],[For(Id('i'),Id('low'),BinaryOp('<',Id('i'),Id('high')),IntLiteral(1),([],[If([(BinaryOp('<',ArrayCell(Id('arr'),[Id('j')]),Id('min')),[],[Assign(Id('min'),ArrayCell(Id('arr'),[Id('j')]))]),(BinaryOp('>',ArrayCell(Id('arr'),[Id('j')]),Id('max')),[],[Assign(Id('max'),ArrayCell(Id('arr'),[Id('j')]))])],([],[]))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_too_much_loop_and_if(self):
        """ """
        input = """
        Var: vardecl = { "drr", 0x123};
        Function: test
        Body:
            Var: x = 12;
            For(i = "dasd" * 12, "dasd", "d") Do
                Var: m = 10;
                If m != 10 Then
                    Var: x;
                    
                ElseIf m && False Then
                    Var: x;
                    print(x);
                Else
                    Do
                        If k == 10 Then
                            Var: i;
                            x = int(input());
                            Break;
                        EndIf.
                    While True EndDo.
                EndIf.
            EndFor.
        EndBody."""
        expect=Program([VarDecl(Id('vardecl'),[],ArrayLiteral([StringLiteral('drr'),IntLiteral(291)])),FuncDecl(Id('test'),[],([VarDecl(Id('x'),[],IntLiteral(12))],[For(Id('i'),BinaryOp('*',StringLiteral('dasd'),IntLiteral(12)),StringLiteral('dasd'),StringLiteral('d'),([VarDecl(Id('m'),[],IntLiteral(10))],[If([(BinaryOp('!=',Id('m'),IntLiteral(10)),[VarDecl(Id('x'),[],None)],[]),(BinaryOp('&&',Id('m'),BooleanLiteral(False)),[VarDecl(Id('x'),[],None)],[CallStmt(Id('print'),[Id('x')])])],([],[Dowhile(([],[If([(BinaryOp('==',Id('k'),IntLiteral(10)),[VarDecl(Id('i'),[],None)],[Assign(Id('x'),CallExpr(Id('int'),[CallExpr(Id('input'),[])])),Break()])],([],[]))]),BooleanLiteral(True))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_basic2(self):
        """ """
        input = """
        Var: k = 5, m = {2,5} ;
        Function: test_demo
        Parameter: x,y,z
        Body:
        a[1.2+6] = (5+2) ; 
        EndBody."""
        expect=Program([VarDecl(Id('k'),[],IntLiteral(5)),VarDecl(Id('m'),[],ArrayLiteral([IntLiteral(2),IntLiteral(5)])),FuncDecl(Id('test_demo'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',FloatLiteral(1.2),IntLiteral(6))]),BinaryOp('+',IntLiteral(5),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_return_and_continue(self):
        """ """
        input = """
        Var: k,j,y={};
        Function: test_demo
        Parameter: x,y,z
        Body:
            Return a+.8; 
            Continue; 
        EndBody."""
        expect=Program([VarDecl(Id('k'),[],None),VarDecl(Id('j'),[],None),VarDecl(Id('y'),[],ArrayLiteral([])),FuncDecl(Id('test_demo'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[Return(BinaryOp('+.',Id('a'),IntLiteral(8))),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_return_and_break(self):
        """ """
        input = """
        Var: p = {};
        Function: test_demo
        Parameter: x,y,z
        Body:
            Return foo(foo(a[10]));
            Break; 
            Continue; 
        EndBody."""
        expect=Program([VarDecl(Id('p'),[],ArrayLiteral([])),FuncDecl(Id('test_demo'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[Return(CallExpr(Id('foo'),[CallExpr(Id('foo'),[ArrayCell(Id('a'),[IntLiteral(10)])])])),Break(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_break_in_for(self):
        """ """
        input = """
        Var: k,j,y={};
        Function: breal
        Parameter: x,y,z
        Body:
            For (i=2, i<10, exp() + exp(5)) Do
                Break;        
            EndFor.
        EndBody."""
        expect=Program([VarDecl(Id('k'),[],None),VarDecl(Id('j'),[],None),VarDecl(Id('y'),[],ArrayLiteral([])),FuncDecl(Id('breal'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[For(Id('i'),IntLiteral(2),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',CallExpr(Id('exp'),[]),CallExpr(Id('exp'),[IntLiteral(5)])),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_var_in_func(self):
        input = """
        Function: main
        Body:
        Var: x, y[1][2];
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,2],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_return_arr_cell(self):
        input = """
        Function: main
        Body:
        Return a[1][2][3];
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))    
    
    

    def test_one_break(self):
        input = """
        Function: main
        Body:
        Break;
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    

    def test_continue_in_if(self):
        input = """
        Function: main
        Body:
            If a Then Continue; 
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[If([(Id('a'),[],[Continue()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    def test_continue_in_for(self):
        input = """
        Function: main
        Body:
            For (i=2, i<10, exp() + exp(5)) Do
                Continue; 
                Continue;
                Break;        
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(2),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',CallExpr(Id('exp'),[]),CallExpr(Id('exp'),[IntLiteral(5)])),([],[Continue(),Continue(),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    def test_continue_in_while(self):
        input = """
        Function: main
        Body:
        While a Do
            Continue;
        EndWhile.
        Return ;
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[While(Id('a'),([],[Continue()])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    def test_many_assing_stm_in_fucnction(self):

        input = """Function: varinstmtlist
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                i = i + 1;
                j = j + 10;
            While i <= 10
            EndDo.
        EndBody."""
            
        expect=Program([FuncDecl(Id('varinstmtlist'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[Dowhile(([VarDecl(Id('k'),[],IntLiteral(10))],[Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral(10)))]),BinaryOp('<=',Id('i'),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_simple_love_for(self):
        
        input = """
        Function: foroke
        Body:
            For (i = 0, i < 10, 2) Do
                writeln(i);
                read(5,0); 
            EndFor.
        EndBody."""
           
        expect=Program([FuncDecl(Id('foroke'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('read'),[IntLiteral(5),IntLiteral(0)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_for_and_assign(self):
        
        input = """
        Function: for
        Parameter: n[5]
        Body:
            For (i = 0, i < 10, 1) Do
                n[i]=n+i \.8;
            EndFor.
        EndBody."""
            
        expect=Program([FuncDecl(Id('for'),[VarDecl(Id('n'),[5],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[Assign(ArrayCell(Id('n'),[Id('i')]),BinaryOp('+',Id('n'),BinaryOp('\\.',Id('i'),IntLiteral(8))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_much_so_much(self):
        
        input = """
        Function: formissing
        Body:
            For (i=12, i < l, i*i) Do
            goo("a");
            try_hard(); 
            EndFor.
        EndBody."""
            
        expect=Program([FuncDecl(Id('formissing'),[],([],[For(Id('i'),IntLiteral(12),BinaryOp('<',Id('i'),Id('l')),BinaryOp('*',Id('i'),Id('i')),([],[CallStmt(Id('goo'),[StringLiteral('a')]),CallStmt(Id('try_hard'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    def test_not_qual(self):
        input = """ Function: whiledif
            Body:
            Var: x=20;
            While True Do
                If x==0 Then Break;
                ElseIf a=/= 0 Then
                    x=x\.2;
                Else writeln(x);
                EndIf.
            EndWhile.
        EndBody."""
           
        expect=Program([FuncDecl(Id('whiledif'),[],([VarDecl(Id('x'),[],IntLiteral(20))],[While(BooleanLiteral(True),([],[If([(BinaryOp('==',Id('x'),IntLiteral(0)),[],[Break()]),(BinaryOp('=/=',Id('a'),IntLiteral(0)),[],[Assign(Id('x'),BinaryOp('\\.',Id('x'),IntLiteral(2)))])],([],[CallStmt(Id('writeln'),[Id('x')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_equal(self):
        input = """ Function: equal
        Body:
        If 1 Then Return 1==2;
        EndIf.
        EndBody."""
            
        expect=Program([FuncDecl(Id('equal'),[],([],[If([(IntLiteral(1),[],[Return(BinaryOp('==',IntLiteral(1),IntLiteral(2)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_double_null_func(self):
        input = """ 
        Function: equal
        Body:
        EndBody.
        Function: notequal
        Body:
        EndBody."""
            
        expect=Program([FuncDecl(Id('equal'),[],([],[])),FuncDecl(Id('notequal'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_ForStmt_in_ForStm(self):
        input = """
        Var: a;
        Function: main
        Body:
            For (i=2, i<10, 1) Do
                For (i=2, i<10, exp()) Do
                    If x%2==0 Then
                        printStrLn(arg);
                    Else
                        printStrLn(arg);
                        Continue;
                    EndIf.
                EndFor.
                Continue;
            EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(2),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[For(Id('i'),IntLiteral(2),BinaryOp('<',Id('i'),IntLiteral(10)),CallExpr(Id('exp'),[]),([],[If([(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id('printStrLn'),[Id('arg')])])],([],[CallStmt(Id('printStrLn'),[Id('arg')]),Continue()]))])),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_simple_while_stm(self):
        input = """
        Var: a;
        Function: main
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[0] = 0o5 +. 0xEE;
                i = i + 1;
            EndWhile.
            Return;
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[IntLiteral(0)]),BinaryOp('+.',IntLiteral(5),IntLiteral(238))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_simple_while_stm_in_while_stm(self):
        input = """
        Var: b;
        Function: main
        Body:
            Var: i = 0;
            While (i < 5) Do
                i = i + 1;
                While (i < 5) Do
                    foo(10);
                EndWhile.
            EndWhile.
            Return;
        EndBody.
        """
        expect=Program([VarDecl(Id('b'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[CallStmt(Id('foo'),[IntLiteral(10)])]))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_simple_if_stm_in_while_stm(self):
        input = """
        Var: b;
        Function: bonaoquametvidatten
        Body:
            Var: i = 0.1;
            While (i <= 5) Do
                If m != 10 Then
                    f = 1;
                EndIf.
            EndWhile.
            Return;
        EndBody.
        """
        expect=Program([VarDecl(Id('b'),[],None),FuncDecl(Id('bonaoquametvidatten'),[],([VarDecl(Id('i'),[],FloatLiteral(0.1))],[While(BinaryOp('<=',Id('i'),IntLiteral(5)),([],[If([(BinaryOp('!=',Id('m'),IntLiteral(10)),[],[Assign(Id('f'),IntLiteral(1))])],([],[]))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_simple_if_else_stm_in_while_stm(self):
        input = """
        Var: b;
        Function: tenhamlagibaygio
        Body:
            Var: i = 0.0e4;
            While (i <= 5) Do
                If m != 10 Then
                    x(x);
                Else
                EndIf.
            EndWhile.
            Return;
        EndBody.
        """
        expect=Program([VarDecl(Id('b'),[],None),FuncDecl(Id('tenhamlagibaygio'),[],([VarDecl(Id('i'),[],FloatLiteral(0.0))],[While(BinaryOp('<=',Id('i'),IntLiteral(5)),([],[If([(BinaryOp('!=',Id('m'),IntLiteral(10)),[],[CallStmt(Id('x'),[Id('x')])])],([],[]))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_simple_if_else_elseif_stm_in_while_stm(self):
        input = """
        Var: b;
        Function: canytuongdattest
        Body:
            Var: i = 0.0e4;
            While (i <= 5) Do
                If m != 10 Then
                    x(x);
                ElseIfm == 10 Then a = (-1)[8];
                Else
                EndIf.
            EndWhile.
            Return;
        EndBody.
        """
        expect=Program([VarDecl(Id('b'),[],None),FuncDecl(Id('canytuongdattest'),[],([VarDecl(Id('i'),[],FloatLiteral(0.0))],[While(BinaryOp('<=',Id('i'),IntLiteral(5)),([],[If([(BinaryOp('!=',Id('m'),IntLiteral(10)),[],[CallStmt(Id('x'),[Id('x')])]),(BinaryOp('==',Id('m'),IntLiteral(10)),[],[Assign(Id('a'),ArrayCell(UnaryOp('-',IntLiteral(1)),[IntLiteral(8)]))])],([],[]))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    def test_simple_fully_program88888(self):
        '''global vars,some param, body: var + one stmt'''
        input = """
        Var: a,exp;
        Function: ppl_3
        Parameter: a
        Body:
            Var: b="string",c[10][10];
            b=a\exp;
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('exp'),[],None),FuncDecl(Id('ppl_3'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('b'),[],StringLiteral('string')),VarDecl(Id('c'),[10,10],None)],[Assign(Id('b'),BinaryOp('\\',Id('a'),Id('exp')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

    
