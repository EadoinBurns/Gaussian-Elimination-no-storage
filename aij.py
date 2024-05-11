"""
MECH 309 Winter 2024
Question 3 on Project
Date: Mar 28, 2024
Author: E. Burns

"""
#Test matrix
######################################################################################################################

import numpy as np


def random_nonsingular_matrix_and_b(n):
    while True:
        # Generate a random matrix of shape (n, n) with values between 1 and 10
        A = np.random.randint(1, 10, size=(n, n))

        # Check if the determinant is non-zero
        if np.linalg.det(A) != 0:
            # Generate a random vector b of length n
            b = np.random.randint(1, 10, size=n)
            return A, b


#Length of test matrix
######################################################################################################################

n = 14
A,B = random_nonsingular_matrix_and_b(n)
A1 = A
B1 = B
print("Random Matrix A:")
print(A)
print("\nRandom Vector b:")
print(B)

#My aij finder
######################################################################################################################

def a(i,j):
    i = i-1
    j = j-1
    aij=A[i][j]
    for k in range(0,i) if i<=j else range(0,j):
        pivot = A[k][k]
        sag = A[i][k]
        crow = A[k][j]
        if k > 0:
            pivot = a(k+1,k+1)
            sag = a(i+1,k+1)
            crow = a(k+1,j+1)
        aij = aij - crow*(sag/pivot)
    return aij
print('aij = ',a(4,4))

#My bi finder
######################################################################################################################

def b(i):

    i = i-1
    bi = B[i]
    for k in range(0,i):
        bee = B[k]
        if k > 0:
            bee = b(k+1)
        bi = bi - bee*(a(i+1,k+1)/a(k+1,k+1))


    return bi
print('bi = ',b(4))


#My backsub
######################################################################################################################

x = [0] * n
x[n-1] = b(n) / a(n,n)

for i in range(n-2, -1, -1):
    sum = b(i+1)
    for j in range(i+1, n):
        sum -= a(i+1,j+1) * x[j]


    x[i] = sum / a(i+1,i+1)


print("Solution:")
for i in range(n):
    print("x{} = {:.2f}".format(i+1, x[i]))



