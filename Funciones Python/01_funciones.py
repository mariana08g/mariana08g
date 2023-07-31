def comprar (x, y ,z):
    may = 0
    if x > y:
        if x < z: 
            may = x
        else: 
            
            may= z
    elif y > z:
        may = y
    else: 
        may = z
    return may 
x = float(input("digite un numero: "))
y = float(input("digite un numero: "))
z = float("digite un numero: ")
print( comprar(x, y, z))
        
        