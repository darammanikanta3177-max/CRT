'''
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i**2)

print(res)

li = [1,2,3,4,5]
res = []
for i in li:
    if i%2==0:
        res.append(i)
print(res)

print([i for i in li if i%2==0])

li = ['a', 'b','c']
res = ''
for ch in li:
    res+=ch + ' '
print(res)
print(" ".join(li))

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    
n = int(input())
k = 1
for i in range(1,n+1):
    print(" "*(n-i)+" *"*i)
for j in range(n-1,0,-1):
    print(" "*(n-j)+" *"*j)
    
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
for i in range(1,n+1):
    print(" "*(n-i)+" ".join(str(k) for k in range(1,i+1)))
'''