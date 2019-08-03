__author__ = 'Steven Bustos'

import sys
sys.setrecursionlimit( 3*10000 )

"""
Funciones de Notebook de clase
"""

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
       # print 'v = ', v
        if color[v] == 'white':
            count += 1
            DFS_Visit(G, v, color)
    return count

T = int( sys.stdin.readline().strip())
while( T>0 ):
    T-=1
    m,n = map(int, sys.stdin.readline().split(" "))

    G1 = {}
    for i in xrange(n):
        a,b = map(int, sys.stdin.readline().split())
        make_link(G1, a, b)

    c,d = map(int, sys.stdin.readline().split(" "))
    color = {}
    for v in G1:
        color[v] = 'white'

    noInvitados = m-DFS_Visit(G1, c, color)
    print d*noInvitados

