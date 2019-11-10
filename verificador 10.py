#calculadora nro10
#esta calculadora muestra el volumen de la esfera

 #declaracion de variables
valor_aproximado_pi,radio_de_la_esfera,volumen_de_la_esfera=0.0,0.0,0.0

#calculadora
valor_aproximado_pi=3.14
radio_de_la_esfera=9
volumen_de_la_esfera=( 4*valor_aproximado_pi*radio_de_la_esfera*radio_de_la_esfera*radio_de_la_esfera)/3
verificador=(volumen_de_la_esfera==3052.08)

#mostrar datos
print("valor_aproximado_pi es", valor_aproximado_pi)
print("radio_de_la_esfera es", radio_de_la_esfera)
print("volumen_de_la_esfera es", volumen_de_la_esfera)
print("volumen_de_la_esfera==3052.08", verificador)
