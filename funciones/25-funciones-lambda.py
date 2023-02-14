# Lambda es una manera de crear funciones anónimas (no tiene nombre) que luego se pueden almacenar en variables.
# No se recomienda cuando hay que dar más de una intrucción
# Beneficios
# -> Lo podemos utilizar cuando queremos hacer algo sencillo y rápido.
# -> Retornan automáticamente


# Creando una funcion lambda para multiplicar por dos
multiplicar_por_dos= lambda x : x*2
print(multiplicar_por_dos(5))


# definiendo una lista de números 
numeros = [1,2,3,4,5,6,7,8,9]

# creando función comun para ver si es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
# usando filter con una función común

numeros_pares=filter(es_par,numeros)

print(list(numeros_pares))


# Creando lo mismo pero con funcion lambda

numeros_pares_lambda = filter(lambda numero: numero % 2 == 0, numeros)

print(list(numeros_pares_lambda))




