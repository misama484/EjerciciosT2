# Ej1

# Escribe un programa para leer a través del historial de correos del archivo
# mbox-short.txt y construir un histograma mediante un diccionario para
# contar cuántos mensajes han llegado desde cada dirección de correo
# electrónico que aparece en el archivo.

# Abrimos archivo con el manejador
man = open("mbox-short.txt")
# creamos diccioanrio
dicEmail = dict()

for linea in man:
    # eliminamos el salto de linea al final de cada linea
    linea = linea.rstrip()
    # buscamos la linea que empieza por from
    if linea.startswith("From: "):
        # buscamos el primer espacio en blanco
        lin = linea.find(" ")
        # anyadimos a varialble lo que hay despues del  espacio
        email = linea[lin + 1:]
        if email not in dicEmail:
            dicEmail[email] = 1
        else:
            dicEmail[email] = dicEmail[email] + 1
print(dicEmail)
# -------------------------------------------------------------------------------------------------------------
# Ej2

# A partir del resultado del ejercicio anterior, agrupa en un diccionario los
# nombres de dominio y el número de mensajes que se recibieron desde cada
# uno

dominios = dict()

for email in dicEmail:
    arroba = email.find("@")
    dominio = email[arroba + 1:]

    if dominio not in dominios:
        dominios[dominio] = 1
    else:
        dominios[dominio] = dominios[dominio] + 1
print(dominios)
# ------------------------------------------------------------------------------------------------------------
# Ej3
# A partir del resultado del ejercicio anterior, indica el nombre de dominio
# desde el que se han recibido más correos, ayudándote de una lista de tuplas
# (contador, dominio).

# nos creamos una tupla que almacenara un conjunto con cada clave-valor del diccionario
# dict_items([('uct.ac.za', 2), ('media.berkeley.edu', 2), ('umich.edu', 2), ('iupui.edu', 3), ('caret.cam.ac.uk', 1), ('gmail.com', 1)])
tuplaDominios = dominios.items()
# creamos una lista donde almacenaremos el conjunto clave-valor, pero con los campo invertidos(valor-clave)
# para poder ordenarlos luego
lstDominios = list()
# por cada clave-valor en la tupla
for clave, valor in tuplaDominios:
    lstDominios.append((valor, clave))
# [(2, 'uct.ac.za'), (2, 'media.berkeley.edu'), (2, 'umich.edu'), (3, 'iupui.edu'), (1, 'caret.cam.ac.uk'), (1, 'gmail.com')]
# una vez anyadidos a la lisa, con los valores invertidos, como el primer campo es el num de veces que aprarece el dominio,
# los ordenamos de mayor a menor(por defecto ordena de menor a mayor, asi que aplicamos un reverse = True
lstDominios = sorted(lstDominios, reverse=True)
print(lstDominios)
# imprimimos el dominio desde el que se recibieron mas correos (cuidado con el +, al no ser un String, no funciona, usar ","
print("Dominio con mas correos: ", lstDominios[0])
# print(tuplaDominios)