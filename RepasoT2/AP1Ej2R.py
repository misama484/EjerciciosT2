# EJ2
# Escribe un programa que solicite al usuario dos números enteros y
# calcule su división, indicando si se trata de una división exacta o no.

num1 = int(input("numero1? "))
num2 = int(input("numro 2? "))

if num1 % num2 == 0:
    print("Es exacta")
else:
    print("no lo es")