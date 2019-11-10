#imput
supermercado=input("nombre del supermercado ")
nombre_del_dueño=input("nombre del dueño")
nro_de_verduras=int(input("ingrese nro de verduras:"))
nro_de_frutas=int(input("ingrese nro de frutas:"))
nro_de_gaseosa=int(input("ingrese nro de gaseosa:"))
precio_por_cada_verdura=int(input("ingrese precio por cada verdura:"))
precio_por_cada_fruta=int(input("ingrese precio por cada fruta"))
precio_por_cada_gaseosa=int(input("ingrese precio por cada gaseosa"))



#procesing
total_gastos=(nro_de_frutas*precio_por_cada_fruta + nro_de_verduras*precio_por_cada_verdura + nro_de_gaseosa*precio_por_cada_gaseosa)


#output
print("#################################")
print("# supermercado: EL SUPER")
print("nro de verduras:",nro_de_verduras,"                     precio por cada verdura:",precio_por_cada_verdura)
print("nro de frutas:",nro_de_frutas,"                     precio por cada fruta:",precio_por_cada_fruta)
print("nro de gaseosa:",nro_de_gaseosa,"                     precio por cada gaseosa:",precio_por_cada_gaseosa)


print("total_gastos:", total_gastos)
