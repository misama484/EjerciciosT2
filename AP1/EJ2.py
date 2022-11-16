# EJ2
# Escribe un programa que solicite al usuario dos números enteros y
# calcule su división, indicando si se trata de una división exacta o no.

n1 = int(input("Introduzca primer numero: "))
n2 = int(input("Introduzca el segundo numero: "))

operacion = n1 / n2

if n1 % n2 == 0:
    resultado = "La division es exacta"
else:
    resultado = "La division NO es exacta"

redondeo = round(operacion, 2)

print("El resultado de dividir " + str(n1) + " y " + str(n2) + " es: " + str(redondeo))
print(resultado)
