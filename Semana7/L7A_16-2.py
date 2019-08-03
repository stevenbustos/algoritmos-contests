__author__ = 'Steven Bustos'
import sys
sys.setrecursionlimit( 3*10000 )

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
        if color[v] == 'white':
            count += 1
            DFS_Visit(G, v, color)
    return count

T = int( sys.stdin.readline().strip())
while( T>0 ):
    T-=1
    N,M = map(int, sys.stdin.readline().split(" "))
    m = [[]*N for i in range(N)]

    for i in xrange(N):
        m[i] = list(sys.stdin.readline().strip())

    movX = [-1, -1, -1, 0, 0, 1, 1, 1]
    movY = [-1, 0, 1, -1 , 1, -1, 0, 1]

    graf = []
    totalNodes = {}
    nodes = {}
    cola = []

    for i in xrange(N):
        for j in xrange(M):
            if m[i][j] == "@":
                pos = M*i+j
                totalNodes[pos] = ""
                cola.append((i,j))
                while cola <> []:
                    ix,jx = cola.pop(0)
                    for k in xrange(len(movX)):
                        px = ix+movX[k]
                        py = jx+movY[k]
                        idx = M*ix+jx
                        idx2 = M*px+py
                        if px >= 0 and py >= 0 and px < N and py < M and m[px][py] == m[ix][jx]:
                            graf.append((idx,idx2))
                            nodes[idx] = ""


    rest = len(totalNodes) - len(nodes)

    G = {}
    for v1 , v2 in graf:
        make_link(G,v1,v2)

    print connected_components(G) + rest