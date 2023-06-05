
try:
    def find_maximum(lista):
        return max(lista)
    
    listado = [5, 6, 20, 50, 100, 8, 10, 320, 4]

    mayor = find_maximum(listado)
    print(f'el numero mayor de la lista es: {mayor}')
except Exception as error:
    print(error)
    print('El programa presento un error pero continua')