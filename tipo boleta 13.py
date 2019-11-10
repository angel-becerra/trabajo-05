#imput
empresa_de_cervesa=input("nombre de la empresa de cervesa")
nombre_del_dueño=input("nombre del dueño")
nro_de_cervesa_pilsen=int(input("ingrese nro de cervesa pilsen:"))
nro_de_cervesa_cristal=int(input("ingrese nro de cervesa cristal:"))
nro_de_gaseosa_guarana=int(input("ingrese nro de gaseosa guarano:"))
precio_por_cada_cervesa_pilsen=int(input("ingrese precio por cervesa pilsen:"))
precio_por_cada_cervesa_cristal=int(input("ingrese precio por cada cervesa cristal"))
precio_por_cada_gaseosa_guarana=int(input("ingrese precio por cada gaseosa guarana"))



#procesing
total_gastos=( nro_de_cervesa_pilsen*precio_por_cada_cervesa_pilsen + nro_de_cervesa_cristal*precio_por_cada_cervesa_cristal + nro_de_gaseosa_guarana*precio_por_cada_gaseosa_guarana)


#output
print("#################################")
print("# empresa_de_cervesa: EL CERVECERO")
print("nro de cervesa pilsen:",nro_de_cervesa_pilsen ,"                     precio por cada cervesa pilsen:",precio_por_cada_cervesa_pilsen)
print("nro de cervesa cristal:",nro_de_cervesa_cristal,"                    precio de sueldo choferes:",precio_por_cada_cervesa_cristal)
print("nro de gaseosa guarana:",nro_de_gaseosa_guarana,"                    precio por cada gaseosa guarana:",precio_por_cada_gaseosa_guarana)


print("total_gastos:", total_gastos)
