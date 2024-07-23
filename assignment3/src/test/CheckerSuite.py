import unittest
from TestUtils import TestChecker
from AST import *

"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 15/4/2024
"""

class CheckerSuite(unittest.TestCase):
    # def test_fail(self):
    #     input = """
    #         dynamic x
    #         number a[2] <- [[x],[x,x]]
    #         func main() return
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0], NumberType), None, ArrayLit(ArrayLit(Id(x)), ArrayLit(Id(x), Id(x))))"
    #     self.assertTrue(TestChecker.test(input, expect, 1001)) 
    # def test_fail1(self):
    #     input = """
    # func main() begin
    #     dynamic x
    #     dynamic y
    #     number a[3, 1, 2] <- [[x,[x,x]], y]
    # end

    #         """
    #     expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 1002))   
    # def test_fail2(self):
        
    #     input = """
    # func main() begin
    #     dynamic x
    #     dynamic y
    #     number a[3, 1, 2] <- [[y,[x,x]], y]
    # end

    #         """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), ArrayLit(Id(x), Id(x))), Id(y))"
    #     self.assertTrue(TestChecker.test(input, expect, 1003))  
    # def test_fail3(self):
        
    #     input = """
    # func main() begin
    #     dynamic x
    #     dynamic y
    #     number a[3, 1, 2] <- [[x], [[x]]]
    # end

    #         """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x)), ArrayLit(ArrayLit(Id(x))))"
    #     self.assertTrue(TestChecker.test(input, expect, 1004)) 
        
        
          
    def test_ok(self):
        input = """
func main()
            begin
                dynamic num
                bool arr <- num and (num > num)
            end
"""
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 401))
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
        self.assertTrue(TestChecker.test(input, expect, 401))
        
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
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
func foo()
begin
      number a <- 3
end
func foo()
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
func main()
func foo()
begin
number a <- main()
end
func main() return 
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 401))
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
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
dynamic a
string x[1] <- [a]
func main() return
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
func main() return
func aaa()
begin
dynamic a
a <- [[1, 2], [3, true]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(3.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
func main()
begin
    number a[1, 2, 3, 4]
    var b <- a[0]
    number c[2, 3, 4]
    b <- c
    number d[1, 3, 4]
    b <- d
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 491))
        input = """
func foo(number a)

func main()
begin
    number a <- foo(1)
    return
end

func foo(number a)
begin
    return
end
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 410))
        input = """

func foo(number a[2,2]) return  1
        
func main()
begin
    dynamic x
    return foo([[x,x], [x,x]])
    
    dynamic y
    return foo([[y,y], [y]])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y)), ArrayLit(Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 500))
        input = """
            dynamic a
            number x
            func foo() return
            func main() begin
                var y <- a+foo(x)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 30))
        input = """
func main()
begin
    number a[2,2]
    dynamic x
    a <- [x,x]
    x <- [1,2]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
        
    def test_sai(self):
        input = """
func f(number x, number x)
func f(number x, number y) begin
return x + y
end
func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
func foo(number a)
func main()
begin
dynamic x
foo([x])
end                                
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
func foo(number a)
func main()
begin
dynamic x
var y <- foo([x])
end                                  
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, CallExpr(Id(foo), [ArrayLit(Id(x))]))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
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
        self.assertTrue(TestChecker.test(input, expect, 401))
        
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
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        
        input = """
dynamic a <- [1,2,3]

func main() begin
number i
a[i] <- [1,2]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [Id(i)]), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
dynamic x
number a[2,2] <- [x,[x,x]]
func main() return
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
func foo() begin
     number a
     if (true) number a
end
func main() return
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
func foo(number x, string y)
func foo(number x, number x) return
func main()
begin
end
"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
func main()
begin
dynamic a
var x <- a[0]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        input = """
dynamic a
string x <- [a]
func main() return
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
#         input = """
# func main() return
# func aaa()
# begin
# dynamic a
# number b<- a[0]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))
        
        
        input = """
            func main() return
            func aaa(number a, bool b)
            begin
            number b
            end
            
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_430(self):
        input = """
        dynamic x
        dynamic y
        var a <-[x and x,x+y]
        func main()
        func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_431(self):
        input = """
        func foo(number x)
        func main()
        func main() 
        begin
        number a[2,1] <- [foo(1), [foo(2)]]
        end
        func foo(number z) return [1]
        """
        expect = "Type Mismatch In Expression: ArrayLit(CallExpr(Id(foo), [NumLit(1.0)]), ArrayLit(CallExpr(Id(foo), [NumLit(2.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_531(self):
        input = """
        func foo(number x)
        func main()
        func main() 
        begin
        number a[2,1] <- [foo(1), foo(2)]
        end
        func foo(number z) return [[1]]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(NumLit(1.0))))"
        self.assertTrue(TestChecker.test(input, expect, 531))
        
    def test_duy(self):
        input = """

func foo(number a[2,2]) return  1
        
func main()
begin
    dynamic x
    return foo([[x,x], [x,x]])
    
    dynamic y
    return foo([[y,y], [y]])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y)), ArrayLit(Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 500))
        
        input = """
            dynamic x
            number a[2,2] <- [x,[x,x]]
            func main() return
        """    
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 900))
        
        input = """
 func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 1401))
        input = """
func main()
begin
dynamic a
var x <- a[0]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
func main()
begin
dynamic a
var x <- a[0]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
#         input = """
# func main()
# begin
# dynamic a
# number x <- a[0]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_Votien_0(self):
        input = """
            func main()
            begin
                dynamic x
                number a[1,1] <- [[x[1]]]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([1.0, 1.0], NumberType), None, ArrayLit(ArrayLit(ArrayCell(Id(x), [NumLit(1.0)]))))"
        self.assertTrue(TestChecker.test(input, expect, 100))
 
        input = """
            dynamic x
            number a[2,2] <- [x,[x,x]]
            func main() return
        """    
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 900))

        input = """
            dynamic x
            number a[2,2] <- [[x], [[x]]]
            func main() return
        """    
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x)), ArrayLit(ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 900))
        
            
        input = """
            func main() begin
                dynamic x
                x <- (x=1) or ("abc" == "abc")
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 902))    
    
    
    def test_Votien_01(self):
        input = """
            func main()
            begin
                dynamic x
                number a[1,1] <- [[x[1]]]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([1.0, 1.0], NumberType), None, ArrayLit(ArrayLit(ArrayCell(Id(x), [NumLit(1.0)]))))"
        self.assertTrue(TestChecker.test(input, expect, 100))


    def test_Votien_1(self):
        input = """
            func foo(number a, string a)
            func foo(number a, string a) return 
            func main() return
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_Votien_2(self):
        input = """
            func foo(number a, string a)
            func foo(number a) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 102))



    def test_Votien_3(self):
        input = """
            func foo(number a[1,2,3])
            func foo(number a[1,2]) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 103))


    def test_Votien_4(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                number b
                if (true) number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 104))
        
    def test_Votien_5(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                else number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_Votien_6(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                
                for b until true by 1
                    number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 106))
        
    def test_Votien_7(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true)
                begin
                    number a
                end
                
                begin
                    number a
                end
                
                for a until true by 1
                begin
                    number a
                end
            end
            func main() 
            begin
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 107))        


    def test_Votien_8(self):
        input = """
            func main() 
            begin
                dynamic x
                if ([x]) x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(x)), AssignStmt(Id(x), NumLit(1.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 108)) 
        
    def test_Votien_9(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until y[1] by 1
                    return
            end
        """
        expect = "Type Cannot Be Inferred: For(Id(x), ArrayCell(Id(y), [NumLit(1.0)]), NumLit(1.0), Return())"
        self.assertTrue(TestChecker.test(input, expect, 109)) 
        
    def test_Votien_10(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 110)) 
               

    def test_Votien_11(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 111)) 
               
    def test_Votien_12(self):
        input = """
            func main() 
            begin
                dynamic x
                return x[1]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayCell(Id(x), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 112))   
        
    def test_Votien_13(self):
        input = """
            func main() 
            begin
                dynamic x
                return [x, [x, x]]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 113))                

    def test_Votien_13(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                number a <- 1 + foo([[x]])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(x)))])))"
        self.assertTrue(TestChecker.test(input, expect, 113)) 
                       
    def test_Votien_14(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                dynamic y
                var a <- [x, [[1,2]], [[y, 1]]]
                x <- [[0,0]]
                y <- x[0,0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 114)) 


    def test_Votien_15(self):
        input = """
            func foo(number a) return
            func main() 
            begin
                return foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 115)) 
        
    def test_Votien_16(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                var a <- 1 * 2 + 3 * foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(+, BinaryOp(*, NumLit(1.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]))))"
        self.assertTrue(TestChecker.test(input, expect, 116)) 

    def test_Votien_17(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        self.assertTrue(TestChecker.test(input, expect, 117)) 

    def test_Votien_18(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        self.assertTrue(TestChecker.test(input, expect, 118))    
        
    def test_Votien_19(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 119))     
        
    def test_Votien_20(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 120))     
        
        
    def test_Votien_21(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 121))   
        
        
    def test_Votien_22(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 122))   
        
    def test_Votien_23(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 123))   
        
    def test_Votien_24(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a[1,1,1,1] <- [[[[x]]]]
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 124))  
        
    def test_Votien_25(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a <- 1 + [[[[x]]]]
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x)))))))"
        self.assertTrue(TestChecker.test(input, expect, 125))  
                       
    def test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_2_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_3_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
        
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_3_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 428))

        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
        
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
        
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_4_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_5_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
       
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
        
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    
        
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
        
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
        
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

        input = """
            func main()begin
                dynamic a
                if (a) return
                elif (a)  return
                else return
                
                if(true) return
                elif (1) return
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), Return()), [(NumLit(1.0), Return())], None)"
        self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   
        
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
        
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  

    def test_6_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        

        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
        
        input = """
            func VoTien()
            func main() begin
                number VoTien_ <- VoTien()
            end
            func VoTien() begin
            end
        """
        # expect = "???"
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 477))

        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_7_full(self):
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
        self.assertTrue(TestChecker.test(input, expect, 499))
        
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
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
        self.assertTrue(TestChecker.test(input, expect, 499))
        
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 499))
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))    \
            
        input = """
            func a()
            func a() return 1
            func main() begin 
                a()
            end
             
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_arraylit(self):
        
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))        
        
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 502))        
        
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))     
        

        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))   
        
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 502))   
        
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 502))  
        
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 502))  

        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 502))    
        
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 502))     
        
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))     
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))  
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 502)) 
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 502)) 
        
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502)) 
        
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502)) 
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502)) 
  
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 501)) 

        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        input = """
            func main() begin
                dynamic x
                number a <- 1 + x[1,3]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayCell(Id(x), [NumLit(1.0), NumLit(3.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        input = """
            func main() begin
                dynamic x
                number a <- 1 + [x]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 501)) 

        input = """
            func main() begin
                dynamic x
                number a <- 1 + [x,1]
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), ArrayLit(Id(x), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
        
    def test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))   

        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))   

        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 406))       
        
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))     
        
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406)) 

        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
                
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        

    def test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 407)) 
        

        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 407))      
        
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 407)) 
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 407))




    
    def test_no_entry_point(self):
        input = """
            number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

        input = """
            number a
            func VoTien() begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
        input = """
            number a
            func main(number a) begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
        input = """
            number a
            func main(number a, number c[1]) begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
        input = """
            number main
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))


        input = """
            number a
            func main() begin 
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_Break_Continue_in_loop(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    break
                    continue
                    for i until true by 1
                    begin
                        for i until true by 1
                        begin
                            break
                            continue
                        end
                        break
                        continue
                    end
                        break
                        continue
                    begin
                        break
                        continue
                    end
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    number i
                end
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 403))    
        
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    begin
                        number i
                    end
                end
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 403))   
        
    def test_no_definition_for_a_funtion_And_Redeclared(self):
        input = """
            func a()
            func main() begin 
            end
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

        input = """
            func a()
            
            func a(number c) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    

        input = """
            func a(number c)
            
            func a(number d) begin 
            end
            func main() begin 
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))  
                
        input = """
            func a(number c)
            
            func a() begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    
        
        input = """
            func a(number c)
            
            func a(string a) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    
        
        input = """
            func a() begin 
            end
            func a()
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    

        input = """
            func a()
            func a(string c)
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
                
        input = """
            func a() begin 
            end
            func a() begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    
        
        input = """
            func a(number a) begin 
            end
            func a(string c) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    

        input = """
            func a() begin 
            end
            func a()
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))    
        
                
        input = """
            func a(number a) begin 
            end
            func a(string c)
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401))  
        
        input = """
            number a
            func main() begin 
            end
            func a(string c)

        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 401))  
        
        input = """
            func a(string c) return
            func main() begin 
            end
            number a

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        input = """
            string a
            func main() begin 
            end
            number a
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        input = """
            func a(number a, number c, string a)
            func main() begin 
            end
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        input = """
            func a(number a, number c, string a)
            func main() begin 
            end
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number a[3]) begin
            end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401)) 

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number writeString
                number c
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401)) 
                

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                string e
            end
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
               

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                number k
                string e
            end
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
               
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number a
                    number e
                    number k
                    string k
                end
            end
        """
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
               
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number e
                    number z
                    begin
                        number e
                    end
                    number z
                end
            end
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
        
        # check Type array
        input = """
            func a(number a[1,3,4])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 

        input = """
            func a(number a[1,3])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
                             
        input = """
            func a(number a[1,3,2,4])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
                             
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(string a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 401)) 

        input = """
            number readNumber
            func main() begin 
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))              

        input = """
            func readNumber()
            func main() begin 
            end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 401))    

        input = """
            func readNumber() begin
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 401))          

        input = """
            func writeString()
            func main() begin 
            end
        """
        expect = "Redeclared Function: writeString"
        self.assertTrue(TestChecker.test(input, expect, 401))    

        input = """
            func writeString() begin
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: writeString"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
        
                
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401)) 

    def test_Undeclared(self):
     

        input = """
            number a <- a
            number b <- b
            var d <- z
            func main() begin 
            end
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 404))   
        
        input = """
            number a
            number b
            var c <- d
            func main() begin 
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 404))  
        
        input = """
            number a
            number b
            number c <- a
            func main() begin 
                string c <- c
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))    
    
        input = """
            number a
            number b
            var c <- a
            func main() begin 
                var c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 404))   
        
        input = """
            number a
            number b
            var c <- a
            func main(number k, number j) begin 
                var x <- k
                var y <- c
                var c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 404))  
        
        input = """
            number a
            number b
            var c <- a
            func main(number k, number j) begin 
                number z <- z
                begin
                    var c <- a
                    var b <- x
                end
            end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 404))  
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- a()
                var d <- b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 404))  
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 404)) 
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- k()
            end
        """
        expect = "Undeclared Function: k"
        self.assertTrue(TestChecker.test(input, expect, 404)) 

        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                number a
                var c <- a()
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404)) 

        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                number a <- a()
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404)) 
        
        
                
        input = """
            func a()
                return
            func main(number k, number j) begin 
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 404)) 
        
        input = """
            func a() begin
                a()
                main()
            end
            func main() begin 

            end
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 404)) 
        
        input = """
            func a()
            func main() begin 
                a()
                writeNumber(1.1)
                writeString("string")
                writeBool(true)
                var a <- readNumber()
                var b <- readString()
                var c <- readBool()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404)) 
           
    def test_For_if(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))   
        
        input = """
            func main() begin 
                string i
                for i until true by 1
                begin
                end
            end
        """
        expect = "Type Mismatch In Statement: For(Id(i), BooleanLit(True), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 405))   
        
        input = """
            func main() begin 
                string i
                for i until true by 1
                begin
                end
            end
        """
        expect = "Type Mismatch In Statement: For(Id(i), BooleanLit(True), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 405))   
        
        input = """
            func main() begin 
                dynamic i
                for i until true by 1
                begin
                    number i
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))  
        
        input = """
            func main() begin 
                number i
                for i until 1 by 1
                begin
                end
            end
        """
        expect = "Type Mismatch In Statement: For(Id(i), NumLit(1.0), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 405))    
        
        input = """
            func main() begin 
                number i
                dynamic j
                for i until j by 1
                begin
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))   
        
        input = """
            func main() begin 
                number i
                dynamic j
                for i until true by "1"
                begin
                end
            end
        """
        expect = "Type Mismatch In Statement: For(Id(i), BooleanLit(True), StringLit(1), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 405))  
        
        input = """
            func main() begin 
                number i
                dynamic j
                for i until true by j
                begin
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))   
        
        
        input = """
            func main() begin 
                bool i
                dynamic j
                
                if (i) return
                
                if (i)
                    if (i) return
                    else return
                elif (i) return
                elif (true) return
                elif (false) return
                else begin
                    number i
                end
                
                if (i) return
                else return     
                
                
                if (i) begin
                    number i
                end
                elif (i) begin
                    number i
                end
                elif (true) begin
                    number i
                end
                elif (false) return       

            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))        
        
        input = """
            func main() begin 
                number i
                dynamic j
                
                if (i) return
                elif (true) return
                elif (true) return
                elif (false) return
                else return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(i), Return()), [(BooleanLit(True), Return()), (BooleanLit(True), Return()), (BooleanLit(False), Return())], Return())"
        self.assertTrue(TestChecker.test(input, expect, 405))        
                
        input = """
            func main() begin 
                string i
                dynamic j
                
                if (true) return
                elif (true) return
                elif (i) return
                elif (false) return
                else return
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), Return()), [(BooleanLit(True), Return()), (Id(i), Return()), (BooleanLit(False), Return())], Return())"
        self.assertTrue(TestChecker.test(input, expect, 405))        
                        
        input = """
            func main() begin 
                number i
                dynamic j
                
                if (j) return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))        
                        
        input = """
            func main() begin 
                number i
                dynamic j
                
                if (true) return
                elif (j) return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))        
               
        input = """
            func main() begin 
                number i
                dynamic j
                
                if (true) return
                elif (false) return
                elif (j) return
                else return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))                 
        
    def test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))   

        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))   

        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 406))       
        
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))    
        
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 406))   
        
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))     
        
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406)) 

        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        
                
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
        

    def test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 407)) 
        

        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 407))      
        
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))   
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 407)) 
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_VarDecl(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 408)) 

        input = """
            func foo()
            func main() begin 
                number a
                dynamic b <- a
                var c <- b
                dynamic d
                number k <- d
                d <- foo()
            end
            func foo()
                return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408)) 
        
        input = """
            number a <- a
            func main() begin 
                string a <- a
                begin
                    dynamic b <- a
                    string a <- b
                    begin
                        number a <- b
                    end
                end
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 408)) 
        
        input = """
            var a <- a
            func main() begin 
                
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 408)) 
        
        input = """
            dynamic a <- a
            func main() begin 
                
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 408)) 
        
        
    def test_TypeMismatchInExpression(self):
        input = """
            func main() begin 
                var c <- 1 + 1
                var d <- c + 2
                d <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))  
        
        input = """
            func main() begin 
                dynamic a
                dynamic b <- a + 1
                dynamic c
                dynamic d 
                dynamic e <- c * d
                return a
                return b
                return c
                return d
                return e
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
        input = """
            func main() begin 
                string a
                dynamic b <- a / 1
            end
        """
        
        expect = "Type Mismatch In Expression: BinaryOp(/, Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 409))  
        
        input = """
            func main() begin 
                dynamic a
                dynamic b <- true - a
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(-, BooleanLit(True), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        input = """
            func main() begin 
                dynamic a
                dynamic b <- "a" - true
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(-, StringLit(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 409))  
        
        input = """
            func main() begin 
                begin
                    dynamic a
                    var c <- a = 1
                    a <- 3
                end
                begin
                    dynamic a
                    var c <- 1 <= a
                    a <- 2
                end
                begin
                    dynamic a
                    var c <- 1 < a
                    a <- 1
                end
                begin
                    dynamic a
                    dynamic b
                    var c <- b > a
                    a <- 1
                    b <- 2
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        input = """
            func main() begin 
                begin
                    dynamic a
                    var c <- a = true
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        input = """
            func main() begin 
                begin
                    dynamic a
                    var c <- a <= a
                    c <- a <= true
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=, Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        
        input = """
            func main() begin 
                begin
                    var a <- "s"
                    var c <- a = a
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))                 
    

        input = """
            func main() begin 
                begin
                    dynamic a
                    var c <- a and false
                    a <- true
                end
                begin
                    dynamic a
                    var c <- true or a
                    a <- true
                end
                begin
                    dynamic a
                    var c <- a or a
                    a <- true
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        input = """
            func main() begin 
                begin
                    var a <- "s"
                    var c <- a or a
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, Id(a), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))   
        
        input = """
            func main() begin 
                begin
                dynamic a 
                    var c <- 1 or a
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, NumLit(1.0), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))   
        
        input = """
            func main() begin 
                begin
                dynamic a 
                    var c <-  a and 1
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 409))       
        
        input = """
            func main() begin 
                begin
                    dynamic a 
                    var b <- "a" ... "B"
                    var c <-  a ... b
                    a <- "1"
                end
                begin
                    dynamic a 
                    var b <- "a" ... "B"
                    var c <-  b ... a
                    a <- "1"
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))               

        input = """
            func main() begin 
                begin
                    dynamic a 
                    var b <- 1 ... "B"
                    var c <-  a ... b
                    a <- "1"
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., NumLit(1.0), StringLit(B))"
        self.assertTrue(TestChecker.test(input, expect, 409))    
        
        input = """
            func main() begin 
                begin
                    dynamic a 
                    var b <- 1 ... a
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., NumLit(1.0), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))   
        
        input = """
            func main() begin 
                begin
                    dynamic a 
                    var b <- -a
                    a <- 1
                    b <- 2
                end
                begin
                    dynamic a 
                    var b <- not a
                    a <- false
                    b <- true
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409)) 
        
        input = """
            func main() begin 
                begin
                    dynamic a <- "a"
                    var c <- -1
                    var b <- -a
                end
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))  
        
        input = """
            func main() begin 
                begin
                    dynamic a <- 1
                    var c <- not true
                    var b <- not a
                end
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))              

        input = """
            func main() begin 
                begin
                    dynamic a <- [[1], [2], [1+"a"]]
                end
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))              
        

    def test_call(self):
        input = """
            func a() return
            func a1(number a) return
            func a2(number b, string c[2]) return
            func main() begin 
                a()
                a1(1)
                a2(1, ["1", "2"])
                writeNumber(1)
                writeBool(true)
                writeString("a")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))  

        input = """
            func a() return
            func a1(number a) return
            func a2(number b, string c[2]) return
            func main() begin 
                dynamic v
                a1(v)
                v <- 1       
                dynamic x   
                dynamic y
                 a2(x, y)
                 x <- 1
                 y <- ["a", "C"]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))  

        input = """
            func a() return
            func a1(number a) return
            func a2(number b, string c[2]) return
            func main() begin 
                a1()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a1), [])"
        self.assertTrue(TestChecker.test(input, expect, 410))  
    
        input = """
            func a() return
            func a1(number a) return
            func a2(number b, string c[2]) return
            func main() begin 
                a1("a")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a1), [StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a() return
            func a1(number a) return
            func a2(number b, string c[2]) return
            func main() begin 
                a1(1, 2)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a1), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a() begin
            end
            func a1(number a) return [1,2]
            func a2(number b, string c[2]) return
            func main() begin 
                a()
                a1(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a1), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))    \
            
        input = """
            func a()
            func a() return 1
            func main() begin 
                a()
            end
             
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func a() return 1
            func a1(number a) return 3 
            func a2(number b, string c[2]) return 2
            func main() begin 
                var c <- a1(1) + a2(1, ["a", "b"]) + a()
                number x <- readNumber()
                bool y <- readBool()
                string z <- readString()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a() return 1
            func a1(number a) return 2
            func a2(number b, string c[2]) return 3
            func main() begin 
            
    
                dynamic v
                return a1(v)
                v <- 1       
                dynamic x   
                dynamic y
                return a2(x, y)
                 x <- 1
                 y <- ["a", "C"]
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a()
            func main() begin 
                number c <- a()
            end
            func a() return
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 410))  
        
        input = """
            func a(number a)
            func main() begin 
                number c[2] <- a(1)
            end
            func a(number c) return [1,2]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func a(number a)
            func main() begin 
                number c[2] <- a()
            end
            func a(number c) return [1,2]
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func a(number a)
            func main() begin 
                number c[2] <- a("1")
            end
            func a(number c) return [1,2]
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func a(number a) return
            func main() begin 
                number c[2] <- a(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func main() begin 
                number a[1, 2, 3, 4]
                number b
                var d <- a[1,2]
                var e <- a[1,2, 4, 5]
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func main() begin 
                number a[1, 2, 3, 4]
                number b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func main() begin 
                number a[1, 2, 3, 4]
                dynamic b
                var c <- a[b]
                b <- 1
                c <- a[1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
            func main() begin 
                number a[1,2,3,4]
                var c <- a[1]
                number b[2,3,4]
                c <- b
                 number d[1,3,4]
                 c <- d
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
        
        input = """
func test(number x)

func main()
begin
    number test
    begin
        number x <- test(2018) + 1
    end
end
"""
        expect = "No Function Definition: test"
        self.assertTrue(TestChecker.test(input, expect, 489))
        
        input = """
func main()
begin
    string x
    begin
        number x <- (10 + x) * 2
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
        

        
        input = """
func main()
begin
    number a[2,2]
    dynamic x
    a <- [x,x]
    x <- [1,2]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
