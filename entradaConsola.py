__author__ = 'Estudiante'
import sys

T = int( sys.stdin.readline().strip())
while( T>0 ):
    T-=1
    N = int(sys.stdin.readline().strip())
    m = [[]*N for i in range(N)]

    for i in xrange(N):
        m[i] = list(sys.stdin.readline().strip())
