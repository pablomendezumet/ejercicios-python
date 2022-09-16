"""
Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros 
en el rango del 1 al 100, que representaría la tarjeta de bingo de una persona. 
Una vez generado los números aleatorios solicitar al usuario que ingrese 3 números 
enteros, a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó 
ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte, no marcó 
ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”.
"""
import random

#Definicion de variables
nros = int()
cartilla = int()
cas1 = int()
cas2 = int()
cas3 = int()
#Inicializar variables
cartilla=[]
contador = 0
#Proceso

# Otra forma de lectura de los 15 numeros aleatorios entre el rango 1 al 100
#for i in range(15):
#    if contador <= i:
#        nros = random.randint(1,100)
#        cartilla.append(nros)
#    print(cartilla)

while contador <= 15:
    nros = random.randint(1,101)
    cartilla.append(nros)
    contador += 1

print(cartilla)
print("Ingresa tres numeros: ")
cas1 = int(input("Nro. 1 >> "))
cas2 = int(input("Nro. 2 >> "))
cas3 = int(input("Nro. 3 >> "))

#comprobamos si uno de los valores ingresados pertenece a la tarjeta generada

if cas1 in cartilla or cas2 in cartilla or cas3 in cartilla:
    print("El jugador marcó algún número de la tarjeta")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")




#Salida

#Prueba en la Shell
"""                                      


"""