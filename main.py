from src.inventario import (
    agregar_producto, ver_inventario, eliminar_producto,
    calcular_estadisticas,editar_producto,
    buscar_en_menu,ejecutar_carga_interactiva,guardar_datos
)
# ==============================
# MENÚ PRINCIPAL
# ==============================

while True:

    print("----- MENÚ -----")
    print("1. Agregar producto.")
    print("2. Ver inventario.")
    print("3. Editar producto.")
    print("4. Buscar producto.")
    print("5. Eliminar producto.")
    print("6. Total productos.")
    print("7. Guardar CSV.")
    print("8. Cargar CSV.")
    print("9. Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        ver_inventario()

    elif opcion == "3":
        editar_producto()
    
    elif opcion == "4":
        buscar_en_menu()

    elif opcion == "5":
        eliminar_producto()    

    elif opcion == "6":
        calcular_estadisticas()

    elif opcion == "7": 
            guardar_datos()

    elif opcion == "8": 
            ejecutar_carga_interactiva()    

    elif opcion == "9":
        confirmacion = input("¿Desea guardar los cambios en el CSV antes de salir? (S/N): ").upper()
        
        if confirmacion == "S":
            guardar_datos() # Llama a la función que ya definimos en src/inventario
            print("Datos guardados correctamente.")
            
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.\n")