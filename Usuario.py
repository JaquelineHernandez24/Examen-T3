class Usuario:
    def __init__(self, nombre, email, telefono):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    # Getters y setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    # Métodos de la clase Usuario
    def registrar(self):
        print(f"Usuario {self._nombre} registrado con éxito.")

    def iniciar_sesion(self):
        print(f"Bienvenido {self._nombre}, sesión iniciada.")
