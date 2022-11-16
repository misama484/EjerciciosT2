# Ej2

# A partir del resultado del ejercicio anterior, agrupa en un diccionario los
# nombres de dominio y el número de mensajes que se recibieron desde cada
# uno

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
print(dic)
