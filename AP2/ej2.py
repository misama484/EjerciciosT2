#Ej2

#  Escribe un programa que vaya preguntando al usuario los números ganadores
# de la lotería de Navidad, los vaya almacenando en una lista y, cuando
# introduzca un -1 para finalizar, los muestre por pantalla ordenados de menor
# a mayor

#Solicitamos el numero ganador de la loteria
numero = int(input("Introduce un numero ganador de la loteria: "))
#Creamos una lista vacia
numeros = []
#separamos el numero introducido de la lista y lo añadimos a la lista
for num in str(numero):
    numeros.append(num)

#ordenamo la lista de menor a mayor
numeros.sort()
for num in str(numero):
    print(num)
