
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()


n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()
    
n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
    
k=1
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()
    
k=65
n = int(input())
for i in range(0,n):
    for j in range(i+1):
        print(chr(k),end=' ')
        k+=1
    print()

HALLOW SHAPE:
n = int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j ==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
n = int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()