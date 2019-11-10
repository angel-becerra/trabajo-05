#calculadora nro06
#esta calculadora  muestra la presion hidrostatica

#declaracion de variables
densidad_liquido,gravedad,haltura,presion_hidrostatica=0.0,0.0,0.0,0.0

#calculadora
densidad_liquido=0.8
gravedad=9.8
haltura=6
presion_hidrostatica=(densidad_liquido*gravedad*haltura)
verificador=(presion_hidrostatica==47.040000000000006)

#mostrar datos
print("densidad_liquido es", densidad_liquido)
print("gravedad es", gravedad)
print("haltura es", haltura)
print("presion_hidrostatica es", presion_hidrostatica)
print("presion_hidrostatica==47.040000000000006", verificador)
