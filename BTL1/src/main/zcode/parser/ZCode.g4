grammar ZCode;

@lexer::header {
from lexererr import *
# Student ID: 2011357
}

options {
	language = Python3;
}

program: nullablenewlinelist decllist EOF;

//Parser
decllist: decl decllist | decl;

decl: funcdecl | vardecl;

vardecl: (typdecl | implidecl) nullablenewlinelist;

typdecl: typ IDENTIFIER (ASSIGN expr | );

implidecl: implivardecl | implidynadecl;

implivardecl: VAR IDENTIFIER ASSIGN expr;

implidynadecl: DYNAMIC IDENTIFIER (ASSIGN expr | );

funcdecl: FUNC IDENTIFIER LRB parameterlist RRB nullablenewlinelist (returnstate | blockstate | ) nullablenewlinelist;

funcdeclonly: FUNC IDENTIFIER LRB parameterlist RRB;

parameterlist: parameterprime | ;

parameterprime: param CM parameterprime | param;

param: typ IDENTIFIER;

newlinelist: NEWLINE newlinelist | NEWLINE;

nullablenewlinelist: NEWLINE nullablenewlinelist | ;

typ: NUMBER | BOOL | STRING;

returnstate: RETURN (expr | ) newlinelist;

blockstate: BEGIN (expr | newlinelist) END newlinelist;

arraylit: LSB elementlist RSB;

elementlist: expr CM elementlist | expr;

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

expr7: expr7 LSB exprlist RSB | expr8;

expr8: IDENTIFIER | literal | LRB expr RRB;

literal: NUMLIT | BOOLLIT | STRINGLIT | arraytype;

arraytype: IDENTIFIER LSB exprlist RSB;

exprlist: expr CM exprlist | expr;

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

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
LINECMT: '##' .*? ('\n'|EOF) -> skip;

//Literals
NUMLIT: INTEGER DECIMAL? EXPONENT?;
fragment INTEGER: [0-9]+;
fragment DECIMAL: '.'[0-9]*;
fragment EXPONENT: ('e'|'E')('+'|'-')?[0-9]+;
BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' CHARSEQ* '"' {self.text = self.text[1:-1]};

fragment ESCAPESEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\';
fragment CHARSEQ: ~[\b\t\n\f\r"\\] | ESCAPESEQ | '\'"';


WS: [ \t\r]+ -> skip; // skip spaces, tabs
ILLEGAL_ESCAPE: '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'~[bfrnt'\\]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* {self.text = self.text[1:]; raise UncloseString(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};