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

#Proceso
for i in range(15):
    numeros = random.randint(1, 100)
    numcartilla = numeros
    
    print(str(numcartilla),list[i])
#Salida

#Prueba en la Shell
"""                                      


"""