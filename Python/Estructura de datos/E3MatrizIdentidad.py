def matrizIdentidad(n):
  matriz = []
  for i in range(n):
    sub = []
    for j in range(n):
      sub.append(0)
    sub[i] = 1
    matriz.append(sub)
  for fila in matriz:
    print(fila)
    
matrizIdentidad(5)
