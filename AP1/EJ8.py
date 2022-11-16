# EJ8
# Escribe un programa que calcule el equivalente humano de la edad de un gato, introducida por el usuario.
# En este sentido, el primer año de vida del gato equivale a 15 años de edad en humanos,
# mientras que el segundo año solo equivale a 10 años humanos. Cuando el gato es completamente adulto,
# sin embargo, cada año gatuno equivale a 4 años humanos.

edadGato = int(input("Introduzca la edad del gato: "))

if edadGato == 1:
    edadHumana = 15
    print("La edad del gato en años humanos es de: " + str(edadHumana))
elif edadGato == 2:
    edadHumana = 25
    print("La edad del gato en años humanos es de: " + str(edadHumana))
else:
    edadHumana = 25 + ((edadGato - 2) * 4)
    print("La edad del gato en años humanos es de: " + str(edadHumana))
