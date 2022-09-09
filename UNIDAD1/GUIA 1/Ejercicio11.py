"""
Multiplicación. Ingresar un número cualquiera por teclado y 
que muestre su respectiva tabla del 1 al 10.
"""
#Definicion de variables
tabla = int()
contador = int()
resultado = int()

#Inicializar variables
tabla = int(input("Ingrese Tabla de Multiplicar: "))
contador = 1
resultado  = 0

#Proceso
while contador <= tabla:
    resultado = tabla * contador
    print(tabla," X ", contador, " = ",resultado)
    i = i+1

#Prueba decescritorio 1
"""                                      
Tabla   contador    resultado      Input Screen                         OutputScreen
                                    Ingresar Tabla de Multiplicar:_5
5       1           5                                                   5 X 1 = 5
5       2           10                                                  5 X 2 = 10
5       3           15                                                  5 X 3 = 15
5       4           20                                                  5 X 4 = 20
5       5           25                                                  5 X 5 = 25

"""