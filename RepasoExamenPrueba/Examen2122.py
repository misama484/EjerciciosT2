import random

# Desarrolla un programa a modo de juego para practicar cálculo mental.
# El juego irá preguntando por el resultado secuencial de sumas o restas (la operación se elegirá
# de forma aleatoria) de números enteros elegidos aleatoriamente entre 1 y 100, partiendo de 0.
# El juego acaba cuando la persona usuaria falla la respuesta, momento en el que se le informa de
# cuántos aciertos seguidos ha tenido.

# comenzamos solicitado al usuari que empiece el juego

start = input("Juego de la suma, pulse 'S' (start) para iniciar.").lower()
if type(start) is not str:
    print("ERROR")
if start == "S":
    cont = 0
    while True:
        print("Vamos con las sumas, en el momento que falles, pierdes")
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        suma = num1 + num2

        print(str(num1) + " + " + str(num2) + "?")

        print(suma)
        try:
            result = input()

            if int(result) == suma:
                print("Correcto!!!", "Siguiente suma")
                cont = cont + 1
            else:
                print("Has Fallado, lo siento...\nHas acertado " + str(cont) + " sumas")
                break
        except:
            print("Deberias haber introducido un numero \nHas acertado " + str(cont) + " sumas")
            result = input("Vuelve a intentarlo")
            if int(result) == suma:
                print("Correcto!!!", "Siguiente suma")
                cont = cont + 1
            else:
                print("Has Fallado, lo siento...\nHas acertado " + str(cont) + " sumas")
                break


