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
# nos dice cuantas veces encontró la coincidencia de
count
# LEN -> cuenta los caracteres de una cadena

# ATARSWITH -> virifica si una cadena comienza con 
# ENDSWITH -> virifica si una cadena termina con 

# REPLACE -> reemplaza un valor por otro 
# SPLIT -> separa por un parametro dado

print(alphanumeric)