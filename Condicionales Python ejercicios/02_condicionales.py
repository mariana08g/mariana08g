def verificar_edad():
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))

        if edad < 0 or edad > 100:
            print("Por favor, ingrese una edad válida (entre 0 y 100 años).")
        elif edad >= 18:
            print(f"{nombre}, usted es mayor de edad.")
        else:
            print(f"{nombre}, usted es menor de edad.")
    except ValueError:
        print("Error: Ingrese solo un número entero válido para la edad.")

if __name__ == "__main__":
    verificar_edad()
