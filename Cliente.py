from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self, nombre, email, telefono, direccion_envio):
        super().__init__(nombre, email, telefono)
        self._direccion_envio = direccion_envio
        self._historial_compras = []

    # Getters y setters
    def get_direccion_envio(self):
        return self._direccion_envio

    def set_direccion_envio(self, direccion_envio):
        self._direccion_envio = direccion_envio

    def get_historial_compras(self):
        return self._historial_compras

    def set_historial_compras(self, historial_compras):
        self._historial_compras = historial_compras

    # Métodos adicionales
    def realizar_compra(self, producto):
        self._historial_compras.append(producto)
        print(f"Compra realizada: {producto}")

    def ver_historial_compras(self):
        print(f"Historial de compras: {self._historial_compras}")
