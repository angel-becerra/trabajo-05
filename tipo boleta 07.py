#imput
empresa=input("nombre de la empresa")
nro_ruc=int(input(" nro de ruc"))
nro_de_empleados_marketing=int(input("ingrese nro de empleados de markting:"))
nro_de_empleados_recursos_humanos=int(input("ingrese nro de empleados de recursos humanos:"))
nro_de_empleados_administrativos=int(input("ingrese nro de empleados de administracion:"))
nro_de_empleados_limpieza=int(input("ingrese nro de empleados de limpieza:"))



#procesing
total_de_empleados=(nro_de_empleados_marketing + nro_de_empleados_recursos_humanos +nro_de_empleados_administrativos + nro_de_empleados_limpieza)


#output
print("#################################")
print("# empresa: ORIGINALINS")
print("nro ruc:", nro_ruc)
print("nro de empleados de marketing:", nro_de_empleados_marketing)
print("nro de empleados de recursos_humanos:", nro_de_empleados_recursos_humanos)
print("nro de empleados de administrativos:", nro_de_empleados_administrativos)
print("nro de empleados de limpieza:", nro_de_empleados_limpieza)



print("total_de_empleados:", total_de_empleados)
