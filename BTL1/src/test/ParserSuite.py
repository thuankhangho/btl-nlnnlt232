import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_simple_program3(self):
        input = """func main() begin
        aPI[3] <- 3.14
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_005(self):
        """test function declaration"""
        input = """func main()
            begin
                var j <- 1
                for i until i >= 10 by 1
                    writeNumber(i)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))