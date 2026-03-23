import csv
import os
from datetime import date
from T8ArbolAVL import ArbolAVL


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'ciudades.csv')

ciudades = []
with open(csv_path, 'r') as archivo:
    for fila in csv.DictReader(archivo):
        idCiudad = int(fila['IdCiudad'])
        abr = fila['Abr']
        fecha = date.strptime(fila['Inicio'], '%Y-%m-%d')
        ciudades.append((idCiudad, abr, fecha, fecha.year))

arbol = ArbolAVL()
for idCiudad, abr, fecha, año in ciudades:
    arbol.insertar(abr)

print("=" * 60)
print(f"Total de ciudades: {len(ciudades)}")
print("\nÁrbol AVL:")
arbol.mostrar_arbol()
print("\nRecorrido en orden:")
print(arbol.recorrido_inorden())
print("=" * 60)
