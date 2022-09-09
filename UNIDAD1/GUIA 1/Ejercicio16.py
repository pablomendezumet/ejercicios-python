"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio 
y luego, proponga una dirección de mail para el nombre y apellido ingresado de 
acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente 
manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar 
la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra 
del nombre y la primera letra del apellido son la misma entonces utilizar: .@ Por ejemplo 
para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección 
de mail sería: soledad.steffolani@umet.edu.ar
"""
#Definicion de variables
nombre = str()
apellido = str()
arroba = str()
dominio1 = str()
dominio2 = str()
punto = str()
nombremin = str()
apellidomin = str()
comparanom = str()
comparaape = str()

#Inicializar variables
nombre = input("Ingrese Nombre >>>")
apellido = input("Ingrese Apellido >>>")
arroba = "@"
dominio1 = "umet.edu.ar"
dominio2 = "colegiorosarito.edu.ar"
punto = "."

#Proceso
nombremin = nombre.lower()
apellidomin = apellido.lower()
comparanom = (nombremin[slice(1)])
comparaape = (apellidomin[slice(1)])

#Salida
if comparanom == comparaape:
    print("Tu propuesta de Mail es: ",nombremin+punto+apellidomin+arroba+dominio2)
else:
    print("Tu propuesta de Mail es: ",comparanom+apellidomin+arroba+dominio1)
#Prueba de Escritorio 1
"""                                      


"""