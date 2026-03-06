'''
n = int(input("Enter a number: "))
l = len(str(n))
res = 0
for i in range(n):
    res+=int(i)**l
print("amstrong number" if res==n else "not an armstrong number")
'''
'''
n = int(input("Enter a number: "))
s = 0
for i in range(1,n//2 + 1):
    if n%i==0:
        s+=i
print("perfect number" if s==n else "not a perfect number")
'''
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) 
n = int(input("Enter a number: "))
print("The factorial of the number is: ",factorial(n))
'''
