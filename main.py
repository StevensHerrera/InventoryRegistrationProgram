# Solicitar el nombre del producto al usuario
nombre = input("Ingrese el nombre del producto: ")

# Solicitar y validar el precio del producto
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break  # Sale del ciclo si el valor es válido
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar y validar la cantidad del producto
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break  # Sale del ciclo si el valor es válido
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# Calcular el costo total multiplicando precio por cantidad
costo_total = precio * cantidad

# Mostrar los resultados en la consola
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")