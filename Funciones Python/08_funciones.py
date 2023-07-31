def contar_letras_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas
cadena_ejemplo = "Hola!"
mayusculas, minusculas = contar_letras_mayusculas_minusculas(cadena_ejemplo)

print("Número de letras mayúsculas:", mayusculas)
print("Número de letras minúsculas:", minusculas)
