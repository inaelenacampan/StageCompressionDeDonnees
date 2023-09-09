""" 
Fonctions pour la compression avec les ondelettes Haar
"""

import numpy as np
import math
import images

def create_matrix(n):
    
    """ creation de la matrice de la base de Haar"""
    
    A = np.zeros((n,n))
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ((j <= n/2) and (i == 2*j-1 or i==2*j)):
                A[i-1,j-1] = 1/math.sqrt(2)
            elif ((j > n/2) and (i == 2*(j - n/2) -1 )):
                A[i-1,j-1] = 1/math.sqrt(2)
            elif ((j > n/2) and (i == 2*(j - n/2))):
                A[i-1,j-1] = -1/math.sqrt(2)
            else:
                A[i-1,j-1] = 0
    
    return A

def multiply_matrix(A, M):
    """ multiplication de matrices """
    
    # calcul de la transposee
    At = A.transpose()
    
    # N = (tA)MA
    N = np.matmul(np.matmul(At, M), A)
    
    return N

def remove_small_values(N, e):
    
    # e = precision
    n = N.shape[1]
    
    for i in range(n):
        for j in range(n):
            if(abs(N[i,j]) < e):
                N[i,j] = 0

def new_matrix(N, A):
    
    # inverse de la matrice
    iA = np.linalg.inv(A)
    
    # M' = t(A^(-1))N(A^(-1)
    M  = np.matmul(np.matmul(iA.transpose(), N), iA)
    
    return M

def HaarImageCompression(n, M ,e):
    
    A = create_matrix(n)
    N = multiply_matrix(A, M)
    
    images.generate_image(N)
    
    remove_small_values(N, e)
    
    return new_matrix(N, A)