x = int(input("ingrese el numero de filas: "))
numero = 1
for i in range(x+1):
    for j in range(x-i):
        print(end = " ")
    for j in range(i):
        print(numero, end = " ")
        numero += 1
    print()