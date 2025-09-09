class DobleFormato:
#este metodo debe permitir que los trabajos solo se puedan enviar en formato .pdf o .docx
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        if not (self.nombre_archivo.endswith('.pdf') or self.nombre_archivo.endswith('.docx')):
            raise ValueError("El archivo debe estar en formato .pdf o .docx")
#metodo que permita la seleccion de formato
    def seleccionar_formato(self):
        if self.nombre_archivo.endswith('.pdf'):
            return f"El archivo '{self.nombre_archivo}' es un documento PDF."
        elif self.nombre_archivo.endswith('.docx'):
            return f"El archivo '{self.nombre_archivo}' es un documento Word (.docx)."
        else:
            return "Formato no soportado."