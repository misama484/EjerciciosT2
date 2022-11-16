#Ej6

#Escribe un programa que indique cuántas palabras diferentes hay en El
#Quijote (archivo el_quijote.txt), mostrándolas antes en orden
#alfabético.

#Abrimos el archivo
archivo = open("el_quijote.txt")
#creamos una lista vacia
palabras = []
#recorremos el archivo
for linea in archivo:
    #separamos las palabras de la linea
    for palabra in linea.split():
        #añadimos la palabra a la lista
        palabras.append(palabra)

#cerramos el archivo
archivo.close()
#ordenamos la lista de palabras alfabeticamente
palabras.sort()
#creamos una lista vacia
palabrasDistintas = []
#recorremos la lista de palabras
for palabra in palabras:
    #si la palabra no esta en la lista de palabras unicas
    if palabra not in palabrasDistintas:
        #añadimos la palabra a la lista de palabras unicas
        palabrasDistintas.append(palabra)

#mostramos el numero de palabras unicas
print("El numero de palabras unicas es: " + str(len(palabrasDistintas)))