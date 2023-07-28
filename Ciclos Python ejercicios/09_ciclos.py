u = int(input("digite el limite: ")) 
patron = ""
for i in range(u + 2):
    patron = ""
    for d in range(1, i):
        patron = patron + (f"{d}")
    print(patron)