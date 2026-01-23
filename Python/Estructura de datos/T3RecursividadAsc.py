def tablaAsc (tabla, cant, contador=1):
  if contador<cant:
    print(f"{tabla}x{contador}={tabla*contador}")
    tablaAsc(tabla, cant, contador+1)
  else:
    print(f"{tabla}x{contador}={tabla*contador}")

def tabladesc (tabla, cant):
  if 1<cant:
    print(f"{tabla}x{cant}={tabla*cant}")
    tabladesc(tabla, cant-1)
  else:
    print(f"{tabla}x{cant}={tabla*cant}")

tablaAsc(5, 10)
print("")
tabladesc(5, 10)