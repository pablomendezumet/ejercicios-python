"""
Área de un triángulo. Desarrolle un programa para calcular el área 
de un triángulo, cargando por teclado el valor de la base, pero 
sabiendo que su altura es igual al cuadrado de la base.
"""
#Definicion de variables
base = float()
altura = float()
area = float()

#Inicializar variables
base = float(input("Ingrese la Base: "))

#Proceso
altura = base**2
area = (base * altura)/2
#Salida
print("El Área del Triangulo es: ",area)
#Prueba de Escritorio 1
"""                                      
base    altura  area    Input Screen        Output Screen
                        Ingrese la Base:_ 4
4       16      32                          El Area del Triangulo es:32
"""
