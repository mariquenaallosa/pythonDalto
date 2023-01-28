cadena1= "Hola, soy Dalto"
cadena2 = "Bienvenido"

# DIR -> Devuelve la lista de atributos válidos del objeto pasado 
# funcion
print(dir(cadena1))

# UPPER -> convierte a mayusculas
mayus = cadena1.upper()
# LOWER -> convierte a minusculas
minus = cadena1.lower()
# CAPITALIZE -> primera en mayúscula
capit = cadena1.capitalize()

# FIND -> método encuentra la primera aparición del valor específicado, sino devuelve -1. Posicion de la primera letras
find = cadena1.find("soy")
# INDEX -> método encuentra la primera aparición del valor específicado, sino devuelve una excepcion(muy importante lo de la excepcion)
ind = cadena1.index("soy")


#ISNUMERIC -> si es numerico devuelve true
numeric = cadena1.isnumeric()
#ISALPHA -> si es alfa numérico devuelve true
# espacio no es alfanumerico así que siempre que tenga espacios me tira False
alphanumeric = cadena1.isalpha()
# COUNT -> devuelve el número de ocurrencias de una subcadena dada.
# nos dice cuantas veces encontró la coincidencia de una cadena dentro de otra cadena
contar_coincidencia = cadena1.count("a")
# LEN -> cuenta los caracteres de una cadena
# FUNCION
contar_len = len(cadena1)

# STARSWITH -> virifica si una cadena comienza con 
empieza = cadena1.startswith("H")
# ENDSWITH -> virifica si una cadena termina con 
termina = cadena1.startswith("e")


# REPLACE -> reemplaza un valor por otro 
# cadena_nueva = cadena_vieja.replace(viejo, nuevo)
cadena_nueva = cadena1.replace("la", "lu")
cadena_nueva = cadena1.replace(",", " ")
cadena_nueva_2= cadena_nueva.capitalize()

# SPLIT -> separa por un parametro dado
# nos devuelve una lista
cadena_separada = cadena1.split(",")


print(cadena_separada)