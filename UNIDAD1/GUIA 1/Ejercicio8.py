"""
Conversión de medidas. Desarrolle un programa para convertir 
una medida dada en pies a sus equivalentes en: yardas, pulgadas, 
centimetros, metros. Sabiendo que: 1 pie = 12 pulgadas, 
1 yarda = 3 pies, 1 pulgada = 2.54 centímetros, 1 metro =1000 
"""
#Definicion de variables
yardas = float()
pies = float()
pulgadas = float()
metros = float()

#Inicializar variables
medida = int(input("Ingresa medida en pie: "))
yardas = 3
pie = 12
pulgadas = 2.54
metros = 1000

#Proceso
yardare = medida/yardas
piere = medida*pie
pulgadasre = medida*pie*pulgadas
metrosre = pulgadasre/metros

#Salida
print("Se ingreso ",medida,"Pies que su equivalente en Yardas es: ",yardare)
print("Se ingreso ",medida,"Pies que su equivalente en Pulgadas es: ",piere)
print("Se ingreso ",medida,"Pies que su equivalente en Centimetros es: ",pulgadasre)
print("Se ingreso ",medida,"Pies que su equivalente en Metros es: ",metrosre)

#Prueba de escritorio 1
"""                                      
yardas  pie pulgada metros  medida  yardare piere   pulgadasre  metrosre    Input Screen                Output Screen
                                                                            Ingresa medida en Pie:_3
3       12  2.54    1000    3        1       36      91.44       0.09144                                Se ingreso, 3 Pies que su equivalencia en Yarda es: 1
                                                                                                        Se ingreso, 3 Pies que su equivalencia en Pulgadas es: 36
                                                                                                        Se ingreso, 3 Pies que su equivalencia en Centimetros es: 91.44
                                                                                                        Se ingreso, 3 Pies que su equivalencia en Metros es: 0.09144
"""