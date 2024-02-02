// Student ID: 20512496
// Name: Nguyen Khanh Huy
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;
//Parser

//Lexer
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

//Operators
PLUS: '+';

MINUS: '-';

MULTIPLY: '*';

DIVIDE: '/';

MOD: '%';

EQ: '=';

NEQ: '!=';

LE: '<';

GE: '>';

LEQ: '<=';

GEQ: '>=';

COMPARE: '==';

CONCAT: '...';

ASSIGN: '<-';

//Separators
LRB: '(';

RRB: ')';

LSB: '[';

RSB: ']';

CM: ',';

NEWLINE: '\n';

//Literals
NUMLIT: INTLIT DEC? EXP?;

fragment INTLIT: [0-9]+;

fragment DEC: '.'? [0-9]*;

fragment EXP: [Ee][+-]?[0-9]+;

LINECMT: '##' .*? ('\n'|'\r'|'\f'|EOF) -> skip;

STRINGLIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

fragment CHAR_LIT: ~["\\\r\n\f] | '\\' [bfrnt'\\] | '\'"';

ID: [A-Za-z_][A-Za-z_0-9]*;

WS: [ \t\r]+ -> skip; // skip spaces, tabs

UNCLOSED_STRING: '"' CHAR_LIT* ('\r\n' | '\n' | EOF) {
		if self.text[-1] == '\n' and self.text[-2] == '\r': raise UncloseString(self.text[1:-2])
		elif self.text[-1] == '\n': raise UncloseString(self.text[1:-1])
		else: raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' CHAR_LIT* ([\r\f] | '\\' ~[bfrnt'\\]) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};