grammar ZCode;

@lexer::header {
from lexererr import *
# Student ID: 2011357
}

options {
	language = Python3;
}

program: decllist EOF;

//Parser
decllist: decl decllist | decl;

decl: funcdecl | vardecl;

vardecl: (VAR IDENTIFIER ASSIGN expression) | (typ | DYNAMIC) IDENTIFIER (ASSIGN expression | );

funcdecl: FUNC IDENTIFIER LRB parameterlist RRB newlinelist (returnstate | blockstate | );

funcdeclonly: FUNC IDENTIFIER LRB parameterlist RRB;

parameterlist: parameterprime | ;

parameterprime: param CM parameterprime | param;

param: typ IDENTIFIER;

newlinelist: NEWLINE newlinelist | ;

typ: NUMBER | BOOL | STRING;

returnstate: RETURN (IDENTIFIER | NUMLIT) NEWLINE;

blockstate: BEGIN (IDENTIFIER | NEWLINE | ) END NEWLINE;

arraylit: LSB elementlist RSB;

elementlist: expression CM elementlist | ;

expression: NUMLIT; //temporary

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

IDENTIFIER: [a-zA-Z_][a-zA-Z_]*;
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