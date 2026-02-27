#Clases
class Car:
#Atributos (esto no suele usarse)
  color = "red"
#constructor
  def __init__ (self, brand, model, plate, ignition = False):
    self.brand = brand
    self.model = model
    self.plate = plate
    self.ignition = ignition
#metodos
  def ignite(self):
    self.ignition = not(self.ignition)


#Instanciar y utilizar el objeto
car1 = Car("Toyota", "yaris", "AMD-32k")

print(car1.color, " ", car1.brand, " ", car1.ignition)
car1.ignite()
print(car1.color, " ", car1.brand, " ", car1.ignition)
