# 1. Primer ejercicio
# def evaluacion(nota):
# 	estado = "Promovido"

# 	if nota < 11:
# 		estado = "Sustitorio"

# 	return estado

# print(evaluacion(14))

# 2. Segundo ejercicio

print('Calificación del Primer Semestre')

nota =int(input('Ingrese su nota: '))

def evaluacion(nota):
	estado = "Promovido"

	if nota < 11:
		estado = "Sustitorio"

	return estado

print(evaluacion(nota))