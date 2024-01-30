grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: ;

IDENTIFIER: [a-z] [a-z0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;