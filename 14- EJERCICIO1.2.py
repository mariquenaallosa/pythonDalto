palabras_promedio = 2
palabras_dalto = palabras_promedio + palabras_promedio * 0.3



frase = input("Decime una frase y calculo cuanto tardas en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

duracion = cantidad_de_palabras *10 // palabras_promedio / 10
duracion_dalto = cantidad_de_palabras* 10 // palabras_dalto / 10

print("------------------------------------------")
print (f"Dijiste {cantidad_de_palabras} palabras, y tardarias aproximadamente {duracion} segundos en decirlo")
print (f"Dalto lo diriía en {duracion_dalto} segundos")
print("------------------------------------------")


if  duracion >= 60:
    print("Pará flaco, te pedi una frase, no un testamento")
else :
    print(f"Tardarias en decirla aproximadamente {duracion} segundos")
