import unittest
from TestUtils import TestChecker

class CheckSuite(unittest.TestCase):
    def test401(self):
        input = """
func f()
begin
    dynamic x
    x <- [[1, 2, 3], [4, 5, 6]]
    return x[0, 0]
end

func main()
begin
    number x <- f()
end

"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test402(self):
        input = """
func f(number x)

func main()
begin
    number x <- f(2)
    writeNumber(x)
end

func f(number x)
begin
    if (x >= 2) return f(x - 1) + f(x - 2)
    return 1
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test403(self):
        input = """
func main()
begin
    var x <- [[1, 2, 3], [4, 5, 6]]
    var y <- x[0, 0] + 1
    writeBool(y)
end

"""
        expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test404(self):
        input = """
func main ()                                      
begin                                       
var i <-1                                                     
for i until true by 1                                 
var x<-1     
                                     
var y<- x                                        
end                                     
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test405(self):
        input = """
dynamic x
func main()
begin
    x <- [1, 2, 3, 4, 5, 6]
    var y <- x[0, 0] + 1
    writeNumber(y)
end

"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test406(self):
        input = """
dynamic x <- f(2)
func f(number x)

func main()
begin

end
"""
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test407(self):
        input = """
func f(number x)

dynamic x <- f(2) + 1

func f(number y)
begin
    if (y <= 1) return 1
    return y * f(y - 1)
end

func main()
begin
    return 2
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test408(self):
        input = """
func f(number x)

dynamic x <- f(2) + 1

func main()
begin
    return
end
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test409(self):
        input = """
func f(number x[2, 3])
    return x[2]

func main()
begin
    number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    writeNumber(f()[2])
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test410(self):
        input = """
func f(number x[2, 3])
    return x

func main()
begin
    number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    writeNumber(f(x)[0, 1])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test411(self):
        input = """
func f(number x[2, 3])
    return x

func main()
begin
    dynamic x <- [[1, 2, 3], [4, 5, 6]]
    var y <- x[0, 0]
    writeString(y)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test412(self):
        input = """
func f(number x[2, 3], number i, number j)
    return x[i, j]

func main()
begin
    dynamic x <- [[1, 2, 3], [4, 5, 6]]
    var i <- 0
    for i until i >= 2 by 1
        for j until j >= 3 by 1
            writeNumber(f(x, i, j))
end
"""
        expect = "Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test413(self):
        input = """
func main()
begin
    number x <- readNumber()
    if (x <= 10) writeString("Number is less than or equal to 10")
    elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
    else writeString("Invalid number!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test414(self):
        input = """
func isPrime(number x)

func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("x is a prime number")
    else writeString("x is not a prime number")
end

func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
    begin
        if (x % i = 0) return false
    end
    return true
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test415(self):
        input = """
func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main()
begin
    var num1 <- readNumber()
    var num2 <- readNumber()
    if (areDivisors(num1, num2)) writeString("Yes")
    else writeString("No")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test416(self):
        input = """
func f()
begin
    var i <- 0
    for i until i > 10 by 1
    begin

    end
    continue
end

func main()
begin
    f()
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test417(self):
        input = """
func findMax(number x[10], number n)
begin
    if (n = 1) return x[0]
    number k <- findMax(x, n - 1)
    if (k >= x[n]) return k
    return x[n]
end

func main()
begin
    dynamic x <- [3, 4, 0, 1, 2, 7, 9, 8, 5, 6]
    writeNumber(findMax(x, 10))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test418(self):
        input = """
func main()
begin
    number x <- 2 + true
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test419(self):
        input = """
func main () 
begin
var i <-1                                                     
if (true)
 var x<-1    

var y<- x 
end                                                         
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test420(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[3, 3] <- [a, b, c]
    a <- [1, 2, 3]
    b <- [4, 5, 6]
    c <- [7, 8, 9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test421(self):
        input = """
func f(number x[3])
begin
    return
end
    
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    f([a, b, c])
    a <- 3
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test422(self):
        input = """
func f(number x[2, 3])
    
func main()
begin
    dynamic a
    number x[2, 3] <- f(a)
    a[0] <- [1, 2, 3]
end

func f(number x[2, 3])
    return x
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test423(self):
        input = """
func f(number x)
begin
    if (x = 0) return 0
    elif (x = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- [1, 2, 3]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test424(self):
        input = """
func max(number x, number y)
begin
    if (x <= y) return y
    return x
end

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    number z <- readNumber()
    writeNumber(max(max(x, y), z))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test425(self):
        input = """
func pow(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(pow(x, y))
end

func pow(number a, number b)
begin
    if (b = 0) return 1
    number k <- pow(a, b / 2)
    if (b % 2 = 0) return k * k
    return a * k * k
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test426(self):
        input = """
func add(number x, number x)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(add(x, y))
end

func add(number a, number b)
begin
    return a + b
end
"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test427(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(pow(x, y))
end

func add(number a, number b)
begin
    return a + b
end
"""
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test428(self):
        input = """
func add(number x, number y)

func main()
begin
    var i <- 0
    for i until i > 10 by 0
    begin
        i <- add(i, 1)
        writeNumber(i)
    end
end

func add(number a, number b)
begin
    number x <- a + b
    return x
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test429(self):
        input = """
func f(number x)

func main()
begin
    number x <- 10
    number y <- f(x)
    writeNumber(y)
end

func f(string x)
begin
    return x == "Hello"
end
"""
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test430(self):
        input = """
func main()
begin
    var i <- 0
    for i until i < 0 by 1
    begin
        string x <- readString()
        if (x == "Hello") 
        begin
            x <- x ... ", world!"
            writeString(x)
        end
        else writeString("Try again")
    end
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test431(self):
        input = """
func f(number arr[10], number n)
begin
    var i <- 0
    for i until i >= n by 1
        writeNumber(arr[i])
end

"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test432(self):
        input = """
func f(number arr[10], number n)
begin
    var i <- 0
    for i until i >= n by 1
        writeNumber(arr[i])
end

func main()
begin
    dynamic n
    f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
    n <- 10
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test433(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[2, 2] <- [a, [b, 2]]
    a <- 2
    b <- 3
    c <- true
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test434(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[3, 2] <- [a, b, [c, 0]]
    a <- [1]
    b <- [3, 4]
    c <- 0
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test435(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [readNumber(), a, b, c]
    a <- 3
    b <- x[0]
    c <- a + b
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test436(self):
        input = """
func main()
begin
    dynamic x <- readBool()
    dynamic y <- not readBool()
    if (x and y) writeNumber(1)
    else writeNumber(0)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test437(self):
        input = """
func main()
begin
    dynamic x
    if (x) writeString("x is infer to true value")
    else writeString("x is infer to false value")
    x <- 1 + true
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test438(self):
        input = """
func main()
begin
    dynamic x
    if (x) writeString("x is infer to true value")
    else writeString("x is infer to false value")
    x <- not (true and not false) and not (false and not true)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test439(self):
        input = """
            func main() return
            func aaa(number a, bool b)
            begin
            number b
            end
            
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test440(self):
        input = """
func f()
begin
    dynamic x
    x <- (x - 2) * (x + true)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test441(self):
        input = """
number a <- 1 + "Hello"
func main()
    return
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test442(self):
        input = """
func f()

func main()
begin
    number x <- g(1, 2, 3)
end
"""
        expect = "Undeclared Function: g"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test443(self):
        input = """
number x
number y
func f()

func main()
    return
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test444(self):
        input = """
func main()
            begin
                dynamic num
                bool arr <- num and (num > num)
            end
"""
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test445(self):
        input = """
func f()
begin

end
dynamic a
number b
bool c
string d
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test446(self):
        input = """
func f(number x)
begin
    return f(x)
end

func main()
begin
    dynamic d <- f(10)
end
"""
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test447(self):
        input = """
func f(number x)
begin
    return 1
end

func main()
begin
    f(2018)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2018.0)])"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test448(self):
        input = """
func main()
begin
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test449(self):
        input = """
func main()
begin
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test450(self):
        input = """
number x
number y
func add()
    return x + y

func main()
begin
    x <- readNumber()
    y <- readNumber()
    writeNumber(add())
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test451(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    dynamic a <- add(x, y) + 1
end

func add(number x, number y)
    return "Hello"
"""
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test452(self):
        input = """
func f()begin
number c[3,2] <- [[6,7],[4,5],[4,5]]
return c[2,0]
end
func main() begin
number a <- f() 
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test453(self):
        input = """
func main()
begin
    number arr[3, 2] <- [[1, 2], [3, 4], [5, 6]]
    number b[2] <- arr[1]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test454(self):
        input = """
func f(number arr[10], number x)

func main()
begin
    dynamic n
    var i <- 0
    number arr[10]
    for i until true by 1
    begin
        n <- readNumber()
        if ((n > 10) or (n <= 0)) writeString("Try again")
        else break
    end
    
    for i until i >= n by 1
        arr[i] <- readNumber()
    
    f(arr, n)
end

func f(number a[5], number n)
    return
"""
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test455(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    number arr[2, 2] <- [[a, b]]
    number c[2, 2] <- arr
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test456(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    var arr <- [[a], [b], [c], [1]]
    arr <- [[1], [2], [3], [4]]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test457(self):
        input = """
func main()
begin
    dynamic x <- "Hello"
    if (x == "Hello") writeString(x)
    else writeString("Something weird!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test458(self):
        input = """
func main()
begin
    dynamic x <- [1, 2, 3]
    dynamic a <- x
    writeNumber(a[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test459(self):
        input = """
func foo( number a, number b[1,2] )
func foo( number a, number b[1,2] )
func main()
begin
end
func foo( number a, number b[1,2] )
return 1
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test460(self):
        input = """
func foo()
begin
      number a <- 3
end
func foo()
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test461(self):
        input = """
func f(number a[3], number b[3])
    return

func main()
begin
    f([1, 3, 2], [1, "Hello", 2])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test462(self):
        input = """
dynamic a <- [[3, 9, 2, 10, -1], [0, -10, 5, 3, 11], [10, 9, -27, 36, 4]]
func sort(number a[5])
begin
    var i <- 0
    var j <- 0
    for i until i > 4 by 1
        for j until j > 4 by 1
            if (a[i] > a[j])
            begin
                var temp <- a[i]
                a[i] <- a[j]
                a[j] <- temp
            end
end

func main()
begin
    var i <- 0
    for i until i > 2 by 1
        sort(a[i])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test463(self):
        input = """
func main()
func foo()
begin
number a <- main()
end
func main() return 
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test464(self):
        input = """
func f(number n)

number a[2, 3] <- [[f(1), f(2), f(3)], [f(4), f(5), f(6)]]
func main()
begin
    var i <- 0
    dynamic j <- 0
    for i until i > 1 by 1
        for j until j > 2 by 1
            writeNumber(a[i, j])
end

func f(number a)
    return a
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test465(self):
        input = """
func f(number x[2, 3])
    return x[0]

func main()
begin
    dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test466(self):
        input = """
func f(number n)

func main()
begin
    var i <- f(2, 3)
end

func f(number a)
    return a
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test467(self):
        input = """
func f(number x, number y)

func main()
begin
    var i <- f(2)
end

func f(number a)
    return a
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test468(self):
        input = """
dynamic a
func main()
begin
    var i <- a ... 2.75
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test469(self):
        input = """
func func1()
func main()
    begin
    number a <- func1()
    end
func func2()
func func1()
    begin
    var b <- func2()
    return b
    end
func func2() return 1
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, CallExpr(Id(func2), []))"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test470(self):
        input = """
func main()
begin
    if (1) writeBool(true)
    else writeBool(false)
end
"""
        expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test471(self):
        input = """
func main()

func main()

func main()
begin
    if (1) writeBool(true)
    else writeBool(false)
end
"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test472(self):
        input = """
number a
bool b
string c
dynamic d
func main()
begin
    if (b) d <- 1 + a
    else d <- a - 1.75
    c <- "Hello, world!"
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test473(self):
        input = """
func f(number arr[10], number n)
begin
    if ((n < 0) or (n >= 10)) return -999
    number i <- 0
    for i until i >= n by 1
        if (arr[i] < 10) return i
    
    return not (n < 20)
end

func main()
begin
    f([1, 9, 6, 5, 3, 8, 10, 28, 0, -10], 10)
end
"""
        expect = "Type Mismatch In Statement: Return(UnaryOp(not, BinaryOp(<, Id(n), NumLit(20.0))))"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test474(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    var arr <- [[a, 1], [b, true], [c, "Hello"]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test475(self):
        input = """
dynamic x
dynamic y
func main()
begin
    dynamic z
    dynamic arr <- [[1, x], [2, y], [3, z]]
    x <- 20
    y <- 30
    z <- "Hi"
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test476(self):
        input = """
func main()
begin
    var x <- [10, 20, 40]
    var y <- [true, false, true]
    number a[2, 3] <- [x, y]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test477(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 3] <- [x, y]
    x <- [10, 20, 40]
    y <- [true, false, true]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test478(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 3] <- [x, y]
    y <- [y[1] + y[2], y[2] - y[0], y[0] + y[1] < y[2]]
    x <- [1, 9, 6]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(BinaryOp(+, ArrayCell(Id(y), [NumLit(1.0)]), ArrayCell(Id(y), [NumLit(2.0)])), BinaryOp(-, ArrayCell(Id(y), [NumLit(2.0)]), ArrayCell(Id(y), [NumLit(0.0)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(y), [NumLit(0.0)]), ArrayCell(Id(y), [NumLit(1.0)])), ArrayCell(Id(y), [NumLit(2.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test479(self):
        input = """
func f(number x, bool y, string z)
    return not y

func main()
begin
    dynamic x
    dynamic y
    dynamic z
    bool t <- f(x, y, z)
    writeBool(y and not t)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test480(self):
        input = """
func main()
begin
    var x <- [[1, 2], [3, 4, 5]]
    writeNumber(x[0, 2])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test481(self):
        input = """
func test(number x)
begin
    var y <- test
    test(2018)
end
"""
        expect = "Undeclared Identifier: test"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test482(self):
        input = """
func test(number x)
begin
    var a <- x
    var b <- -a
    var c <- a + b
    writeNumber(a + b + c)
end

func main()
begin
    test(2018)
    return -1
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test483(self):
        input = """
dynamic a
string x[1] <- [a]
func main() return
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test484(self):
        input = """
dynamic a
func main()
begin
    var x <- [a, [1, 2, 3]]
    a <- [1, 9, 6]
    x <- [[3, 9, 6], [1, 3, 2]]
    writeNumber(x[0, 0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test485(self):
        input = """
dynamic a
func main()
begin
    dynamic b
    dynamic c
    dynamic d
    var e <- 1
    var x <- [a, [b], [[c]], [[[d, e]]]]
    c <- [-10, 2 / 3 % 0.75]
    b <- [c]
    a <- [b]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test486(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    var x <- [a, b, c, [[1, 2, 3, 4], [5, 6, 7, 8]]]
    c[0] <- d
    d <- [0, 3, 1]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(d), ArrayLit(NumLit(0.0), NumLit(3.0), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test487(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c <- a ... ", world!"
    a <- b
    b <- [1, 2, 3]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test488(self):
        input = """
func main() return
func aaa()
begin
dynamic a
a <- [[1, 2], [3, true]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(3.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test489(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test490(self):
        input = """
dynamic x
func f(number x)
    return x + 1

func main()
begin
    x <- f(20, 30, 40) + 1
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(20.0), NumLit(30.0), NumLit(40.0)])"
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test491(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))
        
    
    def test492(self):
        input = """
func f(number x, number y)
begin
    if (y == 0) return x
    return f(y, x % y)
end

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    dynamic res <- f(x, y)
    writeString(res)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(y), NumLit(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test493(self):
        input = """
func f(number x, number y)
begin
    if (y = 0) return x
    return f(y, x % y)
end

func main()
begin
    number x[10]
    number y[10]
    var i <- 0
    for i until i >= 10 by 1
        x[i] <- readNumber()
    
    for i until i >= 10 by "Hello"
        y[i] <- readNumber()
    
end
"""
        expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), StringLit(Hello), AssignStmt(ArrayCell(Id(y), [Id(i)]), CallExpr(Id(readNumber), [])))"
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test494(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [a, b, c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test495(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x
    x <- [a, b, [c]]
end
"""
        expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test496(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- (a ... b) ... c
    writeString(x)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test497(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [a, [b, c], [2, 3]]
    writeNumber(a[0] + a[1] + b + c)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test498(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic x <- [a, [b, c], [2, d]]
    d <- x[0, 0] + x[0, 1]
    writeNumber(a[0] + a[1] + b + c + d)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test499(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic x <- [a, [b, c], [d + 20, d ... "Hello"]]
    d <- x[0, 0] + x[0, 1]
    writeNumber(a[0] + a[1] + b + c + d)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(d), StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 499))
    
    def test500(self):
        input = """
func main()
begin
    number arr[2, 2] <- [1, 2, 3, 4]
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 500))