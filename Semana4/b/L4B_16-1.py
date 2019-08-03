__author__ = 'Steven Bustos'
import sys

def binarySearch(n, lista):
    bot = 0
    top = len(lista) - 1
    while bot <= top:
        mid = (bot + top) / 2
        if lista[mid] == n:
            pass
        elif lista[mid] < n :
            bot = mid + 1
        else:
            top = mid - 1
    return bot

T = int(sys.stdin.readline().strip())
while(T > 0):
    T -= 1
    Z = sys.stdin.readline()
    N = sys.stdin.readline()
    M = sys.stdin.readline()

    N = map(int,N.strip("\n").split(" "))
    M = map(int,M.strip("\n").split(" "))
    N.sort()
    X = ""
    Y = []

    for i in N:
        Y.append(i)

    for i in M:
        if i in Y:
            if N.count(i) > 1:
                X += str(len(N)-N[::-1].index(i))+ " "
            else:
                X += str((N.index(i)+1))+ " "
        else:
            X += str(binarySearch(i,N))+ " "

    print X
