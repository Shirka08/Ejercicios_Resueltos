'''
# Define una rutina que devuelve True si una matriz es
# antisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1. 
'''



def esAntisimetrica(matriz):
    for i in matriz:
        if len(i) != len(matriz):
            return False

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != -matriz[j][i]:
                return False

    return True




   

# Casos Test:


assert esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

assert esAntisimetrica([[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]])  == False



assert esAntisimetrica([[1,0,0,0,0,0,0,0,0]]) == False
#>>>False

assert esAntisimetrica([[0, 1, 2], 
                              [-1, 0, 3], 
                              [-2, -3, 0]])   
#>>> True



assert  esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])  == False
#>>> False

assert  esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]) == False
#>>> False










