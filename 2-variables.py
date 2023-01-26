a = 2 
b = 3

c = a + b

print(c)

# Definiendoo una variable con camelCase
nombreCompleto = "Lucas Dalto"
print(nombreCompleto)

# Definiendoo una variable con sanke_case (es el recomendable)
nombre_completo = "Lucas"
print(nombre_completo)



# concatenar con fStrings -> para concatenar sin problemas de tipos de datos

bienvenida = f"Hola {nombreCompleto} ¿Cómo estás?"

print(bienvenida)

# concatenar con  + 
bienvenida = "Hola " + "¿Cómo estás?"

print(bienvenida)

# operadores de pertenecia (in - not in)
print("ola" in bienvenida) #true
print("pedro" in bienvenida) #false
print("pedro" not in bienvenida) #true

# Borrar datos -> Hacer que una variable no esté más declarada 
del bienvenida
