__author__ = 'Steven Bustos'

import sys

def countingSort(array, maxVal):
    m = maxVal + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in xrange(m):
        for c in xrange(count[a]):
            array[i] = a
            i += 1
    return array

T = int(sys.stdin.readline().strip())
while (T>0):
    n = int(sys.stdin.readline().strip())
    l = map(int, sys.stdin.readline().strip().split(" "))
    maxim = max(l)
    sol = countingSort(l,maxim)
    solution = []
    for i in reversed(sol):
        if i not in solution:
            solution.append(i)
        else:
            pass
    solString = ""
    #print solution
    for i in solution:
        solString += str(i) + " "
    print solString
    T-=1