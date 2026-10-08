# nombre=Ivan Rangel 
# Programa=Diplomados Online
# Funcion del archivo: En este archivo estaran registrados las Clases del SGA-DO

#En clase "Persona" sirve para guardar los datos en general de cualquier persona que se registre 


class Persona:
    def __init__(self, cedula, nombre, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo

    def mostrarInformacion(self):
        print(f"Cedula: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")


class Alumno(Persona):
    # La clase "Alumno" almacena los datos específicos del estudiante
    def __init__(self, cedula, nombre, correo, tipo_programa):
        super().__init__(cedula, nombre, correo)
        self.tipo_programa = tipo_programa  # Curso, Diplomado o Bootcamp

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Programa: {self.tipo_programa}")


class Profesor(Persona):
    def __init__(self, cedula, nombre, correo, especialidad_materia):
        super().__init__(cedula, nombre, correo)
        self.especialidad_materia = especialidad_materia

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Especialidad/Materia: {self.especialidad_materia}")


class Notas:
    def __init__(self, cedula_encontrada, notas):
        self.cedula_encontrada = cedula_encontrada
        self.notas = notas

    def mostrar_Notas(self):
        print(f"Cedula: {self.cedula_encontrada}")
        print(f"Notas: {self.notas}")