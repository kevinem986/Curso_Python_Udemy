class Computador():

	def __init__(self):
		self.marca = "Toshiba"
		self.procesador = "Intel"
		self.mouse = 1
		self.teclado = 1

		self.suspendido = False

	def ejecucion(self, suspension):
		self.suspendido = suspension

		if(self.suspendido):
			print("El equipo está suspendido")
		else:
			print("El equipo está en ejecución")

	def estado(self):
		print("La marca de PC",self.marca,"tiene un procesador",self.procesador,", cuenta con",self.mouse,"mouse y",self.teclado, "teclado")
		
pc = Computador()

print("Marca: ", pc.marca)
print("Procesador: ", pc.procesador)
print("Mouse: ", pc.mouse)
print("Teclado: ", pc.teclado)

pc.ejecucion(True)
pc.estado()

print("************************************************")
pc2 = Computador()

print("Marca: ", pc2.marca)
print("Procesador: ", pc2.procesador)
print("Mouse: ", pc2.mouse)
print("Teclado: ", pc2.teclado)

pc2.ejecucion(False)
pc2.estado()