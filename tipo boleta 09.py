#imput
libreria=input("nombre de la libreria")
nombre_comprador=input("nombre del comprador")
nro_de_cuadernos=int(input("ingrese nro de cuadernos:"))
nro_de_lapiceros=int(input("ingrese nro de lapiceros:"))
nro_de_libros=int(input("ingrese nro de libros:"))
precio_de_cuadernos=int(input("ingrese precio de cuadernos:"))
precio_de_lapiceros=int(input("ingrese precio de lapiceros"))
precio_de_libros=int(input("ingrese precio de libros"))


#procesing
total_pagar=(nro_de_cuadernos*precio_de_cuadernos + nro_de_lapiceros*precio_de_lapiceros +nro_de_libros*precio_de_libros)


#output
print("#################################")
print("# libreria: EL SABER")
print("nombre_comprador:",nombre_comprador)
print("nro de cuadernos:",nro_de_cuadernos ,"                     precio por cuaderno:",precio_de_cuadernos)
print("nro de lapiceros:",nro_de_lapiceros ,"                     precio por lapicero:",precio_de_lapiceros)
print("nro de libros:",nro_de_libros ,"                           precio por libro:",precio_de_libros)

print("total_pagar:", total_pagar)
