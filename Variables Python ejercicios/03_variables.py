def calcular_distancia_recorrida():
    try:
        velocidad_kph = float(input("Ingrese la velocidad en kilómetros por hora (Km/h): "))
        tiempo_horas = float(input("Ingrese el tiempo en horas: "))

        # Convertir la velocidad de Km/h a Km/hora
        velocidad_kmhora = velocidad_kph

        # Calcular la distancia recorrida en Km
        distancia_km = velocidad_kmhora * tiempo_horas

        print("La distancia recorrida es:", distancia_km, "Km")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_distancia_recorrida()
