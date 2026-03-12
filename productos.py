

products = []

def agregar_producto(nombre, precio, cantidad):
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    products.append(producto)

def mostrar_inventario():
    print("\n=== INVENTARIO ===")
    for producto in products:
        print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
    print("===================")
