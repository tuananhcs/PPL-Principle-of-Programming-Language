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
//program  : VAR COLON ID SEMI EOF ;
program: (var_declare)*(func_declare)* EOF ;
//***************************************************** */ Variable Declaration
var_declare
	: VAR COLON  (variable ('=' (scalar_type|composit_type))?)(COMMA variable ('=' (scalar_type|composit_type))?)* SEMI
	;
variable_list: (variable)(COMMA variable)* ;
variable: composit
        | scalar 
        ;
        //moi sua compost ____________S_______________________________________________________
composit: ID (LSB INT_LITERAL RSB)+  ; 
composit_type: array_lit;  
array_lit: LB   ((array_lit | INT_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL  )  ( COMMA  (INT_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL  | array_lit )  )* )?   RB;

scalar  : ID ; 
scalar_type: INT_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL; 
/*******************************************************************************func_declare */
//identifier: 
assign_stm:  index_exp '=' exp SEMI
        | ID '=' exp SEMI
        ;
parameter_name: variable_list;  
func_declare : FUNCTION COLON ID (PARAMETER COLON parameter_name)? (BODY COLON)(var_declare* stm*)(ENDBODY DOT);  
//stm_list:  stm* ; 
stm     : assign_stm
        | function_call_stm
        | if_stm 
        | for_stm 
        | while_stm
        | do_while_stm
        | function_call_stm
        | return_stm
        | break_stm
        | continue_stm
        ;
function_call_stm: function_call SEMI; 
function_call : ID LP RP
                | ID LP (exp)(COMMA exp)* RP ;
return_stm: RETURN exp? SEMI;
if_stm: IF exp THEN (var_declare* stm*) (ELSEIF exp THEN (var_declare*stm*))* (ELSE (var_declare*stm*))?  ENDIF DOT ;
for_stm: FOR LP ID '=' exp COMMA  exp COMMA exp RP DO (var_declare* stm*) ENDFOR DOT ;
while_stm: WHILE exp DO (var_declare* stm*) ENDWHILE DOT ; 
do_while_stm: DO (var_declare* stm*) WHILE exp ENDDO DOT ;
break_stm: BREAK SEMI ;
continue_stm : CONTINUE SEMI; 
exp:    exp1 RL_OP exp1 
        | exp1
        ; 
RL_OP: EQUAL| NOTEQUAL | LESSTHAN | GREATERTHAN | LESSTHAN_EQUAL | GREATERTHAN_EQUAL | NOTEQUAL_FLOAT | LESSTHAN_FLOAT | GREATERTHAN_FLOAT | LESSTHAN_EQUAL_FLOAT | GREATERTHAN_EQUAL_FLOAT;   
exp1:   exp1 LOGICAL_OP exp2
        | exp2 
        ; 
LOGICAL_OP:CONJUNCTION | DISJUNCTION  ;
exp2:   exp2 ADD exp3
        | exp2 ADD_FLOAT exp3
        | exp2 SUB exp3
        | exp2 SUB_FLOAT exp3
        | exp3 
        ;  
exp3:   exp3 MULTIPLYING exp4
        | exp4
        ; 
MULTIPLYING: MUL | MUL_FLOAT |DIV| DIV_FLOAT |MOD ;
exp4:   NEGATION exp4
        | exp5
        ; 
exp5:   SUB exp5
        | SUB_FLOAT exp5 
        | exp6
        ;

exp6: array_lit
        | BOOLEAN_LITERAL
        | STRING_LITERAL
        | INT_LITERAL 
        | LP exp RP
        | index_exp
        | ID
        | FLOAT_LITERAL
        | function_call
        ;
index_exp: (ID|function_call) (LSB exp RSB)+ ;

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


