# Listas 
# -> Sirve para grupar datos
# -> SE PUEDEN MODIFICAR
lista = ["Lucas", "Soy Daalto", True , 1.85]

# completo
print(lista)
# por posición
print(lista[0])


# Tuplas 
# -> similar a las listas pero ocupan () 
# -> NO SE PUEDE MODIFICAR
tupla = ("Lucas", "Soy Daalto", True , 1.85)
print(tupla)
print(tupla[0])

# Es válido
lista[3]= False



# No es válido
 # tupla[3]= False Error

print(lista[3])



# Conjunto (set)
# -> No tienen un orden fijo, es desordenado
# -> Se puede modificar el conjunto pero no cada elemento por separado
# -> No se puede acceder por indice a un elemento del conjunto, se hace con un bucle únicamente
# -> No permite repetir valores


conjunto = {"Lucas", "Soy Daalto", True , 1.85}
print(conjunto)
print(conjunto)



# Diccionario(dict)
# -> Desordenado
# -> Similar a JSON en JS (clave:valor)
diccionario = {
    "nombre":"Lucas",
    "apellido": "Dalto",
    "esta_emocionado": True,
    "canal_yt" : "Soy Dalto",
    "altura": 1.84,
    "dato_duplicado": "Soy Dalto"

}

print(diccionario)
print(diccionario["nombre"])
# print(diccionario[key])