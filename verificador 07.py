#calculadora nro07
#esta calculadora muestra la dilatacion lineal de uma particula al ser sometida a una variacion de temperatura

#declaracion de variables
coeficiente_diltacion,longitud_inicial,variacion_temperatura,dilatacion_lineal=0.0,0.0,0.0,0.0

#calculadora
coeficiente_diltacion=0.0008
longitud_inicial=20
variacion_temperatura=80
dilatacion_lineal=(coeficiente_diltacion*longitud_inicial*variacion_temperatura)
verificador=(dilatacion_lineal==1.28)

#mostar datos
print("coeficiente_dilatacion es", coeficiente_diltacion)
print("longitud_inicial es", longitud_inicial)
print("variacion_temperatura es", variacion_temperatura)
print("dilatacion_lineal es", dilatacion_lineal)
print("dilatacion_lineal==1.28",verificador)
