# Ej6

# Escribe un programa que almacene en un diccionario la lista de la compra que
# vaya indicando el usuario, de manera que el programa pregunta por el artículo
# y su precio y se añade el par al diccionario hasta que el usuario decida
# terminar. Finalmente, deberá mostrarse por pantalla la lista de la compra
# ordenada de mayor a menor precio de artículo y el importe total.

# declaramos el diccionario
listaCompra = dict()

# bucle para introducir los articulos
while True:
    # solicitamos el item al usuario
    item = input("Introduzca elemento a comprar:")
    # comprobamos que no es "exit"
    if item == "exit":
        break
    # solicitamos el precio del item
    precio = input("Introduzca el precio:")
    # anyadimos al diccionario
    listaCompra[item] = precio

print(listaCompra)

# calculamos el precio final de la lista de la compra
total = 0
# sumamos el precio de cada item y mostramos el total
for item in listaCompra:
    total = total + float(listaCompra[item])

print("El total de la compra es:", total)
