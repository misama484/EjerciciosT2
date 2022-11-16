# Ej8

# Escribe un programa que reciba una serie de palabras que le indique el usuario
# y las agrupe por su letra inicial mediante un diccionario ordenado.

# declaramos el diccionario
dic = dict()

# bucle para introducir las palabras
while True:
    # solicitamos la palabra al usuario
    palabra = input("Introduzca palabra:")
    # comprobamos que no es "exit"
    if palabra == "0":
        break
    # anyadimos al diccionario comparando si la clave ya existe, si no existe la crea
    if palabra[0] not in dic:
        dic[palabra[0]] = palabra
    else:
        dic[palabra[0]] = dic[palabra[0]] + ", " + palabra

print(dic)

#odenamos el diccionario
print(sorted(dic.items()))






