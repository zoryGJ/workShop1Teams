#Grados F y  C
try:
    F = float(input('Ingrese la temperatua en Fahrenheit (F°) que desea convertir: '))

    def conversorCelsius(Fa):
        return (Fa - 32) * 5/9

    GradosConvertidos = conversorCelsius(F)

    print(f'La conversion a grados Celsius es: {GradosConvertidos}C°')
except Exception as error:
    print(error)
    print('El programa no se detuvo a pesar del error')