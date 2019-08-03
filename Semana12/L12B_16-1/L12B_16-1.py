__author__ = 'Steven Bustos'

import sys

def lcsDP2(a, b):
    distance = 0
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
                if lengths[i+1][j+1] > distance:
                    distance =lengths[i+1][j+1]
            else:
                lengths[i+1][j+1] = 0
    return distance

T = int(sys.stdin.readline().strip())
while(T>0):
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print lcsDP2(str1, str2)
    T -= 1
