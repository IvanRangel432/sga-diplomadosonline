# nombre=Ivan Rangel 
# Programa=Diplomados Online
# Funcion del archivo: En este archivo estaran registrados las Clases del SGA-DO

#En clase "Persona" sirve para guardar los datos en general de cualquier persona que se registre 

class Persona:
    def __init__(self,cedula,nombre,correo):
        self.cedula=cedula
        self.nombre=nombre
        self.correo=correo

    def mostrarInformacion(self):
     print(f"Cedula:{self.cedula}")
     print(f"Nombre:{self.combre}")
     print(f"Correo:{self.correo}")


class Alumno:
    # La clase "Alumnos" la usamos para almacenar los datos del estudiante
      def __init__(self, cedula, correo, nombre, tipo_programa):
        self.cedula = cedula
        self.correo = correo
        self.nombre = nombre
        self.tipo_programa = tipo_programa # El curso o la carrera que este haciendo el estudiante

    # Por pantalla se muestra la informacion del alumno
      def mostrarInformation(self):
        print(f"Cedula: {self.cedula}")
        print(f"Programa: {self.tipo_programa}")
        print(f"Correo: {self.correo}")
        print(f"Nombre: {self.nombre}")

class Profesor:
      def __init__(self, cedula, nombre, especialidad_materia, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.especialidad_materia = especialidad_materia

      def mostrarInformacion(self):  # Aqui se mostrara la informacion del nuevo profesor
        print(f"Cedula: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Especialidad_materia: {self.especialidad_materia}")

class Notas:
    def __init__(self, cedula_encontrada, notas):
          self.cedula_encontrada = cedula_encontrada
          self.notas = notas

    # En esta parte se mostraran en pantalla las notas del alumno buscado por la cedula
    def mostrar_Notas(self):
        print(f"Cedula: {self.cedula_encontrada}")
        print(f"Notas: {self.notas}")
    
