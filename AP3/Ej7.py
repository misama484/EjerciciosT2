# Ej7

# Escribe un pequeño programa para gestionar las facturas pendientes de ser
# cobradas por una empresa. Las facturas se almacenarán en un diccionario en
# el que la clave será el número de factura y el valor el importe total de la
# factura. El programa deberá preguntarle al usuario si desea añadir una nueva
# factura, pagar una factura existente o bien finalizar. Si lo que desea es añadir
# una nueva factura, preguntará por el número de la factura y su importe y el
# par se añadirá al diccionario. Si, en cambio, desea pagar una factura existente,
# se pedirá el número de factura y esta se eliminará del diccionario.

# declaramos el diccionario
listaFacturas = dict()
# listaFacturas = {1: 150, 2: 200}
id = 0
totalFact = 0
while True:
    print("Que desea hacer?:")
    print("1. Mostrar facturas")
    print("2. Anyadir factura")
    print("3. Pagar factura")
    print("4. Salir")
    option = input("...")
    if option == "1":
        print(listaFacturas)

    if option == "2":
        id = id + 1
        totalFact = input("Introduzca total factura:")
        listaFacturas[id] = totalFact
        print("factura anyadida")

    if option == "3":
        id = int(input("Introduzca id:"))
        if listaFacturas.get(id):
            print(listaFacturas[id])
            confirm = input("Desea pagar factura? -- si/no")
            if confirm == "si":
                del listaFacturas[id]
                print("Factura Pagada!!")

    if option == "4":
        break
