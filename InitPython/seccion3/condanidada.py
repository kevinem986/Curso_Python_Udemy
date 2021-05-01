print("Programa de Becas al Extranjero")

edad = int(input("Ingrese la edad del estudiante: "))
print(edad)

if edad >= 18:
	print("Usted cumple con el requisito de tener la mayoría de edad.")
	print("**************************************************************")
	ponderado = float(input("Ingrese el promedio ponderado del estudiante: "))

	if ponderado >= 15.5:
		print("Su promedio cumple con los requisitos del programa.")
		print("**************************************************************")

		no_curso_aprobados = int(input("Ingrese el número de cursos aprobados del estudiante: "))

		if no_curso_aprobados >= 36:
			print("Si cumple con los requisitos de cursos aprobados.")

			salario = int(input("Ingrese el salario familiar del estudiante: "))

			if salario < 15000:
				print("Usted si cumple con los requisitos del programa")
			else:
				print("Su salario es superior a S/15000, por lo tanto no puede postular.")
		else:
			print("El requisito de cursos aprobados es de 36, por lo tanto no puede postular.")
	else:
		print("Su promedio debe ser mayor de 15.5, por lo tanto no puede postular.")
else:
	print("Debe ser mayor de edad para postular, por lo tanto no puede postular.")