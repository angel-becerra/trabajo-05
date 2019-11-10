#imput
licoreria=input("nombre de la licoreria")
nombre_comprador=input("nombre del comprador")
nro_de_tragos=int(input("ingrese nro de tragos:"))
nro_de_flor_de_caña=int(input("ingrese nro de flor de caña:"))
nro_de_ron_cartavio=int(input("ingrese nro de ron cartavio:"))
precio_por_cada_flor_de_caña=int(input("ingrese precio de flor de caña:"))
precio_de_cada_ron_cartavio=int(input("ingrese precio de cada ladrillo"))


#procesing
total_pagar=(nro_de_ron_cartavio*precio_de_cada_ron_cartavio + nro_de_flor_de_caña*precio_por_cada_flor_de_caña )


#output
print("#################################")
print("licoreria: EL ABUELO")
print("nombre_comprador:",nombre_comprador)
print("nro de tragos:",nro_de_tragos)
print("nro de flor de caña:",nro_de_flor_de_caña ,"                                precio por cada flor de caña :", precio_por_cada_flor_de_caña)
print("nro de ron cartavio:",nro_de_ron_cartavio ,"                           precio por cada ron cartavio:",precio_de_cada_ron_cartavio)

print("total_pagar:", total_pagar)
