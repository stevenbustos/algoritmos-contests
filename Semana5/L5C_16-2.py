__author__ = 'Steven Bustos'
import sys

T = int(sys.stdin.readline())

for i in range(T):
    X = map(int, sys.stdin.readline().split())
    Y = X[0]
    for j in range(len(X)):
        Y += X[j]
    if Y/2 == len(X)-1:
        print 'Arbol'
    else:
        print 'No arbol'