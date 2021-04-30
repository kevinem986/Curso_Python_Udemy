# nombrediccionario = {a1:a,...}

dic1 = {"Juan":"Ingeniero","Jose":"Medico","Jorge":"Abogado"}

dic2 = {"Juan":23,"Jose":20,"Jorge":26}

# Combinar lista con diccionario
lis = ["Dell", "Lenovo", "Sony VAIO", "Toshiba"]
dic3 = {lis[0]: "Laptop", lis[1]: "All one", lis[2]: "Equipo", lis[3]: "PC"}

# Combinar tupla con diccionario
tup = "HP", "Samsung", "Sony", "Huawei"
dic4 = {tup[0]: "Impresora", tup[1]: "Tablet", tup[2]: "Equipo", tup[3]: "Celular"}

print(dic1)
print(dic2)

# Buscar por posición el valor del parametro en el diccionario
print(dic1["Juan"])
print(dic2["Jorge"])

print(dic3)
print(dic3["Lenovo"])

print(dic4)
print(dic4["Sony"])