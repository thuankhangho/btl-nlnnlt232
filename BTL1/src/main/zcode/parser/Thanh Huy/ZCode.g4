grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
    language=Python3;
}

// declared 
program:  keyword_var EOF;
list_declared: declared list_declared | declared;
declared: (function | variables) ignore;
// TODO declared variable
variables: implicit_var | keyword_var | implicit_dynamic; 

implicit_var: VAR ID ASSIGNINIT expression;
keyword_var:NUMBER ID ;
//keyword_var: (BOOL | NUMBER | STRING) (ID|array_type)(ASSIGNINIT expression| );

implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression | );

// TODO declared function
function: FUNC ID LPAREN parameters_list  RPAREN (ignore? return_statement | ignore? block_statement | ignore);
parameters_list: parameterprime|;
parameterprime:parameter COMMA parameterprime|parameter;
parameter: (BOOL | NUMBER | STRING ) ID ;

// TODO Expression
list_expr: expression COMMA list_expr | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL|DOUBlEEQUAL|DIFF|LESS|GREATER|LESSEQUAL|GREATEREQUAL) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: expression7 (LBRACKET index_operator RBRACKET) | expression8;
index_operator: expression COMMA index_operator|expression;
expression8: ID | NUMBER_LIT | STRING_LIT | TRUE | FALSE | LPAREN expression RPAREN | array_type|function_call;
function_call:ID LPAREN argument_list RPAREN;

// TODO Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET list_expression RBRACKET;
list_expression : expression COMMA list_expression | expression;
array_type: ID LBRACKET list_number RBRACKET;
list_number: NUMBER_LIT COMMA list_number |NUMBER_LIT;


// TODO  Statements
statement_list: statement statement_list | ; 
statement: variable_declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement | call_statement | block_statement;

// Variable Declaration Statement
variable_declaration_statement: variables ignore;

// Assignment Statement
assignment_statement: lhs ASSIGNINIT expression ignore ;

lhs: (ID | ID LBRACKET list_expr RBRACKET);



// If Statement
if_statement: IF LPAREN expression RPAREN ignore? statement elif_list|else_statement|;
elif_list:elif_statement ignore? elif_list|;
elif_statement: ELIF LPAREN expression RPAREN ignore? statement;
else_statement: ELSE statement ignore;

// For Statement
for_statement: FOR ID UNTIL expression BY expression ignore? statement;

// Break Statement
break_statement: BREAK ignore;

// Continue Statement
continue_statement: CONTINUE ignore;

// Return Statement
return_statement: RETURN (expression)? ignore;

// Function Call Statement
call_statement: ID LPAREN argument_list RPAREN ignore;

argument_list: argument_prime |;
argument_prime: expression COMMA argument_prime|expression;


// Block Statement
block_statement: BEGIN ignore statement_list END ignore;
// kí tự bỏ qua
ignore: NEWLINE ignore |NEWLINE;

// TODO Keyword
//BOOL_LIT
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

// TODO Operators
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

// TODO Separators
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal 
STRING_LIT: '"' (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"')* '"'
{
    self.text = self.text[1:-1];
};
NUMBER_LIT: INTEGER_PART DECIMAL_PART? EXPONENT_PART?;
fragment INTEGER_PART: [0-9]+;
fragment DECIMAL_PART: '.'[0-9]*;
fragment EXPONENT_PART: ('e' | 'E') ('+' | '-')? [0-9]+;

// NEWLINE COMMENTS WS
NEWLINE: '\n'; // newline
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS: [ \t\r\f\b]+ -> skip ; // skip spaces, tab
// TODO ERROR
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
//! -------------------------- end Lexical structure ------------------- //
