from src.inventario import agregar_producto,ver_inventario,eliminar_producto,editar_producto,calcular_estadisticas
# Menú principal

while True:

    print("----- MENÚ -----")
    print("1. Agregar producto.")
    print("2. Ver inventario.")
    print("3. Editar producto.")
    print("4. Eliminar producto.")
    print("5. Total productos.")
    print("6. Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        ver_inventario()

    elif opcion == "3":
        editar_producto()

    elif opcion == "4":
        eliminar_producto()    

    elif opcion == "5":
        calcular_estadisticas()    

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.\n")