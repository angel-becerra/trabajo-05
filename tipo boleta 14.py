#imput
bodega_vendedora_verduras=input("nombre de la bodega vendedora de verduras ")
nombre_del_dueño=input("nombre del dueño")
nro_de_brocoli_vendido=int(input("ingrese nro de brocoli vendido:"))
nro_de_zanahoria_vendida=int(input("ingrese nro de zanahoria vendida:"))
nro_de_tomates_vendidos=int(input("ingrese nro de tomates vendidos:"))
precio_por_cada_brocoli=int(input("ingrese precio por cada brocoli:"))
precio_por_cada_zanahoria=int(input("ingrese precio por cada zanahoria"))
precio_por_cada_tomate=int(input("ingrese precio por cada tomate"))



#procesing
total_gastos=(nro_de_brocoli_vendido*precio_por_cada_brocoli + nro_de_zanahoria_vendida*precio_por_cada_zanahoria + nro_de_tomates_vendidos*precio_por_cada_tomate)


#output
print("#################################")
print("# bodega: DOÑA CINTHIA")
print("nro de brocoli vendida:",nro_de_brocoli_vendido,"                     precio por cada brocoli:",precio_por_cada_brocoli)
print("nro de zanahoria vendida:",nro_de_zanahoria_vendida,"                     precio por cada zanahoria:",precio_por_cada_zanahoria)
print("nro de tomate vendidos:",nro_de_tomates_vendidos,"                     precio por cada tomate:",precio_por_cada_tomate)


print("total_gastos:", total_gastos)
