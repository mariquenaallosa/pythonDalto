# LISTAS Y TUPLAS SE ITERAN DE LA SIGUIENTE MANERA


animales = ["gato","perro","loro", "cocodrilo"]

for animal in animales : 
    print (animal)


numeros= [0,1,2,3]
for numero in numeros :
    resultado = numero * 2
    print (resultado)


# iterar ambas listas 
# -> deben tener la misma cantidad de elementos 


for numero,animal in zip(animales,numeros):
    print(f"Recorriendo la lista 1 {numero}")
    print(f"Recorriendo la lista 2 {animal}")



for num in range(5,12):
    print(num)




for nume in range(20):
    print(nume)

# forma no optima de recorre una lista por su indice 
#-> NO FUNCIONA en conjuntos
for numer in range(len(numeros)):
    print(numeros[numer])

# forma correcta de recorre una lista por su indice
# -> enumerate() nos devulve tuplas (indice, valor) 
#    para acceder a valor nos tocará ingresar por indice de tupla 
#    [0] -> para el índice
#    [1] -> para ver el valor
for num in enumerate(numeros):
    print(num)


# usando else 

for numero in numeros :
    print(numero)
else:
    print("El bucle terminó")


# for en una línea de código 

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)