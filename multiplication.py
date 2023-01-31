import numpy as np


a = np.random.randint(10, size=(10**6, 10**3))
b = np.random.randint(10, size=(10**3, 10**6))
c = np.random.randint(10, size=(10**6, 1))



def do_multiplication(matrix_1, matrix_2):
     return matrix_1 @ matrix_2
    

def handle_multipliction(matrix_1, matrix_2, matrix_3):
    firt_multiplication = do_multiplication(matrix_1, matrix_2)
    second_multiplication = do_multiplication(firt_multiplication, matrix_3)
    return second_multiplication


d = handle_multipliction(a, b, c)
print(d)