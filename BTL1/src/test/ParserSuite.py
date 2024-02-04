import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    
    def test_201(self):
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
        expect = "Error on line 1 col 7: string"
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
        input = """var temp <- true > (x >= z)
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
        expect = "Error on line 6 col 22: i"
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
        expect = "Error on line 1 col 9: ["
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
        input = """number a[2] <- [1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_231(self):
        input = """var a[3] <- [2,"why not",false]
        """
        expect = "Error on line 1 col 5: ["
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
        
    def test_233(self):
        input = """number a[3] <- [2,"why not",false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        
    def test_234(self):
        input = """func main()
        begin
        a <- a[1+1]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test_235(self):
        input = """func getNumofShape()
        begin
        return _numOfShape
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test_236(self):
        input = """var x <- 65
        func test(number n)
        begin
            if (n == 0) return true
            else return false
        end
        
        func _inc()
        
        func main()
        begin
            var delta <- test(3)
            writeInt(delta)
        end
        
        func _inc()
        begin
            n <- n + delta
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test_237(self):
        input = """func railfence(string ciphertext, number key)
        begin
            if (key <= 1) return ciphertext
            string matrix[15]
            for i until i < 15 by 1
            begin
                ##15 for each row
                ## maximum 15 rows
                string matrix_a[15]
            end
            
            bool dir <- true
            ## true for down, false for up
            var row <- 0
            var col <- 0
            for i until i < length(ciphertext) by 1
            begin
                if (row == 0) dir <- true
                if (row == key - 1) dir <- false
                rail[2,3] <- null
                col <- col + 1
                if (dir == true) row <- row + 1
                else row <- row - 1
            end
            
            number index <- 0
            for i until i < key by 1
            begin
                for j until j < length(ciphertext) by 1
                begin
                    if ((matrix[1] == null) and (index < length(ciphertext)))
                        begin
                            matrix[1] <- ciphertext[1,2]
                            index <- index[1][2] + 1
                        end
                end
            end
            
            row <- 0
            
            col <- 0
            
            
            string result
            
            for i until i < length(ciphertext) by 1 
            begin
                ## check the direction of flow
                if (row == 0)
                    dir <- true
                elif (row == key - 1)
                    dir <- false
 
                ## place the marker
                if (rail[row] != "*")
                    result <- rail[col]
                col <- col + 1
 
                ## find the next row using direction flag
                if (dir == true)
                    row <- row + 1
                else row <- row - 1
            end
            return result
        end
        """
        expect = "Error on line 34 col 45: ["
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_238(self):
        input = """func main()
        begin
            if (i == 3) continue
            else writeInt(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_239(self):
        input = """func main()
        begin
            continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_240(self):
        input = """func main()
        begin
            return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        
    def test_241(self):
        input = """func main()
        begin
            continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_242(self):
        input = """func main()
        begin
            if (x == 5)
            begin
                return 0
            end
            elif (x == 6)
            begin
                return x
            end
            else continue ##stop
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        
    def test_243(self):
        input = """func main()
        begin
            return length[1,2] < 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
        
    def test_244(self):
        input = """func main()
        begin
            return length[1,2] < 3 and (1 < 2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_245(self):
        input = """func main()
        begin
            return length[1,2] ... 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_246(self):
        input = """func main()
        begin
            string message <- "This is an unclosed string literal"
            writeString(message)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_247(self):
        input = """main()
        begin
        end
        """
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_248(self):
        input = """dynamic a[2]
        func main()
        begin
        end
        """
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_249(self):
        input = """string a[2,3,4,5,6]
        func main()
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_250(self):
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    
    def test_251(self):
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_252(self):
        input = """func main() begin
        aPI[3] <- 3.14
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_253(self):
        input = """number temp
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    
    def test_254(self):
        """test function declaration"""
        input = """func main()
            begin
                var j <- 1
                for i until i >= 10 by 1
                    writeNumber(i)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_255(self):
        input = """func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_256(self):
        input = """func main()
        begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_257(self):
        input = """func isPrime(number x)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_258(self):
        input = """func main()
        begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_259(self):
        input = """dynamic temp[5] <- 3
        """
        expect = "Error on line 1 col 12: ["
        self.assertTrue(TestParser.test(input,expect,259))

    def test_260(self):
        input = """bool a["string"]
        bool a[[1,2]]
        bool a[1+1]
        """
        expect = "Error on line 1 col 7: string"
        self.assertTrue(TestParser.test(input, expect, 260))
        
    def test_261(self):
        input = """func test()
            func test() return 1
            func main()
            func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
        
    def test_262(self):
        input = """var temp <- true > (x >= z)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test_263(self):
        input = """dynamic temp <- false ... x
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
        
    def test_264(self):
        input = """dynamic temp
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        
    def test_265(self):
        input = """func main(number x[2])
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                a <- 1
                ## comment
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
        
    def test_266(self):
        input = """func main(number x[2])
            begin
            if (i < 0) return
                ## comment
            elif (i = 0) writeString("Hi") 
                ## comment
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        
    def test_267(self):
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
        self.assertTrue(TestParser.test(input, expect, 267))
        
    def test_268(self):
        input = """func main()
            begin
                begin
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        
    def test_269(self):
        input = """func main(number x, string y)
            begin
                begin
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        
    def test_270(self):
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
        self.assertTrue(TestParser.test(input, expect, 270))
        
    def test_271(self):
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
        expect = "Error on line 6 col 22: i"
        self.assertTrue(TestParser.test(input, expect, 271))
        
    def test_272(self):
        input = """func test()
        begin
            var i <- 0
            return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
        
    def test_273(self):
        input = """func test() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
        
    def test_274(self):
        input = """func test() return arr[5,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test_275(self):
        input = """func _inc(number n, number delta)
        begin
            n <- n + delta
            return n
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        
    def test_276(self):
        input = """func _main()
        begin
            var delta <- fact(3)
            inc(x, delta)
            writeInt(x)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test_277(self):
        input = """func fact(number n)
        begin
            if (n == 0) return 1
            else return n * fact(n - 1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        
    def test_278(self):
        input = """dynamic a[5]
        """
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input, expect, 278))
        
    def test_279(self):
        input = """func test()
        begin
            text <- "Hello" ... 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test_280(self):
        input = """number a[2] <- [1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test_281(self):
        input = """var a[3] <- [2,"why not",false]
        """
        expect = "Error on line 1 col 5: ["
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test_282(self):
        input = """func test() begin
        if (a > 10) return writeString(a)
        elif (b > 10) return a[5]
        elif (c > 10) return 3
        else return false
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
        
    def test_283(self):
        input = """number a[3] <- [2,"why not",false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        
    def test_284(self):
        input = """func main()
        begin
        a <- a[1+1]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        
    def test_285(self):
        input = """func getNumofShape()
        begin
        return _numOfShape
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        
    def test_286(self):
        input = """var x <- 65
        func test(number n)
        begin
            if (n == 0) return true
            else return false
        end
        
        func _inc()
        
        func main()
        begin
            var delta <- test(3)
            writeInt(delta)
        end
        
        func _inc()
        begin
            n <- n + delta
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        
    def test_287(self):
        input = """func railfence(string ciphertext, number key)
        begin
            if (key <= 1) return ciphertext
            string matrix[15]
            for i until i < 15 by 1
            begin
                ##15 for each row
                ## maximum 15 rows
                string matrix_a[15]
            end
            
            bool dir <- true
            ## true for down, false for up
            var row <- 0
            var col <- 0
            for i until i < length(ciphertext) by 1
            begin
                if (row == 0) dir <- true
                if (row == key - 1) dir <- false
                rail[2,3] <- null
                col <- col + 1
                if (dir == true) row <- row + 1
                else row <- row - 1
            end
            
            number index <- 0
            for i until i < key by 1
            begin
                for j until j < length(ciphertext) by 1
                begin
                    if ((matrix[1] == null) and (index < length(ciphertext)))
                        begin
                            matrix[1] <- ciphertext[1,2]
                            index <- index[1][2] + 1
                        end
                end
            end
            
            row <- 0
            
            col <- 0
            
            
            string result
            
            for i until i < length(ciphertext) by 1 
            begin
                ## check the direction of flow
                if (row == 0)
                    dir <- true
                elif (row == key - 1)
                    dir <- false
 
                ## place the marker
                if (rail[row] != "*")
                    result <- rail[col]
                col <- col + 1
 
                ## find the next row using direction flag
                if (dir == true)
                    row <- row + 1
                else row <- row - 1
            end
            return result
        end
        """
        expect = "Error on line 34 col 45: ["
        self.assertTrue(TestParser.test(input, expect, 287))
        
    def test_288(self):
        input = """func main()
        begin
            if (i == 3) continue
            else writeInt(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
        
    def test_289(self):
        input = """func main()
        begin
            continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_290(self):
        input = """func main()
        begin
            return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_291(self):
        input = """func main()
        begin
            continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
        
    def test_292(self):
        input = """func main()
        begin
            if (x == 5)
            begin
                return 0
            end
            elif (x == 6)
            begin
                return x
            end
            else continue ##stop
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_293(self):
        input = """func main()
        begin
            return length[1,2] < 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_294(self):
        input = """func main()
        begin
            return length[1,2] < 3 and (1 < 2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_295(self):
        input = """func main()
        begin
            return length[1,2] ... 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_296(self):
        input = """func main()
        begin
            string message <- "This is an unclosed string literal"
            writeString(message)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
        
    def test_297(self):
        input = """main()
        begin
        end
        """
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_298(self):
        input = """dynamic a[2]
        func main()
        begin
        end
        """
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_299(self):
        input = """string a[2,3,4,5,6]
        func main()
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))