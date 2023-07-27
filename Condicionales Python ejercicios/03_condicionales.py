def determinar_positivo_negativo_cero():
    try:
        numero = float(input("Ingrese un número: "))

        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es cero.")
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    determinar_positivo_negativo_cero()
