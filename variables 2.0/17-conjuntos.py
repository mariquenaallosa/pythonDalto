# Crear conjuntos con set ()
conjunto = set(["dato1",])
print(conjunto)
print("---------------------------")


# Meter conjunto dentro de otro conjunto
# frozenset
# -> crea un conjunto inmutable que puede estar congelado para que sea hasheable
print("Meter conjunto dentro de otro conjunto")
print("---------------------------")

conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)
print("---------------------------")

# Teoría de conjuntos
print("Teoría de conjuntos")
print("---------------------------")
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

# Verificar si es un subconjunto

resultado1 = conjunto3.issubset(conjunto4)
resultado2 = conjunto4.issubset(conjunto3)


#otra forma de verificar 
resultado3 = conjunto4 <= conjunto3

#Mostrar resultados
print("Subconjunto")
print (resultado1)
print (resultado2)
print (resultado3)
print("---------------------------")

# Verificar si es un superconjunto 
resultado4 = conjunto3.issuperset(conjunto4)
resultado5 = conjunto4.issuperset(conjunto3)

#otra forma de verificar 
resultado6 = conjunto3 > conjunto4

#Mostrar resultados
print("Superconjunto")
print (resultado4)
print (resultado5)
print (resultado6)
print("---------------------------")

# Verificar si hay algún número en común
# isdisjonit() -> True cuando no hay ningún elemento en común

resultado7 = conjunto4.isdisjoint(conjunto3)
print(resultado7)
