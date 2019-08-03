__author__ = 'Steven Bustos'
import sys
import heapq

T = int(sys.stdin.readline().strip())
while(T>0):
    l = sys.stdin.readline().strip().split(" ")
    finalList = []
    eliminarList = []

    for i in l:
        if i != "*":
            heapq.heappush(finalList, -int(i))
        elif i == "*" and finalList == []:
            eliminarList.append(str(-1))

        elif i == "*" :
            b = heapq.heappop(finalList)
            eliminarList.append(str(-b))

    print " ".join(eliminarList)

    T-=1
