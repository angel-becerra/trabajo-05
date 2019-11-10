#calculadora nro03
#esta calculadora muestra la velocidad final de una particula en MRUV

#declaracion de variables
velocidad_inicial,velocidad_final,aceleracion,tiempo_movimiento=0.0,0.0,0.0,0.0

#calculadora
velocidad_inicial=12
aceleracion=4
tiempo_movimiento=5
velocidad_final=( velocidad_inicial + (aceleracion*tiempo_movimiento))
verificador=(velocidad_final== 32)
#mostrar datos
print("velocidad_inicial es", velocidad_inicial)
print("aceleracion es", aceleracion)
print("tiempo_movimiento es", tiempo_movimiento)
print("velocidad_final es", velocidad_final)
print("velocidad_final==32", verificador)
