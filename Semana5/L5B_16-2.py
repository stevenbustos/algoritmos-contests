__author__ = 'Steven Bustos'
import sys

Lines = sys.stdin.readlines()
L = int(Lines[0])
i = 1
while L > 0:
    L -=1
    A = Lines[i].split()
    n = int(A[0])
    p1 = float(A[1])
    p2 = float(A[2])
    p3 = float(A[3])
    i += 1
    even = 0
    odd = 0
    if n%2 == 0:
        even = n/2
        odd = n/2
    else:
        even = (n/2)+1
        odd = n - even
    pp = ((even*(even-1))/2)
    ii = ((odd*(odd-1))/2)
    pi = ((n*(n-1))/2) - (pp + ii)
    edges = pp*p1 + ii*p3 + pi*p2
    print int(edges)