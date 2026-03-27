import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario está vacío. No hay nada que guardar.")
        return
    try:
        # Crea la carpeta si no existe
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            if incluir_header:
                writer.writeheader()
            for p in inventario:
                writer.writerow({"nombre": p["nombre"], "precio": p["precio"], "cantidad": p["cantidad"]})
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"Error de permisos o escritura: {e}")

def cargar_csv(ruta):
    productos_cargados = []
    errores = 0
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    nombre = fila["nombre"].strip()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    if precio < 0 or cantidad < 0 or not nombre: raise ValueError
                    productos_cargados.append({
                        "nombre": nombre, "precio": precio, 
                        "cantidad": cantidad, "total": precio * cantidad
                    })
                except:
                    errores += 1
        return productos_cargados, errores
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None, 0
