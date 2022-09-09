"""
Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto
"""
#Definicion de variables
num1 = int()
num2 = int()
division = float()
cociente = float()
resto = ()
#Inicializar variables
num1 = int(input("Ingresa dividendo: "))
num2 = int(input("Ingresa Divisor: "))

#Proceso
division = num1 // num2
cociente = num1 / num2
resto = num1 % num2
#Salida
print("La division es:",division)
print("El Cociente es:",cociente)
print("El Resto es:",resto)

#Prueba decescritorio 1
"""                                      
num1    num2    division    cociente    resto   Input Screen            Output Screen
                                                Ingresa Dividendo:_8
                                                Ingresa Divisor:_3
8       3       2           2.6666665   2                               La division es 2
                                                                        El cociente es 2.6666665
                                                                        El Resto es 2     
"""                                  
#Prueba decescritorio 2
"""                                      
num1    num2    division    cociente    resto   Input Screen            Output Screen
                                                Ingresa Dividendo:_17
                                                Ingresa Divisor:_7
17      7       2           2.428571    3                               La division es 2
                                                                        El cociente es 2.428571428571
                                                                        El Resto es 3  

"""