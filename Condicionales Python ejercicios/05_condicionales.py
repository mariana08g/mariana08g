def calcular_promedio_aprobacion():
    try:
        nota1 = float(input("Ingrese la nota 1 (0.0 - 5.0): "))
        nota2 = float(input("Ingrese la nota 2 (0.0 - 5.0): "))
        nota3 = float(input("Ingrese la nota 3 (0.0 - 5.0): "))

        # Calcular el promedio de las notas
        promedio = (nota1 + nota2 + nota3) / 3

        print(f"El promedio del estudiante es: {promedio:.2f}")

        if promedio >= 3.0:
            print("Aprobó.")
        else:
            print("No aprobó.")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos entre 0.0 y 5.0.")

if __name__ == "__main__":
    calcular_promedio_aprobacion()
