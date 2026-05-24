inventario = []

def mostrar_menu():
    print("\n=== INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = int(input("Precio: "))
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print(f"✓ {nombre} agregado correctamente")

def mostrar_productos():
    if len(inventario) == 0:
        print("El inventario está vacío")
        return
    print("\n--- PRODUCTOS ---")
    for i, producto in enumerate(inventario):
        print(f"{i+1}. {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")

def buscar_producto():
    nombre = input("¿Qué producto buscas? ").lower()
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == nombre:
            print(f"✓ Encontrado → Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado")

def eliminar_producto():
    nombre = input("¿Qué producto eliminar? ").lower()
    for producto in inventario:
        if producto["nombre"].lower() == nombre:
            inventario.remove(producto)
            print(f"✓ {producto['nombre']} eliminado")
            return
    print("Producto no encontrado")
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")