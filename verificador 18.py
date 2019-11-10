#calculadora nro18
#esta calculadora muestra la intensidad de corriente electrica

# Asignacion de valores
intensidad_corriente_electrica,carga,tiempo=0.0,0.0,0.0

#calculadora
carga=900000
tiempo=1.5
intensidad_corriente_electrica=carga/tiempo
verificador=(intensidad_corriente_electrica==600000)

# Mostrar valores
print("carga = ",carga)
print("tiempo = ",tiempo)
print("intensidad_corriente_electrica = ",intensidad_corriente_electrica)
print("intensidad_corriente_electrica==600000", verificador)
