class Contactos:
    CONTACTOS = []
    def __init__(self, nombre, telefono, correo, cargo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cargo = cargo

    def RegistarContacto(self):
        self.nombre = input("Ingrese el nombre del contacto: ")
        self.telefono = input("Ingrese el teléfono del contacto: ")
        self.correo = input("Ingrese el correo del contacto: ")
        self.cargo = input("Ingrese el cargo del contacto: ")
        if self.nombre and self.telefono and self.correo and self.cargo:
            print("Contacto registrado exitosamente.")
        else:
            print("Error: Todos los campos son obligatorios.")
def BuscarContactos():
    if not Contactos.CONTACTOS:
        print("No hay contactos registrados.")
        return
    informacion = input("Buscar por (nombre, telefono, correo, cargo): ").strip().lower()
    valor = input(f"Ingrese el valor para {informacion}: ").strip().lower()
    encontrados = [c for c in Contactos.CONTACTOS if getattr(c, informacion, '').lower() == valor]
    if encontrados:
        for c in encontrados:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}, Correo: {c.correo}, Cargo: {c.cargo}")
        else:
            print("No se encontraron contactos con esa informacion.")

def EliminarContacto(self):
        if not Contactos.CONTACTOS:
            print("No hay contactos registrados.")
            return
        nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
        for i, c in enumerate(Contactos.CONTACTOS):
            if c.nombre.lower() == nombre.lower():
                del Contactos.CONTACTOS[i]
                print("Contacto eliminado exitosamente.")
                return
        print("Contacto no encontrado.")

def MostrarContactos():
        if not Contactos.CONTACTOS:
            print("No hay contactos registrados.")
            return
        for c in Contactos.CONTACTOS:
            print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}, Correo: {c.correo}, Cargo: {c.cargo}")
def main():
    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Registrar Contacto")
        print("2. Buscar Contacto")
        print("3. Eliminar Contacto")
        print("4. Mostrar Todos los Contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            c = Contactos('', '', '', '')
            c.RegistarContacto()
            if c.nombre and c.telefono and c.correo and c.cargo:
                Contactos.CONTACTOS.append(c)
        elif opcion == '2':
            BuscarContactos()
        elif opcion == '3':
            if Contactos.CONTACTOS:
                nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
                for i, c in enumerate(Contactos.CONTACTOS):
                    if c.nombre.lower() == nombre.lower():
                        del Contactos.CONTACTOS[i]
                        print("Contacto eliminado exitosamente.")
                        break
                else:
                    print("Contacto no encontrado.")
            else:
                print("No hay contactos registrados.")
        elif opcion == '4':
            MostrarContactos()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()