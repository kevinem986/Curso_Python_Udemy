class Persona:
	def __init__(self, nombre, edad, residencia):
		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def estado(self):
		print("Nombre: ", self.nombre,
			  "\nEdad: ", self.edad,
			  "\nLugar de Residencia: ", self.residencia)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre, edad, residencia):
	# def __init__(self, salario, antiguedad):

		super().__init__(nombre, edad, residencia)		
		# super().__init__("Juan", 23, "Peru")
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super().estado()
		print("Salario: ",self.salario,
			  "\nAntigüedad: ",self.antiguedad,"años.")

emp = Empleado(3000, 5, "Juan", 23, "Peru")
# emp = Empleado(3000, 5)
emp.descripcion()
print(isinstance(emp,Empleado))

# emp2 = Empleado(10000, 7, "Jose", 21, "Peru")
# # emp = Empleado(3000, 5)
# emp2.descripcion()

emp2 = Persona("Jose", 21, "Peru")
# emp = Empleado(3000, 5)
emp2.estado()
print(isinstance(emp2,Empleado))