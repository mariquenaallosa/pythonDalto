diccionario = {
    "nombre":"Lucas",
    "apellido": "Dalto",
    "subs": 1000
}

# Recorrer diccionario para obtener claves
for key in diccionario:
    print(f"La clave es: {key}")

# Recorrer diccionario con .items() 
#-> nos devuelve una tupla(clave,valor)
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor correspondiente a la clave es: {value}")