class Mascota:
  raza = None
  tamaño = None
  sexo = None
  especie = None
  colorPelo = None 
  
  def __init__(self,raza,tamaño,especie):
    self.raza = raza
    self.tamaño = tamaño
    self.especie = especie

  def adiestramiento (self):
    print("Su mascota esta adiestrada")
    
  def correr (self):
    print("Correr")
    
  def dormir (self):
    print("dormir")
    
  def edad (self,edad):
    print("Edad",edad, "años")

gato = Mascota("Gato esfinge","Pequeño","Mamífero")
print("Raza: ",gato.raza)
print("Tamaño: ",gato.tamaño)
print("Especie: ",gato.especie)
gato.sexo="Macho"
gato.colorPelo="Rosa"
print(gato.colorPelo)
print(gato.sexo)
gato.adiestramiento()
gato.correr()
gato.dormir()
gato.edad(2)
print("\n"*2)
perro = Mascota("Labrador","grnade","Mamífero")
print("Raza: ",perro.raza)
print("Tamaño: ",perro.tamaño)
print("Especie: ",perro.especie)
gato.sexo="Hembra"
gato.colorPelo="blanco"
print(gato.colorPelo)
print(gato.sexo)
gato.adiestramiento()
gato.correr()
gato.dormir()
gato.edad(5)