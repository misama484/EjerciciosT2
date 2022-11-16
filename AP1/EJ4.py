# EJ4
# Escribe un programa que solicite dos números enteros e indique si el mayor es múltiplo del menor.

n1 = int(input("Introduzca primer numero "))
n2 = int(input("Introduca segundo numero "))

if n1 > n2:
    mayor = n1
    menor = n2

elif n2 > n1:
    mayor = n2
    menor = n1


if menor % mayor == 0:
    print("El numero " + str(mayor) + " NOes multiplo de " + str(menor))
else:
    print("El numero " + str(mayor) + " es multiplo de " + str(menor))
