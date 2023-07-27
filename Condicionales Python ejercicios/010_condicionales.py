def calcular_total_pagar(cantidad, precio_unitario_original):
    if cantidad <= 5:
        total_pagar = cantidad * precio_unitario_original
    elif cantidad < 10:
        precio_con_descuento = precio_unitario_original * 0.95  # 5% de descuento
        total_pagar = cantidad * precio_con_descuento
    else:
        precio_con_descuento = precio_unitario_original * 0.92  # 8% de descuento
        total_pagar = cantidad * precio_con_descuento

    return total_pagar

if __name__ == "__main__":
    try:
        cantidad_articulos = int(input("Ingrese la cantidad de artículos a comprar: "))
        precio_unitario = float(input("Ingrese el precio unitario original: "))

        if cantidad_articulos < 0 or precio_unitario < 0:
            print("Error: Ingrese valores no negativos para cantidad de artículos y precio unitario.")
        else:
            total_pagar = calcular_total_pagar(cantidad_articulos, precio_unitario)
            print(f"El total a pagar es: ${total_pagar:.2f}")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")
