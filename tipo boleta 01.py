#imput
cliente=input("nombres y apellidos")
nro_de_dni=int(input("ingrese numero de dni:"))
nro_de_ruc=int(input("ingrese nro de ruc:"))
nombre_libro01=input("ingrese nombre del libro nro01:")
nombre_libro02=input("ingrese nombre del libro nro02:")
precio_libro01=input("ingrese precio del libro nro01:")
precio_libro02=input("ingrese precio del libro nro02:")

#procesing
total_pagar=(precio_libro01 + precio_libro02)

#output
print("#################################")
print("# libreria-Bazar: El PEDRITO")
print("cliente:", cliente)
print("nro de DNI:", nro_de_dni)
print("nro de ruc:", nro_de_ruc)
print("libro01:", nombre_libro01,"                precio:",precio_libro01)
print("libro02:", nombre_libro02,"                precio:",precio_libro02)

print("total a pagar:", total_pagar)


