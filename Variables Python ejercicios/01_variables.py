def multiplicar_tres_numeros():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))

        resultado = numero1 * numero2 * numero3

        print("El resultado de la multiplicación es:", resultado)
    except ValueError:
        print("Error: Ingrese solo números válidos.")

if __name__ == "__main__":
    multiplicar_tres_numeros()

