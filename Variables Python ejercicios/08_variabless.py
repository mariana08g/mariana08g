def calcular_promedio():
    try:
        numeros = []
        for i in range(5):
            numero = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)

        # Calcular el promedio
        promedio = sum(numeros) / len(numeros)

        print("El promedio de los números ingresados es:", promedio)
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_promedio()
