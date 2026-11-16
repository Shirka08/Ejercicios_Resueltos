# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.





def esMarizCuadrada(matriz):
    for i in matriz:
        if len(i) != len(matriz):
            return False
    return True


def SonNumerosEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if type(numero) != int:
                return False
    return True

def NumerosCorrectos(sudoku):
    for fila in sudoku:
        for numero in fila:
            if numero < 1 or numero > len(sudoku):
                return False
    return True
       
def FilasBien(sudoku):
    numeros = []
    for fila in sudoku:
        for numero in fila:
            if numero in numeros:
                return False
            numeros.append(numero)
        numeros = []
    return True

def ColumnasBien(sudoku):
    numeros = []
    for columna in range(len(sudoku)):
        for fila in range(len(sudoku)):
            if sudoku[fila][columna] in numeros:
                return False
            numeros.append(sudoku[fila][columna])
        numeros = []
    return True

def check_sudoku(sudoku):
    if not esMarizCuadrada(sudoku):
        return False
    if not SonNumerosEnteros(sudoku):
        return False
    if not NumerosCorrectos(sudoku):
        return False
    if not FilasBien(sudoku):
        return False
    if not ColumnasBien(sudoku):
        return False
    return True
    











correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]





# Casos test

assert check_sudoku(incorrecto1) == False
assert check_sudoku(correcto) == True
assert check_sudoku(incorrecto2) == False
assert check_sudoku(incorrecto3) == False
assert check_sudoku(incorrecto4) == False
assert check_sudoku(incorrecto5) == False
assert check_sudoku(incorrecto6) == False