__author__ = 'Steven Bustos'
import sys

def mtxMult(matrixA, matrixB):
    a_11 = (matrixA[0][0] * matrixB[0][0]) + (matrixA[0][1] * matrixB[1][0])
    a_12 = (matrixA[0][0] * matrixB[0][1]) + (matrixA[0][1] * matrixB[1][1])
    b_21 = (matrixA[1][0] * matrixB[0][0]) + (matrixA[1][1] * matrixB[1][0])
    b_22 = (matrixA[1][0] * matrixB[0][1]) + (matrixA[1][1] * matrixB[1][1])
    fila1 = [a_11, a_12]
    fila2 = [b_21, b_22]
    return [fila1, fila2]

def iteracionesN(n, matrix):
    if n == 0:
        return 0
    if n == 2:
       return mtxMult(matrix, matrix)
    elif n == 1:
        return matrix
    elif n == 0:
        return 0
    elif n % 2 == 0:
        aux = iteracionesN(n / 2, matrix)
        return mtxMult(aux, aux)
    else:
        a1 = iteracionesN((n - 1) / 2, matrix)
        aux = mtxMult(a1, a1)
        return mtxMult(matrix, aux)


T = int(sys.stdin.readline().strip())
while(T > 0):
    T -= 1
    n = int( sys.stdin.readline().strip() )
    fila1 = map( int, sys.stdin.readline().strip().split(" ") )
    fila2 = map( int, sys.stdin.readline().strip().split(" ") )

    matrix = [ fila1, fila2 ]
    matrixFinal = iteracionesN(n, matrix)

    res1 = str(matrixFinal[0][0])+" "+str(matrixFinal[0][1])
    res2 = str(matrixFinal[1][0])+" "+str(matrixFinal[1][1])
    print res1
    print res2
    print " "