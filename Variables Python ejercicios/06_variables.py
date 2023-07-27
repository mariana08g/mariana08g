def calcular_porcentajes():
    try:
        numero = float(input("Ingrese un número: "))
        treinta_porcentaje = numero * 0.3
        sesenta_porcentaje = numero * 0.6
        noventa_porcentaje = numero * 0.9

        print("El 30% de", numero, "es:", treinta_porcentaje)
        print("El 60% de", numero, "es:", sesenta_porcentaje)
        print("El 90% de", numero, "es:", noventa_porcentaje)
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    calcular_porcentajes()
