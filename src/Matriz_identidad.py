# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)



def esMatrizIdentidad(matrix):
        for i in matrix:                              #Por cada fila en la matriz
              if len(i) != len(matrix):               #Si el numero de filas es ditinto del numero de listas(columnas) de la matriz
                  return False                        #Debuelve Falso, Esto comprueba si la matriz es cuadrada
        for i in range(len(matrix)):                  #Recorre las filas
            for j in range(len(matrix)):              #Recorre las columnas
                if i == j and matrix[i][j] != 1:      #Si la posicion de la fila y la coluna es la misma (1,1) y esa posicion es distinta de 1
                    return False                      #Debuelve Falso
                elif i != j and matrix[i][j] != 0:    #Si la posicion de la fila y la columna no es el mismo numero y por tanto no se encuentran en la diagonal principal y este numero es distinto de 0
                    return False                      #Debuelve Falso
        return True



















    # Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
assert esMatrizIdentidad(matrix1) == True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

assert esMatrizIdentidad(matrix2) == False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

assert esMatrizIdentidad(matrix3) == False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

assert esMatrizIdentidad(matrix6) == False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
assert esMatrizIdentidad(matrix7) == False


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

assert esMatrizIdentidad(matrix4) == False


matrix5 = [[1,0,0,0,0,0,0,0,0]]

assert esMatrizIdentidad(matrix5) == False
