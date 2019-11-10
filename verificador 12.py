#calculadora nro12
# Calculo del volumen de prisma cuadrangular

#declaracion de variables
volumen_prisma_cuadrangular,largo,ancho,altura=0.0,0.0,0.0,0.0

#calculadora
largo=12
ancho=12
altura=8.5
volumen_prisma_cuadrangular=largo*ancho*altura
verificacion=(volumen_prisma_cuadrangular==1224)

# Mostrar valores
print("largo = ",largo)
print("ancho = ",ancho)
print("altura = ",altura)
print("volumen_prisma_cuadrangular = ",volumen_prisma_cuadrangular)
print("volumen_prisma_cuadrangular==1224", verificacion)
