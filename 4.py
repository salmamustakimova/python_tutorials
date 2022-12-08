import random


#N = 10
#A = []
#for i in range(N):
  #  A.append(random.randint(0,100))
#print(A)

def merge_two_list(a,b):
    C = []
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            C.append(a[i])
            i+=1
        else:
            C.append(b[j])
            j+=1
    if i<len(a):
        C+=a[i:]
    if j<len(b):
        C+=b[j:] 
    return C       

def merge_sort(A):
    if len(A)==1:
        return A
    middle=len(A)//2
    left=merge_sort(A[:middle])
    right=merge_sort(A[middle:])
    return merge_two_list(left,right)

N = 10
A = []
for i in range(N):
    A.append(random.randint(0,100))
print(A)
print(merge_sort(A))

import unittest
class TestMergeSort(unittest.TestCase):
    def test_mergesort(self):
        F=[90,6,34,2]
        F_o=[2,6,34,90]
        i=merge_sort(F)
        print(F,i)
        self.assertTrue(F_o==i)

if __name__ == '__main__':
    unittest.main()