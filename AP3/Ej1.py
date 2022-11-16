# Ej1

# Escribe un programa para leer a través del historial de correos del archivo
# mbox-short.txt y construir un histograma mediante un diccionario para
# contar cuántos mensajes han llegado desde cada dirección de correo
# electrónico que aparece en el archivo.

# Abrimos el archivo con el manejador
man = open('mbox-short.txt')
# Creamos un diccionario vacío
dic = dict()

# por cada linea en el archivo eliminamos el salto de linea al final y condicionamos si empieza con 'From'
for linea in man:
    linea = linea.rstrip()
    if linea.startswith('From:'):
        # Buscamos el primer espacio en blanco, que es el precede al email
        lin = linea.find(" ")
        # anyadimos a email el valor de despues del espacio en blanco
        email = linea[lin + 1:]
        # Si el email no esta en el diccionario lo agregamos con valor 1
        if email not in dic:
            dic[email] = 1
        # Si el email esta en el diccionario le sumamos 1 al valor
        else:
            dic[email] = dic[email] + 1
print(dic)
