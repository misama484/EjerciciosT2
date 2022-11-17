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

print("A) El libro consta de", str(cont), "palabras\n")

# b) (1 punto) Cuántas veces aparece la palabra "whale" (ballena) en el texto
libro2 = open("moby.txt", encoding="utf8")
whaleDict = dict()
cont2 = 0
for linea in libro2:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        # pasamos a minusculas todas las palabras antes de evaluarlas
        palabra = palabra.lower()
        if palabra == "whale":
            if palabra not in whaleDict:
                # la anyadimos con valor 1
                whaleDict[palabra] = 1
            else:
                # le sumamos 1 al valor
                whaleDict[palabra] = whaleDict[palabra] + 1
print("B) La palabra whale aparece", whaleDict.get("whale"), "veces\n")

# (1.5 puntos) Cuáles son las 20 palabras más frecuentes del texto, es decir, las que
# aparecen más veces a lo largo del mismo, junto con el número de veces que aparece
# cada una.
libro3 = open("moby.txt", encoding="utf8")
repeticiones = dict()
# extraemos la palabras a un diccionario para evaluarlas
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

print("C) Las 20 palabras mas frecuentes en el libro son:")
# imprimimos los 20 primeros registros
print(lst[0:19], "\n")

# d) (1.5 puntos) Cuál es la letra del abecedario con la que hay más palabras (sin repetir)
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
#creamos una lista
lst2 = list()
#anyadimos los valores del diccionario, al orden inverso, para poder extraer la mas repetida
for clave, valor in words.items():
    lst2.append((valor, clave))
#ordenamos
lstOrd = sorted(lst2, reverse=True)
#print(lstOrd)
print("D) La letra del abecedario con la que empiezan más palabras en el texto es la", lstOrd[0][1],
      ".Letra por la que empiezan", lstOrd[0][0], "palabras\n")
