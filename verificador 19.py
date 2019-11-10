#calcularo nro19
# esta calculadora muestra el  volumen de la piramide cuadrangular regular

# Asignacion de valores
area_base_cuadrada,altura=0.0,0.0

#calculadora
area_base_cuadrada=800
altura=18
volumen_piramide_cuadrangular_regular=area_base_cuadrada*altura/3
verificador=(volumen_piramide_cuadrangular_regular==4800)

# Mostrar valores
print("area_base_cuadrada = ",area_base_cuadrada)
print("altura = ",altura)
print("volumen_piramide_cuadrangular_regular = ",volumen_piramide_cuadrangular_regular)
print("volumen_piramide_cuadrangular_regular==4800", verificador)
