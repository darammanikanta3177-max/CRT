''' Debugging in python
bug--> Errors
Debugging--> finding and fixing errors
Types of errors
types of errors
1. syntax errors --> missing of colon snd indentation
2.logical errors--> missing of logic
3.runtime errors-->division by zero
debugging techniques
1.print()
2.try-except
3.using pdb-->python debugger
        purpose-->1)to execute code line by line
                 2)to check variable values at different stages
                 3)pause the execution point
pdb commands
1.n-->to execute the output in a next line
2.p variable--> to get the value of a variable 
3.I--> list nearby code
4.c--> continue execution
5.s--> step into function
6.r-->return from function
7.h--> help
8.q--> quit the execution

try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid input.")
    '''
import pdb
def add(a,b):
    pdb.set_trace() #setting a breakpoint
    return a+b
a=int(input("Enter first number: "))    
b=int(input("Enter second number: "))
print(add(a,b))