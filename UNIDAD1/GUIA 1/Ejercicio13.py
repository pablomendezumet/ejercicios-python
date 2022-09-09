"""
Crear un conversor de dólares a pesos y pesos a dólares, 
donde se ingrese por teclado el valor del peso actual
"""
#Definicion de variables
pesos = int()
dolares = float()
valor = int()
#Inicializar variables
valor = int(input("Ingresar Pesos/Dolares: "))
tcambio = 297

#Proceso
dolares = valor / tcambio
pesos = valor * tcambio
#Salida
print("Ingreso", valor,"dolares, recibira en Pesos: ",pesos)
print("Ingreso", valor,"Pesos, recibira en Dolares: ",dolares)

#Prueba en la Shell
"""                                      
dolares     pesos   valor   tcambio     Input Screen                Output Screen   
                                    Ingresar Pesos/Dolares:_500
                    500     297
148500      1.6835                                                  Ingreso 500 Dolares, recibira en Pesos: 148500
                                                                    Ingreso 500 Pesos, recibira en Dolaress: 1.6835

"""