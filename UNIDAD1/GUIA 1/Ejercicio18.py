"""
Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos 
humanos de una empresa que permita informar el jornal de un determinado operario. 
Usted deberá cargar por teclado el código de turno que el operario trabajó ese día 
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. 
La política de trabajo en la empresa es que los operarios de la misma pueden trabajar 
en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 
40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
"""
#Definicion de variables
cod1 = int()
cod2 = int()
htrab = int()
jnocturno = float()
jdiurno = float()
jornalope = float()

#Inicializar variables
print("INGRESE TURNO DE TRABAJO")
print("")
print("1  TURNO DIURNO")
print("2  TURNO NOCTURNO")
cod1 = "1"
cod2 = "2"
jdiurno = 35.5
jnocturno = 40.6
turno = str(input("Digite el turno laboral: "))
if turno == str(cod1) or turno == str(cod2):  
    htrab = int(input("Digite la cantidad de horas trabajadas: "))
else:
    print("Codigo Incorrecto, vuelva a digitar")
    turno = str(input("Digite el turno laboral: "))

#Proceso
while True:
    if  turno == cod1:
        jornalope = jdiurno * htrab
        print("Turno Laboral: ",str(cod1))
        print("Horas Trabajadas del Operraio: ",htrab)
        print("El Jornal del Operario del turno diurno es: ",round(jornalope,2)," Pesos")
        break;
    elif turno == cod2:
        jornalope = jnocturno * htrab
        print("Turno Laboral: ",str(cod2))
        print("Horas Trabajadas del Operario: ",htrab)
        print("El Jornal del Operario del turno nocturno es: ",round(jornalope,2)," Pesos")
        break;
    else:
        print("Codigo Incorrecto")
        break;

#Salida

#Prueba de Escritorio 1
"""                                      


"""