import random


N = 10
A = []

for i in range(N):
    A.append(random.randint(0,100))
# print(A)

def insertion_sort(A):
    for i in range(1,len(A)):
        temp=A[i]
        j=i-1
        while j>=0 and temp<A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=temp
    return A
# print(insertion_sort(A))

import unittest
class TestInsertionSorts(unittest.TestCase):
    def test_sort(self):
        V = [25,100,45,200,67,1,8,91]
        V_o = [1,8,25,45,67,91,100,200]
        insertion_sort(V)
        # print(V, V_o)
        self.assertTrue(V==V_o)
        #return V==V_o


if __name__ == '__main__':
    unittest.main()