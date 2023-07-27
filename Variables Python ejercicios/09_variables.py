def calcular_valor_compra():
    try:
        valor_unitario = float(input("Ingrese el valor unitario del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos comprados: "))

        # Calcular el valor sin IVA
        valor_sin_iva = valor_unitario * cantidad

        # Calcular el IVA (16% del valor sin IVA)
        iva = valor_sin_iva * 0.16

        # Calcular el valor total con IVA
        valor_total = valor_sin_iva + iva

        print("El valor total a pagar es:", valor_total)
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_valor_compra()
