#Numeros Fibonacci
try:
    numeros = 10

    a , b = 0 , 1

    cont = 0

    while cont < numeros:
        print(a)
        a, b = b, a + b
        cont += 1
except Exception as error:
    print(error)
    print('El programa fallo pero sigue corriendo')