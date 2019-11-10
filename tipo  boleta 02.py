#imput
cliente=input("nombres y apellidos")
nro_de_dni=int(input("ingrese numero de dni:"))
nro_de_ruc=int(input("ingrese nro de ruc:"))
nombre_producto01=input("ingrese nombre del producto nro01:")
nombre_producto0102=input("ingrese nombre del producto nro02:")
precio_producto01=input("ingrese precio del producto nro01:")
precio_producto02=input("ingrese precio del producto nro02:")

#procesing
total_pagar=(precio_producto01 + precio_producto02)

#output
print("#################################")
print("# ferreteria: El PAISA")
print("cliente:", cliente)
print("nro de DNI:", nro_de_dni)
print("nro de ruc:", nro_de_ruc)
print("producto01:", nombre_producto01,"                precio:",precio_producto01)
print("producto02:", nombre_producto02,"                precio:",precio_producto02)

print("total a pagar:", total_pagar)
