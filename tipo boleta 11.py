#imput
academia=input("nombre de la academia")
nro_ruc=input("nombre de ruc")
nro_de_alumnos_letras=int(input("ingrese nro de alumnos letras:"))
nro_de_alumnos_ingenieria=int(input("ingrese nro de alumnos ingenieria:"))
nro_de_alumnos_biomedicas=int(input("ingrese nro de alumnos biomedicas:"))
precio_del_ciclo_academico=int(input("ingrese precio del ciclo academico:"))



#procesing
total_ingresos=( nro_de_alumnos_letras*precio_del_ciclo_academico + nro_de_alumnos_ingenieria*precio_del_ciclo_academico + nro_de_alumnos_biomedicas*precio_del_ciclo_academico)


#output
print("#################################")
print("# academia: IMPULSANDO")
print("nro de alumnos letras:",nro_de_alumnos_letras ,"                     precio del ciclo academico:",precio_del_ciclo_academico)
print("nro de alumnos ingenieria:",nro_de_alumnos_ingenieria ,"                     precio del ciclo academico:",precio_del_ciclo_academico)
print("nro de alumnos biomedicas:",nro_de_alumnos_biomedicas,"                     precio del ciclo academico:",precio_del_ciclo_academico)


print("total_ingresos:", total_ingresos)
