"""
Galería de Arte. Una galería de arte desea preparar un catálogo de sus cuadros 
más famosos. Se realiza una prueba con tres cuadros y por cada uno se ingresa 
el año en que fue creado. El programa deberá verificar si todos los cuadros son 
anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 
y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. 
Si no hay ninguno, imprimir el mensaje “Renovar stock”.
"""
#Definicion de variables
cuadro1 = int()
cuadro2 = int()
cuadro3 = int()
anterior= int()
anioactual: int()
suma = int()

#Inicializar variables
cuadro1 = int(input("Ingrese la fecha del cuadro 1: "))
cuadro2 = int(input("Ingrese la fecha del cuadro 2: "))
cuadro3 = int(input("Ingrese la fecha del cuadro 3: "))
anterior = 1905-10
anioactual = 2000
cuadros = [cuadro1, cuadro2, cuadro3]
contador = 0
suma = 0
#Proceso
for i in cuadros:
    if i < anterior:
        contador = contador+1
        suma = contador
        print("El cuadros del año ",i," tiene una antiguedad de: ",anioactual - i+1," años")        
else:
    print("total cuadros antiguos: ",suma)
    if suma <= 0:
        print("Renovar Stock")
    
#Salida

#Prueba en la Shell
"""                                      


"""