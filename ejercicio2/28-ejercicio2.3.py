# Creando una función que muestre la serie de fibonacci entre 0 y el número pasado por parámetro

numero = int(input("Ingrese un número: "))


def fibonacci(numero):
    a,b = 0,1
    for i in range(numero):
        if a+b > numero: return numero
        else: a,b = b,a+b
    return numero


print(fibonacci(numero))