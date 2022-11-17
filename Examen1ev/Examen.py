# Abrimos fichero con el manejador
libro = open("moby.txt", encoding="utf8")

# creamos un diccionario
dic = dict()

# a) (1 punto) Cuántas palabras distintas contiene el texto,
cont = 0
# leemos el fichero linea a linea
for linea in libro:
    # eliminamos el salto de linea
    linea = linea.rstrip()
    # separamos la linea en palabras
    palabras = linea.split()

    for palabra in palabras:
        cont = cont + 1
        if palabra not in dic:
            # la anyadimos con valor 1
            dic[palabra] = 1
        else:
            # le sumamos 1 al valor
            dic[palabra] = dic[palabra] + 1

print("el libro consta de", str(cont), "palabras")

# b) (1 punto) Cuántas veces aparece la palabra "whale" (ballena) en el texto
libro2 = open("moby.txt", encoding="utf8")
whale = dict()
cont2 = 0
for linea in libro2:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        # pasamos a minusculas todas las palabras antes de evaluarlas
        palabra = palabra.lower()
        if palabra == "whale":
            if palabra not in whale:
                # la anyadimos con valor 1
                whale[palabra] = 1
            else:
                # le sumamos 1 al valor
                whale[palabra] = whale[palabra] + 1
print("la palabra whale aparece", whale.get("whale"), "veces")

# (1.5 puntos) Cuáles son las 20 palabras más frecuentes del texto, es decir, las que
# aparecen más veces a lo largo del mismo, junto con el número de veces que aparece
# cada una.
libro3 = open("moby.txt", encoding="utf8")
repeticiones = dict()

for linea in libro3:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra not in repeticiones:
            repeticiones[palabra] = 1
        else:
            repeticiones[palabra] = repeticiones[palabra] + 1
# creamos una lista
lst = list()
# por cada clave-valor, lo anyadimos a la lista, pero con los parametros cambiados para poder ordenarlos
for clave, valor in repeticiones.items():
    lst.append((valor, clave))
# ordenamos de mayor a menor
lst = sorted(lst, reverse=True)
# print(lst)

print("las 20 palabras mas frecuentes en el libro son:")
# imprimimos los 20 primeros registros
print(lst[0:19])

# Cuál es la letra del abecedario con la que hay más palabras (sin repetir)
# en el texto que empiezan con esa letra, junto con el número de palabras que empiezan
# con esa letra. Ejemplo de salida ficticia:

libro4 = open("moby.txt", encoding="utf8")
words = dict()

for linea in libro4:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra[0] not in words:
            words[palabra[0]] = 1
        else:
            words[palabra[0]] = words[palabra[0]] + 1

lst2 =list()
for clave, valor in words.items():
    lst2.append((valor, clave))
lstOrd = sorted(lst2, reverse=True)
print(lstOrd)
print("La letra del abecedario con la que empiezan más palabras en el texto es la", lstOrd[0][1], ".Letra por la que empiezan", lstOrd[0][0], "palabras")
