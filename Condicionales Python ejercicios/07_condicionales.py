def imprimir_orden_ascendente_descendente():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        # Ordenar en forma ascendente utilizando condicionales
        if num1 <= num2 and num1 <= num3:
            menor = num1
            if num2 <= num3:
                medio = num2
                mayor = num3
            else:
                medio = num3
                mayor = num2
        elif num2 <= num1 and num2 <= num3:
            menor = num2
            if num1 <= num3:
                medio = num1
                mayor = num3
            else:
                medio = num3
                mayor = num1
        else:
            menor = num3
            if num1 <= num2:
                medio = num1
                mayor = num2
            else:
                medio = num2
                mayor = num1

        print("Números en orden ascendente:", menor, medio, mayor)
        print("Números en orden descendente:", mayor, medio, menor)

    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    imprimir_orden_ascendente_descendente()
