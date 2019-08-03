__author__ = 'Steven Bustos'
import sys

def misterio1( n ):
    c = 4
    s = 0
    i = 1
    while ( i < n ):
        c += 1
        j = i
        c += 1
        while ( j <= n ):
            c += 1
            k = 2
            c += 1
            while ( k <= j ):
                c += 1
                s += 2
                c += 1
                k += 1
                c += 1
            c += 1
            j += 1
            c += 1
        c += 1
        i += 1
        c += 1
    return c

def misterio2(n):
    c = 4
    x = 1
    i = 0
    while i < n*n:
        c += 1
        i += 1
        c += 1
        x = x*2
        c += 1
    return c

T = int(sys.stdin.readline().strip())
while(T > 0):
    T -= 1
    m,n = map(int, sys.stdin.readline().split())
    if m == 1:
        print misterio1(n)
    elif m == 2:
        print misterio2(n)