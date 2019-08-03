__author__ = 'Steven Bustos'

import sys
"""
def countingSort(array, maxVal):
    count = [0] * (maxVal+1)
    for x in array:
        count[x] += 1
    i = 0
    for x in xrange((maxVal+1)):
        for y in xrange(count[x]):
            array[i] = x
            i += 1
    return array"""

def countingSort(array, maxVal, alfa):
    count = [0] * maxVal
    for x in array:
        count[alfa[x]] += 1
    i = 0
    for x in xrange(maxVal):
        for y in xrange(count[x]):
            array[i] = alfa[x]
            i += 1
    return array

T = int(sys.stdin.readline().strip())
while (T>0):
    l = sys.stdin.readline().strip().split(" ")
    s = [i for i in sys.stdin.readline().strip()]
    alfa = {}
    for i in enumerate(l):
        alfa[i[1]] = i[0]
        alfa[i[0]] = i[1]
    #print countingSort2(s, max(s), alfa)
    #desString = [alfa[i] for i in s]
    solString = ""
    #for i in countingSort(desString, 26):
        #solString += alfa[i]
    for i in countingSort(s, ord(max(s)), alfa):
        solString += i
    print solString
    T-=1