#Ej4

# Escribe un programa que pida al usuario una frase y muestre por pantalla el
# número de veces que contiene cada vocal.

 #solicitamos la frase al usuario
frase = input("Introduce una frase: ")
#creamos una lista con las vocales
vocales = ["a", "e", "i", "o", "u"]
#recorremos la lista de vocales
for vocal in vocales:
    #contamos las veces que aparece cada vocal en la frase
    #y mostramos el resultado
    print("La vocal " + vocal + " aparece " + str(frase.count(vocal)) + " veces")