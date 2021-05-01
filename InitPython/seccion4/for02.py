count = 0

for a in "tutocodev@gmail.com":
	
	if(a=="@" or a=="."):
		count=count+1

if count==2:
	print("El email está correcto.")
else:
	print("No cumple con el formato establecido.")