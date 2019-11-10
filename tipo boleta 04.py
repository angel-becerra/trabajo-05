#imput
empresa=input("nombre de la empresa")
cliente=input("nombre del cliente" )
nro_de_ruc=int(input("ingrese nro de ruc:"))
cantidad_producto01=input("ingrese nombre del producto nro01:")
cantidad_producto02=input("ingrese nombre del producto nro02:")
total_pagar_producto01=input("ingrese total a pagar  del producto nro01:")
total_pagar_producto02=input("ingrese total a pagar  del producto nro02:")

#procesing
total_pagar=(total_pagar_producto01 + total_pagar_producto02)

#output
print("#################################")
print("# distribuidora: DON LUIS")
print("EMPRESA:", EMPRESA)
print("cliente:", cliente)
print("nro de ruc:", nro_de_ruc)
print("producto01:", cantidad_producto01,"                precio:",total_pagar_producto01)
print("producto02:", cantidad_producto02,"                precio:",total_pagar_producto02)

print("total a pagar:", total_pagar)
