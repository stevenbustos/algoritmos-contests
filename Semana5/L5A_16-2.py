__author__ = 'Steven Bustos'
import sys
import math
Lines = sys.stdin.readlines()
X = []
for i in Lines:
    X = i.split()
    n = int(X[1])

    if X[0] == "chain":
        print n-1
    elif X[0] == "ring":
        print n
    elif X[0] == "grid":
        print 2*n - 2*int(math.sqrt(n))
    elif X[0] == "complete":
        print n*(n-1)/2
    else:
        pass