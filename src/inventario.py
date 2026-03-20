# Aca se definen las funciones para llamarlas en el archivo main
# Crear una lista para guardar los productos
inventario = []


# Función para agregar un producto
def agregar_producto():
    # Pedir nombre del producto
    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para el precio.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # Calcular total
    costo_total = precio * cantidad

    # Guardar producto en el inventario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": costo_total,
    }

    inventario.append(producto)

    print("Producto agregado correctamente.\n")
    
"""
# Función para ver el inventario
def ver_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        print("\n--- INVENTARIO ---")
        for i, producto in enumerate(inventario):
            print(
                str(i + 1)
                + ". Producto: "
                + producto["nombre"]
                + " | Precio: "
                + str(producto["precio"])
                + " | Cantidad: "
                + str(producto["cantidad"])
                + " | Total: "
                + str(producto["total"])
            )
        print()
"""

def ver_inventario():
    if not inventario:  # En Python, una lista vacía se evalúa como False
        print("El inventario está vacío.\n")
        return

    print("\n--- INVENTARIO ---")
    for i, p in enumerate(inventario, start=1):
        # Usamos f-strings para formatear todo de una vez
        print(f"{i}. Producto: {p['nombre']:15} | Precio: ${p['precio']:>6.2f} | "
              f"Cant: {p['cantidad']:>3} | Total: ${p['total']:>8.2f}")
    print()

# Función para editar un producto
def editar_producto():
    if not inventario:
        print("No hay productos para editar.\n")
        return

    ver_inventario()
    try:
        opcion = int(input("Ingrese el número del producto que desea editar: "))
        indice = opcion - 1

        if 0 <= indice < len(inventario):
            p = inventario[indice]
            print(f"\nEditando: {p['nombre']}")
            print("(Presione Enter para mantener el valor actual)")

            # Editar Nombre
            nuevo_nombre = input(f"Nombre [{p['nombre']}]: ")
            if nuevo_nombre:
                p['nombre'] = nuevo_nombre

            # Editar Precio
            nuevo_precio = input(f"Precio [{p['precio']}]: ")
            if nuevo_precio:
                p['precio'] = float(nuevo_precio)

            # Editar Cantidad
            nueva_cantidad = input(f"Cantidad [{p['cantidad']}]: ")
            if nueva_cantidad:
                p['cantidad'] = int(nueva_cantidad)

            # Recalcular el total automáticamente
            p['total'] = p['precio'] * p['cantidad']
            
            print("Producto actualizado con éxito.\n")
        else:
            print("Número fuera de rango.\n")

    except ValueError:
        print("Error: Ingrese un valor válido.\n")

# Función para eliminar un producto
def eliminar_producto():
    if len(inventario) == 0:
        print("No hay productos para eliminar.\n")
        return

    ver_inventario()

    while True:
        try:
            indice = int(input("Ingrese el número del producto a eliminar: "))

            if 1 <= indice <= len(inventario):
                inventario.pop(indice - 1)
                print("Producto eliminado.\n")
                break
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Ingrese un número válido.")

# Función para ver el total de los productos en el inventario
def calcular_estadisticas():
    if not inventario:
        print("El inventario está vacío. No hay estadísticas que calcular.\n")
        return

    # Sumamos todos los totales y todas las cantidades
    valor_total_inventario = sum(p['total'] for p in inventario)
    cantidad_total_productos = sum(p['cantidad'] for p in inventario)
    total_tipos_productos = len(inventario)

    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Total de productos (stock total): {cantidad_total_productos}")
    print(f"Tipos de productos registrados:  {total_tipos_productos}")
    print(f"Valor total del inventario:      ${valor_total_inventario:,.2f}")
    print("-" * 35 + "\n")
