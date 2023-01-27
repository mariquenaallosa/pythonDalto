#LIST -> crea una lista
# funcion
lista = list(["hola","dalto",34])

#LEN -> cantidad de elementos de la lista
lista_len = len(lista)
print (lista_len)

#APPEND -> agrega un elemento a la lista
# modifica la lista
lista.append("chau")
print(lista)
#INSERT -> agrega un elemento a la lista en un índice específico
lista.insert(2,"adios")
print(lista)

#EXTEND -> agrega varios elementos a la lista
lista.extend([False, 20.3])
print(lista)


#POP -> elimina un elemento de una lista, pide indice y devuelve valor
lista.pop(0)
print(lista)
#REMOVE -> remueve un elemento de una lista, pide valor
lista.remove("adios")
print(lista)
#CLEAR -> remove todos los elementos de una lista

lista.clear()
print(lista)


lista.extend([False, 20.3,34,2,5])

#SORT -> ordena una lista de forma ascendente a descendente
# (si usamos el parametro reverse=True lo ordena al revés)
lista.sort()
print(lista)
#REVERSE -> invierte el orden de una lista
lista.reverse()
print(lista)



# LO UNICO QUE PODEMOS ES HACER CON UN TUPLA ES CONTAR CUANTOS ELEMENTOS TIENEN
# Y USAR LA FUNCION INDEX ->> BUSCA LA POSICION EN LA QUE ESTÁ

 # LAS TUPLAS Y LOS CONJUNTOS(SET) SON INMUTABLES


# CONJUNTOS -> SÓLO SE PUEDEN SACAR ELEMENTOS Y REMOVER ELEMENTOS