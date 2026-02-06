import numpy as np
arr =  list(map(int,input("Enter the elements of the array: ").split()))
if len(set(arr))>=3:
    print(sorted(set(arr))[-3])
else:
    print(max(arr))