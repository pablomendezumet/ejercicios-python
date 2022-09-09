"""
Ahorros. Escribir un programa en el cual muestre a fin de año el 
total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.
"""
#Definicion de variables
sueldo = float()
contador = int()
ahorro = int()
sumatotal = float()

#Inicializar variables
sueldo = 0
contador = 0
ahorro = 0.1 * sueldo
sumatotal = 0

#Proceso
sueldo = float(input("Ingrese Sueldo: "))
contador = contador + 1
sumatotal = ahorro + sumatotal
ahorro = 0.1 * sueldo

#Salida
while contador <= 12:
    sumatotal = ahorro + sumatotal 
    print("El ahorro en el mes ",contador, "es de: ",ahorro)
    contador = contador + 1
    
else:
    print("El total ahorrado es: ",sumatotal)
#Prueba en la Shell
"""                                      
sueldo  contador    ahorro  sumatotal   Input Screen            Output Screen
0       0           0       0           Ingrese Sueldo:_50000
50000   1           5000    5000                                El ahorro en el mes 1 es de 5000
        2                   10000                               El ahorro en el mes 2 es de 5000 
        3                   15000                               El ahorro en el mes 3 es de 5000
        4                   20000                               El ahorro en el mes 4 es de 5000
        5                   25000                               El ahorro en el mes 5 es de 5000
        6                   30000                               El ahorro en el mes 6 es de 5000
        7                   35000                               El ahorro en el mes 7 es de 5000
        8                   40000                               El ahorro en el mes 8 es de 5000
        9                   45000                               El ahorro en el mes 9 es de 5000
        10                  50000                               El ahorro en el mes 10 es de 5000
        11                  55000                               El ahorro en el mes 11 es de 5000
        12                  60000                               El ahorro en el mes 12 es de 5000
                                                                El total ahorrado es: 60000
"""