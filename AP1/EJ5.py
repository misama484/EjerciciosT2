# EJ5
# Escribe un programa que le pregunte al usuario si desea calcular el área de un triángulo o la de un círculo.
# Si se elige que se quiere calcular el área de un triángulo, el programa tiene que solicitar la base y la altura y mostrar el área
# como salida. Si se elige que se quiere calcular el área de un círculo, el programa solicitará entonces el radio y mostrará,
# igualmente, el área de este como salida. NOTA: El área de un triángulo es igual a la mitad de su base multiplicada por su altura.
# El área de un círculo se corresponde con Pi multiplicado por su radio al cuadrado. Nota: Utiliza como valor de Pi el valor 3.141592
import math

while (True):
    figura = input("Escriba la figura que desea calcular su area, trialgulo o circulo ")
    
    if figura == "triangulo":
        base = int(input("Introduzca la base del triangulo: "))
        altura = int(input("Introduzac la altura del triangulo: "))
        area = (base * altura) / 2
        print("El area del triangulo introducido es: " + str(area))
        break

    elif figura == "circulo":
        radio = int(input("Introduca el radio de la circunferencia: "))
        area = (radio ** 2) * math.pi
        print("El area del circulo introducido es: " + str(area))
        break

    else:
        print("Introduzca triangulo o circulo")
