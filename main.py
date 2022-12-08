import os
import random


def funny_bear(array):
    out = []
    for idx in range(len(array)-1, 0, -1):
        out.append(array[idx])
    return out

def funny_bunny(array):
    out=[]
    for i in range(0, 5):
        out.append(array[i])
    return out



# some = os.listdir('C:/Users/79870')
# some = funny_bear(some)
# some = funny_bunny(some)
# for cur_dir in some:
#     print(cur_dir)
# print('hello')
N = 10
test_array = []
for i in range(N):
    test_array.append(random.randint(0,100))
print(test_array)
for j in range(N-1):
    F=0
    min=j
    for i in range(N-1-j):
        if test_array[i]>test_array[i+1]:
            a = test_array[i]
            test_array[i]=test_array[i+1]
            test_array[i+1]=a
     
            F = 1
            if test_array[i]<test_array[min]:
                i=min
    if F==0:
        break
    if min!=j:
        b = test_array[j]
        test_array[j]=test_array[min]
        test_array[min]=b
print(test_array)   

import unittest
