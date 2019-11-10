#imput
ferrteria=input("nombre de la ferreteria")
nombre_comprador=input("nombre del comprador")
nro_de_cementos=int(input("ingrese nro de cementos:"))
nro_de_fierros=int(input("ingrese nro de fierros:"))
nro_de_ladrillos=int(input("ingrese nro de ladrllos:"))
precio_de_cada_cemento=int(input("ingrese precio de cada cemento:"))
precio_del_fierro=int(input("ingrese precio del fierro:"))
precio_de_cada_ladrillo=int(input("ingrese precio de cada ladrillo"))


#procesing
total_pagar=(nro_de_cementos*precio_de_cada_cemento + nro_de_fierros*precio_del_fierro +nro_de_ladrillos*precio_de_cada_ladrillo)


#output
print("#################################")
print("# ferreteria: EL TORNO")
print("nombre_comprador:",nombre_comprador)
print("nro de cementos:",nro_de_cementos ,"                     precio por cada cementos:", precio_de_cada_cemento)
print("nro de fierro:",nro_de_fierros ,"                     precio del fierro:",precio_del_fierro)
print("nro de ladrillos:",nro_de_ladrillos ,"                           precio por cada ladrillo:",precio_de_cada_ladrillo)

print("total_pagar:", total_pagar)
