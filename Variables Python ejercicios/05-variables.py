def calcular_porcentaje():
    try:
        numero = float(input("Ingrese un número: "))
        porcentaje = numero * 0.2
        print("El 20% de", numero, "es:", porcentaje)
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    calcular_porcentaje()
