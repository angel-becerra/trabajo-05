#calculadora nro08
#esta calculadora muestra la fuerza de repulsion entre dos cargas

#declaracion de variables
carga01,carga02,constante_electrica,distancia_entre_particulas,fuerza_de_repulsion=0.0,0.0,0.0,0.0,0.0

#calculadora
carga01=95
carga02=45
constante_electrica=9*10000000000000000
distancia_entre_particulas=5
fuerza_de_repulsion=( constante_electrica*carga02*carga01)/(distancia_entre_particulas*distancia_entre_particulas)
verificador=(fuerza_de_repulsion==153900000000000000000)

#mostrar variables
print("carga01 es", carga01)
print("carga02 es", carga02)
print("constante_electrica es", constante_electrica)
print("distancia_entre_particulas es", distancia_entre_particulas)
print("fuerza_de_repulsion es", fuerza_de_repulsion)
print("fuerza_de_repulsion==153900000000000000000",verificador)
