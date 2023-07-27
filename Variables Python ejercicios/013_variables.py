def transformar_a_horas_minutos():
    try:
        tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))

        # Calcular horas, minutos y segundos
        horas = tiempo_segundos // 3600
        minutos = (tiempo_segundos % 3600) // 60
        segundos = tiempo_segundos % 60

        print(f"El tiempo de {tiempo_segundos} segundos es:")
        print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")
    except ValueError:
        print("Error: Ingrese solo un número válido.")

if __name__ == "__main__":
    transformar_a_horas_minutos()
