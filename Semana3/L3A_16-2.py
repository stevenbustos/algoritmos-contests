__author__ = 'Steven Bustos'
import sys

def conFormula(n):
    return ((n+1)**3)+(n+2)

T = int(sys.stdin.readline().strip())
while( T>0 ):
    T-=1
    n = int(sys.stdin.readline().strip())
    print conFormula(n)