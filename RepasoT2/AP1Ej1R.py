# AP1
# Ej1
# Escribe un programa que solicite al usuario su peso (en kilogramos)
# y su altura (en metros) y calcule su índice de masa corporal (IMC).
# El IMC se calcula con la fórmula IMC = peso / altura2.
# Los valores normales de IMC están entre 20 y 25,
# aunque dichos valores también se ven influidos por la edad, el sexo,
# constitución física, etc.

peso = int(input("Introduce tu peso en kg:"))
altura = float(input("Introduce tu altura en metros"))

cuadradoAltura = pow(altura, 2)
imc = peso / cuadradoAltura
imc = imc.__round__(2)

if imc < 20:
    print(str(imc) + "IMC por debajo dell umbral")
if imc > 25:
    print(str(imc), "IMC por ENCIMA del umbral")
else:
    print(str(imc) + " Esta en el imc ideal")
