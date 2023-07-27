def tipo_de_pago(cuenta):
    if cuenta < 150000:
        return "Efectivo"
    elif cuenta <= 300000:
        return "Celular (dinero electrónico)"
    elif cuenta <= 600000:
        return "Tarjeta de débito"
    else:
        return "Tarjeta de crédito"

if __name__ == "__main__":
    try:
        monto_cuenta = float(input("Ingrese el monto de la cuenta: "))
        decision_pago = tipo_de_pago(monto_cuenta)
        print(f"El tipo de pago recomendado es: {decision_pago}")
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos.")
