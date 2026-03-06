'''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        '''
'''
n = int(input("Enter a number: "))
if n>=0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1*int(str(n)[::-1])) 
    '''
n = int(input("Enter a number: "))
