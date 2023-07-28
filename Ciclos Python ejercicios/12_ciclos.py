def patron_Z(filas):
    for i in range(filas):
        for j in range(filas):
            if i == 0 or i == filas - 1:
                print('*', end=' ')
            elif i + j == filas - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Pedir al usuario el número de filas para el patrón Z
try:
    num_filas = int(input("Ingrese el número de filas para el patrón Z: "))
    if num_filas < 3:
        print("El patrón Z no puede generarse con menos de 3 filas.")
    else:
        patron_Z(num_filas)
except ValueError:
    print("Error: Ingrese un número entero válido.")
