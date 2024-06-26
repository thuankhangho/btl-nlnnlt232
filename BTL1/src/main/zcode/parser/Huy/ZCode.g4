// Student ID: 20512496
// Name: Nguyen Khanh Huy
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//Parser
program: nullablenewlinelist declist EOF;
declist: decl declist | decl ;
decl: funcdecl | vardecl;

vardecl: (typedecl | variabledecl | dynamicdecl) nullablenewlinelist;
typedecl: typ (ID | arrtype) (valueinit | );
valueinit: ASSIGN exp;
variabledecl: VAR ID valueinit ;
dynamicdecl: DYNAMIC ID (valueinit | ) ;

funcdecl: FUNC ID LRB paramlist RRB nullablenewlinelist (returnstmt | blockstmt | );
paramlist: paramprime | ;
paramprime: param CM paramprime | param;
param: typ ID;
typ: NUMBER | BOOL | STRING;

relational: EQ | COMPARE | NEQ | LE | GE | LEQ | GEQ ;
exp: exp1 CONCAT exp1 | exp1;
exp1:exp2 relational exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (PLUS | MINUS) exp4 | exp4;
exp4: exp4 (MULTIPLY | DIVIDE | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6 ;
exp6: MINUS exp6 | exp7;
exp7: (ID | funcall) (LSB indexoperator RSB) | exp8 ;
exp8: ID | NUMLIT | BOOLIT | STRINGLIT | arrtype | funcall | LRB exp RRB;
indexoperator: exp CM indexoperator | exp;

arrtype: (ID | funcall) LSB numlist RSB;
numlist: NUMLIT CM numlist | NUMLIT;

funcall: ID LRB argumentlist RRB ;
argumentlist: argumentprime | ;
argumentprime: exp CM argumentprime | exp;

vardeclstmt: (typedecl | variabledecl | dynamicdecl) nonnullablenewlinelist;
assignmentstmt: lhs ASSIGN exp nonnullablenewlinelist;
lhs: ID | arrtype;
ifstmt: IF LRB exp RRB nullablenewlinelist stmt (elsestmt | elifstmtlist | );
elsestmt: ELSE stmt;
elifstmtlist: elifstmt nonnullablenewlinelist elifstmtlist | elifstmt;
elifstmt: ELIF LRB exp RRB stmt;
forstmt: FOR ID UNTIL exp BY exp nullablenewlinelist stmt;
breakstmt: BREAK nonnullablenewlinelist;
continuestmt: CONTINUE nonnullablenewlinelist;
returnstmt: RETURN (exp | ) nonnullablenewlinelist;
funcallstmt: funcall nonnullablenewlinelist;
blockstmt:BEGIN nonnullablenewlinelist nullablestmtlist END nonnullablenewlinelist;
stmt: vardeclstmt | assignmentstmt | ifstmt | forstmt | breakstmt | continuestmt
 | returnstmt | funcallstmt | blockstmt;
nullablestmtlist: stmt nullablestmtlist |  ;

arrlit: LSB nonnullableexplist RSB;
nonnullableexplist: exp CM nonnullableexplist | exp;

nullablenewlinelist: NEWLINE nullablenewlinelist |  ;
nonnullablenewlinelist: NEWLINE nonnullablenewlinelist | NEWLINE;

//Lexer
BOOLIT: TRUE | FALSE;

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
LINECMT:'##' .*? ('\n'|EOF) -> skip;
NUMLIT: INTLIT DEC? EXP?;

fragment INTLIT: [0-9]+;

fragment DEC: '.'? [0-9]*;

fragment EXP: [Ee][+-]?[0-9]+;

STRINGLIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

fragment ESCAPESEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\'' | '\\\\';
fragment CHAR_LIT: ~[\b\t\n\f\r"\\] | ESCAPESEQ | '\'"';

ID: [A-Za-z_][A-Za-z_0-9]*;

WS: [ \t\r]+ -> skip; // skip spaces, tabs

ILLEGAL_ESCAPE: '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'~[bfrnt'\\]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' ('\\' [btnfr'\\] | ~[\r\t\n\\"] )* {self.text = self.text[1:]; raise UncloseString(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};