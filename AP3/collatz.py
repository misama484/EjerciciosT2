#congetura de collatz
# si el numero es par, se divide entre 2, si es impar se multiplica por 3 y sumamos 1

num = int(input("introduce un numero"))
cont = 0
# evaluamos par
while cont <= 5:
    if num % 2 == 0:
        num = num / 2
        print(num)
    else:
        if num == 1:
            cont = cont + 1
            print("Bucles => " + str(cont))
        num = int((num * 3) + 1)
        print (str(num))
