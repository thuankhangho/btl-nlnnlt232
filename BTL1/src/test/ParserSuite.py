import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    
    def test_201(self):
        """Simple program: int main() {} """
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_202(self):
        input = """func main() begin
        aPI[3] <- 3.14
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_203(self):
        input = """number temp
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_204(self):
        """test function declaration"""
        input = """func main()
            begin
                var j <- 1
                for i until i >= 10 by 1
                    writeNumber(i)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_205(self):
        input = """func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_206(self):
        input = """func main()
        begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_207(self):
        input = """func isPrime(number x)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_208(self):
        input = """func main()
        begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_209(self):
        input = """dynamic temp[5] <- 3
        """
        expect = "Error on line 1 col 12: ["
        self.assertTrue(TestParser.test(input,expect,209))

    def test_210(self):
        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 210))