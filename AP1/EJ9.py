# EJ9
# Escribe un programa que lea tres números por la entrada estándar (teclado) y escriba el máximo.


n1 = int(input("Introduzca primer numero "))
n2 = int(input("Introduca segundo numero "))
n3 = int(input("Introduca tercer numero "))

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
elif n3 > n1 and n3 > n2:
    mayor = n3

print("El numero mayor es: " + str(mayor))

