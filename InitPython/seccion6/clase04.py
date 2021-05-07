class Computador():

	def __init__(self):
		self.__marca = "Toshiba"
		self.__procesador = "Intel"
		self.__mouse = 1
		self.__teclado = 1

		self.__ejecutar = False

	def ejecucion(self, ejecuciones):
		self.__ejecutar = ejecuciones

		if(self.__ejecutar):
			update = self.__actualizacion_automatica()

		if(self.__ejecutar and update):
			print("El equipo está en ejecución")
		else:
			print("El equipo está suspendido")

	def __actualizacion_automatica(self):
		print("El equipo se está actualizando")

		self.servupdate="Activado"

		if(self.servupdate == "Activado"):
			return True
		else:
			return False

	def estado(self):
		print("La marca de PC",self.__marca,"tiene un procesador",self.__procesador,", cuenta con",self.__mouse,"mouse y",self.__teclado, "teclado")
		
pc = Computador()

pc.ejecucion(True)
pc.estado()

print("************************************************")
pc2 = Computador()
# pc2.teclado = 2

pc2.ejecucion(False)
pc2.estado()