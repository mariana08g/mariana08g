def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos
    cadena_limpia = re.sub(r'[^a-zA-Z]', '', cadena.lower())
    # Comparar la cadena original con su reverso
    return cadena_limpia == cadena_limpia[::-1]
cadena_ejemplo = "Anita lava la tina"
if es_palindromo(cadena_ejemplo):
    print(f'"{cadena_ejemplo}" es un palíndromo.')
else:
    print(f'"{cadena_ejemplo}" no es un palíndromo.')
