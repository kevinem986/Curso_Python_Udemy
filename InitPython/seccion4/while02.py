edad = int(input("Ingrese la edad de la persona: "))

while edad < 18 or edad > 70:
	print("Aún no estas apto para sufragar.")
	print("*************************************")
	edad = int(input("Ingrese la edad de la persona nuevamente: "))

print("Gracias por venir a informarte.")