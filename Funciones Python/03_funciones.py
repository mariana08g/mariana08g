def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
lista_muestra = (8, 2, 3, 0, 7)
resultado = sumar_lista(lista_muestra)
print("Resultado esperado:", resultado)  
