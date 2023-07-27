def calcular_raiz_cuadrada():
    try:
        numero = float(input("Ingrese un número: "))

        # Caso especial para el número 0
        if numero == 0:
            raiz_cuadrada = 0
        else:
            # Aproximación inicial
            raiz_cuadrada = numero / 2

            # Iteraciones para mejorar la aproximación
            for _ in range(10):
                raiz_cuadrada = 0.5 * (raiz_cuadrada + numero / raiz_cuadrada)

        print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    calcular_raiz_cuadrada()
