__author__ = 'Steven Bustos'
import sys

T = int(sys.stdin.readline().strip())
while ( T > 0 ):
    T -= 1
    N = int(sys.stdin.readline().strip())
    m = [[] * N for i in range(N)]

    for i in xrange(N):
        m[i] = list(sys.stdin.readline().strip())

    fila = 0
    fila2 = 0
    columna = 0
    columna2 = 0

    for i in xrange(N):
        countF = 0
        for j in xrange(N):
            if m[i][j] == "#":
                countF = countF + 1
        if countF > fila:
            fila = countF
            fila2 = i + 1

    for i in xrange(N):
        countC = 0
        for j in xrange(N):
            if m[j][i] == "#":
                countC = countC + 1
        if countC > columna:
            columna = countC
            columna2 = i + 1


    print "%s %s" % (fila2, columna2)
