#Crear funcion simple

# def saludar():
#     print("Holas Lucas")

# Ejecutar funcion simple
# saludar ()


# Cear funcion con parámetros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "f":
        adjetivo = "reina"
    elif sexo =="m":
        adjetivo = "titán"
    else:
        adjetivo = "amor"

    print(f"Hola {nombre} mi {adjetivo}, como andas?")



saludar("Camila","f")
saludar("Camila","F")
saludar("Lucas","m")
saludar("Lucas","t")


# Crear una funcion que retorne multiples valores

def crear_pass_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    passw = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return passw,num

# Desempaquetar el retorno de la funcion
password_rand, primer_num = crear_pass_random(5)

# Mostrando los resultados
print(f"Tu contraseña nueva es: {password_rand}")
print(f"El número utilizado para crearla fue: {primer_num}")





