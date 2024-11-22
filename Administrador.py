from Usuario import Usuario
class Administrador(Usuario):
    def __init__(self, nombre, email, telefono, nivel_acceso):
        super().__init__(nombre, email, telefono)
        self._nivel_acceso = nivel_acceso

    # Getters y setters
    def get_nivel_acceso(self):
        return self._nivel_acceso

    def set_nivel_acceso(self, nivel_acceso):
        self._nivel_acceso = nivel_acceso

    # Métodos adicionales
    def gestionar_productos(self):
        print("Gestionando productos en el sistema.")

    def ver_reportes(self):
        print("Viendo reportes del sistema.")
