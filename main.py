
nombre_usuario_correcto = "samuel"
contraseña_correcta = "123"


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

   
    total_manzana = cantidad_manzana * productos['manzana']
    total_banano = cantidad_banano * productos['banano']
    total_fresa = cantidad_fresa * productos['fresa']
    total = total_manzana + total_banano + total_fresa


    print(f"Total a pagar: ${total}")

    confirmacion = input("¿Desea realizar la compra? (s/n): ")
    if confirmacion.lower() == "s":
        print("Gracias por su compra. ¡Hasta luego!")
    else:
        print("Compra cancelada. ¡Hasta luego!")

else:
    print("Nombre de usuario o contraseña incorrectos. Inicio de sesión fallido.")