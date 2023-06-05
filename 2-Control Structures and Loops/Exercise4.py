#numeros primos

try:
    num = int(input('Escribe el numero que quieres comprobar si es primo: '))

    def verificarPrimo(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    if verificarPrimo(num):
        print(f'{num} es un numero primo')
    else:
        print(f'{num} no es un numero primo')
except Exception as error:
    print(error)
    print('El programa fallo pero continua')