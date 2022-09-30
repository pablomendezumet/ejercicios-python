"""
Elecciones presidenciales. Según la Ley Electoral de la República Argentina, 
el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas: 
Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco 
por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto, 
aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los 
votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor 
de diez puntos porcentuales respecto del total de los votos afirmativos válidamente 
emitidos sobre la fórmula que le sigue en número de votos.
Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo 
al escrutnio ejecutado por las Juntas Electorales, y cuyo resultado único para toda 
la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el 
artículo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta 
(30) días.
Articulo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas 
en la primera, resultando electa la que obtenga mayor número de votos afirmativos 
válidamente emitidos. 
Desarrollar un programa que permita ingresar, para los 3 parti dos más votados: fórmula 
(presidente + vice) y cantidad de votos obtenidos. Luego determinar: Qué fórmula obtuvo 
el mayor porcentaje. Si la fórmula resulta elegida o se requiere segunda vuelta. En este 
caso, indicar también quienes parƟcipan de la segunda vuelta.
""" 
print("****************************************************************************************")
print("****************************************************************************************")
print("**            ELECCIONES ELECTORALES 2023 DE LA REPUBLICA ARGENTINA                   **")
print("**                                                                                    **")
print("**                   FORMULA PARA PRESIDENTE Y VICEPRESIDENTE                         **")
print("**                                                                                    **")
print("**        PARTICIPANTE:  PARTIDO ROJO                                                 **")
print("**                       PRESIDENTE: ROJO1                                            **")
print("**                       VICEPRESIDENTE: ROJO2                                        **")
print("**                                                                                    **")
print("**        PARTICIPANTE:  PARTIDO VERDE                                                **")
print("**                       PRESIDENTE: VERDE1                                           **")
print("**                       VICEPRESIDENTE: VERDE2                                       **")
print("**                                                                                    **")
print("**        PARTICIPANTE:  PARTIDO AZUL                                                 **")
print("**                       PRESIDENTE: AZUL1                                            **")
print("**                       VICEPRESIDENTE: AZUL2                                        **")
print("**                                                                                    **")
print("****************************************************************************************")
print("****************************************************************************************")
print("")
print("")
print("ELIJA UNA OPCIÓN PARA MARCAR SU VOTO PREFERENCIAL")
print("")
print("OPCION 1 : PARTIDO ROJO")
print("OPCION 2 : PARTIDO VERDE")
print("OPCION 3 : PARTIDO AZUL")
print("OPCION 00 : SALIR DEL SISTEMA")
print("OPCION 09 : RESULTADO TOTAL")
print("")
#Definicion de variables
votparroj = int()
votparver = int()
votparazu = int()
totvotroj = int()
totvotver = int()
totvotazu = int()
totvotos = int()
portotvotroj = float()
portotvotver = float()
portotvotazu = float()
portotvot = int()
voto = str()

#Inicializar variables
totvotroj = 0
totvotver = 0
totvotazu = 0
portotvot = 100 
contador = 0
votparrojo = 0
votparver = 0
votparazu = 0
voto = ""

#Proceso
voto = str(input("Marque su Opción >>> "))

#Salida
while True:
    while voto == "1":
        votparroj =+ 1
        totvotroj = totvotroj + votparroj
        print("Total Voto Rojo: ",totvotroj)
        voto = (input("Marque su Opción >>> "))
    while voto == "2":
        votparver =+ 1
        totvotver = totvotver + votparver
        print("Total Voto Verde: ",totvotver)
        voto = (input("Marque su Opción >>> "))
    while voto == "3":
        votparazu =+ 1
        totvotazu = totvotazu + votparazu
        print("Total Voto Azul: ",totvotazu)
        voto = (input("Marque su Opción >>> "))
    while voto == "09":
        totvotos = totvotroj + totvotver + totvotazu
        portotvotroj = (totvotroj*portotvot)/totvotos
        portotvotver = (totvotver*portotvot)/totvotos
        portotvotazu = (totvotazu*portotvot)/totvotos
        print("")
        print("------------------------------------------------------------------")
        print("---------RESULTADO TOTAL OFICIAL EN LAS ELECCIONES 2023-----------")
        print("Total de votos emitidos : ",totvotos,"resultado porcentual al 100%")
        print("------------------------------------------------------------------")
        print("Total votos Partido Rojo : ",totvotroj,"resultado porcentual al ",round(portotvotroj,2),"%")
        print("Total votos Partido Verde : ",totvotver,"resultado porcentual al ",round(portotvotver,2),"%")
        print("Total votos Partido Azul : ",totvotazu,"resultado porcentual al ",round(portotvotazu,2),"%")
        print("------------------------------------------------------------------")
        if portotvotroj >= 45: 
            print("El Presidente y Vicepresidente del Partido Rojo son electos para el Periodo 2023-2027")
            break;
        else:
            if portotvotroj >= 40 and portotvotver <= 30 and portotvotazu <= 30:
                print("El Presidente y Vicepresidente del Partido Rojo son electos para el Periodo 2023-2027")
                break;   
        if portotvotver >= 45: 
            print("El Presidente y Vicepresidente del Partido Verde son electos para el Periodo 2023-2027")
            break;
        else:
            if portotvotver >= 40 and portotvotroj <= 30 and portotvotazu <= 30:
                print("El Presidente y Vicepresidente del Partido Verde son electos para el Periodo 2023-2027")
                break;        
        if portotvotazu >= 45: 
            print("El Presidente y Vicepresidente del Partido Azul son electos para el Periodo 2023-2027")
            break;
        else:
            if portotvotazu >= 40 and portotvotroj <= 30 and portotvotver <= 30:
                print("El Presidente y Vicepresidente del Partido Azul son electos para el Periodo 2023-2027")
                break;
        while portotvotroj < 45 and portotvotver < 45 and portotvotazu < 45:
            if portotvotroj > portotvotver and portotvotver > portotvotazu:
                print("Partido Rojo: "+str(portotvotroj))
                print("Partido Verde: "+str(portotvotver))
                print("Partido Azul: "+str(portotvotazu))
                print("Pasan a la segunda vuelta el Partido Rojo y el Partido Verde")
                break;
            if portotvotroj > portotvotver and portotvotazu > portotvotver:
                print("Partido Rojo: "+str(portotvotroj))
                print("Partido Verde: "+str(portotvotver))
                print("Partido Azul: "+str(portotvotazu))
                print("Pasan a la segunda vuelta el Partido Rojo y el Partido Azul")
                break;
            if portotvotver > portotvotroj and portotvotazu > portotvotroj:
                print("Partido Rojo: "+str(portotvotroj))
                print("Partido Verde: "+str(portotvotver))
                print("Partido Azul: "+str(portotvotazu))
                print("Pasan a la segunda vuelta el Partido Verde y el Partido Azul")
                break;
        else:
            break;
    while voto == "00":
        print("Salistes del Sistema")
        break;
    print("Registro Electoral de la localidad Nueva Esperanza")
    break;
#Prueba en la Shell
