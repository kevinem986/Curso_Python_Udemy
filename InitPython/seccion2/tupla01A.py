a = (1,4,5.6,"Juan")

# Lista a transformar en tupla
b = ["Jorge",6.7, "Peru", 28]

# Convertir lista a tupla
c = tuple(b)

# Convertir tupla a lista
tup = (3, "Jose", 7.6, "Trujillo", "Jonas")
d = list(tup)

#Contar elementos de una tupla
countTup = len(d)

# Mostrar la posicion de un elemento en una tupla
positionTupla = a[3]

# Tuplas sin paréntesis
tup2 = "Trujillo", "Lima", 13001, 28, 3.5

print(a)
print(a[1])
# Resultado de la lista convertida en tupla
print(b)
print(c)
# Resultado de la tupla convertida en lista
print(d)
print(countTup)
print(positionTupla)
print(tup2)