# EJ6
# Escribe un programa que determine si un alumno puede o no aprobar el curso en convocatoria ordinaria,
# según si ha suspendido, o no, la primera, la segunda y la tercera evaluación, y teniendo en cuenta que es posible
# aprobar el curso con la primera evaluación suspendida.
# La información de aprobado o suspenso en cada evaluación se le solicita al usuario como entrada.

ev1 = input("Introduzca el resultado de la 1a evaluacion: ")
ev2 = input("Introduzca el resultado de la 2a evaluacion: ")
ev3 = input("Introduzca el resultado de la 3a evaluacion: ")

if ev1 == "suspenso":
    valorEv1 = 1
elif ev1 == "aprobado":
    valorEv1 = 0
else:
    valorEv1 = 2


if ev2 == "suspenso":
    valorEv2 = 1
elif ev2 == "aprobado":
    valorEv2 = 0
else:
    valorEv2 = 2

if ev3 == "suspenso":
    valorEv3 = 1
elif ev3 == "aprobado":
    valorEv3 = 0
else:
    valorEv3 = 2


if valorEv1 or valorEv2 or valorEv3 == 2:
    print("ERROR, introduzca aprobado o suspenso en cada una de las evaluaciones")

elif valorEv2 == 1 or valorEv3 == 1:
    if valorEv2 == 1 and valorEv3 == 1:
        print("has suspendiso la segunda y la tercera evaluacion, no puedes aprobar el curso")
    elif valorEv3 == 1:
        print("has suspendiso la tercera evaluacion, no puedes aprobar el curso")
    else:
        print("has suspendiso la segunda, no puedes aprobar el curso")
else:
    if valorEv1 == 1:
        print("has suspendiso la primera evaluacion, pero puedes aprobar el curso")
    else:
        print("Enhorabuena!! Has aprobado todo el curso!!")
