"""
Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor 
del último dígito de un número entero? ¿Y cómo obtendría los dos últimos 
dígitos? Desarrolle un programa que cargue un número entero por teclado, 
y muestre el último dígito del mismo (por un lado) y los dos últimos 
dígitos (por otro lado).

"""
#Definicion de variables

digito = int()
restodigito = int()
ultimodigito = int()
dosultimosdig = int()

#Inicializar variables
digito = int(input("Ingrese un Digito: "))

#Proceso
restodigito = digito%2
ultimodigito = digito % 10
dosultimosdig = digito % 10**2

#Salida
print("Resto del digito: ",restodigito)
print("Ultimo digito: ",ultimodigito)
print("Dos ultimos digitos: ",dosultimosdig)

#Prueba de Escritorio 1
"""
digito  restodigito ultimodigito    dosultimosdig   Input Screen            Output Screen
                                                    Ingrese un Digito:_3456
3456    0           6               56                                      Resto del digito: 0
                                                                            Ultimo digito: 6
                                                                            Dos ultimos digitos: 56
"""

#Prueba de Escritorio 2
"""
digito  restodigito ultimodigito    dosultimosdig   Input Screen            Output Screen
                                                    Ingrese un Digito:_5679
5679    1           9               79                                      Resto del digito: 1
                                                                            Ultimo digito: 9
                                                                            Dos ultimos digitos: 79
"""