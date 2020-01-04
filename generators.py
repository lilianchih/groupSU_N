from sympy import sqrt, Rational, zeros, I, pprint
from copy import deepcopy

N = 7;

def Lambda(N):
    set = []
    #symmetric
    for j in range(N-1):
        for k in range(j+1, N):
            matrix = zeros(N, N)
            matrix[j, k] = 1
            matrix[k, j] = 1
            set.append(deepcopy(matrix))
    #antisymmetric
    for j in range(N-1):
        for k in range(j+1, N):
            matrix = zeros(N, N)
            matrix[j, k] = -I
            matrix[k, j] = I
            set.append(deepcopy(matrix))
    #diagonal, traceless
    for l in range(N-1):
        matrix = zeros(N, N)
        for j in range(l+1):
            matrix[j, j] = 1
        matrix[l+1, l+1] = -(l+1)
        matrix *= sqrt(Rational(2, (l+1)*(l+2)))
        set.append(deepcopy(matrix))
    return set

g = Lambda(N)

for i in range(len(g)):
    pprint(g[i])