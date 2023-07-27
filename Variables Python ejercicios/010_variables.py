def calcular_salario():
    try:
        salario_diario = float(input("Ingrese el salario diario del empleado: "))
        dias_trabajados = int(input("Ingrese el número de días trabajados: "))

        # Calcular el salario bruto (sin descuentos)
        salario_bruto = salario_diario * dias_trabajados

        # Calcular los descuentos de pensión y salud
        descuento_pension = salario_bruto * 0.10
        descuento_salud = salario_bruto * 0.15

        # Calcular el salario neto (con descuentos)
        salario_neto = salario_bruto - descuento_pension - descuento_salud

        print("El salario neto a pagar al empleado es:", salario_neto)
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_salario()
