def fibonacci(cantidad, a=0, b=1):
  lista = []
  for i in range(cantidad):
    lista.append(a)
    a, b = b, a+b
  print(lista)


fibonacci(10)