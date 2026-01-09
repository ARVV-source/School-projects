nombres = ['Ana', 'Luis', 'Carlos', 'Marta']
materias = ['Matemáticas', 'Física', 'Química', 'Biología']
calificaciones = [[10, 9, 8, 7],
                  [9, 7, 6, 8],
                  [8, 9, 5, 9],
                  [7, 8, 9, 10]]

prom_alumno = []
prom_materia = []

for i in calificaciones:
  prom_alumno.append((sum(i))/4)

for i in range (len(calificaciones)): 
  suma=0
  for o in range (len(calificaciones)):
    suma = suma + calificaciones[o][i]
  prom_materia.append(suma/4)

for i in range (len(materias)):
  print(f"      {materias[i]}" , end="")
print("      Promedio")

for i in range (len(nombres)):
  print(f"{nombres[i]:<8}", end="")
  for z in range (len(calificaciones)):
    print(f"       {calificaciones[i][z]}", end="    ")
  print(f"           {prom_alumno[i]}")
print("promedio", end="     ")
for materia in prom_materia:
  print(materia, end="        ")