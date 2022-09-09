"""
Crear un conversor de pies y pulgadas a centímetros.
"""
#Definicion de variables
pie = float()
pulgada = float()
texpie = str()
texpul = str()
resultado = float()

#Inicializar variables
tipomedida = input("Ingresa medida a convertir (pulgada ó pie) >>> ")
cantmedida = int(input("Ingresa la cantidad a convertir >>> "))
pulgada = 2.54
pie = 12 * pulgada
resultado = 0

#Proceso
texpie = str("pie")
texpul = str("pulgada")

#Salida
if texpie == tipomedida:
    resultado = pie * cantmedida
    print(cantmedida," Pies equivale a ",resultado," centimetros")
else:
    resultado = pulgada * cantmedida
    print(cantmedida," Pulgadas equivale a ",resultado," centimetros")

#Prueba de Escritorio 1
"""                                      
pie     pulgada     texpie  texpul  resultado   tipomedida  cantmedida  Input Screen                    Output Screen
                                                                        Ingresa medida pul ó pie:_pie
                                                                        Ingresa cantidad a convertir:_8
30.48   2.54        pie     pulgada             pie         8
                                    243.84                                                              8 Pies equivale a 243.84 centimetros

"""
#Prueba de Escritorio 2
"""                                      
pie     pulgada     texpie  texpul  resultado   tipomedida  cantmedida  Input Screen                    Output Screen
                                                                        Ingresa medida pul ó pie:_pulgada
                                                                        Ingresa cantidad a convertir:_9
30.48   2.54        pie     pulgada             pulgada     9
                                    22.86                                                               9 Pulgadas equivale a 22.86 centimetros

"""