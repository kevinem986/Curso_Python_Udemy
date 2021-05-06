def listar_cursos(*cursos):
	for elemento in cursos:
		#for sub elemento in elemento		
		# yield elemento
		yield from elemento

cursos_listados = listar_cursos("CTA", "Matematicas", "Lenguajes", "Historia", "Fisica")

print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))