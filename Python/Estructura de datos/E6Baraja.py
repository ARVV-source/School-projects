valor = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
figura = ["C♥","D♦","T♣","P♠"]
Baraja = [[i+j for j in valor]for i in figura]
for fila in Baraja:
  print(fila)
  