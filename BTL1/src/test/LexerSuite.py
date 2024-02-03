import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_101(self):
        input = """ "This is a string containing tab \\t" """
        expect = """This is a string containing tab \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,101))
        
    def test_102(self):
        input = """ "\'"Where is John?; He asked me" """
        expect = """'"Where is John?; He asked me,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,102))
        
    def test_103(self):
        input = """ func main() return 1 """
        expect = """func,main,(,),return,1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_104(self):
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,104))

    def test_105(self):
        self.assertTrue(TestLexer.test("## this is a comment\n var x <- 10","var,x,<-,10,<EOF>",105))
        
    def test_106(self):
        input = "a <- 5 ##this is a line comment"
        expected = "a,<-,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 106))

    def test_107(self):
        input = "x << 2 >> y"
        expected = "x,<,<,2,>,>,y,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 107))

    def test_108(self):
        input = "## This is a block comment so // has no meaning here */\n##This is a line comment so /* has no meaning here"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 108))

    def test_109(self):
        input = "_a123"
        expected = "_a123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 109))

    def test_110(self):
        input = "__"
        expected = "__,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 110))

    def test_111(self):
        input = "__main__"
        expected = "__main__,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 111))

    def test_112(self):
        input = "a\r"
        expected = "a,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 112))

    def test_113(self):
        input = "=="
        expected = "==,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 113))

    def test_114(self):
        input = "..."
        expected = "...,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 114))

    def test_115(self):
        input = "]"
        expected = "],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 115))

    def test_116(self):
        input = "123"
        expected = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 116))

    def test_117(self):
        input = "0.5"
        expected = "0.5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))

    def test_118(self):
        input = "1."
        expected = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 118))

    def test_119(self):
        input = "1e1"
        expected = "1e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 119))

    def test_120(self):
        input = "1.e1"
        expected = "1.e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 120))

    def test_121(self):
        input = "e1"
        expected = "e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 121))

    def test_122(self):
        input = "1.E+1"
        expected = "1.E+1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 122))

    def test_123(self):
        input = "e+1"
        expected = "e,+,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 123))

    def test_124(self):
        input = "E1e"
        expected = "E1e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 124))

    def test_125(self):
        input = "10.1e-10"
        expected = "10.1e-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 125))

    def test_126(self):
        input = "143e"
        expected = "143,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 126))

    def test_127(self):
        input = "0.33E-3"
        expected = "0.33E-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 127))

    def test_128(self):
        input = "128e+42"
        expected = "128e+42,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 128))

    def test_129(self):
        input = "1E-3"
        expected = "1E-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 129))

    def test_130(self):
        input = "12.3e-30"
        expected = "12.3e-30,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 130))

    def test_131(self):
        input = "a <- true"
        expected = "a,<-,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 131))

    def test_132(self):
        input = "a <- fals"
        expected = "a,<-,fals,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 132))

    def test_133(self):
        input = "falsetrue"
        expected = "falsetrue,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 133))

    def test_134(self):
        input = """ "'" """
        expected = "',<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 134))

    def test_135(self):
        input = """ "\'"\'"" """
        expected = """'"'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expected, 135))

    def test_136(self):
        input = "\"123\k Hi\""
        expected = "Illegal Escape In String: 123\k"
        self.assertTrue(TestLexer.test(input, expected, 136))

    def test_137(self):
        input = "\"123 Hi\""
        expected = "123 Hi,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 137))

    def test_138(self):
        input = "\"Hello\" \"World\""
        expected = "Hello,World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 138))

    def test_139(self):
        input = "print \"Hello, World!\""
        expected = "print,Hello, World!,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 139))

    def test_140(self):
        input = "\"Hello \q World!\""
        expected = "Illegal Escape In String: Hello \q"
        self.assertTrue(TestLexer.test(input, expected, 140))

    def test_141(self):
        input = """ He asked me "Where's John?" """
        expected = "He,asked,me,Where's John?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 141))

    def test_142(self):
        input = """ "'isn''t'" """
        expected = "'isn''t',<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 142))

    def test_143(self):
        input = """"Where is John?"""
        expected = "Unclosed String: Where is John?"
        self.assertTrue(TestLexer.test(input, expected, 143))

    def test_144(self):
        input = "\"dkjoiue\\s\""
        expected = "Illegal Escape In String: dkjoiue\s"
        self.assertTrue(TestLexer.test(input, expected, 144))

    def test_145(self):
        input = "\",./;'p[213]!@#@!$\""
        expected = ",./;'p[213]!@#@!$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 145))

    def test_146(self):
        input = "\"Hello\^\""
        expected = "Illegal Escape In String: Hello\^"
        self.assertTrue(TestLexer.test(input, expected, 146))

    def test_147(self):
        input = "\"Hello$\""
        expected = "Hello$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 147))

    def test_148(self):
        input = "\"Hello\$\""
        expected = "Illegal Escape In String: Hello\$"
        self.assertTrue(TestLexer.test(input, expected, 148))

    def test_149(self):
        input = "\"Hello // World\""
        expected = "Hello // World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 149))

    def test_150(self):
        input = "\"Hello ^ World\""
        expected = "Hello ^ World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 150))
        
    def test_151(self):
        input = "\"Hello \& World\""
        expected = "Illegal Escape In String: Hello \&"
        self.assertTrue(TestLexer.test(input, expected, 151))
        
    def test_152(self):
        input = "[1,2,3]"
        expected = "[,1,,,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 152))
        
    def test_153(self):
        input = "[\"a\",1,true]"
        expected = "[,a,,,1,,,true,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 153))
        
    def test_154(self):
        input = "var a <- [\"a\",\"b\",\"c\",\"d\"]"
        expected = "var,a,<-,[,a,,,b,,,c,,,d,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 154))
        
    def test_155(self):
        input = "[[a,b,c],a,b,c]"
        expected = "[,[,a,,,b,,,c,],,,a,,,b,,,c,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 155))
        
    def test_156(self):
        input = "[a,b,c,d],e]"
        expected = "[,a,,,b,,,c,,,d,],,,e,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 156))
        
    def test_157(self):
        input = "[a,b,c,d],e,[f,g,h]]"
        expected = "[,a,,,b,,,c,,,d,],,,e,,,[,f,,,g,,,h,],],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 157))
        
    def test_158(self):
        input = "\"new X()\""
        expected = "new X(),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 158))
        
    def test_159(self):
        input = "\"\"\"\""
        expected = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 159))
        
    def test_160(self):
        input = "number a <- 1E+3"
        expected = "number,a,<-,1E+3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 160))
        
    def test_161(self):
        input = "[2.3, 4.2, 102e3]"
        expected = "[,2.3,,,4.2,,,102e3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 161))
        
    def test_162(self):
        input = "abc\t"
        expected = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 162))
        
    def test_163(self):
        input = "1234567"
        expected = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 163))
        
    def test_164(self):
        input = "1234.567"
        expected = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 164))
        
    def test_165(self):
        input = "\"Hi\"\""
        expected = "Hi,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expected, 165))
        
    def test_166(self):
        input = "a == 2"
        expected = "a,==,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 166))
        
    def test_167(self):
        input = "a % 5 == 2"
        expected = "a,%,5,==,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 167))
        
    def test_168(self):
        input = "a and 2"
        expected = "a,and,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 168))
        
    def test_169(self):
        input = "a and & 2"
        expected = "a,and,Error Token &"
        self.assertTrue(TestLexer.test(input, expected, 169))
        
    def test_170(self):
        input = "a or | 2"
        expected = "a,or,Error Token |"
        self.assertTrue(TestLexer.test(input, expected, 170))
        
    def test_171(self):
        input = "a / 2"
        expected = "a,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 171))
        
    def test_172(self):
        input = "a != 2"
        expected = "a,!=,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 172))
        
    def test_173(self):
        input = "func constructor"
        expected = "func,constructor,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 173))
        
    def test_174(self):
        input = "## This is a block comment,\n##that span in many lines"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 174))
        
    def test_175(self):
        input = "[0-9][a-zA-Z]"
        expected = "[,0,-,9,],[,a,-,zA,-,Z,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 175))
        
    def test_176(self):
        input = "sleep/study/relax/aesthetic"
        expected = "sleep,/,study,/,relax,/,aesthetic,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 176))
        
    def test_177(self):
        input = "\"\#metoo\""
        expected = "Illegal Escape In String: \#"
        self.assertTrue(TestLexer.test(input, expected, 177))
        
    def test_178(self):
        input = "\"Lofi \And \Chill\""
        expected = "Illegal Escape In String: Lofi \A"
        self.assertTrue(TestLexer.test(input, expected, 178))
        
    def test_179(self):
        input = "\"$$$\""
        expected = "$$$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 179))
        
    def test_180(self):
        input = "[\"$\"$$]"
        expected = "[,$,Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 180))
        
    def test_181(self):
        input = "$$$"
        expected = "Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 181))
        
    def test_182(self):
        input = """\b"""
        expected = "Error Token "
        self.assertTrue(TestLexer.test(input, expected, 182))
        
    def test_183(self):
        input = "\"\%\""
        expected = "Illegal Escape In String: \%"
        self.assertTrue(TestLexer.test(input, expected, 183))
        
    def test_184(self):
        input = "a[2] <- a[1][2]"
        expected = "a,[,2,],<-,a,[,1,],[,2,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 184))
        
    def test_185(self):
        input = "a[2[3[4[5[6[7[8[9]]]]]]]]"
        expected = "a,[,2,[,3,[,4,[,5,[,6,[,7,[,8,[,9,],],],],],],],],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 185))
        
    def test_186(self):
        input = """string a <- test string ##this comment is irrelevant"\n"""
        expected = "string,a,<-,test,string,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 186))
        
    def test_187(self):
        input = "bool a <- [a,b,c,d,e,...]"
        expected = "bool,a,<-,[,a,,,b,,,c,,,d,,,e,,,...,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 187))
        
    def test_188(self):
        input = """say "'"Hello World'"" """
        expected = "say,'\"Hello World'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 188))
        
    def test_189(self):
        input = """print "Hello \nWorld"""
        expected = "print,Unclosed String: Hello "
        self.assertTrue(TestLexer.test(input, expected, 189))
        
    def test_190(self):
        input = """ print "Hello \\nWorld" """
        expected = "print,Hello \\nWorld,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 190))