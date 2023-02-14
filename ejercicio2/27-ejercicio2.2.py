# Crear una funcion que nos devuelva los números primos entre 0 y el número que pasamos
#pedir numero al usuario
numero = int(input("Ingrese un número para obtener la lista de números primos: "))

# funcion que nos devueva si es primo o no 
def es_primo(numero):
    # verificar que el número no se pueda dividir por numeros entre 0 y numero-1
    for i in range(2,numero-1):
        # si es divisible por alguno retornamos false y termina el bucle
        if numero % i == 0: return False
    # si no es divisible por alguno retornamos true, significa que el número es primo
    return True
    
# funcion que retorna una lista con los números primos
def primos_hasta(numero):
    primos=[]
    for i in range(3,numero+1):
        resultado = es_primo(i)
        if resultado== True:
            primos.append(i)
            
    return primos
    

resultado = primos_hasta(numero)
print(resultado)
