__author__ = 'Steven Bustos'

import sys

def kbonacci(A, B, n):
    suma = sum(A)
    if suma <= 10**100:
        A.append(suma)
        B.append(suma)
        A.pop(0)
        n += 1
        kbonacci(A, B, n)
    else:
        pass
    return len(B)

T = int(sys.stdin.readline().strip())
while(T>0):
    l = sys.stdin.readline().strip().split(" ")
    A = []
    for i in l:
        A.append(int(i))
    B = A[:]
    n = len(A)
    print kbonacci(A, B, n)
    T -= 1