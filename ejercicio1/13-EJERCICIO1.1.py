# EJERCICIO 1

# duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

este_curso = 1.5


# crudo duracion
otros_crudo = 5

este_crudo = 3.5



# Diferencias de duración
diferencia_con_min = round(100 - este_curso / otros_cursos_min * 100)
diferencia_con_max = round(100 - este_curso / otros_cursos_max*100)
diferencia_con_promedio = round(100 - este_curso / otros_cursos_promedio * 100)

# mostrando diferencias de duracion
print("-------------------------------")
print("El curso de Dalto dura: ")
print (f"  - un {diferencia_con_min}% menos que el más rápido de los otros cursos")
print (f"  - un {diferencia_con_max}% menos que el más lento de los otros cursos")
print (f"  - un {diferencia_con_promedio}% menos que el promedio de los otros cursos")
print("-------------------------------")

# Diferencia de crudo para saber el tiempo vacío

timepo_vacio_promedio = round(100 - otros_cursos_promedio / otros_crudo * 100)
tiempo_vacio_dalto = round(100 - este_curso / este_crudo *100 )

# mostrando diferencia de tiempo vacío
print (f"Un curso promedio quita un {timepo_vacio_promedio}% de tiempo vacío")
print (f"Este curso de Dalto quita un {tiempo_vacio_dalto}% de tiempo vacío")
print("-------------------------------")





# Diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a {round(otros_cursos_promedio /este_curso *10)} de otro curso")
print(f"Ver 10 horas de otro curso equivale a {round(este_curso /otros_cursos_promedio *10)} de este curso")
print("-------------------------------")
