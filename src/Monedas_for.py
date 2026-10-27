# coding = utf-8
'''
Define un prodecimiento, euros, que toma como entrada un entero positivo en euros
y devuelve el número de monedas de 5 céntimos, de 2 cénts. y de 1 cénts. requeridos 
para formar ese valor. El valor retornado debe ser una lista de tres números:
el número de monedas de 5 cénts, de 2 cénts. y de 1 cénts. necesarias.
Tu respuesta debe usar el menor número posible usandp primero cuantas más monedas
de 5 cénts posible, luego de 2 y finalmente de 1 (para sumar el total)
'''



def calcular_cambio(pago):
    numeroDeMonedas = [0, 0, 0]                                      # Inicializamos la lista con tres ceros para las monedas de 5, 2 y 1 céntimos

    if pago == 0:
        return numeroDeMonedas                                       # Si el pago es 0, devolvemos la lista con ceros
    
    tiposDeMonedas = [5, 2, 1]                                       # Definimos los tipos de monedas disponibles

    monedaIndex = 0                                                  # Inicializamos el índice para recorrer los tipos de monedas
    
    for moneda in tiposDeMonedas:
               numeroDeMonedas[monedaIndex] = pago // moneda         # Calculamos cuántas monedas de este tipo se necesitan
               pago = pago % moneda                                  # Actualizamos el pago restante después de usar las monedas 

               if pago == 0:
                   break                                             # Si el pago restante es 0, salimos del bucle
               else: 
                     monedaIndex += 1                                # Pasamos al siguiente tipo de moneda
    return numeroDeMonedas                                           # Devolvemos la lista con el número de monedas necesarias                
   
     



CASOS TEST:

print(calcular_cambio(8))
assert calcular_cambio(8) == [1, 1, 1]
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.

print(calcular_cambio(5))
assert calcular_cambio(5) == [1, 0, 0]
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.

print(calcular_cambio(29))
assert calcular_cambio(29) == [5, 2, 0]
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.

print(calcular_cambio(0))
assert calcular_cambio(0) == [0, 0, 0]
#>>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.