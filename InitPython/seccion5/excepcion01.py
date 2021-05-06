def suma(n1, n2, n3):
	return n1 + n2 + n3

def resta(n1, n2, n3):
	return n1 - n2 - n3

def multiplicacion(n1, n2, n3):
	return n1 * n2 * n3

def division(n1, n2, n3):
	# Validación división entre 0
	try:
		return n1 / n2 / n3
	except ZeroDivisionError:
		print("No es divisible entre 0.")
		return "Operación fállida."	

while True:
	try:
		a = int(input("Ingrese el primer número: "))
		b = int(input("Ingrese el segundo número: "))
		c = int(input("Ingrese el tercer número: "))
		break
	except ValueError:
		print("Ingrese datos válidos.")

operacion = input("Introduce el número de operación a ejecutar (suma(1), resta(2), multiplicación(3), división(4)): ")

if operacion == "1":
	print(suma(a, b, c))
elif operacion == "2":
	print(resta(a, b, c)) 
elif operacion == "3":
	print(multiplicacion(a, b, c)) 
elif operacion == "4":
	print(division(a, b, c)) 
else:
	print("Operación no realizada")

print("Operación realizada con éxito")