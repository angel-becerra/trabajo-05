#calculadora nro05
#esta calculadora muestra la energia cinetica de una particula

#declaracion de variables
masa,velocidad,energia_cinetica=0.0,0.0,0.0

#calculadora
masa=6
velocidad=8
energia_cinetica=(masa*velocidad*velocidad)/2
verificador=(energia_cinetica==192)
#mostrar datos
print("masa es", masa)
print("velocidad es", velocidad)
print("energia_cinetica es", energia_cinetica)
print("energia_cinetica==192", verificador)
