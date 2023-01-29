numeros = [4,7,1,42,15]

# Funciona con tuplas, listas, y sets 



# encontrar el máximo valor de una lista
numero_max= max(numeros)
print(numero_max)

# encontrar el minimo valor de una lista
numero_min= min(numeros)
print(numero_min)

# redondear a x digitos 
# round(numero,cantidad de decimales)
# por defecto la casntidad de decimales es 0 

numero = round(12.3456346,2)
print(numero)


# bool () 
# retorna :
#   False -> 0 , vacio , False , None
#   True -> distinto de 0, True, cadena, datos no vacios

resultado_bool = bool(0)
print(resultado_bool)

# all()
# retorna :
# True -> si todos los valores son verdaderos
resultado_all = all([123,"true",[1,2,3]]) # verdadero
print(resultado_all)
resultado_all = all([0,"true",[1,2,3]]) # falso
print(resultado_all)


# sum()
# -> suma todos los valores de un iterable

resultado_sum = sum(numeros)
print(resultado_sum)