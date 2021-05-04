import unittest
from TestUtils import TestAST
from AST import *

from main.bkit.utils.AST import Id, IntLiteral, VarDecl

class ASTGenSuite(unittest.TestCase):

    def test_0(self):
        input = """Var: x;"""
        expect=Program([VarDecl(Id('x'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_1(self):
        input = """
        Var: a = 8, b = 9;
        Var: d,e,f = {1,2,3},g;
        """
        expect=Program([VarDecl(Id('a'),[],IntLiteral(8)),VarDecl(Id('b'),[],IntLiteral(9)),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('g'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_2(self):
        input = """
        Var: a[3] = {1,2,3}, b = True;
        Var: c[4] = 1;
        """
        expect=Program([VarDecl(Id('a'),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('b'),[],BooleanLiteral(True)),VarDecl(Id('c'),[4],IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_3(self):
        input = """
        Var: a[3][4][6][1000] = "This is a string";
        Var: var_1 = True;
        """
        expect=Program([VarDecl(Id('a'),[3,4,6,1000],StringLiteral('This is a string')),VarDecl(Id('var_1'),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_4(self):
        input = """
        Var: a = 0xABC, b = 0o123;
        """
        expect=Program([VarDecl(Id('a'),[],IntLiteral(2748)),VarDecl(Id('b'),[],IntLiteral(83))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_5(self):
        input = """
        Var: a[0][0xACD][0O353] = {{1,3}, 0o123, 0X34};
        Var: arr_0X123 = 0O123; 
        """
        expect=Program([VarDecl(Id('a'),[0,2765,235],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(83),IntLiteral(52)])),VarDecl(Id('arr_0X123'),[],IntLiteral(83))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_6(self):
        input = """
        Var: a_1 = 0x13ACFE44;
        Var: a_2 = "safds\\fsdfds\\rfasdfsdf";
        """
        expect=Program([VarDecl(Id('a_1'),[],IntLiteral(330104388)),VarDecl(Id('a_2'),[],StringLiteral('safds\\fsdfds\\rfasdfsdf'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_7(self):
        input = """
        Var: arr0x_123[1][0x123ABC] = {{"Hello"}, 0O1243, {"0x123"}, "0O123"};
        """
        arrLit = ArrayLiteral([ArrayLiteral([StringLiteral("Hello")]), IntLiteral(675), ArrayLiteral([StringLiteral("0x123")]), StringLiteral("0O123")])
        expect=Program([VarDecl(Id('arr0x_123'),[1,1194684],ArrayLiteral([ArrayLiteral([StringLiteral('Hello')]),IntLiteral(675),ArrayLiteral([StringLiteral('0x123')]),StringLiteral('0O123')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_8(self):
        input = """
        Var: arr = "This is a string"; **This is a comment**
        Var: a[3][4] = {{{{{{}}}}}};
        """
        varDecl1 = VarDecl(Id('arr'), [], StringLiteral("This is a string"))
        varDecl2 = VarDecl(Id('a'), [3, 4], ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])])])]))
        expect=Program([VarDecl(Id('arr'),[],StringLiteral('This is a string')),VarDecl(Id('a'),[3,4],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_9(self):
        input = """
        ** Var: a = skfajs**
        Var: real_A_A_A_B_B_B = {True,{"string",{0x123,{0o123} **asdfsd**}}};
        """
        expect=Program([VarDecl(Id('real_A_A_A_B_B_B'),[],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([StringLiteral('string'),ArrayLiteral([IntLiteral(291),ArrayLiteral([IntLiteral(83)])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # TEST FUNCTION DECLARATION

    def test_10(self):
        input = """
        Function: fun
        Parameter: a
        Body:
        EndBody.
        """
        expect=Program([FuncDecl(Id('fun'),[VarDecl(Id('a'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """
        Function : foo1
        Body:
            Var: a = 8;
            a = a + 6;
        EndBody.
        Function : foo2
        Body:
            Var: hex = 0x12344A ;
            res = hex > 565;
        EndBody.
        """
        func1 = FuncDecl(Id('foo1'), [], ([VarDecl(Id('a'), [], IntLiteral(8))], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral(6)))]))
        func2 = FuncDecl(Id('foo2'), [], ([VarDecl(Id('hex'), [], IntLiteral(1193034))], [Assign(Id('res'), BinaryOp('>', Id('hex'), IntLiteral(565)))]))
        expect=Program([FuncDecl(Id('foo1'),[],([VarDecl(Id('a'),[],IntLiteral(8))],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(6)))])),FuncDecl(Id('foo2'),[],([VarDecl(Id('hex'),[],IntLiteral(1193034))],[Assign(Id('res'),BinaryOp('>',Id('hex'),IntLiteral(565)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
        Function: this_is_function_1
        Parameter: a, str
        Body:
            a = a + str;
            this_is_function_1(a+1, str+1);
            println(a);
        EndBody.
        """
        expect=Program([FuncDecl(Id('this_is_function_1'),[VarDecl(Id('a'),[],None),VarDecl(Id('str'),[],None)],([],[Assign(Id('a'),BinaryOp('+',Id('a'),Id('str'))),CallStmt(Id('this_is_function_1'),[BinaryOp('+',Id('a'),IntLiteral(1)),BinaryOp('+',Id('str'),IntLiteral(1))]),CallStmt(Id('println'),[Id('a')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
        Function: foo_32_is_32
        Parameter:  a , b
        Body:
            Var: real = 2343.0e3;
            **Just a comment**
            Var: intVar = 0x12233;
            res = real +. intVar;
            Return res;
        EndBody.
        """
        vardecl1 = VarDecl(Id('real'), [], FloatLiteral(2343.0e3))
        vardecl2 = VarDecl(Id('intVar'), [], IntLiteral(74291))
        stmt = Assign(Id('res'), BinaryOp('+.', Id('real'), Id('intVar')))
        returnstmt = Return(Id('res'))
        func = FuncDecl(Id('foo_32_is_32'), [VarDecl(Id('a'), [], FloatLiteral(0.0004)), VarDecl(Id('b'), [], BooleanLiteral(True))], ([vardecl1, vardecl2], [stmt, returnstmt]))
        expect=Program([FuncDecl(Id('foo_32_is_32'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('real'),[],FloatLiteral(2343000.0)),VarDecl(Id('intVar'),[],IntLiteral(74291))],[Assign(Id('res'),BinaryOp('+.',Id('real'),Id('intVar'))),Return(Id('res'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
        Function: foo
        Parameter: a,b,c,d,e,f
        Body:
            (a + foo(3))[5] = 5;
        EndBody.
        """
        eleExp = ArrayCell(BinaryOp('+', Id('a'), CallExpr(Id('foo'), [IntLiteral(3)])), [IntLiteral(5)])
        paramlist = [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None)]
        stmt = Assign(eleExp, IntLiteral(5))
        func = FuncDecl(Id('foo'), paramlist, ([], [stmt]))
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None)],([],[Assign(ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[IntLiteral(3)])),[IntLiteral(5)]),IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
        Function: foo_2
        Body:
            Var: arr[5] = {{}};
            **Comment again #$%$#%^#@^#**
            arr["string"] = "string";
            println(arr);
        EndBody.
        """
        vardecl = VarDecl(Id('arr'), [5], ArrayLiteral([ArrayLiteral([])]))
        assign = Assign(ArrayCell(Id('arr'), [StringLiteral("string")]), StringLiteral("string"))
        stmt = CallStmt(Id('println'), [Id('arr')])
        func = FuncDecl(Id('foo_2'), [], ([vardecl], [assign, stmt]))
        expect=Program([FuncDecl(Id('foo_2'),[],([VarDecl(Id('arr'),[5],ArrayLiteral([ArrayLiteral([])]))],[Assign(ArrayCell(Id('arr'),[StringLiteral('string')]),StringLiteral('string')),CallStmt(Id('println'),[Id('arr')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
        Function: this_is_function **bla bla**
        Parameter: a 
        Body:
            Var: a = 0x123;
            a = this_is_function(0x123) + arr["string"];
            Return a;
        EndBody.
        """
        vardecl = VarDecl(Id('a'), [], IntLiteral(291))
        stmt = Assign(Id('a'), BinaryOp('+', CallExpr(Id('this_is_function'), [IntLiteral(291)]), ArrayCell(Id('arr'), [StringLiteral("string")])))
        retstmt = Return(Id('a'))
        func = FuncDecl(Id('this_is_function'), [VarDecl(Id('a'), [], IntLiteral(291))], ([vardecl], [stmt, retstmt]))
        expect=Program([FuncDecl(Id('this_is_function'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[],IntLiteral(291))],[Assign(Id('a'),BinaryOp('+',CallExpr(Id('this_is_function'),[IntLiteral(291)]),ArrayCell(Id('arr'),[StringLiteral('string')]))),Return(Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
        Function: foo_goo
        Parameter: arr[12][3][0o654] 
        Body:
            **Var : a = 9;**
            arr["0o123"] = foo(6.000001)[5];
            foo(c(b()));
        EndBody.
        """
        paramlist = [VarDecl(Id('arr'), [12, 3, 428], ArrayLiteral([ArrayLiteral([])]))]
        assign = Assign(ArrayCell(Id('arr'), [StringLiteral("0o123")]), ArrayCell(CallExpr(Id('foo'), [FloatLiteral(6.000001)]), [IntLiteral(5)]))
        callstmt = CallStmt(Id('foo'), [CallExpr(Id('c'), [CallExpr(Id('b'), [])])])
        func = FuncDecl(Id('foo_goo'), paramlist, ([], [assign, callstmt]))
        expect=Program([FuncDecl(Id('foo_goo'),[VarDecl(Id('arr'),[12,3,428],None)],([],[Assign(ArrayCell(Id('arr'),[StringLiteral('0o123')]),ArrayCell(CallExpr(Id('foo'),[FloatLiteral(6.000001)]),[IntLiteral(5)])),CallStmt(Id('foo'),[CallExpr(Id('c'),[CallExpr(Id('b'),[])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """
        Function: foo_1
        Body:
            goo_1(foo_1());
        EndBody.
        """
        callstmt1 = CallStmt(Id('goo_1'), [CallExpr(Id('foo_1'), [])])
        func1 = FuncDecl(Id('foo_1'), [], ([], [callstmt1]))

        expect=Program([FuncDecl(Id('foo_1'),[],([],[CallStmt(Id('goo_1'),[CallExpr(Id('foo_1'),[])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
        Function: goo_1
        Parameter: this_is_a_param
        Body:
            foo_1();
            a[0.00045][5e30][0o123][0x123] = (foo_1() % goo_1()) \\. a[4];
        EndBody. 
        """
        callstmt = CallStmt(Id('foo_1'), [])
        arraycell = ArrayCell(Id('a'), [FloatLiteral(0.00045), FloatLiteral(5e30), IntLiteral(83), IntLiteral(291)])
        binaryop = BinaryOp('\\.', BinaryOp('%', CallExpr(Id('foo_1'), []), CallExpr(Id('goo_1'), [])), ArrayCell(Id('a'), [IntLiteral(4)]))
        assign = Assign(arraycell, binaryop)
        func = FuncDecl(Id('goo_1'), [VarDecl(Id('this_is_a_param'), [], None)], ([], [callstmt, assign]))

        expect=Program([FuncDecl(Id('goo_1'),[VarDecl(Id('this_is_a_param'),[],None)],([],[CallStmt(Id('foo_1'),[]),Assign(ArrayCell(Id('a'),[FloatLiteral(0.00045),FloatLiteral(5e+30),IntLiteral(83),IntLiteral(291)]),BinaryOp('\\.',BinaryOp('%',CallExpr(Id('foo_1'),[]),CallExpr(Id('goo_1'),[])),ArrayCell(Id('a'),[IntLiteral(4)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    # TEST IF STATEMENT

    def test_20(self):
        input = """
        Function: test
        Parameter: arr[1000]
        Body:
            If !len(arr) 
                Then Return {}; 
            EndIf.
        EndBody."""
        returnStmt = Return(ArrayLiteral([]))
        ifThenStmt = [(UnaryOp('!', CallExpr(Id('len'), [Id('arr')])), [], [returnStmt])]
        elseStmt = ([], [])
        ifstmt = If(ifThenStmt, elseStmt)
        func = FuncDecl(Id('test'), [VarDecl(Id('arr'), [1000], None)], ([], [ifstmt]))
        expect=Program([FuncDecl(Id('test'),[VarDecl(Id('arr'),[1000],None)],([],[If([(UnaryOp('!',CallExpr(Id('len'),[Id('arr')])),[],[Return(ArrayLiteral([]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """
        Function: a
        Body:
            Var: a[0x123][0o456] = {{{}}};
            If a >= 8 Then
                a[identifier] = 2;
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('a'),[],([VarDecl(Id('a'),[291,302],ArrayLiteral([ArrayLiteral([ArrayLiteral([])])]))],[If([(BinaryOp('>=',Id('a'),IntLiteral(8)),[],[Assign(ArrayCell(Id('a'),[Id('identifier')]),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        input = """
        Function: a
        Body:
            a = !len(arr);
            Return {};
        EndBody.
        """
        expect=Program([FuncDecl(Id('a'),[],([],[Assign(Id('a'),UnaryOp('!',CallExpr(Id('len'),[Id('arr')]))),Return(ArrayLiteral([]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        input = """
        Var: x;
        Function: m
        Body:
            If a == False Then
                a["string"] = a[0xDEF]["string2" **Just comment**];
            EndIf.
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),FuncDecl(Id('m'),[],([],[If([(BinaryOp('==',Id('a'),BooleanLiteral(False)),[],[Assign(ArrayCell(Id('a'),[StringLiteral('string')]),ArrayCell(Id('a'),[IntLiteral(3567),StringLiteral('string2')]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        input = """
        Function: iF_Func
        Body:
            If real_me >= 0.000e4 Then
                real_me = real_me + 1;
            ElseIf real_me < 5 Then
                println("Hello world");
            Else
                foo(9);
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('iF_Func'),[],([],[If([(BinaryOp('>=',Id('real_me'),FloatLiteral(0.0)),[],[Assign(Id('real_me'),BinaryOp('+',Id('real_me'),IntLiteral(1)))]),(BinaryOp('<',Id('real_me'),IntLiteral(5)),[],[CallStmt(Id('println'),[StringLiteral('Hello world')])])],([],[CallStmt(Id('foo'),[IntLiteral(9)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        input = """
        Function: a
        Body:
            If a == foo_2(arr) Then
                Return {False};
            EndIf.
        EndBody.
        
        **New function**
        
        Function: foo_2
        Parameter: a[0x123][0o623]
        Body:
            Var: b = 8;
            If a["index"] == 6 Then
                a["index"] = 566.677 *. 34.34;
            Else
                a["index"] = False;
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('a'),[],([],[If([(BinaryOp('==',Id('a'),CallExpr(Id('foo_2'),[Id('arr')])),[],[Return(ArrayLiteral([BooleanLiteral(False)]))])],([],[]))])),FuncDecl(Id('foo_2'),[VarDecl(Id('a'),[291,403],None)],([VarDecl(Id('b'),[],IntLiteral(8))],[If([(BinaryOp('==',ArrayCell(Id('a'),[StringLiteral('index')]),IntLiteral(6)),[],[Assign(ArrayCell(Id('a'),[StringLiteral('index')]),BinaryOp('*.',FloatLiteral(566.677),FloatLiteral(34.34)))])],([],[Assign(ArrayCell(Id('a'),[StringLiteral('index')]),BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_26(self):
        input = """
        Function: a
        Parameter: a[0x123], str 
        Body:
            If 4 Then 
                If 4 Then 
                    If 4 Then 
                        If 4 Then 
                            If 4 Then
                                println("helloWorld");
                            EndIf.
                        EndIf.
                    EndIf.        
                EndIf.
            EndIf.
        EndBody.
         """
        expect=Program([FuncDecl(Id('a'),[VarDecl(Id('a'),[291],None),VarDecl(Id('str'),[],None)],([],[If([(IntLiteral(4),[],[If([(IntLiteral(4),[],[If([(IntLiteral(4),[],[If([(IntLiteral(4),[],[If([(IntLiteral(4),[],[CallStmt(Id('println'),[StringLiteral('helloWorld')])])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        input = """
        Var: a = "#$%#$^$653664^%#^$%^";
        **Just a comment**
        Function: a
        Body:
            If a >= 7 Then
                print("hello");
            EndIf.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],StringLiteral('#$%#$^$653664^%#^$%^')),FuncDecl(Id('a'),[],([],[If([(BinaryOp('>=',Id('a'),IntLiteral(7)),[],[CallStmt(Id('print'),[StringLiteral('hello')])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_28(self):
        input = """
        Function: foo_test_if
        Parameter: a, b,e,d,g,h
        Body:
            Var: a = 5.e3;
            If (a || 7) && (!a && b) Then
                a = (a || b);
                If a <= 7 Then println(a); EndIf.
            EndIf. 
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo_test_if'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('g'),[],None),VarDecl(Id('h'),[],None)],([VarDecl(Id('a'),[],FloatLiteral(5000.0))],[If([(BinaryOp('&&',BinaryOp('||',Id('a'),IntLiteral(7)),BinaryOp('&&',UnaryOp('!',Id('a')),Id('b'))),[],[Assign(Id('a'),BinaryOp('||',Id('a'),Id('b'))),If([(BinaryOp('<=',Id('a'),IntLiteral(7)),[],[CallStmt(Id('println'),[Id('a')])])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_29(self):
        input = """
         Function: a
         Parameter: var_123 
         Body:
            If var_123 Then Return "Hello";
            ElseIf var_123 == 1 Then 
                println("hello");
            ElseIf var_123 == 2 Then
                Var: a = 4;
                If a == 5 Then 
                    a = ((a || !b) && c) % 32;
                    Return a;
                EndIf.
            Else
                Return True;
            EndIf.
         EndBody.
         """
        expect=Program([FuncDecl(Id('a'),[VarDecl(Id('var_123'),[],None)],([],[If([(Id('var_123'),[],[Return(StringLiteral('Hello'))]),(BinaryOp('==',Id('var_123'),IntLiteral(1)),[],[CallStmt(Id('println'),[StringLiteral('hello')])]),(BinaryOp('==',Id('var_123'),IntLiteral(2)),[VarDecl(Id('a'),[],IntLiteral(4))],[If([(BinaryOp('==',Id('a'),IntLiteral(5)),[],[Assign(Id('a'),BinaryOp('%',BinaryOp('&&',BinaryOp('||',Id('a'),UnaryOp('!',Id('b'))),Id('c')),IntLiteral(32))),Return(Id('a'))])],([],[]))])],([],[Return(BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    # TEST WHILE

    def test_30(self):
        input = """
        Function: foo
        Body:
            While a >= 6 Do
                a = a + 5;
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[While(BinaryOp('>=',Id('a'),IntLiteral(6)),([],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(5)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_31(self):
        input = """
        Var: a[1][3] = {{}};
        Var: b = True;
        Function: foo_1
        Parameter: a,b,c,d,e,f,g,h
        Body:
            While (a + 8) - (a || b) == 8 Do
                a = (a + b) - 7;
                foo(1);
            EndWhile.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[1,3],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id('b'),[],BooleanLiteral(True)),FuncDecl(Id('foo_1'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('g'),[],None),VarDecl(Id('h'),[],None)],([],[While(BinaryOp('==',BinaryOp('-',BinaryOp('+',Id('a'),IntLiteral(8)),BinaryOp('||',Id('a'),Id('b'))),IntLiteral(8)),([],[Assign(Id('a'),BinaryOp('-',BinaryOp('+',Id('a'),Id('b')),IntLiteral(7))),CallStmt(Id('foo'),[IntLiteral(1)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_32(self):
        input = """
        Function: test_while_2
        Body:
            While (a == b - 5) && (a || !b) Do
                a  = 1 + arr[66];
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_while_2'),[],([],[While(BinaryOp('&&',BinaryOp('==',Id('a'),BinaryOp('-',Id('b'),IntLiteral(5))),BinaryOp('||',Id('a'),UnaryOp('!',Id('b')))),([],[Assign(Id('a'),BinaryOp('+',IntLiteral(1),ArrayCell(Id('arr'),[IntLiteral(66)])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_33(self):
        input = """
        Function: foo_2
        Body:
            While a Do
                While a Do
                    While a Do
                        While a Do
                            While a Do
                                While a Do
                                    print(a + 55, base == 16);
                                EndWhile.
                            EndWhile.
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo_2'),[],([],[While(Id('a'),([],[While(Id('a'),([],[While(Id('a'),([],[While(Id('a'),([],[While(Id('a'),([],[While(Id('a'),([],[CallStmt(Id('print'),[BinaryOp('+',Id('a'),IntLiteral(55)),BinaryOp('==',Id('base'),IntLiteral(16))])]))]))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_34(self):
        input = """
        Function: test_While
        Parameter:  arr_23432[3443]
        Body:
            While (arr_23432[0.30023] || 5.49745) >= 98.5345 Do
                If arr["indexString"] == 0.4324 Then
                    a = a + foo(hello);
                EndIf.
            EndWhile.
        EndBody. 
        """
        expect=Program([FuncDecl(Id('test_While'),[VarDecl(Id('arr_23432'),[3443],None)],([],[While(BinaryOp('>=',BinaryOp('||',ArrayCell(Id('arr_23432'),[FloatLiteral(0.30023)]),FloatLiteral(5.49745)),FloatLiteral(98.5345)),([],[If([(BinaryOp('==',ArrayCell(Id('arr'),[StringLiteral('indexString')]),FloatLiteral(0.4324)),[],[Assign(Id('a'),BinaryOp('+',Id('a'),CallExpr(Id('foo'),[Id('hello')])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_35(self):
        input = """
        Function: test_While
        Parameter: some_param
        Body:
            Var: arr[3][4][4][2] = {"fjsakfjskldf$#$#", {24.234,42.2342}};
            If arr == True Then
                arr = (1 + foo(454354))["srre"];
                While !arr Do
                    println(foo(5));
                EndWhile.
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_While'),[VarDecl(Id('some_param'),[],None)],([VarDecl(Id('arr'),[3,4,4,2],ArrayLiteral([StringLiteral('fjsakfjskldf$#$#'),ArrayLiteral([FloatLiteral(24.234),FloatLiteral(42.2342)])]))],[If([(BinaryOp('==',Id('arr'),BooleanLiteral(True)),[],[Assign(Id('arr'),ArrayCell(BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[IntLiteral(454354)])),[StringLiteral('srre')])),While(UnaryOp('!',Id('arr')),([],[CallStmt(Id('println'),[CallExpr(Id('foo'),[IntLiteral(5)])])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_36(self):
        input = """
        Function: test_while
        Parameter: a[5]
        Body:
            While a Do
                While !a Do
                    If a Then
                        println("sfasdfasd", !6, !(f + f(9)));
                    EndIf.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_while'),[VarDecl(Id('a'),[5],None)],([],[While(Id('a'),([],[While(UnaryOp('!',Id('a')),([],[If([(Id('a'),[],[CallStmt(Id('println'),[StringLiteral('sfasdfasd'),UnaryOp('!',IntLiteral(6)),UnaryOp('!',BinaryOp('+',Id('f'),CallExpr(Id('f'),[IntLiteral(9)])))])])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_37(self):
        input = """
        Function: test_while_1_
        Parameter: a,b,c,d,e,f,g
        Body:
            If !(a + foo(foo(5))) Then
                While True Do
                    println(hello);
                EndWhile.
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_while_1_'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('g'),[],None)],([],[If([(UnaryOp('!',BinaryOp('+',Id('a'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(5)])]))),[],[While(BooleanLiteral(True),([],[CallStmt(Id('println'),[Id('hello')])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_38(self):
        input = """
        Function: test_while_1_
        Parameter: a,b,c,d,e,f,g
        Body:
            If !(a + foo(foo(5))) Then
                println(hello);
            EndIf.
        EndBody.
        
                ** COMMENT ** 
                
        Function: test_while_2_
        Parameter: a,b,c,d,e,f,g,h,i,k,l,m,n
        Body:
            If !(a + foo(foo(5))) Then
                While a == foo(foo(foo(foo(!7)))) Do
                    println("I Love You");
                EndWhile.
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_while_1_'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('g'),[],None)],([],[If([(UnaryOp('!',BinaryOp('+',Id('a'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(5)])]))),[],[CallStmt(Id('println'),[Id('hello')])])],([],[]))])),FuncDecl(Id('test_while_2_'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('g'),[],None),VarDecl(Id('h'),[],None),VarDecl(Id('i'),[],None),VarDecl(Id('k'),[],None),VarDecl(Id('l'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([],[If([(UnaryOp('!',BinaryOp('+',Id('a'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(5)])]))),[],[While(BinaryOp('==',Id('a'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[UnaryOp('!',IntLiteral(7))])])])])),([],[CallStmt(Id('println'),[StringLiteral('I Love You')])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
        
    def test_39(self):
        input = """
        Function: wHiLe_HiHi_HeHe
        Parameter: fast
        Body:
            While True Do
                println("Maybe this is the last testcase");
                If 1 == 1 Then Break; EndIf.
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('wHiLe_HiHi_HeHe'),[VarDecl(Id('fast'),[],None)],([],[While(BooleanLiteral(True),([],[CallStmt(Id('println'),[StringLiteral('Maybe this is the last testcase')]),If([(BinaryOp('==',IntLiteral(1),IntLiteral(1)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    # TEST DO WHILE

    def test_40(self):
        input = """
        Function: test_while
        Parameter: var
        Body:
            Do
                print(foo(pdf));
            While a
            EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_while'),[VarDecl(Id('var'),[],None)],([],[Dowhile(([],[CallStmt(Id('print'),[CallExpr(Id('foo'),[Id('pdf')])])]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_41(self):
        input = """
        Function: do_WHILE_2
        Parameter: var
        Body:
            Do
                If var Then
                    println(var);
                EndIf.
            While var
            EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('do_WHILE_2'),[VarDecl(Id('var'),[],None)],([],[Dowhile(([],[If([(Id('var'),[],[CallStmt(Id('println'),[Id('var')])])],([],[]))]),Id('var'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_42(self):
        input = """
        Function: rewrw_rwerwer_rwrwer
        Parameter: laksjflasfjlsf_afefae
        Body:
            Do 
                Do 
                    Do
                        Do
                            a = a + foo(2)[5][0x123];
                        While a EndDo.    
                    While a EndDo.
                While a EndDo.
            While a EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('rewrw_rwerwer_rwrwer'),[VarDecl(Id('laksjflasfjlsf_afefae'),[],None)],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Assign(Id('a'),BinaryOp('+',Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(5),IntLiteral(291)])))]),Id('a'))]),Id('a'))]),Id('a'))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_43(self):
        input = """
        Function: foo_goo
        Parameter: hello[0x123][0o456]
        Body:
            If hello == !(!(!(35 || 4353))) Then
                Do
                    Var: a = 5;
                    println("hello");
                    foo(foo(32587348925793));
                While True EndDo.
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo_goo'),[VarDecl(Id('hello'),[291,302],None)],([],[If([(BinaryOp('==',Id('hello'),UnaryOp('!',UnaryOp('!',UnaryOp('!',BinaryOp('||',IntLiteral(35),IntLiteral(4353)))))),[],[Dowhile(([VarDecl(Id('a'),[],IntLiteral(5))],[CallStmt(Id('println'),[StringLiteral('hello')]),CallStmt(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(32587348925793)])])]),BooleanLiteral(True))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_44(self):
        input = """
        Function: test_do_while
        Parameter: param
        Body:
            Var: vardecl = "43535345";
            Do
                If a Then
                    Do
                        If a Then
                            Do
                                print("hello world");
                            While a EndDo.
                        EndIf.
                    While a EndDo.
                EndIf.
            While a EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_do_while'),[VarDecl(Id('param'),[],None)],([VarDecl(Id('vardecl'),[],StringLiteral('43535345'))],[Dowhile(([],[If([(Id('a'),[],[Dowhile(([],[If([(Id('a'),[],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral('hello world')])]),Id('a'))])],([],[]))]),Id('a'))])],([],[]))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_45(self):
        input = """
        Function: function
        Parameter: hehhehshe
        Body:
            Do
                While a Do
                    print("hfasdfkjals");
                    foo(foo(foo(goo(5))));
                    Do
                        print("Hello world");
                    While a EndDo.
                EndWhile.
            While a == 0
            EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('function'),[VarDecl(Id('hehhehshe'),[],None)],([],[Dowhile(([],[While(Id('a'),([],[CallStmt(Id('print'),[StringLiteral('hfasdfkjals')]),CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(5)])])])]),Dowhile(([],[CallStmt(Id('print'),[StringLiteral('Hello world')])]),Id('a'))]))]),BinaryOp('==',Id('a'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_46(self):
        input = """
        Function: test_do_while
        Parameter: sjfasldfjksl
        Body:
            Do 
                While a >= 0 Do
                    println("hello world");
                    If askdf == "stsafjklsjdlkfj" Then
                        foo(goo(5));
                    EndIf.
                EndWhile.
            While (!(!(a || b))) EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_do_while'),[VarDecl(Id('sjfasldfjksl'),[],None)],([],[Dowhile(([],[While(BinaryOp('>=',Id('a'),IntLiteral(0)),([],[CallStmt(Id('println'),[StringLiteral('hello world')]),If([(BinaryOp('==',Id('askdf'),StringLiteral('stsafjklsjdlkfj')),[],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(5)])])])],([],[]))]))]),UnaryOp('!',UnaryOp('!',BinaryOp('||',Id('a'),Id('b')))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_47(self):
        input = """
        Function: do_whileeeeeeeee
        Parameter: weirwerwerwe
        Body:
            Do
                Return radixsort(arr);
            While !!!!a
            EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('do_whileeeeeeeee'),[VarDecl(Id('weirwerwerwe'),[],None)],([],[Dowhile(([],[Return(CallExpr(Id('radixsort'),[Id('arr')]))]),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',Id('a'))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_48(self):
        input = """
        Function: skldfjsf
        Parameter: uio5u34534oiu435
        Body:
            Do 
                print(jfalksjfljsd);
                foo(fdsafs);
                If a Then
                    goo(rewr);
                EndIf.
            While !!!(wer || wrw || wrw && fksaf) EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('skldfjsf'),[VarDecl(Id('uio5u34534oiu435'),[],None)],([],[Dowhile(([],[CallStmt(Id('print'),[Id('jfalksjfljsd')]),CallStmt(Id('foo'),[Id('fdsafs')]),If([(Id('a'),[],[CallStmt(Id('goo'),[Id('rewr')])])],([],[]))]),UnaryOp('!',UnaryOp('!',UnaryOp('!',BinaryOp('&&',BinaryOp('||',BinaryOp('||',Id('wer'),Id('wrw')),Id('wrw')),Id('fksaf'))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_49(self):
        input = """
        Function: the_last_do_while
        Parameter: rpt_mck
        Body:
            Do
                print("rap melody");
                println("my niece will call you grandma");
                If mck Then
                    love(mck, thanh_draw, gonzo);
                EndIf.
            While mck && tlinh EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('the_last_do_while'),[VarDecl(Id('rpt_mck'),[],None)],([],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral('rap melody')]),CallStmt(Id('println'),[StringLiteral('my niece will call you grandma')]),If([(Id('mck'),[],[CallStmt(Id('love'),[Id('mck'),Id('thanh_draw'),Id('gonzo')])])],([],[]))]),BinaryOp('&&',Id('mck'),Id('tlinh')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    # TEST FOR

    def test_50(self):
        input = """
        Function: for_1
        Parameter: param
        Body:
            For (i = 0, i <= 10, i + 2) Do
                If i == 5 Then Break;
                EndIf.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('for_1'),[VarDecl(Id('param'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<=',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(2)),([],[If([(BinaryOp('==',Id('i'),IntLiteral(5)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_51(self):
        input = """
        Function: for_2
        Parameter: osad, long_nger
        Body:
            For (count = 100, count >= 28, count || 7) Do
                If diss(osad, long_nger) Then
                    diss(long_nger, osad);
                    print("rap battle");
                EndIf.
                watch(audience);
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('for_2'),[VarDecl(Id('osad'),[],None),VarDecl(Id('long_nger'),[],None)],([],[For(Id('count'),IntLiteral(100),BinaryOp('>=',Id('count'),IntLiteral(28)),BinaryOp('||',Id('count'),IntLiteral(7)),([],[If([(CallExpr(Id('diss'),[Id('osad'),Id('long_nger')]),[],[CallStmt(Id('diss'),[Id('long_nger'),Id('osad')]),CallStmt(Id('print'),[StringLiteral('rap battle')])])],([],[])),CallStmt(Id('watch'),[Id('audience')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_52(self):
        input = """
        Function: rapviet
        Parameter: list[324234]
        Body:
            For (i = 1, i <= 15, i + 1) Do
                champion(de_choat);
                Do
                    print("gducky is better than de_choat");
                While champion(gducky) EndDo.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('rapviet'),[VarDecl(Id('list'),[324234],None)],([],[For(Id('i'),IntLiteral(1),BinaryOp('<=',Id('i'),IntLiteral(15)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[CallStmt(Id('champion'),[Id('de_choat')]),Dowhile(([],[CallStmt(Id('print'),[StringLiteral('gducky is better than de_choat')])]),CallExpr(Id('champion'),[Id('gducky')]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_53(self):
        input = """
        Function: loop_for
        Body:
            For (i = !!!!(foo(!(5))), i >= 0x1234, i && 4234) Do
                For (j = 5, j <= 20, j + 1) Do
                    print("hello world");
                    If hello == hello Then
                        foo(foo(!!!!!!t));
                    EndIf.
                EndFor.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('loop_for'),[],([],[For(Id('i'),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',CallExpr(Id('foo'),[UnaryOp('!',IntLiteral(5))]))))),BinaryOp('>=',Id('i'),IntLiteral(4660)),BinaryOp('&&',Id('i'),IntLiteral(4234)),([],[For(Id('j'),IntLiteral(5),BinaryOp('<=',Id('j'),IntLiteral(20)),BinaryOp('+',Id('j'),IntLiteral(1)),([],[CallStmt(Id('print'),[StringLiteral('hello world')]),If([(BinaryOp('==',Id('hello'),Id('hello')),[],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',Id('t')))))))])])])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_54(self):
        input = """
        Function: loop_of_loop
        Body:
            For (i = 1, i < 10, i+1) Do
                For (i = 2, i < 10, i+2) Do
                    For (i = 3, i < 10, i + 3) Do
                        For (i = 4, i < 10, i + 4) Do
                            For (i = 5, i < 10, i + 5) Do
                                For (i = 6, i < 10, i + 6) Do
                                    For (i = 7, i < 10, i + 7) Do
                                        print("hello world");
                                    EndFor.
                                EndFor.
                            EndFor.
                        EndFor.
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('loop_of_loop'),[],([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[For(Id('i'),IntLiteral(2),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(2)),([],[For(Id('i'),IntLiteral(3),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(3)),([],[For(Id('i'),IntLiteral(4),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(4)),([],[For(Id('i'),IntLiteral(5),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(5)),([],[For(Id('i'),IntLiteral(6),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(6)),([],[For(Id('i'),IntLiteral(7),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(7)),([],[CallStmt(Id('print'),[StringLiteral('hello world')])]))]))]))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_55(self):
        input = """
        Function: test_LOOP_FOR
        Parameter: thai_phuc_hiep
        Body:
            For (i = foo(755)[543534], i <= !(76543 || 534534), i + !(!(1))) Do
                If a >= 8 Then println("Hello world"); EndIf.
                While a Do
                    (a + foo[1])[5] = 456.6456 \. 5354334;
                EndWhile.
                Do
                    println("eminem");
                While isAlive(eminem) EndDo.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test_LOOP_FOR'),[VarDecl(Id('thai_phuc_hiep'),[],None)],([],[For(Id('i'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(755)]),[IntLiteral(543534)]),BinaryOp('<=',Id('i'),UnaryOp('!',BinaryOp('||',IntLiteral(76543),IntLiteral(534534)))),BinaryOp('+',Id('i'),UnaryOp('!',UnaryOp('!',IntLiteral(1)))),([],[If([(BinaryOp('>=',Id('a'),IntLiteral(8)),[],[CallStmt(Id('println'),[StringLiteral('Hello world')])])],([],[])),While(Id('a'),([],[Assign(ArrayCell(BinaryOp('+',Id('a'),ArrayCell(Id('foo'),[IntLiteral(1)])),[IntLiteral(5)]),BinaryOp('\\.',FloatLiteral(456.6456),IntLiteral(5354334)))])),Dowhile(([],[CallStmt(Id('println'),[StringLiteral('eminem')])]),CallExpr(Id('isAlive'),[Id('eminem')]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_56(self):
        input = """
        Function: some_blabla_function
        Body: 
            For (i = 69 , i <= !(100 && ( 55|| 5345)), i \. 44793827) Do 
                println("Empty function");
            EndFor.
        EndBody.
            
        ** Function 2**
        
        Function: another_blabla_function
        Parameter: rapviet
        Body:
            For (i = 0, i <= 10000, i + 1) Do
                println("Karik and Rhymatstic is gonna diss Torai9 together");
                If win(karik) || win(rhymmastic) Then
                    println("That\\'s awesome !!!");
                EndIf.
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('some_blabla_function'),[],([],[For(Id('i'),IntLiteral(69),BinaryOp('<=',Id('i'),UnaryOp('!',BinaryOp('&&',IntLiteral(100),BinaryOp('||',IntLiteral(55),IntLiteral(5345))))),BinaryOp('\\.',Id('i'),IntLiteral(44793827)),([],[CallStmt(Id('println'),[StringLiteral('Empty function')])]))])),FuncDecl(Id('another_blabla_function'),[VarDecl(Id('rapviet'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<=',Id('i'),IntLiteral(10000)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[CallStmt(Id('println'),[StringLiteral('Karik and Rhymatstic is gonna diss Torai9 together')]),If([(BinaryOp('||',CallExpr(Id('win'),[Id('karik')]),CallExpr(Id('win'),[Id('rhymmastic')])),[],[CallStmt(Id('println'),[StringLiteral('That\\\'s awesome !!!')])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_57(self):
        input = """
        Function: hello_world
        Parameter: hihi_hehe
        Body:
            For (a= binz(9), a>= binz(9), a + !binz(9)) Do
                love(binz(9) && chaubui(9));
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('hello_world'),[VarDecl(Id('hihi_hehe'),[],None)],([],[For(Id('a'),CallExpr(Id('binz'),[IntLiteral(9)]),BinaryOp('>=',Id('a'),CallExpr(Id('binz'),[IntLiteral(9)])),BinaryOp('+',Id('a'),UnaryOp('!',CallExpr(Id('binz'),[IntLiteral(9)]))),([],[CallStmt(Id('love'),[BinaryOp('&&',CallExpr(Id('binz'),[IntLiteral(9)]),CallExpr(Id('chaubui'),[IntLiteral(9)]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_58(self):
        input = """
        Function: reduce
        Parameter: arr[100], function
        Body:
            Var: res = 0;
            For (i = 0 , i < size(arr), i+1) Do
                res = res + function(arr[i]);
            EndFor.
            Return res;
        EndBody.
        """
        expect=Program([FuncDecl(Id('reduce'),[VarDecl(Id('arr'),[100],None),VarDecl(Id('function'),[],None)],([VarDecl(Id('res'),[],IntLiteral(0))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),CallExpr(Id('size'),[Id('arr')])),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(Id('res'),BinaryOp('+',Id('res'),CallExpr(Id('function'),[ArrayCell(Id('arr'),[Id('i')])])))])),Return(Id('res'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_59(self):
        input = """
        Function: yahoo______
        Parameter: string
        Body:
            println("this is the last function =)))))");
            println("please give me 10 points");
            println("I love you so much");
            println("moah");
            foo(foo(foo(foo(foo(foo(foo(!!!!!!6)))))));
        EndBody.
        """
        expect=Program([FuncDecl(Id('yahoo______'),[VarDecl(Id('string'),[],None)],([],[CallStmt(Id('println'),[StringLiteral('this is the last function =)))))')]),CallStmt(Id('println'),[StringLiteral('please give me 10 points')]),CallStmt(Id('println'),[StringLiteral('I love you so much')]),CallStmt(Id('println'),[StringLiteral('moah')]),CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',IntLiteral(6)))))))])])])])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    # TEST MIX

    def test_60(self):
        input = """
        Var: s = "this is Thai Phuc Hiep";
        Function: main
        Body:
            Var: arr[26];
            f = fact(n) % (0O10443 || 432432);
            While (i < length(s)) Do
                arr[lower(s[i]) - 97] =  arr[lower(s[i]) - 97] +. 1.e0;
            EndWhile.
            max_length = max(arr);
        EndBody.
            
        **New Function**
             
        Function: sum
        Parameter: nope
        Body:
            p = 1.00345345;
            For (i = 1, i < n, 1) Do
                p = p *. i + (!!!!!6456546);
            EndFor.
            Return i;
        EndBody.
        """
        expect=Program([VarDecl(Id('s'),[],StringLiteral('this is Thai Phuc Hiep')),FuncDecl(Id('main'),[],([VarDecl(Id('arr'),[26],None)],[Assign(Id('f'),BinaryOp('%',CallExpr(Id('fact'),[Id('n')]),BinaryOp('||',IntLiteral(4387),IntLiteral(432432)))),While(BinaryOp('<',Id('i'),CallExpr(Id('length'),[Id('s')])),([],[Assign(ArrayCell(Id('arr'),[BinaryOp('-',CallExpr(Id('lower'),[ArrayCell(Id('s'),[Id('i')])]),IntLiteral(97))]),BinaryOp('+.',ArrayCell(Id('arr'),[BinaryOp('-',CallExpr(Id('lower'),[ArrayCell(Id('s'),[Id('i')])]),IntLiteral(97))]),FloatLiteral(1.0)))])),Assign(Id('max_length'),CallExpr(Id('max'),[Id('arr')]))])),FuncDecl(Id('sum'),[VarDecl(Id('nope'),[],None)],([],[Assign(Id('p'),FloatLiteral(1.00345345)),For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),Id('n')),IntLiteral(1),([],[Assign(Id('p'),BinaryOp('+',BinaryOp('*.',Id('p'),Id('i')),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',IntLiteral(6456546))))))))])),Return(Id('i'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_61(self):
        input = """
        Function: iflongnhau
        Parameter: a, b
        Body:
            Var: id[4412][867][9856][867], stringID[108] = "this is a string",literal = 120000e-1,  array[2][4] = {{867,445,987},{76,12,744}};
            If n > 10 Then
                If n <. 20.5 Then Return x;
                EndIf.
                printStrLn(arg);
            Else fact(x);
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('iflongnhau'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('id'),[4412,867,9856,867],None),VarDecl(Id('stringID'),[108],StringLiteral('this is a string')),VarDecl(Id('literal'),[],FloatLiteral(12000.0)),VarDecl(Id('array'),[2,4],ArrayLiteral([ArrayLiteral([IntLiteral(867),IntLiteral(445),IntLiteral(987)]),ArrayLiteral([IntLiteral(76),IntLiteral(12),IntLiteral(744)])]))],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[If([(BinaryOp('<.',Id('n'),FloatLiteral(20.5)),[],[Return(Id('x'))])],([],[])),CallStmt(Id('printStrLn'),[Id('arg')])])],([],[CallStmt(Id('fact'),[Id('x')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_62(self):
        input = """
        Var: x, y=1, y, m[1], n[10] = {1,2,{"antlr",5.4},5.e-1285435};
        Var: a_wrewrwe;
        Function: fact
        Parameter: n, rwrwerwerwer[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
            Var: t, r= 10.;
            Var: thread = 0000212.3123E+31, r= 10.;
            v = (4. \. 3.) *. 3.14 *. r * r * a;
            object = 4 > 7;
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('y'),[],None),VarDecl(Id('m'),[1],None),VarDecl(Id('n'),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([StringLiteral('antlr'),FloatLiteral(5.4)]),FloatLiteral(0.0)])),VarDecl(Id('a_wrewrwe'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('rwrwerwerwer'),[3,44,12799],None),VarDecl(Id('cxa'),[18,1,8,0],None)],([VarDecl(Id('t'),[],None),VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('thread'),[],FloatLiteral(2.123123e+33)),VarDecl(Id('r'),[],FloatLiteral(10.0))],[Assign(Id('v'),BinaryOp('*',BinaryOp('*',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('a'))),Assign(Id('object'),BinaryOp('>',IntLiteral(4),IntLiteral(7)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_63(self):
        input = """
        Var: a, b = 120, d[10] = {1,{{},{}},5};
        Var: f = {12,{{}}};
        Function: test_
        Parameter: flag
        Body:
            If flag[0] && 1 Then
                For(i = 0, i < upp(upp(i)), s()) Do
                    update(f, i, d[i]);
                EndFor.
            ElseIf flag[2] && 2 Then
                Return;
            ElseIf isAlive(flag) Then
                flag = flag * ad - 123 + {1,2} % "124";
            Else
                println("da");
                delete(flag);
            EndIf.
        EndBody.
        
        **this is function main**
         
        Function: main
        Parameter: flags[100], len
        Body:
            For(i = 0, i < len, 1) Do
                test_(flags[i]);
            EndFor.
            Return 0;
        EndBody."""
        expect=Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],IntLiteral(120)),VarDecl(Id('d'),[10],ArrayLiteral([IntLiteral(1),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),IntLiteral(5)])),VarDecl(Id('f'),[],ArrayLiteral([IntLiteral(12),ArrayLiteral([ArrayLiteral([])])])),FuncDecl(Id('test_'),[VarDecl(Id('flag'),[],None)],([],[If([(BinaryOp('&&',ArrayCell(Id('flag'),[IntLiteral(0)]),IntLiteral(1)),[],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),CallExpr(Id('upp'),[CallExpr(Id('upp'),[Id('i')])])),CallExpr(Id('s'),[]),([],[CallStmt(Id('update'),[Id('f'),Id('i'),ArrayCell(Id('d'),[Id('i')])])]))]),(BinaryOp('&&',ArrayCell(Id('flag'),[IntLiteral(2)]),IntLiteral(2)),[],[Return(None)]),(CallExpr(Id('isAlive'),[Id('flag')]),[],[Assign(Id('flag'),BinaryOp('+',BinaryOp('-',BinaryOp('*',Id('flag'),Id('ad')),IntLiteral(123)),BinaryOp('%',ArrayLiteral([IntLiteral(1),IntLiteral(2)]),StringLiteral('124'))))])],([],[CallStmt(Id('println'),[StringLiteral('da')]),CallStmt(Id('delete'),[Id('flag')])]))])),FuncDecl(Id('main'),[VarDecl(Id('flags'),[100],None),VarDecl(Id('len'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),Id('len')),IntLiteral(1),([],[CallStmt(Id('test_'),[ArrayCell(Id('flags'),[Id('i')])])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_64(self):
        input = """
        Var: t = 0;
        Function: mk
        Parameter: x
        Body:
            While a>b Do
                If b>a Then
                    a = b;
                EndIf.
            EndWhile.                
        EndBody.
        
        **New function**
        
        Function: mk
        Parameter: x
        Body:
            If a==3 Then
                If b==a Then
                    write("b==a==3");
                    fwrite("xxx");
                EndIf.
            EndIf.
        EndBody.
        """
        expect=Program([VarDecl(Id('t'),[],IntLiteral(0)),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('>',Id('a'),Id('b')),([],[If([(BinaryOp('>',Id('b'),Id('a')),[],[Assign(Id('a'),Id('b'))])],([],[]))]))])),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[If([(BinaryOp('==',Id('a'),IntLiteral(3)),[],[If([(BinaryOp('==',Id('b'),Id('a')),[],[CallStmt(Id('write'),[StringLiteral('b==a==3')]),CallStmt(Id('fwrite'),[StringLiteral('xxx')])])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_65(self):
        input = """
        Function: parameter
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body:
            a=1;
        EndBody.
        
        Function: mk
        Parameter: x
        Body:
            fun0(fun1(fun2(fun3(fun4("end here")))));
        EndBody.
        """
        expect=Program([FuncDecl(Id('parameter'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[123],None),VarDecl(Id('d'),[123,234,0],None),VarDecl(Id('e'),[],None)],([],[Assign(Id('a'),IntLiteral(1))])),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fun0'),[CallExpr(Id('fun1'),[CallExpr(Id('fun2'),[CallExpr(Id('fun3'),[CallExpr(Id('fun4'),[StringLiteral('end here')])])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_66(self):
        input = """
        Function: main
        Body:
            Var: x = 0., y = 2.;
            While (x =/= f()) Do
                x = x +. 1;
                y = y -. 1;
            EndWhile.
            Return 0;
        EndBody.
        
        Function: main
        Body:
            Do
                Var: k = 12;
                k = -.-k;
                a[2][3 + 3] = foo(2 + k, k, arr[0]);
                m = a[1][2 + f[2]];
            While x == 0 EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],FloatLiteral(0.0)),VarDecl(Id('y'),[],FloatLiteral(2.0))],[While(BinaryOp('=/=',Id('x'),CallExpr(Id('f'),[])),([],[Assign(Id('x'),BinaryOp('+.',Id('x'),IntLiteral(1))),Assign(Id('y'),BinaryOp('-.',Id('y'),IntLiteral(1)))])),Return(IntLiteral(0))])),FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('k'),[],IntLiteral(12))],[Assign(Id('k'),UnaryOp('-.',UnaryOp('-',Id('k')))),Assign(ArrayCell(Id('a'),[IntLiteral(2),BinaryOp('+',IntLiteral(3),IntLiteral(3))]),CallExpr(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('k')),Id('k'),ArrayCell(Id('arr'),[IntLiteral(0)])])),Assign(Id('m'),ArrayCell(Id('a'),[IntLiteral(1),BinaryOp('+',IntLiteral(2),ArrayCell(Id('f'),[IntLiteral(2)]))]))]),BinaryOp('==',Id('x'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_67(self):
        input = """
        Var: a = 4.;
        Var: x = {{},1,"abc"};
        
        **Convert function**
            
        Function: convert
        Parameter: str
        Body:
            Var: array[100];
            Var: length;
            length = length(str) - 1;
            Return length;
        EndBody.
        
        Function: main
        Body:
            convert("thai phuc hiep");
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],FloatLiteral(4.0)),VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([]),IntLiteral(1),StringLiteral('abc')])),FuncDecl(Id('convert'),[VarDecl(Id('str'),[],None)],([VarDecl(Id('array'),[100],None),VarDecl(Id('length'),[],None)],[Assign(Id('length'),BinaryOp('-',CallExpr(Id('length'),[Id('str')]),IntLiteral(1))),Return(Id('length'))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('convert'),[StringLiteral('thai phuc hiep')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_68(self):
        input = """
        Var: t = 0;
        Function: mk
        Parameter: x    
        Body:
            arr[1][2][3][4][55][6][5][4][4] = 1;
        EndBody.
        
        Function: t_2937124
        Parameter: arr[100]
        Body:
            Var: sum = 0;
            create_multi_threads(num_threads);
            For (i = 0, i < len, 1) Do
                lock();
                sum = sum + arr[i];
                unlock();
            EndFor.
            destroy_all_resources();
        EndBody.
        """
        expect=Program([VarDecl(Id('t'),[],IntLiteral(0)),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[Assign(ArrayCell(Id('arr'),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),IntLiteral(6),IntLiteral(5),IntLiteral(4),IntLiteral(4)]),IntLiteral(1))])),FuncDecl(Id('t_2937124'),[VarDecl(Id('arr'),[100],None)],([VarDecl(Id('sum'),[],IntLiteral(0))],[CallStmt(Id('create_multi_threads'),[Id('num_threads')]),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),Id('len')),IntLiteral(1),([],[CallStmt(Id('lock'),[]),Assign(Id('sum'),BinaryOp('+',Id('sum'),ArrayCell(Id('arr'),[Id('i')]))),CallStmt(Id('unlock'),[])])),CallStmt(Id('destroy_all_resources'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_69(self):
        input = """
        Var: a = 7.5, b;
        Function: function
        Body:
        EndBody.
        Function: df 
        Parameter: n 
        Body: 
            Var : a,b,c ;
            c = a[a+3];
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],FloatLiteral(7.5)),VarDecl(Id('b'),[],None),FuncDecl(Id('function'),[],([],[])),FuncDecl(Id('df'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],[Assign(Id('c'),ArrayCell(Id('a'),[BinaryOp('+',Id('a'),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_70(self):
        input = """
        Function: ewqe 
        Parameter: n,k
        Body: 
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.2202;
                i = i + 1;
            EndWhile.
        EndBody.
        
        Function: fact
        Parameter: n[2], a[2][3]
        Body:
            Var: z = {}, t;
            a = a *. x;
        EndBody.
        """
        expect=Program([FuncDecl(Id('ewqe'),[VarDecl(Id('n'),[],None),VarDecl(Id('k'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.2202))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]))])),FuncDecl(Id('fact'),[VarDecl(Id('n'),[2],None),VarDecl(Id('a'),[2,3],None)],([VarDecl(Id('z'),[],ArrayLiteral([])),VarDecl(Id('t'),[],None)],[Assign(Id('a'),BinaryOp('*.',Id('a'),Id('x')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_71(self):
        input = """
        Function: fe 
        Parameter: n, k
        Body: 
            Do
                x= x+1;
            While (x>1) 
            EndDo.
        EndBody.
        
        **This is my function**
        
        Function: varinstmtlist
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                i = i + 1;
            While i <= 10
            EndDo.
        EndBody.
        """
        expect=Program([FuncDecl(Id('fe'),[VarDecl(Id('n'),[],None),VarDecl(Id('k'),[],None)],([],[Dowhile(([],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),BinaryOp('>',Id('x'),IntLiteral(1)))])),FuncDecl(Id('varinstmtlist'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[Dowhile(([VarDecl(Id('k'),[],IntLiteral(10))],[Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]),BinaryOp('<=',Id('i'),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_72(self):
        input = """
        Var : k = 0.3e12;
        
        Function: bar 
        Parameter: n 
        Body: 
            If !a Then b = 5; EndIf.
        EndBody.
        
        Function: test
        Parameter: k, a
        Body:
            Var: str = "this is a string";
            Var: token;
            token = strtok(str, "-");
            While ((token != null)) Do
                printf("%s", token);
                token = strtok(str, "-");
            EndWhile.
        EndBody.
        """
        expect=Program([VarDecl(Id('k'),[],FloatLiteral(300000000000.0)),FuncDecl(Id('bar'),[VarDecl(Id('n'),[],None)],([],[If([(UnaryOp('!',Id('a')),[],[Assign(Id('b'),IntLiteral(5))])],([],[]))])),FuncDecl(Id('test'),[VarDecl(Id('k'),[],None),VarDecl(Id('a'),[],None)],([VarDecl(Id('str'),[],StringLiteral('this is a string')),VarDecl(Id('token'),[],None)],[Assign(Id('token'),CallExpr(Id('strtok'),[Id('str'),StringLiteral('-')])),While(BinaryOp('!=',Id('token'),Id('null')),([],[CallStmt(Id('printf'),[StringLiteral('%s'),Id('token')]),Assign(Id('token'),CallExpr(Id('strtok'),[Id('str'),StringLiteral('-')]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_73(self):
        input = """
        Var: x, s = \"abc\", z = 2;
        Function: fact
        Parameter: x
        Body:
            Do Return a;
            While i != 5 EndDo.
            Return b[5] *. foo(foo(2) + 3);
        EndBody.
        
        Function: mk
        Parameter: x
        Body:
            b = -a;
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('s'),[],StringLiteral('abc')),VarDecl(Id('z'),[],IntLiteral(2)),FuncDecl(Id('fact'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Return(Id('a'))]),BinaryOp('!=',Id('i'),IntLiteral(5))),Return(BinaryOp('*.',ArrayCell(Id('b'),[IntLiteral(5)]),CallExpr(Id('foo'),[BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(3))])))])),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('b'),UnaryOp('-',Id('a')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_74(self):
        input = """
        Function: fh 
        Parameter: n
        Body: **get**
        EndBody.
        
        Function: ahihihi
        Body:
            While !compile() Do EndWhile.
            While !linker() Do EndWhile.
            While !interpreter() Do EndWhile.
            While !notlinker() Do EndWhile.
            If flag Then loader(); Else fail(); EndIf.
            Return runner();
        EndBody.
        """
        expect=Program([FuncDecl(Id('fh'),[VarDecl(Id('n'),[],None)],([],[])),FuncDecl(Id('ahihihi'),[],([],[While(UnaryOp('!',CallExpr(Id('compile'),[])),([],[])),While(UnaryOp('!',CallExpr(Id('linker'),[])),([],[])),While(UnaryOp('!',CallExpr(Id('interpreter'),[])),([],[])),While(UnaryOp('!',CallExpr(Id('notlinker'),[])),([],[])),If([(Id('flag'),[],[CallStmt(Id('loader'),[])])],([],[CallStmt(Id('fail'),[])])),Return(CallExpr(Id('runner'),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_75(self):
        input = """
        Var: a = {1,2,0xFF} , b = \"**nhin cai gi ma nhin\", c ;
        Function: main
            **main func**
        Parameter: x,y,z
            ** 3 parameter**
        Body:
            ** null **
        EndBody.
        
        Function: whileEmpty
        Body:
            While i < 5 Do EndWhile.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(255)])),VarDecl(Id('b'),[],StringLiteral('**nhin cai gi ma nhin')),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[])),FuncDecl(Id('whileEmpty'),[],([],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_76(self):
        input = """
        Function: foo 
        Parameter: n
        Body: 
            Do
            While(x < 10)
            EndDo.
        EndBody.
        
        **New function**
        
        Function: test
        Body:
            Var: flag;
            flag = (True != 123) + !3 * (False && kj % 123 <. f());
            praaa(--------.-.-(!123 == kk * 12 - 3)||False + !!!!!!9==4);
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Dowhile(([],[]),BinaryOp('<',Id('x'),IntLiteral(10)))])),FuncDecl(Id('test'),[],([VarDecl(Id('flag'),[],None)],[Assign(Id('flag'),BinaryOp('+',BinaryOp('!=',BooleanLiteral(True),IntLiteral(123)),BinaryOp('*',UnaryOp('!',IntLiteral(3)),BinaryOp('<.',BinaryOp('&&',BooleanLiteral(False),BinaryOp('%',Id('kj'),IntLiteral(123))),CallExpr(Id('f'),[]))))),CallStmt(Id('praaa'),[BinaryOp('==',BinaryOp('||',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-.',UnaryOp('-.',UnaryOp('-',BinaryOp('==',UnaryOp('!',IntLiteral(123)),BinaryOp('-',BinaryOp('*',Id('kk'),IntLiteral(12)),IntLiteral(3))))))))))))),BinaryOp('+',BooleanLiteral(False),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',IntLiteral(9))))))))),IntLiteral(4))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_77(self):
        input = """
        Function: main
        Body:
            f = f * ffffffff(a[0xFFFF || 0x1111]); 
        EndBody.
        
        **hehe hihi**
        
        **hehe hahaha hihi**
        
        Function: test
        Body:
            Var: k;
            k = "13" + "das";
            k = k && 31 - 13 * (k == 0) || dask;
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[Assign(Id('f'),BinaryOp('*',Id('f'),CallExpr(Id('ffffffff'),[ArrayCell(Id('a'),[BinaryOp('||',IntLiteral(65535),IntLiteral(4369))])])))])),FuncDecl(Id('test'),[],([VarDecl(Id('k'),[],None)],[Assign(Id('k'),BinaryOp('+',StringLiteral('13'),StringLiteral('das'))),Assign(Id('k'),BinaryOp('||',BinaryOp('&&',Id('k'),BinaryOp('-',IntLiteral(31),BinaryOp('*',IntLiteral(13),BinaryOp('==',Id('k'),IntLiteral(0))))),Id('dask')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_78(self):
        input = """
        Var: x, y[2][5];
        Function: factorial
        Body:
            a = {{{1, 2, {2, 5, 7}, 9}, 2, 5}};
            If True 
            Then Return 5 * foo(3);
            Else Return 0;
            EndIf.
        EndBody.
        
        Function: complex
        Body:
            a =-((func1(array)+23) * -func2(4.234234)+arr[3])\.0.54234234;
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[2,5],None),FuncDecl(Id('factorial'),[],([],[Assign(Id('a'),ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(2),IntLiteral(5),IntLiteral(7)]),IntLiteral(9)]),IntLiteral(2),IntLiteral(5)])])),If([(BooleanLiteral(True),[],[Return(BinaryOp('*',IntLiteral(5),CallExpr(Id('foo'),[IntLiteral(3)])))])],([],[Return(IntLiteral(0))]))])),FuncDecl(Id('complex'),[],([],[Assign(Id('a'),BinaryOp('\\.',UnaryOp('-',BinaryOp('+',BinaryOp('*',BinaryOp('+',CallExpr(Id('func1'),[Id('array')]),IntLiteral(23)),UnaryOp('-',CallExpr(Id('func2'),[FloatLiteral(4.234234)]))),ArrayCell(Id('arr'),[IntLiteral(3)]))),FloatLiteral(0.54234234)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_79(self):
        input = """
        Var: rapviet = 4323423;
        Var: rapviet = 2434;
        Var: rapviet = 234324;
        Var: rapviet = 234324;
        
        ** =)))) **
        
        Function: main
        Body:
            x[1+{1,2}] = (func(func)); 
        EndBody.
        
        **nested call**
        
        Function: nestedcall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody.
        """
        expect=Program([VarDecl(Id('rapviet'),[],IntLiteral(4323423)),VarDecl(Id('rapviet'),[],IntLiteral(2434)),VarDecl(Id('rapviet'),[],IntLiteral(234324)),VarDecl(Id('rapviet'),[],IntLiteral(234324)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('x'),[BinaryOp('+',IntLiteral(1),ArrayLiteral([IntLiteral(1),IntLiteral(2)]))]),CallExpr(Id('func'),[Id('func')]))])),FuncDecl(Id('nestedcall'),[],([],[Assign(Id('a'),BinaryOp('-',BinaryOp('+',CallExpr(Id('func1'),[CallExpr(Id('foo'),[IntLiteral(3)])]),IntLiteral(23)),CallExpr(Id('func2'),[CallExpr(Id('goo'),[CallExpr(Id('foo'),[Id('a')])])])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_80(self):
        input = """
        Function: foo
        Body:
            For(i = f() * fp()[12][0o234343], i < f()[13], fn(f)[0x14234233]) Do
                Var: x;
                If x == 1 Then func_1(); k = import();
                ElseIf x Then 
                While i < -12 Do
                    Var: m;
                EndWhile.
                EndIf.
            EndFor.
        EndBody.
        
        ** ahihi **
        
        Function: func_1 
        Parameter: n 
        Body: 
            For (k=4,k<2,3) Do x=6; EndFor.
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.
        
        ** ahehe **
        
        Function: import 
        Parameter: n 
        Body: 
            For (i=0, x<10, i*1) Do x=6; EndFor.
            For (b=0.4234, x<10, i*1) Do x=x+7; EndFor.
            For (c=0x123, x<10, i*1) Do x=x \. 67; EndFor.
            For (d=0o12312, x<10, i*1) Do x= 9 && 6; EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[],([],[For(Id('i'),BinaryOp('*',CallExpr(Id('f'),[]),ArrayCell(CallExpr(Id('fp'),[]),[IntLiteral(12),IntLiteral(80099)])),BinaryOp('<',Id('i'),ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(13)])),ArrayCell(CallExpr(Id('fn'),[Id('f')]),[IntLiteral(337855027)]),([VarDecl(Id('x'),[],None)],[If([(BinaryOp('==',Id('x'),IntLiteral(1)),[],[CallStmt(Id('func_1'),[]),Assign(Id('k'),CallExpr(Id('import'),[]))]),(Id('x'),[],[While(BinaryOp('<',Id('i'),UnaryOp('-',IntLiteral(12))),([VarDecl(Id('m'),[],None)],[]))])],([],[]))]))])),FuncDecl(Id('func_1'),[VarDecl(Id('n'),[],None)],([],[For(Id('k'),IntLiteral(4),BinaryOp('<',Id('k'),IntLiteral(2)),IntLiteral(3),([],[Assign(Id('x'),IntLiteral(6))])),For(Id('i'),IntLiteral(0),BinaryOp('!=',Id('i'),IntLiteral(5)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('x'),IntLiteral(6))]))])),FuncDecl(Id('import'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('x'),IntLiteral(10)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('x'),IntLiteral(6))])),For(Id('b'),FloatLiteral(0.4234),BinaryOp('<',Id('x'),IntLiteral(10)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(7)))])),For(Id('c'),IntLiteral(291),BinaryOp('<',Id('x'),IntLiteral(10)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('x'),BinaryOp('\\.',Id('x'),IntLiteral(67)))])),For(Id('d'),IntLiteral(5322),BinaryOp('<',Id('x'),IntLiteral(10)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('x'),BinaryOp('&&',IntLiteral(9),IntLiteral(6)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_81(self):
        input = """
        Var: x;
        Var: a,b,c;
        Var: a[100];
        Var: d = 0;
        
        Function: callstmt
        Body:
            identifier______function(a,b_,c+.3.e-2);
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('a'),[100],None),VarDecl(Id('d'),[],IntLiteral(0)),FuncDecl(Id('callstmt'),[],([],[CallStmt(Id('identifier______function'),[Id('a'),Id('b_'),BinaryOp('+.',Id('c'),FloatLiteral(0.03))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_82(self):
        input = """
        Function: bar 
        Parameter: n
        Body: 
            a= (a==b)!= c ;
            x= (x =/= y) <. z;
        EndBody.
        
        Function: func_call
        Body:
            x = (!x || True) * kd[12] == 2 % 123 && False \ blala;
            Return;
        EndBody.
        
        Function: factorial
        Parameter: x
        Body:
            For(i = 9.23423423 , foo() * a[98][99] != 1e9, "abc") Do
                x = 213;
                x = x =/= 5435 || !332423;
            EndFor.
            Return; 
        EndBody.
        """
        expect=Program([FuncDecl(Id('bar'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('a'),BinaryOp('!=',BinaryOp('==',Id('a'),Id('b')),Id('c'))),Assign(Id('x'),BinaryOp('<.',BinaryOp('=/=',Id('x'),Id('y')),Id('z')))])),FuncDecl(Id('func_call'),[],([],[Assign(Id('x'),BinaryOp('==',BinaryOp('*',BinaryOp('||',UnaryOp('!',Id('x')),BooleanLiteral(True)),ArrayCell(Id('kd'),[IntLiteral(12)])),BinaryOp('&&',BinaryOp('%',IntLiteral(2),IntLiteral(123)),BinaryOp('\\',BooleanLiteral(False),Id('blala'))))),Return(None)])),FuncDecl(Id('factorial'),[VarDecl(Id('x'),[],None)],([],[For(Id('i'),FloatLiteral(9.23423423),BinaryOp('!=',BinaryOp('*',CallExpr(Id('foo'),[]),ArrayCell(Id('a'),[IntLiteral(98),IntLiteral(99)])),FloatLiteral(1000000000.0)),StringLiteral('abc'),([],[Assign(Id('x'),IntLiteral(213)),Assign(Id('x'),BinaryOp('=/=',Id('x'),BinaryOp('||',IntLiteral(5435),UnaryOp('!',IntLiteral(332423)))))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_83(self):
        input = """
        Var: x;
        Function: test
        Body:
            While True Do
                v = receive(socket, max_len);
                If v Then
                    handle();
                EndIf.
            EndWhile.
        EndBody.
        
        Function: testreturn
        Parameter: n
        Body:
            Var: t=False;
            If n<100 Then
                test();
                t = 2. \. 5.;
            EndIf.
            Return t;
        EndBody.
        """
        expect=Program([VarDecl(Id('x'),[],None),FuncDecl(Id('test'),[],([],[While(BooleanLiteral(True),([],[Assign(Id('v'),CallExpr(Id('receive'),[Id('socket'),Id('max_len')])),If([(Id('v'),[],[CallStmt(Id('handle'),[])])],([],[]))]))])),FuncDecl(Id('testreturn'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('t'),[],BooleanLiteral(False))],[If([(BinaryOp('<',Id('n'),IntLiteral(100)),[],[CallStmt(Id('test'),[]),Assign(Id('t'),BinaryOp('\\.',FloatLiteral(2.0),FloatLiteral(5.0)))])],([],[])),Return(Id('t'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_84(self):
        input = """
        Function: computer_arch
        Parameter: n,k
        Body: 
            For (i = 9.0945345, i < !(53534 || 534543), "index++") Do
                print("9.5 yahooooo !!!!");
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('computer_arch'),[VarDecl(Id('n'),[],None),VarDecl(Id('k'),[],None)],([],[For(Id('i'),FloatLiteral(9.0945345),BinaryOp('<',Id('i'),UnaryOp('!',BinaryOp('||',IntLiteral(53534),IntLiteral(534543)))),StringLiteral('index++'),([],[CallStmt(Id('print'),[StringLiteral('9.5 yahooooo !!!!')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_85(self):
        input = """
        **This is an empty program**
        Var: hello = "maybe not";
        """
        expect=Program([VarDecl(Id('hello'),[],StringLiteral('maybe not'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_86(self):
        input = """
        ** This is a functionnnnnnnn !!!!!! **
        
        Function: reverse
        Parameter: str
        Body:
            For(i = 0, i < len(str) \ 2, s) Do
                str[i] = str[len(str) - i - 1];
            EndFor.
        EndBody.
        
        ** This is a functionnnnnnnn !!!!!! **
        
        Function: xstk 
        Parameter: n
        Body: 
            For (i = 0, i != 5.534543534534, i*1) Do ewxrwerwerwe=6; EndFor.
            Do
                ewrwerwerewr = a + b;
                writeln(ewx);
            While(True || True || True || True) EndDo.
        EndBody.
        
        ** This is end of functionnnnnnnn !!!!!! **
        """
        expect=Program([FuncDecl(Id('reverse'),[VarDecl(Id('str'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),BinaryOp('\\',CallExpr(Id('len'),[Id('str')]),IntLiteral(2))),Id('s'),([],[Assign(ArrayCell(Id('str'),[Id('i')]),ArrayCell(Id('str'),[BinaryOp('-',BinaryOp('-',CallExpr(Id('len'),[Id('str')]),Id('i')),IntLiteral(1))]))]))])),FuncDecl(Id('xstk'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('!=',Id('i'),FloatLiteral(5.534543534534)),BinaryOp('*',Id('i'),IntLiteral(1)),([],[Assign(Id('ewxrwerwerwe'),IntLiteral(6))])),Dowhile(([],[Assign(Id('ewrwerwerewr'),BinaryOp('+',Id('a'),Id('b'))),CallStmt(Id('writeln'),[Id('ewx')])]),BinaryOp('||',BinaryOp('||',BinaryOp('||',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(True)),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_87(self):
        input = """
        Var: t = 0;
        Function: mk
        Parameter: x
        Body:
            Var: r3[4] = 3.e35;
        EndBody.
        Function: m
        Body:
            While d
            Do
                If False
                Then
                    Break;
                foo(5); 
                print(foo(9));
                EndIf.
            EndWhile.
        EndBody.
        """
        expect=Program([VarDecl(Id('t'),[],IntLiteral(0)),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([VarDecl(Id('r3'),[4],FloatLiteral(3e+35))],[])),FuncDecl(Id('m'),[],([],[While(Id('d'),([],[If([(BooleanLiteral(False),[],[Break(),CallStmt(Id('foo'),[IntLiteral(5)]),CallStmt(Id('print'),[CallExpr(Id('foo'),[IntLiteral(9)])])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_88(self):
        input = """
        Function: softwareEngineering
        Parameter: a[5], b
        Body:
            c = mayukochan[0] + x[{1,2, 4}];
        EndBody.
        
        Function: callcomplex
        Body:
            call(a,876,var*.65e-1,arr[3],True,"chuoi",5345\.535435,767*645645);
        EndBody.
        """
        expect=Program([FuncDecl(Id('softwareEngineering'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([],[Assign(Id('c'),BinaryOp('+',ArrayCell(Id('mayukochan'),[IntLiteral(0)]),ArrayCell(Id('x'),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4)])])))])),FuncDecl(Id('callcomplex'),[],([],[CallStmt(Id('call'),[Id('a'),IntLiteral(876),BinaryOp('*.',Id('var'),FloatLiteral(6.5)),ArrayCell(Id('arr'),[IntLiteral(3)]),BooleanLiteral(True),StringLiteral('chuoi'),BinaryOp('\\.',IntLiteral(5345),IntLiteral(535435)),BinaryOp('*',IntLiteral(767),IntLiteral(645645))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_89(self):
        input = """
        Function: babyFunction
        Body:
            Var: foooooo[4234];
            foo = (a + 2)["baby"][0x123];
        EndBody.
        """
        expect=Program([FuncDecl(Id('babyFunction'),[],([VarDecl(Id('foooooo'),[4234],None)],[Assign(Id('foo'),ArrayCell(BinaryOp('+',Id('a'),IntLiteral(2)),[StringLiteral('baby'),IntLiteral(291)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_90(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            a = {12,{{1,2,3}},{},{},4} * "ad" + 14 -. 12 + !!!!!!!!!!!!(!!3);
        EndBody.
        
        Function: iiiiiiiiiiiiiifOKE
        Body:
            If n == 0 Then
                x = 3;
            ElseIf x == !(2) Then
                check = False;
                check = True;
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([],[Assign(Id('a'),BinaryOp('+',BinaryOp('-.',BinaryOp('+',BinaryOp('*',ArrayLiteral([IntLiteral(12),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]),ArrayLiteral([]),ArrayLiteral([]),IntLiteral(4)]),StringLiteral('ad')),IntLiteral(14)),IntLiteral(12)),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',IntLiteral(3)))))))))))))))))])),FuncDecl(Id('iiiiiiiiiiiiiifOKE'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Assign(Id('x'),IntLiteral(3))]),(BinaryOp('==',Id('x'),UnaryOp('!',IntLiteral(2))),[],[Assign(Id('check'),BooleanLiteral(False)),Assign(Id('check'),BooleanLiteral(True))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_91(self):
        input = """
        Function: test
        Parameter: a,b
        Body:
            a = "string 1";
            b = "string 2";
            Return concatenate(a, b);
        EndBody.
        Function: doodoodoo
        Parameter: a[5], b
        Body:
            For (i = 0, i < 10, 2) Do
                print("anonymus");
                print("lucifer");
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('test'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Assign(Id('a'),StringLiteral('string 1')),Assign(Id('b'),StringLiteral('string 2')),Return(CallExpr(Id('concatenate'),[Id('a'),Id('b')]))])),FuncDecl(Id('doodoodoo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('print'),[StringLiteral('anonymus')]),CallStmt(Id('print'),[StringLiteral('lucifer')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_92(self):
        input = """
        Function: main
        Parameter: hello
        Body:
            For(i = initial(), i < bound() + bound()[2343], step(step(8))) Do
                a = in(f(in(2, f())))[f()];
            EndFor.
            If hello Then
                print("hello");
            EndIf.
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[VarDecl(Id('hello'),[],None)],([],[For(Id('i'),CallExpr(Id('initial'),[]),BinaryOp('<',Id('i'),BinaryOp('+',CallExpr(Id('bound'),[]),ArrayCell(CallExpr(Id('bound'),[]),[IntLiteral(2343)]))),CallExpr(Id('step'),[CallExpr(Id('step'),[IntLiteral(8)])]),([],[Assign(Id('a'),ArrayCell(CallExpr(Id('in'),[CallExpr(Id('f'),[CallExpr(Id('in'),[IntLiteral(2),CallExpr(Id('f'),[])])])]),[CallExpr(Id('f'),[])]))])),If([(Id('hello'),[],[CallStmt(Id('print'),[StringLiteral('hello')])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_93(self):
        input = """
        Function: fact
        Parameter : x, a[2]
        Body:
            Var: a = \"abc\", x = {1, \"ABS\", 3};
            If (a) Then EndIf.
        EndBody.
        Function: foo
        Parameter: a
        Body:
            Var: x = 2;
            For (i = 6456.654645,i <= 3242.42334, 980.423423) Do
                print(kiss("16 typh", "min"));
                writeln("OMG !!!");
            EndFor.
        EndBody.
        """
        expect=Program([FuncDecl(Id('fact'),[VarDecl(Id('x'),[],None),VarDecl(Id('a'),[2],None)],([VarDecl(Id('a'),[],StringLiteral('abc')),VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),StringLiteral('ABS'),IntLiteral(3)]))],[If([(Id('a'),[],[])],([],[]))])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(2))],[For(Id('i'),FloatLiteral(6456.654645),BinaryOp('<=',Id('i'),FloatLiteral(3242.42334)),FloatLiteral(980.423423),([],[CallStmt(Id('print'),[CallExpr(Id('kiss'),[StringLiteral('16 typh'),StringLiteral('min')])]),CallStmt(Id('writeln'),[StringLiteral('OMG !!!')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_94(self):
        input = """
        Var: torai9;
        Var: rhymastic;
        Function: beef
        Parameter: youtube
        Body:
            res = diss(torai9, rhymastic);
            If success(res) Then
                writeln("hoooooo, torai9 is just a cock");
            EndIf.
        EndBody.
        """
        expect=Program([VarDecl(Id('torai9'),[],None),VarDecl(Id('rhymastic'),[],None),FuncDecl(Id('beef'),[VarDecl(Id('youtube'),[],None)],([],[Assign(Id('res'),CallExpr(Id('diss'),[Id('torai9'),Id('rhymastic')])),If([(CallExpr(Id('success'),[Id('res')]),[],[CallStmt(Id('writeln'),[StringLiteral('hoooooo, torai9 is just a cock')])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_95(self):
        input = """
        Function: main
        Body:
            For(counter = 0., foo() * a[23] == 2, "asd") Do
                x = 213;
            EndFor.
        EndBody.
        Function: moreThanLove
        Body:
            Var: x = {{1,2,3}, **Comment here** "abc"};
            While (i < 5) Do
                If i == 3 Then Return 1;EndIf.
            i = i || 1;
            EndWhile.
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([],[For(Id('counter'),FloatLiteral(0.0),BinaryOp('==',BinaryOp('*',CallExpr(Id('foo'),[]),ArrayCell(Id('a'),[IntLiteral(23)])),IntLiteral(2)),StringLiteral('asd'),([],[Assign(Id('x'),IntLiteral(213))]))])),FuncDecl(Id('moreThanLove'),[],([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),StringLiteral('abc')]))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[If([(BinaryOp('==',Id('i'),IntLiteral(3)),[],[Return(IntLiteral(1))])],([],[])),Assign(Id('i'),BinaryOp('||',Id('i'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_96(self):
        input = """
        Var: a = 4.000, b = 25.00e0;
        Function: main
        Parameter: a, x, y, a[5]
        Body:
            For (i = 0, i <= 10000, i + 343432.423432 + !("string")) Do
                print("I love min");
                If a Then
                    If a Then
                        If a Then
                            If a Then
                                If a Then
                                    kiss();
                                EndIf.
                            EndIf.
                        EndIf.
                    EndIf.
                EndIf.
            EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('a'),[],FloatLiteral(4.0)),VarDecl(Id('b'),[],FloatLiteral(25.0)),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('a'),[5],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<=',Id('i'),IntLiteral(10000)),BinaryOp('+',BinaryOp('+',Id('i'),FloatLiteral(343432.423432)),UnaryOp('!',StringLiteral('string'))),([],[CallStmt(Id('print'),[StringLiteral('I love min')]),If([(Id('a'),[],[If([(Id('a'),[],[If([(Id('a'),[],[If([(Id('a'),[],[If([(Id('a'),[],[CallStmt(Id('kiss'),[])])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_97(self):
        input = """
        Var: decl =  "5345345345";
        Function: fact
        Body:
            Var : x = 5, y = {{}}; 
            For (i = 0, i < 10, 2) Do
                writeln(i);
                If i == 7 Then Break;
                ElseIf i == 8 Then Continue;
                Else Return nothing;
                EndIf.
            EndFor.
        EndBody.
        """
        expect=Program([VarDecl(Id('decl'),[],StringLiteral('5345345345')),FuncDecl(Id('fact'),[],([VarDecl(Id('x'),[],IntLiteral(5)),VarDecl(Id('y'),[],ArrayLiteral([ArrayLiteral([])]))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('i'),IntLiteral(7)),[],[Break()]),(BinaryOp('==',Id('i'),IntLiteral(8)),[],[Continue()])],([],[Return(Id('nothing'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_98(self):
        input = """
        Var: t = 0;
        Function: mk
        Parameter: x
        Body:
            ** Code Premium **
            print("this is premium code =)))");
            **End Code Premium**
            Do 
                If i == 6 Then Break;
                ElseIf i == 7 Then Continue;
                Else Break;
                EndIf.
            While i <= 10
            EndDo.
        EndBody.
        """
        expect=Program([VarDecl(Id('t'),[],IntLiteral(0)),FuncDecl(Id('mk'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('print'),[StringLiteral('this is premium code =)))')]),Dowhile(([],[If([(BinaryOp('==',Id('i'),IntLiteral(6)),[],[Break()]),(BinaryOp('==',Id('i'),IntLiteral(7)),[],[Continue()])],([],[Break()]))]),BinaryOp('<=',Id('i'),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_99(self):
        input = """
        Function: main
        Body:
            Var: x = 0., y = 2.;
            While (x =/= f()) Do
                x = x +. 1;
                If x == (1 + foo(4))[8][0x123] Then Break;
                Else 
                    While 10 == 10 Do
                        print("what you do");
                        print("what you do");
                        print("what you do for love");
                    EndWhile.
                EndIf.
                y = y -. 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        expect=Program([FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],FloatLiteral(0.0)),VarDecl(Id('y'),[],FloatLiteral(2.0))],[While(BinaryOp('=/=',Id('x'),CallExpr(Id('f'),[])),([],[Assign(Id('x'),BinaryOp('+.',Id('x'),IntLiteral(1))),If([(BinaryOp('==',Id('x'),ArrayCell(BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[IntLiteral(4)])),[IntLiteral(8),IntLiteral(291)])),[],[Break()])],([],[While(BinaryOp('==',IntLiteral(10),IntLiteral(10)),([],[CallStmt(Id('print'),[StringLiteral('what you do')]),CallStmt(Id('print'),[StringLiteral('what you do')]),CallStmt(Id('print'),[StringLiteral('what you do for love')])]))])),Assign(Id('y'),BinaryOp('-.',Id('y'),IntLiteral(1)))])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_100(self):
        input = """
        """
        expect=Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
