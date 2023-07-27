def determinar_par_impar_cero():
    try:
        numero = int(input("Ingrese un número: "))

        if numero == 0:
            print("El número es cero.")
        elif numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    except ValueError:
        print("Error: Ingrese solo un número entero válido.")

if __name__ == "__main__":
    determinar_par_impar_cero()
