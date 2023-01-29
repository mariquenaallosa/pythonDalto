# forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
    return numeros_sumados

resultado = suma([3,5,6])
print(resultado)


# Utilizar el operador * como argumento (*args) 
def sumar(nombre,*numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"


resultado = sumar("Lucas",3,6,7,3,5,76)
print(resultado)


# *args como parametro 
# -> tambien se puede utilizar para desglosar
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([3,6,7,3,5,76])
print(resultado2)