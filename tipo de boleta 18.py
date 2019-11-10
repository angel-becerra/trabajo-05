#imput
tirnda_de_ternos=input("nombre de la tienda de ternos")
nombre_comprador=input("nombre del comprador")
nro_de_ternos=int(input("ingrese nro de ternos:"))
nro_de_corbatas=int(input("ingrese nro de corbatas:"))
nro_de_camisas=int(input("ingrese nro de camisas:"))
precio_por_cada_terno=int(input("ingrese precio de cada terno:"))
precio_por_cada_corbatas=int(input("ingrese precio de cada corbatas:"))
precio_por_cada_camisas=int(input("ingrese precio de cada camisas:"))


#procesing
total_pagar=(nro_de_ternos*precio_por_cada_terno + nro_de_camisas*precio_por_cada_camisas + nro_de_corbatas*precio_por_cada_corbatas )


#output
#output
print("#################################")
print("# tirnda de ternos: Elegante")
print("nro de ternos:",nro_de_ternos,"                     precio por cada terno:",precio_por_cada_terno)
print("nro de corbatas:",nro_de_corbatas,"                     precio por cada corbatas:",precio_por_cada_corbatas)
print("nro de camisas:",nro_de_camisas,"                     precio por cada camisa:",precio_por_cada_camisas)


print("total_pagar:", total_pagar)

