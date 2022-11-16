# AP1
# Ej1
# Escribe un programa que solicite al usuario su peso (en kilogramos)
# y su altura (en metros) y calcule su índice de masa corporal (IMC).
# El IMC se calcula con la fórmula IMC = peso / altura2.
# Los valores normales de IMC están entre 20 y 25,
# aunque dichos valores también se ven influidos por la edad, el sexo,
# constitución física, etc.

peso = int(input('Introduce tu peso en kg: '))
altura = int(input("Introduce tu altura en cm's: "))

cuadradoPeso = peso ** 2
imc = cuadradoPeso / altura

if imc < 20:
    print("Su indice de masa corporal es " + str(
        imc) + ", esta por debajo del umbral, considere usar cupones del McDonal's")
elif imc > 25:
    print("Su indice de masa corporal es " + str(
        imc) + ",  esta por encima del umbral, considere tomar mas ensaladitas...")
else:
    print("Su IMC es " + str(imc) + " esta usted en un IMC correcto, siga asi!!")
