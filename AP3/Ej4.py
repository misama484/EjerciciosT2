# Ej4
# Escribe un programa que almacene en un diccionario los precios de las frutas
# y verduras de la tabla. Deberá preguntarle al usuario por una fruta o verdura
# y un peso en kg., mostrándole por pantalla el importe de esa cantidad de fruta
# o verdura. Si la fruta o verdura no se encuentra en el diccionario, deberá
# informar al usuario.

# "Pimiento italiano": 1.35
# "Mandarina": 0.80
# "Banana": 1.25
# "Tomate del perello": 2.65

# declaramos el diccionario
dic = {"Pimiento italiano": 1.35, "Mandarina": 0.80, "Banana": 1.25, "Tomate del perello": 2.65}
fruta = input("Introduzca la fruta o verdura que desea comprar: ")
peso = float(input("Introduzca el peso en kg.: "))

# si la fruta esta en el diccionario
if fruta in dic:
    frut = dic[fruta]
    # calculamos el precio
    precio = dic[fruta] * peso
    print("El precio de", peso, "kg de ", fruta, "es:", precio)
# si la fruta no esta en el diccionario
else:
    print("No disponemos de esa fruta")
