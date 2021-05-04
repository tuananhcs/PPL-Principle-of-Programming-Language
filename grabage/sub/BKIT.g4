//1811442
grammar BKIT;


@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

//******* Parser ****************************** */
program: (many_var_declare)(many_func_declare) EOF ;
many_var_declare: one_var_declare many_var_declare
                | one_var_declare
                |
                ;
one_var_declare: VAR COLON id_list SEMI
                ;
id_list: (id_list_element)(COMMA id_list)?;

id_list_element:(ID | ID composit)(ASSIGN (array_literal| literal))? ;

composit: (LSB INT_LITERAL RSB)+
           ;
array_literal: LB((array_literal_element)(COMMA(array_literal_element))*)?RB;

array_literal_element: array_literal|literal;

//LITERAL ____________________________________________________
literal: INT_LITERAL
        | FLOAT_LITERAL
        | BOOLEAN_LITERAL
        | STRING_LITERAL
        ;

/*******************************************************************************func_declare */
/*Paser*/
assign_stm:  array_cell ASSIGN exp SEMI
        | ID ASSIGN exp SEMI
        ;

parameter_name:(param_list_element)(COMMA parameter_name)?;

param_list_element:(ID | ID composit);

many_func_declare: one_func_declare many_func_declare
                | one_func_declare
                |
                ;
one_func_declare : FUNCTION COLON ID (PARAMETER COLON parameter_name)? (BODY COLON)(many_var_declare many_stm)(ENDBODY DOT);
many_stm: stm many_stm
        | stm
        |
        ;

stm     : assign_stm
        | call_stm
        | break_stm
        | continue_stm
        | if_stm
        | for_stm
        | while_stm
        | do_while_stm
        | return_stm
        ;
call_stm: ID LP RP SEMI
        | ID LP (exp)(COMMA exp)* RP SEMI;
call_exp : ID LP RP
         | ID LP (exp)(COMMA exp)* RP ;

return_stm: RETURN exp? SEMI;
if_stm: if_then many_elseif* else_part?  ENDIF DOT ;
if_then: IF exp THEN (many_var_declare many_stm) ;
many_elseif: ELSEIF exp THEN (many_var_declare many_stm);
else_part: ELSE (many_var_declare many_stm);

for_stm: FOR LP ID '=' exp COMMA  exp COMMA exp RP DO (many_var_declare many_stm) ENDFOR DOT ;
while_stm: WHILE exp DO (many_var_declare many_stm) ENDWHILE DOT ;
do_while_stm: DO (many_var_declare many_stm) WHILE exp ENDDO DOT ;
break_stm: BREAK SEMI ;
continue_stm : CONTINUE SEMI;
exp:    exp1 EQUAL exp1
        | exp1 NOTEQUAL exp1
        | exp1 LESSTHAN exp1
        | exp1 GREATERTHAN exp1
        | exp1 LESSTHAN_EQUAL  exp1
        | exp1 GREATERTHAN_EQUAL exp1
        | exp1 NOTEQUAL_FLOAT exp1
        | exp1 LESSTHAN_FLOAT exp1
        | exp1 GREATERTHAN_FLOAT  exp1
        | exp1 LESSTHAN_EQUAL_FLOAT  exp1
        | exp1 GREATERTHAN_EQUAL_FLOAT exp1
        | exp1
        ;
exp1:   exp1 CONJUNCTION  exp2
        | exp1 DISJUNCTION exp2
        | exp2
        ;
exp2:   exp2 ADD exp3
        | exp2 ADD_FLOAT exp3
        | exp2 SUB exp3
        | exp2 SUB_FLOAT exp3
        | exp3
        ;
exp3:   exp3 MUL exp4
        | exp3 MUL_FLOAT exp4
        | exp3 DIV exp4
        | exp3 DIV_FLOAT exp4
        | exp3 MOD exp4
        | exp4
        ;

exp4:   NEGATION exp4
        | exp5
        ;
exp5:   SUB exp5
        | SUB_FLOAT exp5
        | exp6
        ;

exp6: array_literal
        | literal
        | ID
        | call_exp
        | array_cell
        | LP exp RP
        ;
array_cell: (ID|call_exp| LP exp RP)  index_op;
index_op: LSB exp RSB
        | LSB exp RSB index_op
        ;

/* Bool */
BOOLEAN_LITERAL: TRUE | FALSE;
//******** Lexer *******************************
//Fragment:
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
/* Comment */
COMMENT : '**' ((~'*') | ('*'~'*'))* '**' -> skip;
UNTERMINATED_COMMENT:'**' .*? {
        raise UnterminatedComment()
        };
fragment UNDERSCORES  : '_';
fragment UPPER        : [A-Z];
fragment LOWER        : [a-z];
fragment DIGIT        : [0-9];
fragment DIGIT_EX0    : [1-9];
ID: LOWER (UNDERSCORES | UPPER | LOWER | DIGIT)* ;
//Operator:
SUB: '-';
SUB_FLOAT: '-.';
ADD: '+';
ADD_FLOAT: '+.';
MUL: '*';
MUL_FLOAT: '*.';
DIV: '\\';
DIV_FLOAT:  '\\.';
MOD: '%';
BODY : 'Body';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDWHILE: 'EndWhile';
FOR: 'For';
ENDFOR: 'EndFor';
BREAK: 'Break';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';
//Boolean Operator:
NEGATION: '!';
CONJUNCTION: '&&';
DISJUNCTION: '||';
//Relational operator:
ASSIGN: '=' ;
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSTHAN_EQUAL: '<=';
GREATERTHAN_EQUAL: '>=';
NOTEQUAL_FLOAT:  '=/=';
LESSTHAN_FLOAT: '<.';
GREATERTHAN_FLOAT: '>.';
LESSTHAN_EQUAL_FLOAT: '<=.';
GREATERTHAN_EQUAL_FLOAT: '>=.';
//Separators:
SEMI: ';' ;
COLON: ':' ;
COMMA: 	',' ;
DOT: '.';
LB: '{';
RB : '}';
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
//literals: *******************************************************************************************
//**Integer**
INT_LITERAL :   DEC | HEX | OCT | '0';
fragment DEC: [1-9][0-9]*;
fragment HEX: '0'[xX][1-9A-F][0-9A-F]* ;
fragment OCT: '0'[oO][1-7][0-7]* ;
//**Float**/
FLOAT_LITERAL : INT_PART ( DECIMAL_PART? EXPONENT_PART | DECIMAL_PART EXPONENT_PART?) ;
fragment EXPONENT_PART: [eE] [+-]? DIGIT+;
fragment DECIMAL_PART: DOT DIGIT*;
fragment INT_PART:  (DIGIT)+;

STRING_LITERAL  :   '"' (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* '"'
        {

                self.text = self.text[1:-1]
        }
        ;

ILLEGAL_ESCAPE  :   '"' (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* ('\\'~[bfrnt'\\] | '\''~'"')
                {
                        raise IllegalEscape(self.text[1:])
                };
UNCLOSE_STRING  :   '"'  (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))*
                {
                        raise UncloseString(self.text[1:])
                };
LITERAL: INT_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL;
ERROR_CHAR:.{
        raise ErrorToken(self.text)
        };


