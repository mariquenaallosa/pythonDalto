ingreso_mensual = 100000

if ingreso_mensual > 10000:
    print ("Estás bien económicamente en cualquier parte del mundo")
elif ingreso_mensual > 10000:
    print ("Estás bien económicamente en LATAM")
elif ingreso_mensual > 500:
    print ("Estás bien económicamente en Argentina")
elif ingreso_mensual > 200:
    print ("Estás bien económicamente en Venezuela")
else:
    print("Sos pobre")

    
# if anidados
ingreso_mensual = 100000
gasto_mensual = 4000

if ingreso_mensual > 10000:
    if gasto_mensual < 7000:
        print ("Estás bien económicamente en cualquier parte del mundo")
    else:
        print("Tenes buenas ganacias pero podrias ajustar tus gastos")
elif ingreso_mensual > 10000:
    print ("Estás bien económicamente en LATAM")
elif ingreso_mensual > 500:
    print ("Estás bien económicamente en Argentina")
elif ingreso_mensual > 200:
    print ("Estás bien económicamente en Venezuela")
else:
    print("Sos pobre")