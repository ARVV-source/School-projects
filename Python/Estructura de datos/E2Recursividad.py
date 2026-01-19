def cuenta_regresiva(n):
  if n>0: 
    print(n) 
    cuenta_regresiva(n-1)
  else:
    print("Boom!")
  

cuenta_regresiva(5)