"""
Escribir un programa que pregunte un nombre de usuario, y 
que después muestre por pantalla si su cantidad de letras 
es par o impar.
"""
#Definicion de variables
nomusuario = str()
valnombre = int()

#Inicializar variables
nomusuario = input("Ingresar Nombre de Usuario: ")
valnombre = len(nomusuario)

#Proceso
if valnombre % 2 == 0:
    print("La cantidad de letras es Par")
else:
    print("La cantidad de letras es Impar")

#Prueba de Escritorio 1
"""                                      
nomusuario  valnombre   valnombre%2 Entrada por Pantalla                Salida por Pantalla
                                    Ingresar nombre de usuario _Ana
Ana         3           1                                               La cantidad de letras es impar
"""
#Prueba de Escritorio 2
"""
nomusuario  valnombre   valnombre%2 Entrada por Pantalla                Salida por Pantalla
                                    Ingresar nombre de usuario _Mirian
Mirian      6           0                                               La cantidad de letras es par

"""