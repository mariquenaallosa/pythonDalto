# creando diccionarios con dict ()
# -> se puede usar para crear diccionarios vacíos
diccionario = dict(nombre="lucas",apellido="dalto")
print(diccionario)

# las listas no pueden ser claves porque son mutables
# los conjuntos tampoco podrían ser claves salvo que sean frozenset() 
# pero las tuplas si 
diccionario = {("dalto","rancio"):"rancio"}

print (diccionario)


# Crear diccionario con fromkeys()
# -> permite crear diccionarios con valores sin asignar es decir None
# -> MÉTODO de diccionario 
# -> itera el primer elemento entonces lo que hace es que la primera palabra se divida para ser claves 
#    para evitar esto hay que ingresar los valores como una lista

diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
