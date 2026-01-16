calificaciones = [[10, 9, 8, 7],
                  [9, 7, 6, 8],
                  [8, 9, 5, 9],
                  [7, 8, 9, 10]]
traspuesta = []

for i in range (len(calificaciones)):
  fila = []
  for j in range (len(calificaciones[0])):
    fila.append(calificaciones[j][i])
  traspuesta.append(fila)

print(traspuesta)