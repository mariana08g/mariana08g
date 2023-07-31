def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado
lista_muestra = (8, 2, 3, -1, 7)
resultado = multiplicar_lista(lista_muestra)
print("Resultado esperado:", resultado)  
