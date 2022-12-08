import random

N = 10
A = []

for i in range(N):
    A.append(random.randint(0,100))
#print(A)

def sort_choice(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]
    return A
#print(sort_choice(A))

import unittest

class TestSortChoice(unittest.TestCase):
    def test_sort_choice(self):
        B=[20,17,1,64]
        B_o=[1,17,20,64]
        sort_choice(B)
        self.assertTrue(B==B_o)

if __name__ == '__main__':
    unittest.main()
    