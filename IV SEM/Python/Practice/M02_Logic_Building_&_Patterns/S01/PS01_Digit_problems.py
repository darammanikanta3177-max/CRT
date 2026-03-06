'''
n = int(input("Enter a number: "))
sum = 0
if n>0:
    sum+=n%10
    n//=10
print("The sum of the digits is: ",sum)
'''
'''
n = int(input("Enter a number: "))  
ev = 0
od = 0
while n>0:
    if n%10%2==0:
        ev+=1
    else:
        od+=1
    n//=10
print("Number of even digits is: ",ev)
print("Number of odd digits is: ",od)
'''
'''
n = int(input("Enter a number: "))
lar = 0
while n>0:
    if n%10>lar:
        lar = n%10
    n//=10
print(lar)
'''