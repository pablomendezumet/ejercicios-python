"""
Escribir un programa que pregunte un nombre de usuario, 
y que después muestre por pantalla si su cantidad de letras es par o impar.
"""
#Definicion de variables
nomusuario = str()
totnomusuario = int()

#Inicializar variables
nomusuario = input("Ingresa Nombre de Ususario: ")

#Proceso
totnomusuario = int(len(nomusuario))

#Salida
if totnomusuario % 2 == 0:
    print(totnomusuario,"Es la cantidad de letras y nombre usuario es Par")
else:
     print(totnomusuario,"Es la cantidad de letras y nombre usuario es Impar")

#Prueba de escritorio 1
"""                                      
nomusuario  totnomusuario   Input Screen                    Output Screen
                            Ingrese Nombre Ususario:_sabino
sabino      6                                               6 es la cantidad de letras y nombre usuario es Par            
"""

#Prueba de escritorio 2
"""                                      
nomusuario  totnomusuario   Input Screen                    Output Screen
                            Ingrese Nombre Ususario:_dalia
dalia       5                                               5 es la cantidad de letras y nombre usuario es Impar            
"""