def calcular_cuadrado():
    try:
        numero = float(input("Ingrese un número: "))
        cuadrado = numero ** 2
        print("El cuadrado de", numero, "es:", cuadrado)
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    calcular_cuadrado()
