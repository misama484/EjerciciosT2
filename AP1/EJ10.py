# EJ10
# Hacer un programa que calcule las ayudas a la compra de la primera vivienda. Necesita saber el precio de la vivienda,
# la zona a la que pertenece (A, B, C, D, E), y el sueldo anual y la edad del comprador.
# El sueldo se corrige por un factor según la zona (A: 0'85, B: 0'9, C: 0'92, D: 0'97, E: 1'00) y
# después se determina su valor proporcional al Salario Mínimo Interprofesional (SMI = 13.300 euros).
# Según esa proporción, la ayuda es un porcentaje del valor de la vivienda
# (<1'5: 15 %, <2'5: 10 %, <3'5: 8 %, <4'5: 5 %). Si el comprador es menor de 35 años, se le suman 3000 euros a la ayuda obtenida.


precio = int(input("Introduzca el precio de la vivienda: "))
zona = input("Introduzca la zona a la que pertenece la vivienda (a, b, c, d, e): ")
sueldo = int(input("Introduzca su sueldo anual: "))
edad = int(input("Introduzca su edad: "))


if zona == "a":
    sueldo = sueldo * 0.85
elif zona == "b":
    sueldo = sueldo * 0.9
elif zona == "c":
    sueldo = sueldo * 0.92
elif zona == "d":
    sueldo = sueldo * 0.97
elif zona == "e":
    sueldo = sueldo * 1
else:
    print("Introduzca una zona valida")

sueldo = sueldo / 13300

if sueldo < 1.5:
    porcentaje = 15
elif sueldo < 2.5:
    porcentaje = 10
elif sueldo < 3.5:
    porcentaje = 8
elif sueldo < 4.5:
    porcentaje = 5
else:
    porcentaje = 0

cuantia = precio * (porcentaje / 100)

print("El porcentaje de la ayuda es del " + str(porcentaje) + "%, y la cuantia es de: " + str(cuantia))

if edad < 35:
    cuantia = precio * (porcentaje / 100) + 3000
    print("Al ser menor de 35 años, se asocia un plus de 3000 eur, la cuantia de la ayuda es de: " + str(cuantia))

