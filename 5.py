import random


N = 10
A = []
for i in range(N):
    A.append(random.randint(0,100))
print(A)

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
print(merge_sort(A))
A=merge_sort(A)
n = int(input())
def search(A,n):
    for i in range(len(A)):
        if A[i]==n:
            return i
        # else:
    return -1

print(search(A,n))
