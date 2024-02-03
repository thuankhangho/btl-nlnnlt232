grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
    language=Python3;
}

// declared
program: ignorenull list_declared EOF;
list_declared: declared list_declared | declared;
declared: funcdecl | vardecl;

// declared function
funcdecl: FUNC ID LPAREN parameterlist RPAREN ignorenull (return_statement | block_statement | );
parameterlist: parameterprime | ;
parameterprime: param COMMA parameterprime | param;
param: typ (ID | array_type);
typ: NUMBER | BOOL | STRING;

// declared variable
vardecl: implicit_var | keyword_var | implicit_dynamic;
keyword_var: typ (ID | array_type) (ASSIGNINIT expression | ) ignore;
implicit_var: VAR ID ASSIGNINIT expression ignore;
implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression | ) ignore;

// Expression
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | DOUBlEEQUAL | DIFF | LESS | GREATER | LESSEQUAL | GREATEREQUAL) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: (ID | function_call) (LBRACKET index_operator RBRACKET) | expression8;
expression8: ID | NUMBER_LIT | STRING_LIT | BOOL_LIT | LPAREN expression RPAREN | function_call;
index_operator: expression COMMA index_operator | expression;
function_call: ID LPAREN argument_list RPAREN;

// Statements
// Variable Declaration Statement
variable_declaration_statement: implicit_var | keyword_var | implicit_dynamic;

// Assignment Statement
assignment_statement: lhs ASSIGNINIT expression ignore ;
lhs: ID | array_type;

// If Statement
if_statement: IF LPAREN expression RPAREN ignorenull statement (elif_list | else_statement | );
elif_list: elif_statement ignorenull elif_list | ;
elif_statement: ELIF LPAREN expression RPAREN ignorenull statement;
else_statement: ELSE statement;

// For Statement
for_statement: FOR ID UNTIL expression BY expression ignorenull statement;

// Break Statement
break_statement: BREAK ignore;

// Continue Statement
continue_statement: CONTINUE ignore;

// Return Statement
return_statement: RETURN (expression | ) ignore;

// Function Call Statement
call_statement: ID LPAREN argument_list RPAREN ignore;

// Block Statement
block_statement: BEGIN ignore statement_list END ignore;

statement: variable_declaration_statement | assignment_statement | if_statement | for_statement | break_statement | continue_statement | return_statement | call_statement | block_statement;
statement_list: statement statement_list | ;

// Value
array_type: ID LBRACKET numberlist RBRACKET;
array_literal: LBRACKET list_expression RBRACKET;
list_expression: expression COMMA list_expression | expression;
numberlist: NUMBER_LIT COMMA numberlist | NUMBER_LIT;
argument_list: argumentprime | ;
argumentprime: expression COMMA argumentprime | expression;

// Kí tự bỏ qua
ignorenull: NEWLINE ignorenull | ;
ignore: NEWLINE ignorenull | NEWLINE;

// Keyword
BOOL_LIT: TRUE | FALSE;
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

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
ASSIGNINIT: '<-';
DIFF: '!=';
LESS: '<';
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';
CONCAT: '...';
DOUBlEEQUAL: '==';

// Separators
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
NEWLINE: '\n';

// Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literal 
STRING_LIT: '"' (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"')* '"'
{
    self.text = self.text[1:-1];
};
NUMBER_LIT: INTEGER_PART DECIMAL_PART? EXPONENT_PART?;
fragment INTEGER_PART: [0-9]+;
fragment DECIMAL_PART: '.'[0-9]*;
fragment EXPONENT_PART: ('e' | 'E') ('+' | '-')? [0-9]+;

// NEWLINE COMMENTS WS
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS: [ \t\r\f\b]+ -> skip ; // skip spaces, tab
// ERROR
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"')* ('\r\n' | '\n' | EOF)
{
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"')* ( [\r\f] | '\\' ~[bfrnt'\\])
{
    raise IllegalEscape(self.text[1:])
};