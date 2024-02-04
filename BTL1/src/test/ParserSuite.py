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
        input = """bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 210))
        
    def test_211(self):
        input = """func test()
            func test() return 1
            func main()
            func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test_212(self):
        input = """var temp <- true > x >= z
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        
    def test_213(self):
        input = """dynamic temp <- false ... x
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
    def test_214(self):
        input = """dynamic temp
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        
    def test_215(self):
        input = """func main(number x[2])
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                a <- 1
                ## comment
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_216(self):
        input = """func main(number x[2])
            begin
            if (i < 0) return
                ## comment
            elif (i = 0) writeString("Hi") 
                ## comment
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test_217(self):
        input = """func main(number x[2])
            begin
                var a <- getString(i)
                var b <- getString(e)
                if (i < 0)
                begin
                var a <- getString(i)
                var b <- getString(e)
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test_218(self):
        input = """func main()
            begin
                begin
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_219(self):
        input = """func main(number x, string y)
            begin
                begin
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_220(self):
        input = """func main()
            begin
                begin
                    begin
                        var a <- 10
                        number a <- 10
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test_221(self):
        input = """func foo(number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1
                begin
                    a[i] <- i * i + 5
                end
            return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_222(self):
        input = """func test()
        begin
            var i <- 0
            return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        
    def test_223(self):
        input = """func test() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test_224(self):
        input = """func test() return arr[5,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test_225(self):
        input = """func _inc(number n, number delta)
        begin
            n <- n + delta
            return n
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
    def test_226(self):
        input = """func _main()
        begin
            var delta <- fact(3)
            inc(x, delta)
            writeInt(x)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        
    def test_227(self):
        input = """func fact(number n)
        begin
            if (n == 0) return 1
            else return n * fact(n - 1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        
    def test_228(self):
        input = """dynamic a[5]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test_229(self):
        input = """func test()
        begin
            text <- "Hello" ... 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        
    def test_230(self):
        input = """number a[2] <- [1,2];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_231(self):
        input = """var a[3] <- [2,"why not",false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        
    def test_232(self):
        input = """func test() begin
        if (a > 10) return writeString(a)
        elif (b > 10) return a[5]
        elif (c > 10) return 3
        else return false
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))