def factorial(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
