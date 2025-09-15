class Curso:
#sera la clase principal, esta tiene que tener todos los datos relacionados a un curso
    def __init__(self, nombre, descripcion, duracion, valor, modalidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.valor = valor
        self.modalidad = modalidad
        #Definir si es presencial o virtual, solo deben existir esas dos opciones
        if modalidad not in ['presencial', 'virtual']:
            raise ValueError("La modalidad debe ser 'presencial' o 'virtual'")          
#metodo que permita la creación de los cursos
    def crear_curso(self):  
        return f"Curso '{self.nombre}' creado con éxito. Descripción: {self.descripcion}, Duración: {self.duracion} horas, Valor: ${self.valor}, Modalidad: {self.modalidad}"

    def actualizar_curso(self, nombre=None, descripcion=None, duracion=None, valor=None, modalidad=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if duracion:
            self.duracion = duracion
        if valor:
            self.valor = valor
        if modalidad:
            if modalidad not in ['presencial', 'virtual']:
                raise ValueError("La modalidad debe ser 'presencial' o 'virtual'")
            self.modalidad = modalidad
        return f"Curso '{self.nombre}' actualizado con éxito."