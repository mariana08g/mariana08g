import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return 0.5 * (base_mayor + base_menor) * altura

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Calcular área del cuadrado")
    print("2. Calcular área del rectángulo")
    print("3. Calcular área del triángulo")
    print("4. Calcular área del círculo")
    print("5. Calcular área del rombo")
    print("6. Calcular área del trapecio")
    print("7. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            lado = float(input("Ingrese la longitud del lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print("El área del cuadrado es:", area)
        elif opcion == 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == 3:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == 4:
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area)
        elif opcion == 5:
            diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
            area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
            print("El área del rombo es:", area)
        elif opcion == 6:
            base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = calcular_area_trapecio(base_mayor, base_menor, altura)
            print("El área del trapecio es:", area)
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida del menú.")
