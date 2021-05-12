class Persona():

	def __init__(self, nombre, apellido, sexo):
		self.nombre = nombre
		self.apellido = apellido
		self.sexo = sexo

		self.hablar = False

	def hablar(self):
		self.hablar = True

	def estado(self):
		print("Nombre: ", self.nombre,
			  "\nApellido: ", self.apellido,
			  "\nSexo: ", self.sexo,
			  "\nHablar: ", self.hablar)

class Supervisor(Persona):
	objetivo = ""

	def objetivos(self):
		self.objetivo = "Tiene que cumplir con las metas mensuales."

	def estado(self):
		print("Nombre: ", self.nombre,
			  "\nApellido: ", self.apellido,
			  "\nSexo: ", self.sexo,
			  "\nHablar: ", self.hablar,
			  "\nObjetivo: ", self.objetivo)

class Obrero(Persona):
	manejarMaq = ""

	def manejar(self):
		self.manejarMaq = "Descargar 80 containers al mes."

	def estado(self):
		print("Nombre: ", self.nombre,
			  "\nApellido: ", self.apellido,
			  "\nSexo: ", self.sexo,
			  "\nHablar: ", self.hablar,
			  "\nObjetivo: ", self.manejarMaq)		