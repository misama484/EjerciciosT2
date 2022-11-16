#Ej3

# Escribe un programa que almacene los módulos de 2º DAM (PSP, AAD, PMM,
# DIN, SGE, etc.) en una lista, pregunte al usuario la nota que ha sacado en cada
# módulo y elimine de la lista los módulos aprobados. Al final, el programa debe
# mostrar por pantalla los módulos que el usuario tiene que recuperar en junio.

#creamos lista con los modulos de 2º DAM
modulos = ["PSP", "AAD", "PMM", "DDI", "SGE", "EIE", "Ingles",]

#recorremos la lista de modulos y
# solicitamos al usuario la nota de cada modulo
for modulo in modulos:
    nota = int(input("Introduce la nota de " + modulo + ": "))
    if nota >= 5:
        print("Modulo aprobadado")
        modulos.remove(modulo)
    else:
        print("Modulo Suspendido")
#recorremos la lista de suspendidos y mostramos mensaje
print("Los modulos que tienes que recuperar son: ")
for modulo in modulos:
    print(modulo)