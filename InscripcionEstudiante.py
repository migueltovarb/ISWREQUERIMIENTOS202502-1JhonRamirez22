class InscripcionEstudiante:
      
      def __init__(self, nombre, correo, horario, modalidad):
         self.nombre = nombre
         self.correo = correo
         self.horario = horario
         self.modalidad = modalidad
         self.inscrito = False
         #Definir si es presencial o virtual, solo deben existir esas dos opciones
         if modalidad not in ['presencial', 'virtual']:
             raise ValueError("La modalidad debe ser 'presencial' o 'virtual'")
         
         #Validar que el correo pertenezca a la universidad cooperativa de Colombia
         if not correo.endswith('@campusucc.edu.co'):
             raise ValueError("El correo debe pertenecer a la universidad cooperativa de Colombia")
         self.inscrito = True
#metodo que permita la inscripción de los estudiantes en los cursos virtuales y presenciales
      def inscribir(self):
          if self.inscrito:
              return f"El estudiante {self.nombre} ya está inscrito."
          else:
              self.inscrito = True
              return f"El estudiante {self.nombre} ha sido inscrito exitosamente."
   