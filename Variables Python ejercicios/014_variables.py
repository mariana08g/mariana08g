def transformar_distancia():
    try:
        distancia_metros = float(input("Ingrese la distancia en metros: "))

        # Transformar a kilómetros, centímetros y milímetros
        distancia_kilometros = distancia_metros / 1000
        distancia_centimetros = distancia_metros * 100
        distancia_milimetros = distancia_metros * 1000

        print("La distancia en diferentes unidades es:")
        print(f"{distancia_kilometros:.3f} kilómetros")
        print(f"{distancia_centimetros:.2f} centímetros")
        print(f"{distancia_milimetros:.1f} milímetros")
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    transformar_distancia()
