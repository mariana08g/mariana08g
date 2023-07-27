def calcular_precio_compra(num_llantas):
    if num_llantas < 6:
        precio_unitario = 240000
    elif num_llantas <= 7:
        precio_unitario = 221000
    else:
        precio_unitario = 180000

    total_pagar = num_llantas * precio_unitario
    return total_pagar

if __name__ == "__main__":
    try:
        cantidad_llantas = int(input("Ingrese el número de llantas que desea comprar: "))
        if cantidad_llantas < 0:
            print("Error: Ingrese un número de llantas válido (mayor o igual a cero).")
        else:
            precio_compra = calcular_precio_compra(cantidad_llantas)
            print(f"El valor total a pagar es: ${precio_compra}")
    except ValueError:
        print("Error: Ingrese solo un número entero válido.")
