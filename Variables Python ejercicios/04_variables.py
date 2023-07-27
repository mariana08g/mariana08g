def calcular_edad():
    try:
        año_actual = int(input("Ingrese el año actual: "))
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))

        # Calcular la edad restando el año de nacimiento del año actual
        edad = año_actual - año_nacimiento

        # Validar que el año de nacimiento no sea mayor al año actual
        if edad < 0:
            print("Error: El año de nacimiento no puede ser mayor al año actual.")
        else:
            print("Su edad es:", edad, "años.")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_edad()
