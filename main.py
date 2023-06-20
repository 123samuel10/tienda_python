productos = {
    'manzana': 1500,
    'banano': 2000,
    'fresa': 500,
    'mango':1000
}


print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")


cantidad_manzana = int(input("Ingrese la cantidad de manzanas que desea comprar: "))
cantidad_banano = int(input("Ingrese la cantidad de plátanos que desea comprar: "))
cantidad_fresa = int(input("Ingrese la cantidad de fresas que desea comprar: "))
cantidad_mango = int(input("Ingrese la cantidad de mangos que desea comprar: "))


total_manzana = cantidad_manzana * productos['manzana']
total_banano = cantidad_banano * productos['banano']
total_fresa = cantidad_fresa * productos['fresa']
total_mango=cantidad_mango* productos['mango']
total = total_manzana + total_banano + total_fresa


print(f"Total a pagar: ${total}")
