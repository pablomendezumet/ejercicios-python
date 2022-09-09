"""
Suma - División - Potencia. Se necesita desarrollar un programa que permita 
calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 
(mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
"""
#Definicion de variables
num1 = int()
num2 = int()
num3 = int()
suma = int()
division = int()
potencia = int()
resultado = int()

#Inicializar variables
num1 = int(input("Ingresa el Primer número: "))
num2 = int(input("Ingresa el Primer número: "))
num3 = int(input("Ingresa el Primer número: "))
#Proceso
suma = num1+num2+num3

#Salida
if suma>10:
    division= suma/2
    resultado=round(division)
    print("La division por 2 es: ",resultado)
else:
    resultado = suma**3
    print("El valor al cubo es: ",resultado)
    
#Prueba de escritorio 1
"""                                      


"""