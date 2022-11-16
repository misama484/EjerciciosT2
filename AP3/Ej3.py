# Ej3
# A partir del resultado del ejercicio anterior, indica el nombre de dominio
# desde el que se han recibido más correos, ayudándote de una lista de tuplas
# (contador, dominio).

# Abrimos el archivo con el manejador
man = open('mbox-short.txt')
# Creamos un diccionario vacío
dic = dict()

# por cada linea en el archivo eliminamos el salto de linea al final y condicionamos si empieza con 'From'
for linea in man:
    linea = linea.rstrip()
    if linea.startswith('From:'):
        # Buscamos el simbolo @, que es el precede al dominio
        lin = linea.find("@")
        # anyadimos a dominio el valor de despues del espacio en blanco
        dominio = linea[lin + 1:]
        # Si el dominio no esta en el diccionario lo agregamos con valor 1
        if dominio not in dic:
            dic[dominio] = 1
        # Si el dominio esta en el diccionario le sumamos 1 al valor
        else:
            dic[dominio] = dic[dominio] + 1
# print(dicEmail)

tupla = dic.items()
print(tupla)
# creamos una lista vacia
lst = list()
# por cada clave/valor del diccionario
for clave, valor in dic.items():
    # anyadimos a la lista la tupla con los campos invertidos
    lst.append((valor, clave))
# ordenamos la lista de mayor a menor
lst = sorted(lst, reverse=True)
print(lst)
print("El dominio con mas correos recibidos es: ", lst[0])
