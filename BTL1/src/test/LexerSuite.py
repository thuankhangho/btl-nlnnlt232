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
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_104(self):
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,104))

    def test_105(self):
        self.assertTrue(TestLexer.test("## this is a comment\n var x <- 10","var,x,<-,10,<EOF>",105))
        
    def test_172(self):
        self.assertTrue(TestLexer.test(""" "'" ""","',<EOF>",172))
        
        
    # def test_complex_string(self):
    #     input = """ "He asked me: \'"Where is John?\'"" """
    #     expect = """He asked me: '"Where is John?'",<EOF>"""
    #     self.assertTrue(TestLexer.test(input,expect,102))
        
    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    