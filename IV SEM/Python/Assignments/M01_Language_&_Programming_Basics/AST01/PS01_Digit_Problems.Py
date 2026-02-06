n = int(input("Enter a number: "))
sum = 0
if n>0:
    sum+=n%10
    n//=10
print("The sum of the digits is: ",sum)