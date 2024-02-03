//2052749
grammar ZCode;

@lexer::header /{
from lexererr import *
}

options {
	language=Python3;
}

// declared 
program: newline_lit_can_null declist EOF;
//decl danh sach cac decl cach nhau boi newline
declist: decl declist | decl; // loai 1
decl: funcdel | vardecl;
vardecl:(type_decl | imp_decl) newline_lit_can_null;
type_decl: (NUMBER | BOOL | STRING) (ID | array_type) ( ASSIGNINIT expr)?;
imp_decl: (VAR ID ASSIGNINIT expr) | (DYNAMIC ID (ASSIGNINIT expr)?);


funcdel: FUNC ID LPAREN list_parameter RPAREN newline_lit_can_null(return_statement | block_statement | ) newline_lit_can_null;  
list_parameter: parameterprime | ;// loai 4
parameterprime: parameter COMMA parameterprime | parameter;
parameter: (NUMBER | BOOL | STRING) ID ;

//function call
function_call: ID LPAREN list_of_argument RPAREN ;
list_of_argument: argumentprime | ;
argumentprime: argument COMMA argumentprime | argument;
argument:expr;

//statement 
var_decl_statement: (type_decl | imp_decl) newline_lit;
//7.2 assignment statement
assignment_statement: lhs ASSIGNINIT expr newline_lit;
lhs:ID | array_type;
//7.3 if statement
if_statement:IF LPAREN expr RPAREN newline_lit_can_null stmt (else_statement? | elif_lit);
else_statement: ELSE stmt;
elif_statement: ELIF LPAREN expr RPAREN stmt;
elif_lit: elifprime | ;// danh sach cac elif cach nhau boi new_line
elifprime: elif_statement NEWLINE elifprime | elif_statement;

stmt: var_decl_statement 
| assignment_statement 
| if_statement 
| for_statement 
| break_statement 
| continue_statement 
| return_statement 
| function_call_statement 
| block_statement;

//7.4 for statement
for_statement: FOR ID UNTIL expr BY expr newline_lit_can_null stmt;
//7.5 break statement
break_statement: BREAK newline_lit;
//7.6 continue statement
continue_statement: CONTINUE newline_lit;
//7.7 return statement
return_statement: RETURN (expr | ) newline_lit;
//7.8 function call statement
function_call_statement:ID LPAREN list_of_argument RPAREN newline_lit;
//7.9 block statement
block_statement:BEGIN newline_lit statement_lit END newline_lit;
statement_lit: stmt statement_lit | ; // loai danh sach cac lit co the rong

//4.4 array type
array_type: (ID | function_call) LBRACKET number_list RBRACKET;
number_list: NUMBER COMMA number_list | NUMBER; //loai 3

newline_lit: NEWLINE newline_lit | NEWLINE;
newline_lit_can_null: NEWLINE newline_lit_can_null | ; 

// array
array_lit:LBRACKET expr_list RBRACKET;
expr_list: expr COMMA expr_list | expr;
expr: expr1 CONCAT expr1 | expr1; // do uu tien 5.7 thang duoi uu tien  // a...b -> concat giua 
expr1: expr2 (EQUAL | EQUALSTRING | NOTEQUAL | LT | GT | LE | GE) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUl | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: (ID | function_call) (LBRACKET index_operator RBRACKET) | expr8;
expr8: ID | NUMBER_LIT | STRING_LIT | BOOL_LIT | LPAREN expr RPAREN | array_type | function_call;
index_operator:expr COMMA index_operator | expr  ;//loai 3 danh sach cac expr cach nhau boi comma ko rong




//! --------------------------  Lexical structure ----------------------- //
//keyword
BOOL_LIT: TRUE | FALSE;

IF:'if';
ELSE:'else';
FOR:'for';
UNTIL:'until';
BY:'by';
BREAK:'break';
CONTINUE:'continue';
ELIF:'elif';
BEGIN:'begin';
END:'end';
NOT:'not';
AND:'and';
OR:'or';
TRUE:'true';
FALSE:'false';
NUMBER:'number';
BOOL:'bool';
STRING:'string';
RETURN:'return';
VAR:'var';
DYNAMIC:'dynamic';
FUNC:'func'; /// khai roi

//operators
ADD:'+';
SUB:'-';
MUl:'*';
DIV:'/';
MOD:'%';
GE:'>=';
LE:'<=';
GT:'>';
LT:'<';
NOTEQUAL:'!=';
EQUAL:'=';
EQUALSTRING:'=='; // SO 2 CHUOI
CONCAT:'...';
ASSIGNINIT: '<-';

//SEPARATOR
LPAREN:'(';
RPAREN:')';
LBRACKET:'[';
RBRACKET:']';
COMMA:',';
// Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;


// Literal 
//! STRING_LIT nhớ dùng python bỏ đi " " đầu và cuối
NUMBER_LIT: INT DECL? EXPONENT?;
fragment INT:[0-9]+;
fragment DECL: '.'[0-9]*;
fragment EXPONENT: ('e'|'E')('+'|'-')?[0-9]+;


STRING_LIT: '"' (ALLOW)* '"' {self.text = self.text[1:-1];};
// với kí tự cho phép là
fragment ALLOW: (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"' );
fragment ILLEGAL:[\r\f] | '\\' ~[bfrnt'\\]; // ki tu ko cho phep 

// NEWLINE COMMENTS WS
//! vì NEWLINE là kí tự kết thúc giống với ';' trong C nên lấy để xử lí bước sau
//! vì ngôn ngữ này COMMENTS chỉ 1 hàng không chung với mấy biểu thức khác nên bắt để xử lí thứ tự các bước sau
//! COMMENTS lên lớp nghe thử thầy nói gì không nha vì này nén lỗi phần lexer cũng được mà nhưng thứ tự ngữ pháp và ở phần tiếp theo -> này tùy thầy thôi
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS : [ \t\r]+ -> skip ; // skip spaces, tabs

// ERROR
//! hiện thực  UNCLOSE_STRING và ILLEGAL_ESCAPE code antlr và python tận dụng lại ý tưởng STRING_LIT
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' ( ALLOW)* ('\r\n' | '\n' | EOF)
{
	if self.text[-1] == '\n' and self.text[-2] == '\r':
		raise UncloseString(self.text[1:-2])
	elif self.text[-1] == '\n':
		raise UncloseString(self.text[1:-1])
	else:
		 UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (ALLOW)* ILLEGAL
{
raise IllegalEscape(self.text[1:])
};
//!  -------------------------- end Lexical structure ------------------- //

