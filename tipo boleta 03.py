#imput
proovedor=input("nombres y apellidos")
nro_de_dni=int(input("ingrese numero de dni:"))
nro_de_ruc=int(input("ingrese nro de ruc:"))
cargamento01=input("ingrese nombre cargamento nro01:")
cargamento02=input("ingrese nombre cargamneto nro02:")
precio_cargamento01=input("ingrese precio del cargamento nro01:")
precio_cargamneto02=input("ingrese precio del cargamento nro02:")

#procesing
total_pagar=(precio_cargamento01 + precio_cargamneto02)

#output
print("#################################")
print("# envasadora: El LOCUTOR")
print("cliente:", cliente)
print("nro de DNI:", nro_de_dni)
print("nro de ruc:", nro_de_ruc)
print("cargamneto01:", nombre_cargamento01,"                precio:",precio_cargamento01)
print("cargamneto02:", nombre_cargamento02,"                precio:",precio_cargamento02)


print("total a pagar:", total_pagar)
