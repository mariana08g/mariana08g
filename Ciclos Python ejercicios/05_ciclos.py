n = int(input("ingrese el numero de limite:"))
anterior = 0
actual = 1 
resultado = 0
for i in range(n): 
    print(f"la suma es: {actual}")   
    resultado = actual + anterior 
    anterior = actual
    actual = resultado
    