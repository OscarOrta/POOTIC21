class Estudiante:
  Nombre = None
  altura = None
  peso = None
  sexo = None
  promedio = None 
  grado = None
  dirección = None
  telefono = None
  edad = None
  matricula = None
  
  def __init__(self,nombre,altura,peso,sexo,promedio):
    self.nombre = nombre
    self.altura = altura
    self.peso = peso
    self.sexo = sexo
    self.promedio = promedio 

  def aprendizaje (self):
    print("aprendizaje")
    
  def apuntar (self):
    print("apuntar")
    
  def RealizarEjercicios (self):
    print("Realización de ejercicios: ")
    
  def Deportes (self,deporte):
    print("Deporte: ",deporte)

  def Examenes (self,exames):
    print("Exámenes realizados: ",exames)

estudiante_01 = Estudiante("Eduardo","1.60","50","Masculino","8.2")
estudiante_01.nombre="Eduardo\t"
estudiante_01.altura= "Altura:1.60\t"
estudiante_01.peso= "Peso:50\t"
estudiante_01.sexo="Sexo:Masculino\t"
estudiante_01.promedio="Promedio:8.2\t"
estudiante_01.grado="Grado:Sexto\t"
estudiante_01.dirección="Dirección:r12\t"
estudiante_01.telefono="Teléfono:7761237\t"
estudiante_01.edad="Edad:18\t"
estudiante_01.matricula="Matrícula: 12345"
print(estudiante_01.nombre,estudiante_01.altura,estudiante_01.peso,estudiante_01.sexo)
print(estudiante_01.promedio,estudiante_01.grado,estudiante_01.dirección,estudiante_01.telefono)
print(estudiante_01.edad,estudiante_01.matricula)
estudiante_01.aprendizaje()
estudiante_01.apuntar()
estudiante_01.RealizarEjercicios()
estudiante_01.Deportes("Futbol")
estudiante_01.Examenes(4)
print("\n"*2)
estudiante_02 = Estudiante("Alondra","1.69","50","Femenino","9")
estudiante_02.nombre="Alondra\t"
estudiante_02.altura= "Altura:1.69\t"
estudiante_02.peso= "Peso:50\t"
estudiante_02.sexo="Sexo:Femenino\t"
estudiante_02.promedio="Promedio:9\t"
estudiante_02.grado="Grado:Cuarto\t"
estudiante_02.dirección="Dirección:f56\t"
estudiante_02.telefono="Teléfono:7761237\t"
estudiante_02.edad="Edad:17\t"
estudiante_02.matricula="Matrícula: 3465"
print(estudiante_02.nombre,estudiante_02.altura,estudiante_02.peso,estudiante_02.sexo)
print(estudiante_02.promedio,estudiante_02.grado,estudiante_02.dirección,estudiante_02.telefono)
print(estudiante_02.edad,estudiante_02.matricula)
estudiante_02.aprendizaje()
estudiante_02.apuntar()
estudiante_02.RealizarEjercicios()
estudiante_02.Deportes("Basketbol")
estudiante_02.Examenes(6)

