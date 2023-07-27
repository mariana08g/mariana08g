def calcular_pulsaciones(edad, genero):
    if genero == 1:  # Género femenino
        pulsaciones = (220 - edad) / 10
    elif genero == 2:  # Género masculino
        pulsaciones = (210 - edad) / 10
    else:
        print("Error: Ingrese un género válido (1 para femenino o 2 para masculino).")
        return None

    return pulsaciones

if __name__ == "__main__":
    try:
        edad = int(input("Ingrese su edad: "))
        genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))

        if edad < 0 or genero not in (1, 2):
            print("Error: Ingrese valores válidos para edad y género.")
        else:
            pulsaciones = calcular_pulsaciones(edad, genero)
            if pulsaciones is not None:
                print(f"El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: {pulsaciones:.2f}")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")
