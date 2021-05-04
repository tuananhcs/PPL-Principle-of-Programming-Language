import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_case_300(self):
        """Simple program: int main() {} """
        input = """
        Var: a ;
        Var: b = 10.1;
        Var: c,d;
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],FloatLiteral(10.1)),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_case_301(self):
        """Simple program: int main() {} """
        input = """
        Var: a = {1,2,3};
        Var: b = 10.1;
        Var: c,d;
        """
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('b'),[],FloatLiteral(10.1)),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
        
    def test_case_302(self):
        input = """
        Var: array[1][3];
        Var: a;
        """
        expect=Program([VarDecl(Id('array'),[1,3],None),VarDecl(Id('a'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_case_303(self):
        input = """
        Var: array[1][3];
        Var: a = 0x1122;
        """
        expect=Program([VarDecl(Id('array'),[1,3],None),VarDecl(Id('a'),[],IntLiteral(4386))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
 
    def test_case_304(self):
        input = """
        Var: array[1][3];
        Var: a = 0x1122;
        Var: b = True;
        """
        expect=Program([VarDecl(Id('array'),[1,3],None),VarDecl(Id('a'),[],IntLiteral(4386)),VarDecl(Id('b'),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_case_305(self):
        input = """
        Var: b = 1.E-10;
        """
        expect=Program([VarDecl(Id('b'),[],FloatLiteral(1e-10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
   
    def test_case_306(self):
        input = """
        Var: b = 1.E-10;
        Var: array[2][1] = {{1},{2}};
        """
        expect=Program([VarDecl(Id('b'),[],FloatLiteral(1e-10)),VarDecl(Id('array'),[2,1],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_case_307(self):
        input = """
        Var: b[11000];
        """
        expect=Program([VarDecl(Id('b'),[11000],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_case_308(self):
        input = """
        Var: b[1000] = {1000};
        Var: c = 0o12;
        Var: e,f = False;
        """
        expect=Program([VarDecl(Id('b'),[1000],ArrayLiteral([IntLiteral(1000)])),VarDecl(Id('c'),[],IntLiteral(10)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_case_309(self):
        input = """
        Var: b[0o12][0x11] = {0x11,0x12,True,False};
        Var: c[12][21] = 12;
        """
        expect=Program([VarDecl(Id('b'),[10,17],ArrayLiteral([IntLiteral(17),IntLiteral(18),BooleanLiteral(True),BooleanLiteral(False)])),VarDecl(Id('c'),[12,21],IntLiteral(12))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_case_310(self):
        input = """
        Var: b[0o12][0x11] = {0x11,0x12,True,False};
        Var: c[12][21] = 12;
        Var : d = True;
        Var : f = 0x11;
        Var : g = 0o12;
        Var : h = "khanh";
        """
        expect=Program([VarDecl(Id('b'),[10,17],ArrayLiteral([IntLiteral(17),IntLiteral(18),BooleanLiteral(True),BooleanLiteral(False)])),VarDecl(Id('c'),[12,21],IntLiteral(12)),VarDecl(Id('d'),[],BooleanLiteral(True)),VarDecl(Id('f'),[],IntLiteral(17)),VarDecl(Id('g'),[],IntLiteral(10)),VarDecl(Id('h'),[],StringLiteral('khanh'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_case_311(self):
        input = """
        Var : a,b;
        Function: foo
        Body:

        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    
    def test_case_312(self):
        input = """
        Var : a,b;
        Function: foo
        Body:
        Var: a,b,c,d;

        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_case_313(self):
        input = """
        Var : a,b;
        Function: foo
        Body:
        Var: a;

        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_case_314(self):
        input = """
        Function: foo
        Body:
        foo();
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[CallStmt(Id('foo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_case_315(self):
        input = """
        Function: foo
        Body:
        foo();
        aaaaaaa();
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[CallStmt(Id('foo'),[]),CallStmt(Id('aaaaaaa'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_case_316(self):
        input = """
        Function: foo
        Body:
        foo(1 + 2);
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),IntLiteral(2))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_case_317(self):
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        foo(a);
        foo1(a,b);

        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[CallStmt(Id('foo'),[Id('a')]),CallStmt(Id('foo1'),[Id('a'),Id('b')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_case_318(self):
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Var: h,k = 10;
        Var: r;
        foo(1);

        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([VarDecl(Id('h'),[],None),VarDecl(Id('k'),[],IntLiteral(10)),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_case_319(self):
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Var: h,k = 10;
        Var: r;
        foo(1 + i);

        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([VarDecl(Id('h'),[],None),VarDecl(Id('k'),[],IntLiteral(10)),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),Id('i'))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_case_320(self):
        input = """
        Function: foo
        Body:
        foo(array[1 + foo()]);
        

        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[CallStmt(Id('foo'),[ArrayCell(Id('array'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_case_321(self):
        input = """
        Function: foo
        Body:
            a[0x1][0X2][0o3][0O4][5] = 6e-789;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),FloatLiteral(0.0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_case_322(self):
        input = """
        Function: foo
        Parameter: a
        Body:
        Var: a = 10;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[],IntLiteral(10))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_case_323(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
        
    def test_case_324(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        a(b(c,d),e);
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[CallStmt(Id('a'),[CallExpr(Id('b'),[Id('c'),Id('d')]),Id('e')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_case_325(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a == b Then 
        
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('==',Id('a'),Id('b')),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_case_326(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a != b Then
        Var: a,c[1][2];
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('!=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_case_327(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_case_328(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
            EndIf.
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    def test_case_329(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
            EndIf.
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    
    def test_case_330(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                foo(b);
            EndIf.
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[CallStmt(Id('foo'),[Id('b')])])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    
    def test_case_331(self):
        input = """
        Function: foo
        Body:
            a[1] = 10;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1)]),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_case_332(self):
        input = """
        Function: foo
        Body:
            a[1] = {10};
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1)]),ArrayLiteral([IntLiteral(10)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_case_333(self):
        input = """
        Function: foo
        Body:
            a[1] = {10,11,12,True,{1}};
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1)]),ArrayLiteral([IntLiteral(10),IntLiteral(11),IntLiteral(12),BooleanLiteral(True),ArrayLiteral([IntLiteral(1)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_case_334(self):
        input = """
        Function: foo
        Body:
            a[1][2] = True;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_case_335(self):
        input = """
        Function: foo
        Body:
            a[1][2] = True;
            a[2] = "Khanh";
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),BooleanLiteral(True)),Assign(ArrayCell(Id('a'),[IntLiteral(2)]),StringLiteral('Khanh'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_case_336(self):
        input = """
        Function: foo
        Body:
            a[1 + foo] = c;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('foo'))]),Id('c'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_case_337(self):
        input = """
        Function: foo
        Body:
            a[1 + foo][foo()] = c;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('foo')),CallExpr(Id('foo'),[])]),Id('c'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_case_338(self):
        input = """
        Function: foo
        Body:
            a[1 + foo][foo()][c] = foo(1);
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('foo')),CallExpr(Id('foo'),[]),Id('c')]),CallExpr(Id('foo'),[IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_case_339(self):
        input = """
        Function: foo
        Body:
            a[1 + foo][foo()][c] = foo(1 + foo());
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('foo')),CallExpr(Id('foo'),[]),Id('c')]),CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_case_340(self):
        input = """
        Function: foo
        Body:
            a[1 + foo][foo()][c] = foo(1 + foo(True));
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('foo')),CallExpr(Id('foo'),[]),Id('c')]),CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[BooleanLiteral(True)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_case_341(self):
        input = """
        Function: foo
        Body:
        foo()[1] = 3;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_case_342(self):
        input = """
        Function: foo
        Parameter: a
        Body:
        Return a;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[Return(Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_case_343(self):
        input = """
        Function: foo
        Body:
        Continue;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_case_344(self):
        input = """
        Function: foo
        Body:
        Break;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_case_345(self):
        input = """
        Function: foo
        Body:
        Continue;
        Continue;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Continue(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_case_346(self):
        input = """
        Function: foo
        Body:
        Return b[10];

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Return(ArrayCell(Id('b'),[IntLiteral(10)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_case_347(self):
        input = """
        Function: foo
        Body:
        Return a;
        Break;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[Return(Id('a')),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_case_348(self):
        input = """
        Function: foo
        Body:
        Var: a,b;
        Break;

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_case_349(self):
        input = """
        Function: foo
        Body:
        foo(q);

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[CallStmt(Id('foo'),[Id('q')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_case_350(self):
        input = """
        Var:x,y;
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_case_351(self):
        input = """
        Var: x,y,d="string";
           Function: main
           Parameter: x,xy,a[10]
           Body:
           While s&&a&&b&&c <=. phuc||(le||hoang +18 *29--3*4) Do
           Var: x,y,z; 
           For(i=i,i<10,i+1*2) Do
            Var: x[10]={10,20,0xACF};
            If i>. 123 Then
                Var: q,r,t;
                If phuc==10 Then
                    phuc(x,y,z+3)[hoang[10]]=a[phuc+ !True + "False"+ foo(8+x)[a-1 + b[c[d]]]];
                ElseIf i>. 2.E-10 Then
                ElseIf i==-1 Then
                    Return;
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x<10*8
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('xy'),[],None),VarDecl(Id('a'),[10],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('phuc'),BinaryOp('||',Id('le'),BinaryOp('-',BinaryOp('+',Id('hoang'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4)))))),([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],[For(Id('i'),Id('i'),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),BinaryOp('*',IntLiteral(1),IntLiteral(2))),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>.',Id('i'),IntLiteral(123)),[VarDecl(Id('q'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('t'),[],None)],[If([(BinaryOp('==',Id('phuc'),IntLiteral(10)),[],[Assign(ArrayCell(CallExpr(Id('phuc'),[Id('x'),Id('y'),BinaryOp('+',Id('z'),IntLiteral(3))]),[ArrayCell(Id('hoang'),[IntLiteral(10)])]),ArrayCell(Id('a'),[BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('phuc'),UnaryOp('!',BooleanLiteral(True))),StringLiteral('False')),ArrayCell(CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(8),Id('x'))]),[BinaryOp('+',BinaryOp('-',Id('a'),IntLiteral(1)),ArrayCell(Id('b'),[ArrayCell(Id('c'),[Id('d')])]))]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(2e-10)),[],[]),(BinaryOp('==',Id('i'),UnaryOp('-',IntLiteral(1))),[],[Return(None),Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),BinaryOp('*',IntLiteral(10),IntLiteral(8))))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_case_352(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.

        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_case_353(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.

        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_case_354(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            Var: a;
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)])),VarDecl(Id('a'),[],None)],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_case_355(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While ngo <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',Id('ngo'),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_case_356(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                    If a == b Then
                    EndIf.
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.

        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue(),If([(BinaryOp('==',Id('a'),Id('b')),[],[])],([],[]))])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    def test_case_357(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.
           If a == b Then
           Var: a;
           EndIf.

           EndWhile.
           EndBody.

        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))])),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_case_358(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    
    def test_case_359(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                    a = foo(foo+foo(foo(foo()))) + foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.

        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))])),Assign(Id('a'),BinaryOp('+',CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))])))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])])])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_case_360(self):
        input = """
        Var: x,y,d="string";
           Function: foo
           Parameter: a,b,c[12][12][1]
           Body:
           While s&&a&&b&&c <=. ngo || (ngo + 18 *29--3*4) Do
           Var: a,r,f[10]; 
           Var: a[1] = 10;
           For(i= 0,i < 100,foo+1) Do
            Var: x[10]={10,20,0xACF};
            If i >=. 123 Then
                Var: khanh = "khanh";
                If khanh=="khanh" Then
                    a = foo(foo+foo(foo(foo())));
                    a = foo(foo+foo(foo(foo()))) + foo(foo+foo(foo(foo())));
                ElseIf i>. 2.e10 Then
                ElseIf i=/=f Then
                    Break;
                    Continue;
                EndIf.
                If (n<.2.0) Then
                    call(length,high[a]);
                    If a == k Then
                    Var:  khanh;
                    EndIf.
                Else Return syscall(a,b,c);
                EndIf.
                Do call2(i); While x < a
                EndDo.
            EndIf.
           EndFor.

           EndWhile.
           EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('d'),[],StringLiteral('string')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[12,12,1],None)],([],[While(BinaryOp('<=.',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',Id('s'),Id('a')),Id('b')),Id('c')),BinaryOp('||',Id('ngo'),BinaryOp('-',BinaryOp('+',Id('ngo'),BinaryOp('*',IntLiteral(18),IntLiteral(29))),BinaryOp('*',UnaryOp('-',IntLiteral(3)),IntLiteral(4))))),([VarDecl(Id('a'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('f'),[10],None),VarDecl(Id('a'),[1],IntLiteral(10))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('+',Id('foo'),IntLiteral(1)),([VarDecl(Id('x'),[10],ArrayLiteral([IntLiteral(10),IntLiteral(20),IntLiteral(2767)]))],[If([(BinaryOp('>=.',Id('i'),IntLiteral(123)),[VarDecl(Id('khanh'),[],StringLiteral('khanh'))],[If([(BinaryOp('==',Id('khanh'),StringLiteral('khanh')),[],[Assign(Id('a'),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))])),Assign(Id('a'),BinaryOp('+',CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))]),CallExpr(Id('foo'),[BinaryOp('+',Id('foo'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))])))]),(BinaryOp('>.',Id('i'),FloatLiteral(20000000000.0)),[],[]),(BinaryOp('=/=',Id('i'),Id('f')),[],[Break(),Continue()])],([],[])),If([(BinaryOp('<.',Id('n'),FloatLiteral(2.0)),[],[CallStmt(Id('call'),[Id('length'),ArrayCell(Id('high'),[Id('a')])]),If([(BinaryOp('==',Id('a'),Id('k')),[VarDecl(Id('khanh'),[],None)],[])],([],[]))])],([],[Return(CallExpr(Id('syscall'),[Id('a'),Id('b'),Id('c')]))])),Dowhile(([],[CallStmt(Id('call2'),[Id('i')])]),BinaryOp('<',Id('x'),Id('a')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_case_361(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
        EndFor.
        EndBody.
        
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_case_362(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
            If a == b Then
            EndIf.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))])),If([(BinaryOp('==',Id('a'),Id('b')),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_case_363(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            foo(1 + foo());
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_case_364(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_case_365(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
                a = b;
            EndFor.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)])),Assign(Id('a'),Id('b'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_case_366(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                Var:g[1][29];
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('g'),[1,29],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_case_367(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                Var:g[1][29];
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
            If a =/= b Then
            Var:a;
            ElseIf a ==b Then
                Var: b;
            Else foo(c);
            EndIf.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('g'),[1,29],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))])),If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[]),(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('b'),[],None)],[])],([],[CallStmt(Id('foo'),[Id('c')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_case_368(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                Var:g[1][29];
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
            If a =/= b Then
            Var:a;
            ElseIf a ==b Then
                Var: b;
            EndIf.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('g'),[1,29],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))])),If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[]),(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('b'),[],None)],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_case_369(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: k;
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:b,c,d,s;
                Var:g[1][29];
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
            If a =/= b Then
            Var:a;
            ElseIf a ==b Then
                Var: b;
            Else foo(c);
            EndIf.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('k'),[],None),VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('g'),[1,29],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))])),If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[]),(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('b'),[],None)],[])],([],[CallStmt(Id('foo'),[Id('c')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_case_370(self):
        input = """
        Var: a,b[10];
        Var: a[1] = {1,2};
        Function: foo
        Parameter: a,b[10]
        Body:
        Var: c,d[1];
        For(i = "khanh", i <= 10, i + 1000) Do
            Var: q,e,r;
            foo(1 + foo());
            Do 
                Var:a;
                Var:b,c,d,s;
                Var:g[1][29];
                foo();
            While a == b EndDo.
            For (i = 1, i < 10, i + 1) Do
                a[1 + x] = {1};
            EndFor.
            If a =/= b Then
            Var:a;
            ElseIf a ==b Then
                Var: b;
            Else foo(c);
            EndIf.
        EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[1],None)],[For(Id('i'),StringLiteral('khanh'),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1000)),([VarDecl(Id('q'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))]),Dowhile(([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('g'),[1,29],None)],[CallStmt(Id('foo'),[])]),BinaryOp('==',Id('a'),Id('b'))),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),Id('x'))]),ArrayLiteral([IntLiteral(1)]))])),If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None)],[]),(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('b'),[],None)],[])],([],[CallStmt(Id('foo'),[Id('c')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_case_371(self):
        input = """
        Var:a;
        Function: b
        Body:
        EndBody.

        Function: c
        Body:
        
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([],[])),FuncDecl(Id('c'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_case_372(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: d;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('d'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_case_373(self):
        input = """
        Var:a;
        Function: b
        Body:
        EndBody.

        Function: c
        Body:
        
        EndBody.

        Function: k
        Body:
        
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([],[])),FuncDecl(Id('c'),[],([],[])),FuncDecl(Id('k'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_case_374(self):
        input = """
        Var:a;
        Function: b
        Body:
        EndBody.

        Function: c
        Body:
        
        EndBody.

        Function: k
        Body:
        func();
        
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([],[])),FuncDecl(Id('c'),[],([],[])),FuncDecl(Id('k'),[],([],[CallStmt(Id('func'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_case_375(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: f;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.

        Function: k
        Body:
        Var: f;
        
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('k'),[],([VarDecl(Id('f'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_case_376(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: f;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.

        Function: k
        Body:
        Var: f,d,g;
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('k'),[],([VarDecl(Id('f'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('g'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_case_377(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: f;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.

        Function: k
        Body:
        Var: f;
        Var: a[1][2];
        
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('k'),[],([VarDecl(Id('f'),[],None),VarDecl(Id('a'),[1,2],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_case_378(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: f;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.

        Function: k
        Body:
        Var: a[1][2];
        Var: a[1][2];
        Var: a[1][1];
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('k'),[],([VarDecl(Id('a'),[1,2],None),VarDecl(Id('a'),[1,2],None),VarDecl(Id('a'),[1,1],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_case_379(self):
        input = """
        Var: a[1][2];
        """
        expect=Program([VarDecl(Id('a'),[1,2],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_case_380(self):
        input = """
        Var:a;
        Function: b
        Body:
        Var: f;
        EndBody.

        Function: c
        Body:
        Var: f;
        EndBody.

        Function: k
        Body:
        Var: a[1][2];
        Var: a[1][2];
        foo(1 + foo());
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),FuncDecl(Id('b'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('c'),[],([VarDecl(Id('f'),[],None)],[])),FuncDecl(Id('k'),[],([VarDecl(Id('a'),[1,2],None),VarDecl(Id('a'),[1,2],None)],[CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[]))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    
    def test_case_381(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o12][8]
        Body:
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,10,8],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    def test_case_382(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[10][0o12][8]
        Body:
        Var: num = 0212.323E+2120, r= 10.;
        EndBody.
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[10,10,8],None)],([VarDecl(Id('num'),[],FloatLiteral('inf')),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_case_383(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o12][8]
        Body:
        Var: num = 0212.323E+2120, r= 10.;
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,10,8],None)],([VarDecl(Id('num'),[],FloatLiteral('inf')),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_case_384(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o132][8]
        Body:
        Var: t, r= 10.;
        Var: num = 0212.323E+2120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,90,8],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('num'),[],FloatLiteral('inf')),VarDecl(Id('r'),[],FloatLiteral(10.0))],[Assign(Id('v'),BinaryOp('*',BinaryOp('*',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('a')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_case_385(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o132][8]
        Body:
        Var: t, r= 10.;
        Var: num = 0212.323E+2120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,90,8],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('num'),[],FloatLiteral('inf')),VarDecl(Id('r'),[],FloatLiteral(10.0))],[Assign(Id('v'),BinaryOp('*',BinaryOp('*',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('a')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_case_386(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o12][8]
        Body:
        Var: t, r= 10.;
        Var: num = 0212.323E+2120, r= 10.;
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,10,8],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('num'),[],FloatLiteral('inf')),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_case_387(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o132][8]
        Body:
        Var: t, r= 10.;
        EndBody.
        
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,90,8],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_case_388(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
            Var: a_2k = 12.21; 
        Function: main
        Parameter: khanh[0x111][0o13][8],a,s,d,f,m
        Body:
        Var: t, r= 10.;
        EndBody.
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),VarDecl(Id('a_2k'),[],FloatLiteral(12.21)),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,11,8],None),VarDecl(Id('a'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_case_389(self):
        input = """
        Var:  m[13425], n[1053245] = {1,2,5.e-145232};
        Function: main
        Parameter: khanh[0x111][0o132][8],a,s,d,f,m
        Body:
        Var: t, r= 10.;
        EndBody.
        """
        expect=Program([VarDecl(Id('m'),[13425],None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(0.0)])),FuncDecl(Id('main'),[VarDecl(Id('khanh'),[273,90,8],None),VarDecl(Id('a'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_case_390(self):
        input = """
        Function: foo
        Parameter: a,b[10]
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_case_391(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:

        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_case_392(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_case_393(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_case_394(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_case_395(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo1
        Body:

        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo1'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_case_396(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo2
        Body:
        Var: a,b[12];
        EndBody.
        
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo2'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_case_397(self):
        input = """
        Function: foo
        Parameter: a,b[10],c,call
        Body:
        If a =/= b Then
        Var: a,c[1][2];
        foo(1);
            If a == b Then
                Var: a;
                Var: a,c,v,s,a;
            EndIf.
        EndIf.
        EndBody.

        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo1
        Body:
        Var: a,b;
        EndBody.
        Function: foo2
        Body:
        Var: a,b[12];
        Var: b[12][123];
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[10],None),VarDecl(Id('c'),[],None),VarDecl(Id('call'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[1,2],None)],[CallStmt(Id('foo'),[IntLiteral(1)]),If([(BinaryOp('==',Id('a'),Id('b')),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('v'),[],None),VarDecl(Id('s'),[],None),VarDecl(Id('a'),[],None)],[])],([],[]))])],([],[]))])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[])),FuncDecl(Id('foo2'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12],None),VarDecl(Id('b'),[12,123],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_case_398(self):
        input = """
        Var: a,b[12];
        Var: a,b[12][11];
        
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12,11],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_case_399(self):
        input = """
        Var: a,b[12];
        Var: a,b[12][11];
        Function: done
        Parameter: foo
        Body:
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[12,11],None),FuncDecl(Id('done'),[VarDecl(Id('foo'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399)) 
    
    
