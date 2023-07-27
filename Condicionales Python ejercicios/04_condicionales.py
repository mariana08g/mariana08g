def determinar_mayor_menor():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if numero1 > numero2:
            mayor = numero1
            menor = numero2
        elif numero1 < numero2:
            mayor = numero2
            menor = numero1
        else:
            print("Ambos números son iguales.")
            return

        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    determinar_mayor_menor()
