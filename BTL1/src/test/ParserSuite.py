import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_202(self):
        """Simple program: int main() {} """
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_203(self):
        input = """func main() begin
        aPI[3] <- 3.14
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_204(self):
        input = """number VoTien
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test_205(self):
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