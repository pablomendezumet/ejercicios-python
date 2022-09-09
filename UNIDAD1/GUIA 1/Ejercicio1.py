"""Desarrolle un programa que pase un peso de kilogramo 
a libras teniendo en cuenta que cada kilogramo equivale 
a 2.2 libras."""

# Definicion de Variables
KILO = float(0)
libra = int(0)
peso = int(0)
resultado = int(0)

#Inicializar variables
KILO = 2.2
peso = int(input("INGRESE PESO EN KILOGRAMOS : "))
resultado = peso * KILO

# Salida
print("CONVIRTIO ",peso," KILOGRAMOS EN ",resultado,"LIBRAS")

#Prueba de Escritorio 1
"""                                      
KILO    libra   peso    resultado       Entrada por pantalla            Salida por Pantalla
0       0       0       0
2.2             5       11.0            INGRESE PESO EN KILOGRAMOS :_5
                                                                        CONVIRTIO 5 KILOGRAMOS EN 11.0 LIBRAS
"""
#Prueba de Escritorio 2
"""
KILO    libra   peso    resultado       Salida por pantalla             Salida por Pantalla
0       0       0       0
2.2             8       17.6            INGRESE PESO EN KILOGRAMOS :_8
                                                                        CONVIRTIO 8 KILOGRAMOS EN 17.6 LIBRAS

"""