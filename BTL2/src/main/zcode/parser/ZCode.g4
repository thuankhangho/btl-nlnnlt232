// Student ID: 2011357
// Student name: Ho Thuan Khang
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: nullablenewlinelist decllist EOF;

//Parser
decllist: decl decllist | decl;

decl: funcdecl | vardecl;

vardecl: (typdecl | implidecl) nullablenewlinelist;

typdecl: typ (IDENTIFIER | arraytype) (ASSIGN expr | );

implidecl: implivardecl | implidynadecl;

implivardecl: VAR IDENTIFIER ASSIGN expr;

implidynadecl: DYNAMIC IDENTIFIER (ASSIGN expr | );

funcdecl: FUNC IDENTIFIER LRB parameterlist RRB nullablenewlinelist (returnstate | blockstate | nullablenewlinelist);

parameterlist: parameterprime | ;

parameterprime: param CM parameterprime | param;

param: typ (IDENTIFIER | arraytype);

newlinelist: NEWLINE newlinelist | NEWLINE;

nullablenewlinelist: NEWLINE nullablenewlinelist | ;

typ: NUMBER | BOOL | STRING;

arraylit: LSB elementlist RSB;

elementlist: expr CM elementlist | expr;

functioncall: IDENTIFIER LRB argumentlist RRB;

relational: EQUAL | CMPRSTR | DIFF | LT | GT | LE | GE;

logical: AND | OR;

adding: PLUS | MINUS;

multiplying: MULTIPLY | DIVIDE | MOD;

expr: expr1 CONCAT expr1 | expr1;

expr1: expr2 relational expr2 | expr2;

expr2: expr2 logical expr3 | expr3;

expr3: expr3 adding expr4 | expr4;

expr4: expr4 multiplying expr5 | expr5;

expr5: NOT expr5 | expr6;

expr6: MINUS expr6 | expr7;

expr7: (IDENTIFIER | functioncall) LSB exprlist RSB | expr8;

expr8: IDENTIFIER | literal | LRB expr RRB | functioncall;

literal: NUMLIT | boollit | STRINGLIT | arraytype;

arraytype: IDENTIFIER LSB numlist RSB;

numlist: NUMLIT CM numlist | NUMLIT;

exprlist: expr CM exprlist | expr;

//Statements
vardeclstate: (typdecl | implidecl) newlinelist;

assignstate: lhs ASSIGN expr newlinelist;

lhs: IDENTIFIER | arraytype;

ifstate: IF LRB expr RRB nullablenewlinelist stmt elifstatelist (elsestate | );

elsestate: ELSE stmt;

elifstatelist: elifstate elifstatelist | ;

elifstate: ELIF LRB expr RRB nullablenewlinelist stmt;

forstate: FOR IDENTIFIER UNTIL expr BY expr nullablenewlinelist stmt;

breakstate: BREAK nullablenewlinelist;

continuestate: CONTINUE nullablenewlinelist;

returnstate: RETURN (expr | ) newlinelist;

functioncallstate: IDENTIFIER LRB argumentlist RRB newlinelist;

argumentlist: argumentprime | ;

argumentprime: expr CM argumentprime | expr;

blockstate: BEGIN newlinelist (stmtlist | ) END newlinelist;

stmtlist: stmt stmtlist | stmt;

stmt: vardeclstate | assignstate | ifstate | forstate | breakstate | continuestate | returnstate | functioncallstate | blockstate;

boollit: TRUE | FALSE;

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
NOT: 'not';
AND: 'and';
OR: 'or';

//Operators
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

//Separators
LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
CM: ',';
NEWLINE: '\n';

LINECMT: '##' .*? ('\n'|EOF) -> skip;

//Literals
NUMLIT: INTEGER DECIMAL? EXPONENT?;
fragment INTEGER: [0-9]+;
fragment DECIMAL: '.'[0-9]*;
fragment EXPONENT: ('e'|'E')('+'|'-')?[0-9]+;
STRINGLIT: '"' CHARSEQ* '"' {self.text = self.text[1:-1]};

fragment ESCAPESEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\'' | '\\\\';
fragment CHARSEQ: ~[\b\t\n\f\r"\\] | ESCAPESEQ | '\'"';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

WS: [ \t\r]+ -> skip; // skip spaces, tabs
ILLEGAL_ESCAPE: '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'~[bfrnt'\\]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' ('\\' [btnfr'\\] | ~[\r\t\n\\"] )* {self.text = self.text[1:]; raise UncloseString(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};