#contar texto

def contarPalabras(archivo):

    diccionario = {}

    with open(archivo, 'r') as file:

        contenido = file.read()
        contenido = contenido.lower()
        contenido = contenido.replace(',', '').replace('.', '')

        palabras = contenido.split()

        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1

    return diccionario

archivo_elegido = 'texto.txt'

resultado = contarPalabras(archivo_elegido)

for palabra, cuenta in resultado.items():
    print(f'{palabra}: {cuenta}')