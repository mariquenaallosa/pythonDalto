# faltó el profe y los alumnos van a armar la clase

# Pedir el nombre y la edad de los compañeros que vinieron a clase

# pedir la cantidad de alumnos presentes
cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "));

# funcion para obtener al asistente y profesor segun edad
def obtener_compañeros(cantidad_de_alumnos):
    compañeros = [];


    # for para pedir info de cada alumno
    for i in range(cantidad_de_alumnos):
        nombre = input("Ingrese el nombre del alumno: ");
        edad = int(input("Ingrese la edad del alumno: "));
        compañero = (nombre, edad);
        
        #agregar info
        compañeros.append(compañero);

    # ordenar de menor a mayor edad
    compañeros.sort( key = lambda x: x[1] );
    asistente = compañeros[0][0];
    profesor = compañeros[-1][0];
    return asistente, profesor;

asistente,profesor = obtener_compañeros(cantidad_de_alumnos);

print("El asistente es: " + asistente + " y el profesor es: " + profesor);



    



