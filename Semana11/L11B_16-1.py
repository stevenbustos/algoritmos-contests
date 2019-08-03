__author__ = 'Steven Bustos'

import sys
import time
sys.setrecursionlimit( 10*10000000 )

def makeTreeM(l,s):
    memo = {}
    def makeTree(l,s):
        if (l,s) in memo:
            return memo[l,s]

        if (l == 1 and s == 2)and (l, s) not in memo:
            memo[l,s] = 12
        if (l == 2 and s == 0)and (l, s) not in memo:
            memo[l,s] = 8
        if (l == 1 and s == 1)and (l, s) not in memo:
            memo[l,s] = 7
        if (l == 0 and s == 3)and (l, s) not in memo:
            memo[l,s] = 4
        if (l == 1 and s == 0) or (l == 0 and s == 2)and (l, s) not in memo:
            memo[l,s] = 3
        """
        if (l==0 and s == 1)and (l, s) not in memo:
            memo[l,s] = 2
        if (l==0 and s == 0)and (l, s) not in memo:
            memo[l,s] = 1
        """
        if (l != 0 and s != 0) and (l, s) not in memo:
            memo[l,s] = 1 + makeTree(l-1, s+1) + makeTree(l, s-1)
        elif l > 0 and (l, s) not in memo:
            memo[l,s] = 1 + makeTree(l-1, s+1)
        elif s > 0 and (l, s) not in memo:
            memo[l,s] = 1 + makeTree(l, s-1)
        return memo[l,s]
    return makeTree(l,s)

T = int(sys.stdin.readline().strip())
while(T>0):
    l,s = map(int, sys.stdin.readline().split(" "))
    t1 = time.clock()
    print makeTreeM(l,s)%9999959999
    t2 = time.clock()
    t3 = t2 - t1
    print t3
    T -= 1

"""
def makeTree(l, s):
    global result
    if l <> 0 and s <> 0:
        makeTree(l-1, s+1)
        makeTree(l, s-1)
        result += 2
    elif l > 0 and (l,s):
        result += 1
        makeTree(l-1, s+1)
    elif s > 0 and (l,s):
        result += 1
        makeTree(l, s-1)
    return

def makeTree(P, l, s):
    if l <> 0 and s <> 0:
        a = l-1
        b = s+1
        P.append((a, b))
        makeTree(P, a, b)
        c = l
        d = s-1
        P.append((c, d))
        makeTree(P, c, d)
    elif l <> 0:
        u = l-1
        v = s+1
        P.append((u, v))
        makeTree(P, u, v)
    elif s <> 0:
        u = l
        v = s-1
        P.append((u, v))
        makeTree(P, u, v)
    return len(P)%9999959999
"""