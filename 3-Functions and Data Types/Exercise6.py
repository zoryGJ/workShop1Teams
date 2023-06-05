def reverse_string(string):
    return string[::-1]


texto = str(input('Por favor ingrese una cadena de texto: '))
reversa = reverse_string(texto)
print(f'la cadena invertida es: {reversa}')

