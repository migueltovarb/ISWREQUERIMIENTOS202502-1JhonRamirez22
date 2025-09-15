class CrearClase:
#Metodo que permita la creacion de clases, al crear virtuales se debe crear un link para la reunion, y en caso de presencial, enviar el horario y el aula de clase
    def __init__(self, nombre_clase, modalidad, horario, aula=None, link_reunion=None):
        self.nombre_clase = nombre_clase
        self.modalidad = modalidad
        self.horario = horario
        self.aula = aula
        self.link_reunion = link_reunion
        
        if modalidad not in ['presencial', 'virtual']:
            raise ValueError("La modalidad debe ser 'presencial' o 'virtual'")
        
        if modalidad == 'presencial' and not aula:
            raise ValueError("Para clases presenciales, se debe especificar el aula")
        
        if modalidad == 'virtual' and not link_reunion:
            raise ValueError("Para clases virtuales, se debe especificar el link de la reunión")