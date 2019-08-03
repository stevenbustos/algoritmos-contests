__author__ = 'Steven Bustos'
import sys

def binarySearch(n, lista, bot, top):
    if bot == top:
        respuesta = bot
    else:
        mid = (bot + top) / 2
        if n < lista[mid]:
            respuesta = binarySearch(n, lista, bot, mid)
        elif n > lista[mid]:
            respuesta = binarySearch(n, lista, mid + 1, top)
        else:
            respuesta = mid
    return respuesta

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
    Y = {}

    for i in N:
        Y[i] = ""

    for i in M:
        if i in Y:
            if N.count(i) > 1:
                X += str(len(N)-N[::-1].index(i))+ " "
            else:
                X += str((N.index(i)+1))+ " "
        else:
            X += str(binarySearch(i,N,0,len(N)))+ " "

    print X