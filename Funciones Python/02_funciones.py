import math

def area_cuadrado(lado):
    return lado * lado

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return 0.5 * base * altura

def main():
    print("Calculadora de áreas de figuras geométricas")
    print("------------------------------------------")
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Triángulo")
    opcion = int(input("Elija una opción (1/2/3): "))

    if opcion == 1:
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        print("El área del cuadrado es:", area_cuadrado(lado))
    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
    else:
        print("Opción inválida. Por favor, elija una opción válida (1/2/3).")

if __name__ == "__main__":
    main()
