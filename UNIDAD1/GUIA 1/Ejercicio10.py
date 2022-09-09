"""
Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.
"""
#Definicion de variables
from ast import Break


val1 = int()
val2 = int()
secuencia = int()

#Inicializar variables
val1 = 0
val2 = 1
suma = 0
contador = 0
#Proceso
secuencia = int(input("ingresa secuencia:"))

#Salida
while contador < secuencia:   
    print(suma, end=" ")
    val1 = val2
    val2 = suma 
    suma = val1 + val2
    contador = contador + 1

#Prueba de Escritorio 1
"""                                      
val1    val2    suma    contador    secuencia   Input Screen            Output Screen
0       1       0       0           5           Ingresa Secuencia:_5    0
1       0       1       1                                               1
0       1       1       2                                               1
1       1       2       3                                               2
1       2       3       4                                               3
2       3       5       5                                               
                                                                        
"""