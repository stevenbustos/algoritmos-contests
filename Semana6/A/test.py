nodos = [7,2]

def sumx(G1):
    G = G1[:]
    reslt = 0
    i = 0
    while i <> len(G) :
        for x in xrange(0,len(G)):
            if i <> x:
                reslt += (G[i] * G[x])
                print G[i], G[x], G[i]*G[x], reslt
        G.pop(0)
    return reslt

def sumx1(G1, P):
    G = G1[:]
    reslt = 0
    i = 0
    sumix = 0
    for x in xrange(len(G)):
        sumix += G[x]
        mult = P - sumix
        reslt += G[x]*mult
    return reslt

#print sumx1(nodos, 11)


