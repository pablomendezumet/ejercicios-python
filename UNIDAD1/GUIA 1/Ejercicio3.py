"""
Escriba un programa que transforme todas las letras 
de una palabra en mayúsculas, minúsculas y la primera 
con minúsculas(capitalización).
"""
#Definicion de variables
texto = str()
palabraM = str()
palabram = str()
Apalabra = str()

#Inicializar variables
texto = input("Ingresar Palabra: ")

#Proceso
palabraM = texto.upper()
palabram = texto.lower()
Apalabra = texto.capitalize()

#Salida
print("Es un texto en Mayúscula >>>",palabraM)
print("Es un texto en Minúscula >>>",palabram)
print("Es un texto en Capital >>>",Apalabra)

#Prueba de Escritorio 1
"""                                      
texto   palabraM    palabram    Apalabra    Entrada por Pantalla    Salida por Pantalla
                                            Ingresar Palabra:_pablo
pablo   PABLO       pablo       Pablo                               Es un texto en Mayúscula >>> PABLO
                                                                    Es un texto en Minúscula >>> pablo
                                                                    Es un texto en Capital >>> Pablo
"""