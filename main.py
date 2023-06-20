
nombre_usuario_correcto = "samuel"
contraseña_correcta = "123"


def aplicar_descuento(total):
    if total > 20000:
        descuento = total * 0.1  # Descuento del 10% si el total es mayor a 20000
        total_con_descuento = total - descuento
        print(f"Se aplicó un descuento de ${descuento}.")
        print(f"Total con descuento: ${total_con_descuento}")
        return total_con_descuento
    else:
        return total


nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")


if nombre_usuario == nombre_usuario_correcto and contraseña == contraseña_correcta:
    print("Inicio de sesión exitoso. ¡Bienvenido a la tienda!")

  
    productos = {
        'manzana': 1500,
        'banano': 2000,
        'fresa': 500
    }

   
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")

    cantidad_manzana = int(input("Ingrese la cantidad de manzanas que desea comprar: "))
    cantidad_banano = int(input("Ingrese la cantidad de plátanos que desea comprar: "))
    cantidad_fresa = int(input("Ingrese la cantidad de fresas que desea comprar: "))

    # Calcular el total a pagar
    total_manzana = cantidad_manzana * productos['manzana']
    total_banano = cantidad_banano * productos['banano']
    total_fresa = cantidad_fresa * productos['fresa']
    total = total_manzana + total_banano + total_fresa

    # Verificar si se aplica descuento
    total_con_descuento = aplicar_descuento(total)

    # Mostrar el total a pagar (con o sin descuento)
    print(f"Total a pagar: ${total_con_descuento}")

    # Realizar la compra
    confirmacion = input("¿Desea realizar la compra? (s/n): ")
    if confirmacion.lower() == "si":
        print("Gracias por su compra. ¡Hasta luego!")
    else:
        print("Compra cancelada. ¡Hasta luego!")

else:
    print("Nombre de usuario o contraseña incorrectos. Inicio de sesión fallido.")