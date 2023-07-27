def calcular_area_cuadrado():
    try:
        lado = float(input("Ingrese la longitud de un lado del cuadrado: "))

        # Calcular el área del cuadrado (área = lado * lado)
        area = lado ** 2

        print("El área del cuadrado es:", area)
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    calcular_area_cuadrado()
