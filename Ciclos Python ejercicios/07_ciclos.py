x = int(input("digite el numero para multiplicar:"))
multi = 0
print(f"la tabla de {x}es")
for i in range(1, 11):
    multi = x * i
    print(f"{x} x {i} = {multi}")
