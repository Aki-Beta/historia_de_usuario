print("DAILY SALES RECORD")
print("Type 'END' when you finish the day's record.")


# Resumen de Ventas
print("\n=== RESUMEN DEL DÍA ===")
print(f"{'Producto':<20} {'Cant.':<8} {'Precio U.':<10} {'Total':<10}")
print("-" * 50)

for producto, datos in ventas.items():
    print(f"{producto:<20} {datos['cantidad']:<8} ${datos['precio_unitario']:<10.2f} ${datos['subtotal']:<10.2f}")

print("-" * 50)
print(f"{'TOTAL GENERAL':<38} ${total_general:.2f}")
