
#Ej1
#Escribe un programa que vaya pidiendo palabras al usuario hasta que este
#introduzca "FIN" y, tras ello, muestre las palabras en orden alfabético inverso.

teclado = input("Introduce una palabra: ")
palabras = []
# lista = ["pepe", "juan", "ana", "maria"]

#Mientras que la palabra introducida sea distinta de "FIN"
#con .casefold() lo hacemos case insensitive
while teclado != "FIN".casefold():
    palabras.append(teclado)
    teclado = input("Introduce una palabra: ")

#ordenamos la lista de palabras alfabeticamente y mostramos
palabras.sort()
for palabra in palabras:
    print(palabra)

