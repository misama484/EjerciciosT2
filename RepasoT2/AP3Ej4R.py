
def ej4():
    # Ej4
    # Escribe un programa que almacene en un diccionario los precios de las frutas
    # y verduras de la tabla. Deberá preguntarle al usuario por una fruta o verdura
    # y un peso en kg., mostrándole por pantalla el importe de esa cantidad de fruta
    # o verdura. Si la fruta o verdura no se encuentra en el diccionario, deberá
    # informar al usuario.

    # "Pimiento italiano": 1.35,
    # "Mandarina": 0.80,
    # "Banana": 1.25,
    # "Tomate del perello": 2.65

    # declaramos el diccionario
    frutas = {"Pimiento italiano": 1.35,
              "Mandarina": 0.80,
              "Banana": 1.25,
              "Tomate del perello": 2.65}
    # solicitamos la fruta al usuario
    fruta = input("Introduzca que fruta/verdura desea comprar").capitalize()
    print(fruta)
    # solicitamos el peso que desea
    peso = float(input("Introduzca el peso en kg"))
    # si la fruta esta en el diccionario
    if fruta in frutas:
        # sacamos el precio de la fruta y lo multiplicamos por el peso
        precio = frutas[fruta] * peso
        # imprimimos el resultado
        print(fruta, precio)
    # si no esta en el diccionario
    else:
        print("No disponemos de esa fruta")

# -----------------------------------------------------------------------------------------------------

def ej5():
# Ej5

# Escribe un programa que almacene en un diccionario el número de horas de
# los módulos de segundo curso de DAM. Por ejemplo, {'Sistemas de gestión
# empresarial': 100, 'Programación de servicios y procesos': 60, 'Acceso a datos':
# 120, … }. Tras ello, deberá mostrar el total de horas del curso y mostrar los
# módulos ordenados alfabéticamente.

# declaramos el diccionario
    modulos = {"Sistemas de gestión empresarial": 100, "Programación de servicios y procesos": 60, "Acceso a datos": 120,
               "Desarrollo de interfaces": 120, "Programación multimedia y dispositivos móviles": 100,
               "Empresa e iniciativa emprendedora": 60,
               "Inglés": 40, "Formacion en centros de trabajo": 400, "Proyecto final": 40}

    # declaramos la variable para el total de horas
    total = 0
    # mostramos los modulos ordenados alfabeticamente
    print(sorted(modulos.items()))
    # sumamos las horas de cada modulo y mostramos el total
    for modulo in modulos:
        total = total + modulos[modulo]
    print("El total de horas del curso es:", total)


# -----------------------------------------------------------------------------------------------------
while True:
    opcion = int(input("introduzca un ejercici o pulse 0 para salir"))
    if opcion == 0:
        break
    elif opcion == 4:
        ej4()
    elif opcion == 5:
        ej5()






