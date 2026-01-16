#Problema 1
a = {"manchego":40, "roquefort":160, "camembert":80}
b = {"manchego":120, "roquefort":120, "camembert":120}
c = {"manchego":150, "roquefort":80, "camembert":80}
bandejas = [a, b, c]
total_queso = 0
for i in a:
  a[i] *= 50
for i in b:
  b[i] *= 80
for i in c:
  c[i] *= 100
for bandeja in bandejas:
  for cant_queso in bandeja.values():
    total_queso += cant_queso
total_queso /= 1000
print(f"La suma de las 3 bandejas tiene: {total_queso} kilos de queso")
def elCuentaquesosinador(Tipo_queso):
  contador=0
  for bandeja in bandejas:
    contador += bandeja[Tipo_queso]
  contador /= 1000
  return contador
print(f"Se necesitan {elCuentaquesosinador("manchego")} kilos de manchego, ", end="")
print(f"{elCuentaquesosinador("roquefort")} kilos de roquefort y {elCuentaquesosinador("camembert")} kilos de camembert")

#problema 2
resultado = {}
horas = {"chico": {"taller": 25, "admin": 1.0}, "mediano": {"taller":30, "admin":1.2}, "grande": {"taller": 33, "admin": 1.3}}
cantidad = {"a" : {"chico": 400, "mediano": 200, "grande": 50}, "b" : {"chico": 300, "mediano": 100, "grande": 30}}
for modelo in cantidad:
  resultado[modelo] = {"taller": 0, "admin": 0}
  for tamano in cantidad[modelo]:
    resultado[modelo]["taller"] += horas[tamano]["taller"]*cantidad[modelo][tamano]
    resultado[modelo]["admin"] += horas[tamano]["admin"]*cantidad[modelo][tamano]
print(f"El modelo A necesita {resultado["a"]["taller"]} horas en taller y {resultado["a"]["admin"]} en administracion")
print(f"El modelo A necesita {resultado["b"]["taller"]} horas en taller y {resultado["b"]["admin"]} en administracion")
