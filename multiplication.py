import numpy as np

"""
generating the random matries of specified length 
for a, b and c using numpy
"""
a = np.random.random((10**6, 10**3))
b = np.random.random((10**3, 10**6))
c = np.random.random((10**6, 1))



"""
The function to handle the multiplication of two matrices
here @ is numpy operator to multiply matrices
"""

def do_multiplication(matrix_1, matrix_2):
     return matrix_1 @ matrix_2
    

def handle_multipliction(matrix_1, matrix_2, matrix_3):

    #first two matrices is multiplied
    firt_multiplication = do_multiplication(matrix_1, matrix_2)

    #the resuting matrix is multiplied with third matrix
    second_multiplication = do_multiplication(firt_multiplication, matrix_3)
    
    return second_multiplication


d = handle_multipliction(a, b, c)
print(d)
