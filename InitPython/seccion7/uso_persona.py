from modulo_persona import *

print("*******************DATOS SUPERVISOR*****************************")
miSupervisor = Supervisor("Juan", "Gonzalez", "Masculino")
miSupervisor.objetivos()
miSupervisor.estado()

print("*******************DATOS SUPERVISOR NO. 02*****************************")
miSupervisor2 = Supervisor("Pedro", "Lopez", "Masculino")
miSupervisor2.objetivos()
miSupervisor2.estado()

print("********************DATOS OBRERO****************************")
miObrero = Obrero("Jose", "Amaranto", "Masculino")
miObrero.manejar()
miObrero.estado()