#EJ7
#Escribe un programa que calcule la nota media del curso teniendo en cuenta las notas (números decimales) de la primera,
# segunda y tercera evaluación y considerando que estas tienen un peso de un 30%, 40% y 30%, respectivamente.

nota1ev = float(input("Introduzca la nota de la primera evaluacion "))
nota2ev = float(input("Introduzca la nota de la segunda evaluacion "))
nota3ev = float(input("Introduzca la nota de la tercera evaluacion "))

valorNota1 = nota1ev * 0.3
valorNota2 = nota1ev * 0.4
valorNota3 = nota1ev * 0.3

notaFinal = valorNota1 + valorNota2 + valorNota3

print(str("La nota final del curso es de: " + notaFinal))
