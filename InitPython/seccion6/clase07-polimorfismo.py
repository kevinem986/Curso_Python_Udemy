class Gerente():
	def marcacion(self):
		print("Marca asistencia solo una vez al día.")

class SubGerente():
	def marcacion(self):
		print("Marca asistencia solo 2 vez al día.")

class JefeArea():
	def marcacion(self):
		print("Marca asistencia 4 veces al día.")

class Asistente():
	def marcacion(self):
		print("Marca asistencia 4 veces al día y firma en el padrón.")

def marcacionTrabajador(trabajador):
	trabajador.marcacion();

mTrabajador = SubGerente()
marcacionTrabajador(mTrabajador)

mTrabajador2 = Gerente()
marcacionTrabajador(mTrabajador2)
		