while registrar:  
    producto = input("Nombre del producto: ").strip()
    
    if producto.upper() == 'FIN':
        registrar = False  # Cambia la condición para salir del bucle
    else:
        try:
            precio = float(input("Precio unitario: $"))
            cantidad = int(input("Cantidad vendida: "))
            
            subtotal = precio * cantidad
            total_general += subtotal
            
            if producto in ventas:
                ventas[producto]['cantidad'] += cantidad
                ventas[producto]['subtotal'] += subtotal
            else:
                ventas[producto] = {'cantidad': cantidad, 'subtotal': subtotal, 'precio_unitario': precio}
            
            print(f"Venta registrada: {cantidad} x {producto} = ${subtotal:.2f}\n")
            
        except ValueError:
            print("Error: Ingresa números válidos para precio y cantidad.\n")

