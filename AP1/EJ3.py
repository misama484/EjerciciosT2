# EJ3
# Escribe un programa que solicite al usuario el año actual y un año cualquiera y que escriba cuántos años
# han pasado desde ese año o cuántos años faltan para llegar a ese año.

anyoActual = int(input("Introduzca el anyo actual "))
anyoCualquiera = int(input("Introduzca el anyo destino "))

if anyoActual > anyoCualquiera:
    result = anyoActual - anyoCualquiera
    print("Han pasado " + str(result) + " desde " + str(anyoCualquiera))
else:
    result = anyoCualquiera - anyoActual
    print("Quedan " + str(result) + " anyos para llegar a " + str(anyoCualquiera))
