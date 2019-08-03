__author__ = 'Steven Bustos'
import sys

# Funcion DFS Visit
def DFS_Visit(G, node, color):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            total_marked += DFS_Visit(G, neighbor, color)
    color[node] = 'black'
    return total_marked

# Funcion para hacer un link
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def connected_components(G):
    color = {}
    for v in G:
        color[v] = 'white'
    count = 0
    for v in G:
        #print 'v = ', v
        if color[v] == 'white':
            count += 1
            DFS_Visit(G, v, color)
    return count

# Funcion que suma las multiplicaciones de los elementos de un arreglo
def sumx(G1):
    G = G1[:]
    reslt = 0
    i = 0
    while i <> len(G) :
        for x in xrange(0,len(G)):
            if i <> x:
                reslt += (G[i] * G[x])
                #print G[i], G[x], G[i]*G[x], reslt
        G.pop(0)
    return reslt
"""
edges1 = [(0, 2), (1, 8), (1, 4), (2, 8),
           (2, 6), (3, 5), (6, 9) ]

G3 = {}
for v1, v2 in edges1:
    make_link(G3, v1, v2)

print connected_components(G3)
"""
G1 = {}
N,M = map(int, sys.stdin.readline().split(" "))
for i in xrange(M):
    a,b = map(int, sys.stdin.readline().split())
    make_link(G1, a, b)

color = {}
for v in G1:
    color[v] = 'white'

numeroNodos = {}
for n in G1:
    numeroNodos[n] = DFS_Visit(G1, n, color)
#print numeroNodos

#nodos = [7, 2, 1, 1]
nodos = []

def sumd(G):
    suma = 0
    for i in G.values():
        if i <> 1:
            suma += i
    return suma

p = N - sumd(numeroNodos)

for i in numeroNodos.values():
    if i <> 1:
        nodos.append(i)

for j in xrange(p):
    nodos.append(1)

#print nodos
print sumx(nodos)

