class Carro():
	#Atributos
	marca = "Audi"
	longitud = 2.5
	ruedas = 4
	motor = 2.5
	color = "negro"
	modelo = "Q5"

	#Propiedades
	arrancar = True
	frenar = False

	def enMarcha(self):
		self.arrancar=False

	def estado(self):
		print(self.arrancar)
		if(self.arrancar):
			return "El auto está en arranque"
		else:
			return "El auto está detenido"

	#Instancia de clase --> nombre_instancia = clase()

auto = Carro()

print("La marca del auto: ", auto.marca)
print("Longitud: ", auto.longitud)
print("Número de ruedas: ", auto.ruedas)
print("Motor: ", auto.motor)
print("Color del auto: ", auto.color)
print("Modelo del auto: ", auto.modelo)

auto.enMarcha()
print(auto.estado())