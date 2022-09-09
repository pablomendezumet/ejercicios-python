"""
División con resto. Plantear un algoritmo que permita informar, 
para dos valores a y b el resultado de la división a/b y el 
resto de esa división.
"""
#Definicion de variables
a = int()
b = int()
division = int()
resto = int()

#Inicializar variables
a = int(input("Ingresar el valor de 'a' :"))
b = int(input("Ingresar el valor de 'b' :"))

#Proceso
division = a // b
resto = a % b

#Salida
print("La división es: ",division)
print("El Resto es: ",resto)

#Prueba de Escritorio 1
"""                                      
a   b   division    resto   Entrada por Pantalla    Salida por Pantalla
                            Ingrese valor de 'a'_ 8
                            Ingrese valor de 'b'_ 4
8   4   2           0                               La división es 2
                                                    El resto es 0
"""
#Prueba de Escritorio 2
"""                                      
a   b   division    resto   Entrada por Pantalla    Salida por Pantalla
                            Ingrese valor de 'a'_ 9
                            Ingrese valor de 'b'_ 2
9   2   4           1                               La división es 4
                                                    El resto es 1
"""