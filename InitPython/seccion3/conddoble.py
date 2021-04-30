sueldo_gerente = int(input('Ingrese el salario del Gerente General: '))
print('Salario del Gerente General: S/{}'.format(sueldo_gerente))

sueldo_jefe_area = int(input('Ingrese el salario del Jefe de Area: '))
print('Salario del Jefe de Area: S/{}'.format(sueldo_jefe_area))

sueldo_asistente = int(input('Ingrese el salario del Asistente: '))
print('Salario del Asistente: S/{}'.format(sueldo_asistente))

sueldo_tecnico = int(input('Ingrese el salario del Técnico: '))
print('Salario del Técnico: S/{}'.format(sueldo_tecnico))

sueldo_practicante = int(input('Ingrese el salario del Practicante: '))
print('Salario del Practicante: S/{}'.format(sueldo_practicante))


if sueldo_gerente > sueldo_jefe_area > sueldo_asistente > sueldo_tecnico > sueldo_practicante:
	print("Se cumple con la estructura jerarquica")
else:
	print("Existencia de falla en el sistema de pagos")