#imput
empresa_de_transportes=input("nombre de la empresa d transportes")
nombre_del_dueño=input("nombre del dueño")
nro_de_buses_por_arreglar=int(input("ingrese nro de buses por arreglar:"))
nro_de_choferes=int(input("ingrese nro de choferes:"))
nro_de_terramosas=int(input("ingrese nro de terramosas:"))
precio_por_arreglar_bus=int(input("ingrese precio por arreglar un bus:"))
precio_de_sueldo_choferes=int(input("ingrese precio de suelto choferes"))
precio_sueldo_de_terramosas=int(input("ingrese precio de sueldo terramosas"))



#procesing
total_gastos=( nro_de_buses_por_arreglar*precio_por_arreglar_bus + nro_de_choferes*precio_de_sueldo_choferes + nro_de_terramosas*precio_sueldo_de_terramosas)


#output
print("#################################")
print("# empresa_de_transportes: el aguila")
print("nro de buses por arreglar:",nro_de_buses_por_arreglar ,"                     precio por arreglar un bus:",precio_por_arreglar_bus)
print("nro de choferes:",nro_de_choferes ,"                                         precio de sueldo choferes:",precio_de_sueldo_choferes)
print("nro de terramosas:",nro_de_terramosas,"                                      precio suelto de terramosas:",precio_sueldo_de_terramosas)


print("total_gastos:", total_gastos)
