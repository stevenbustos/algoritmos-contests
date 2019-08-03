__author__ = 'Steven Bustos'
import sys
import heapq

def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

T = int(sys.stdin.readline().strip())
for case in xrange(T):
    x1,y1 = map(int, sys.stdin.readline().split(" "))
    Q = int(sys.stdin.readline().strip())
    heap = []
    pos = {}
    result = []
    while(Q>0):
        l = sys.stdin.readline().strip().split(" ")
        if len(l) == 3:
            x2 = int(l[1])
            y2 = int(l[2])
            if (x2,y2) not in pos:
                dis = distance(x1,y1,x2,y2)
                pos[(x2,y2)] = dis
                heapq.heappush(heap, dis)
        else:
            k = int(l[1])
            L = pos.keys()
            L.sort()
            if k-1 < len(heap) and len(heap) <> 0 :
                j = heap[k-1]
                for i in pos:
                    if j in pos.values() and pos[i] == j:
                        print i, j
                        #result.append(i)
                        break
            else:
                result.append(-1)
        Q-=1

    print "Caso #%s:" %(case+1)
    for i in result:
        print i
    T-=1