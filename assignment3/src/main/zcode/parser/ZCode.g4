//Student ID: 2113481

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: (NEWLINE)* list_declared EOF;

//! --------------------------  Parser ----------------------- //
//List declarations
list_declared:  declared list_declared |  declared;
declared: function | variables some_endl;

//Variables declarations
variables: implicit_var | name_of_type | implicit_dynamic; 

implicit_var: VAR ID ASSIGN exp;

name_of_type: name_of_type_noass | name_of_type_ass;
name_of_type_noass: (NUMBER | STRING | BOOL) ID (LSB list_size RSB)?;
name_of_type_ass: (NUMBER | STRING | BOOL) ID (LSB list_size RSB)? ASSIGN exp;
list_size: NUMBER_LIT | NUMBER_LIT COMMA list_size;

implicit_dynamic: implicit_dynamic_ass | implicit_dynamic_noass;
implicit_dynamic_noass: DYNAMIC ID;
implicit_dynamic_ass: DYNAMIC ID ASSIGN exp;

//Function declaration
function: FUNC ID LP func_paralist? RP (some_endl? return_stmt |some_endl? block_stmt | some_endl);
func_paralist: name_of_type_noass COMMA func_paralist | name_of_type_noass;

// Expression
exp: exp0 (CONCAT) exp0 | exp0;
exp0: exp1 (EQUAL | COMPARE | DIFF | LT | GT | LTE | GTE) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (ADD | SUB) exp3 | exp3;
exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: SUB exp5 | exp6; 
exp6: (ID | func_call) LSB index_operators RSB | operand; 

index_operators: exp | exp COMMA index_operators;

// Operands
operand: ID | literal | LP exp RP | func_call;

// Literals
literal: NUMBER_LIT | STR_LIT | TRUE | FALSE | arr_lit;

arr_lit: LSB list_exp RSB;
list_exp: exp COMMA list_exp | exp;

//Function call
func_call: ID LP index_operators? RP;

//Statement
stmt: 
	var_dec_stmt 
	| assign_stmt
	| if_stmt
	| for_stmt 
	| break_stmt
	| continue_stmt
	| return_stmt
	| func_call_stmt 
	| block_stmt;

//Variable declaration statement
var_dec_stmt: variables some_endl;

//Assignment Statement
assign_stmt: lhs ASSIGN exp some_endl;
lhs: ID | index_exp; // Left hand side
index_exp: ID LSB index_operators RSB;

//If statement
if_stmt: IF LP exp RP some_endl? stmt elif_stmtlist elsestmt;
elif_stmtlist: elif_stmt elif_stmtlist |;
elif_stmt: ELIF LP exp RP some_endl? stmt;
elsestmt: ELSE some_endl? stmt|;

//For statement
for_stmt: FOR ID UNTIL exp BY exp some_endl? stmt;

//Break statement
break_stmt: BREAK some_endl;

//Continue statement
continue_stmt: CONTINUE some_endl;

//Return statement
return_stmt: RETURN exp? some_endl;

//Function call statement
func_call_stmt: ID LP index_operators? RP some_endl;

//Block statement
block_stmt: BEGIN some_endl liststmt END some_endl;
liststmt: stmt liststmt | ;

//Ignore part
some_endl: NEWLINE+;
//!  -------------------------- end Parser ------------------- //

//! --------------------------  Lexical structure ----------------------- //

//Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

//Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: 'not';
AND: 'and';
OR: 'or';
EQUAL: '=';
ASSIGN: '<-';
DIFF: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
COMPARE: '==';

//Separators
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
COMMA: ','; // Comma

//IdentifierS
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

//LiteralS
fragment INTERGER: [0-9]+;
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: [Ee] [+-]? [0-9]+;
NUMBER_LIT: INTERGER DECIMAL? EXPONENT?;

fragment STR_CHAR: ~[\f\r\n"\\] | ESC_SEQ | '\'"'; 
fragment ESC_SEQ: '\\' [bfrnt'\\];
STR_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};

//NEWLINE COMMENTS WS CR
NEWLINE: '\n'; 
COMMENTS: '##' ~[\n\r\f]* -> skip; // skip Comments
WS: [ \t\b\f]+ -> skip ; // skip WS
CR: '\r' -> skip; //skip carriage return

//Errors
UNCLOSE_STRING: '"' STR_CHAR* (EOF | '\n' | '\r\n') 
{if self.text[-1] == '\n':
	if self.text[-2] == '\r':
		raise UncloseString(self.text[1:-2]);
	else:
		raise UncloseString(self.text[1:-1]);
else:
	raise UncloseString(self.text[1:]);
};

fragment ILLEGAL_ESC: ('\\' ~[fbrnt'\\]);
ILLEGAL_ESCAPE: '"' STR_CHAR* ILLEGAL_ESC {raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};
//!  -------------------------- end Lexical structure ------------------- //


