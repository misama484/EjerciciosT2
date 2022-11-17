
#abrimos el archivo con un manejador
man = open("moby.txt")
#declaramos un diccionario
dic = dict()
# 1. Cuántas palabras distintas contiene el texto
for linea in man:
    #eliminamos el salto de linea final
    linea = linea.rstrip()

    #separamos cada linea en palabras
    palabras = linea.split(" ")
    print(palabras)

