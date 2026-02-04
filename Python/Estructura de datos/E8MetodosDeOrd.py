def insertionSort(lista):
  for i in range (1, len(lista)):
    clave = lista[i]
    valIzq = i - 1
    while valIzq >= 0 and clave < lista[valIzq]:
      lista[valIzq + 1] = lista[valIzq]
      valIzq -= 1
    lista[valIzq + 1] = clave
  return (lista)

def quickSort(lista):
  if len(lista) < 2:
    return lista
  else:
    medio = lista[len(lista)//2]
    izquierda =[num for num in lista if num < medio]
    centro =[num for num in lista if num == medio]
    derecha =[num for num in lista if num > medio]
    return quickSort(izquierda) + centro + quickSort(derecha)

ejemplo = [1,5,3,4,7,6,9,8,2]
print(quickSort(ejemplo))
