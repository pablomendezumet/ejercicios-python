"""
1. Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un 
   programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
    a) Determinar y mostrar el nombre del ganador de la carrera.
    b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del 
       ganador es menor al tiempo record, mostrar un mensaje.
    c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""
#Definicion de variables
n = int()
competidor = int()
totalcompe = int()
nombrecom = str()
tiemporec = float()
tiempocomp = float()
totaltiempo= float()
promedio = float()
conpetidor = int()
i = int()

#Inicializar variables
n = int(input("Ingrese la cantidad de competidores: "))
tiemporec = float(input("Ingrese el tiempo record: "))
nombrecompe = ""
tiempocomp = 0.0
competidor = 0
i = 1

#Proceso
for i in range(n):
    competidor = competidor + i
    nombrecom = str(input("Ingresar nombre de competidor : "))
    ingtiempo = float(input("Ingrese el tiempo del competidor :"))
    tiempocomp = tiempocomp + ingtiempo
    print("total participantes ciclistas: ",i)
    print("promedio de Tiempo ciclistas: ",tiempocomp)

#Salida

#Prueba de Escritorio
