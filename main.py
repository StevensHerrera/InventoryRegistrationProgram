#Se crea la variable producto
producto= float(input("Ingrese nombre del producto: "))
while True:
    try:
        precio_producto=float(input("Ingrese precio del producto: $ "))
        cantidad_producto=int(input("Ingrese cantidad del producto: "))