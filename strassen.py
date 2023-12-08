import numpy as np


def strassen(A, B):
    n = A.size
    C = np.zeros_like(A)
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
        return C
    n_sub = int(n/2)-1
    A11 = A[:n_sub,:n_sub]
    A12 = A[:n_sub,n_sub:n]
    A21 = A[n_sub:n,:n_sub]
    A22 = A[n_sub:n,n_sub:n]
    B11 = B[:n_sub,:n_sub]
    B12 = B[:n_sub,n_sub:n]
    B21 = B[n_sub:n,:n_sub]
    B22 = B[n_sub:n,n_sub:n]
    C11 = C[:n_sub,:n_sub]
    C12 = C[:n_sub,n_sub:n]
    C21 = C[n_sub:n,:n_sub]
    C22 = C[n_sub:n,n_sub:n]
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    C = np.concatenate([np.concatenate([C11, C12], axis=1),np.concatenate([C21, C22],axis=1)], axis=0)
    return C


mat1 = np.array([[1, 4], [3, 1]])
mat2 = np.array([[4, 3], [-1, 0]])

print(strassen(mat1, mat2))