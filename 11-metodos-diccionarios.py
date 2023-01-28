# Métodos de deiccionarios 
diccionario = {
    "nombre" : "lucas",
    "apellidos" : "dalto",
    "subs" : 100000
}


# Keys() -> devuelve las claves 
claves = diccionario.keys()
print(claves)

# get() -> devuelve el valor de una clave
#       -> si no encuentra nada el programa continua

valor_de_clave = diccionario.get("nombre")
print(valor_de_clave)


# pop() -> elimina un elemento
eliminar_pop = diccionario.pop("apellidos")
print(eliminar_pop, diccionario)

# items() -> para iterar 
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# clear() -> elimina todos los elementos 
diccionario.clear()
print(diccionario)



