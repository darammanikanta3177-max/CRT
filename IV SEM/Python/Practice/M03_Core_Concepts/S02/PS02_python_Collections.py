'''
a = [1,23,45,23]
print(a)
print(a[1])
print(a[2])

a = [1,2,3]
print(a*2)

a = [1,2,3]
a.append(4)
a.insert(1,7)
print(a)

a = [(1,2,3,4,5)]
print(a)
a.remove(2)
print(a)
a.pop()
print(a)

a = set([1,2,3,4,5])
a.remove(4)
print(a)

a = {1,2,3,4,5}
b = {6,7,8,9,10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
'''
t1 = (1,2,3,4,5)
del t1
