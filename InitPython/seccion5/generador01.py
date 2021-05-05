# Ejemplo Función

# def listPares(limite):
# 	num = 1
# 	miLista = []

# 	while(num < limite):
# 		miLista.append(num * 2)
# 		num = num + 1

# 	return miLista

# print(listPares(8))

# Ejemplo Generador
def listPares(limite):
	num = 1

	while(num < limite):
		yield(num * 2)
		num = num + 1

returnPares = listPares(8)

# for i in returnPares:
# 	print(i)

# Mostrar elementos especificos del objeto iterable
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")
print(next(returnPares))
print("Puede ingresar aqui ...")