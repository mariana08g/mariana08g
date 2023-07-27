def calcular_hipotenusa():
    try:
        cateto_a = float(input("Ingrese la longitud del primer cateto: "))
        cateto_b = float(input("Ingrese la longitud del segundo cateto: "))

        # Calcular la hipotenusa utilizando el Teorema de Pitágoras (hipotenusa^2 = cateto_a^2 + cateto_b^2)
        hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

        print("La longitud de la hipotenusa es:", hipotenusa)
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_hipotenusa()
