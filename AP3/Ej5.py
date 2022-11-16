# Ej5

# Escribe un programa que almacene en un diccionario el número de horas de
# los módulos de segundo curso de DAM. Por ejemplo, {'Sistemas de gestión
# empresarial': 100, 'Programación de servicios y procesos': 60, 'Acceso a datos':
# 120, … }. Tras ello, deberá mostrar el total de horas del curso y mostrar los
# módulos ordenados alfabéticamente.

# declaramos el diccionario
modulos = {"Sistemas de gestión empresarial": 100, "Programación de servicios y procesos": 60, "Acceso a datos": 120,
           "Desarrollo de interfaces": 120, "Programación multimedia y dispositivos móviles": 100,
           "Empresa e iniciativa emprendedora": 60,
           "Inglés": 40, "Formacion en centros de trabajo": 400, "Proyecto final": 40}
# declaramos la variable para el total de horas
total = 0
# mostramos los modulos ordenados alfabeticamente
print(sorted(modulos.items()))
# sumamos las horas de cada modulo y mostramos el total
for modulo in modulos:
    total = total + modulos[modulo]
print("El total de horas del curso es:", total)
