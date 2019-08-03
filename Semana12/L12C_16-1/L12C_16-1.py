__author__ = 'Steven Bustos'

import sys

def agregateDict(dict, arr, pos, aux):
    if aux not in dict:
        dict[aux] = pos
        arr.append(aux)

def cambio(mon, n):
    dict = {}
    array = []
    dict[0] = 0
    array.append(0)
    while len(array) != 0:
        current = array.pop(0)
        position = dict[current]
        for i in mon:
            aux = current + i
            if aux < n:
                agregateDict(dict, array, position + 1, aux)
            elif aux == n:
                return position+1
    else:
        return -1

T = int(sys.stdin.readline().strip())
while(T>0):
    n,m = map(int, sys.stdin.readline().strip().split(" "))
    l = sys.stdin.readline().strip().split(" ")
    monedas = [int(i) for i in l]
    print cambio(monedas, n)
    T -= 1