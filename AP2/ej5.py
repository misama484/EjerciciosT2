#Ej5
# Escribe un programa en el que el usuario introduzca un número entero y el
# programa genere una frase con las palabras correspondientes a cada cifra. Por
# ejemplo, 547 devolvería "cinco cuatro siete". Las palabras desde el "cero"
# hasta el "nueve" están almacenadas en una lista.

#solicitamos el numero al usuario
numero = int(input("Introduce un numero: "))
#creamos una lista con las palabras de los numeros
numeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

#recorremos la lista de numeros
for num in str(numero):
    #mostramos el numero en palabras
    print(numeros[int(num)])