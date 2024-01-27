grammar ZCode;

@lexer::header {
from lexererr import *
# Student ID: 2011357
}

options {
	language = Python3;
}

program: EOF;

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
NOT: 'not';
AND: 'and';
OR: 'or';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MOD: '%';
EQUAL: '=';
ASSIGN: '<-';
DIFF: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
CONCAT: '...';
CMPRSTR: '==';

IDENTIFIER: [a-zA-Z_][a-zA-Z_]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;