def elementos_unicos(lista):
    lista_unicos = list(set(lista))
    return lista_unicos
lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 5]
lista_sin_duplicados = elementos_unicos(lista_original)
print("Lista original:", lista_original)
print("Lista con elementos únicos:", lista_sin_duplicados)
