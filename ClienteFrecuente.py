from Cliente import Cliente
class ClienteFrecuente(Cliente):
    def __init__(self, nombre, email, telefono, direccion_envio, frecuencia_de_compra):
        super().__init__(nombre, email, telefono, direccion_envio)
        self._frecuencia_de_compra = frecuencia_de_compra
        self._gastototal = 0

    # Getters y setters
    def get_frecuencia_de_compra(self):
        return self._frecuencia_de_compra

    def set_frecuencia_de_compra(self, frecuencia_de_compra):
        self._frecuencia_de_compra = frecuencia_de_compra

    def get_gastototal(self):
        return self._gastototal

    def set_gastototal(self, gastototal):
        self._gastototal = gastototal

    # Métodos adicionales
    def calcular_total_gastado(self):
        print(f"Total gastado por cliente: {self._gastototal}")

    def aplicar_descuento(self, descuento):
        self._gastototal -= descuento
        print(f"Descuento aplicado. Total ahora: {self._gastototal}")

    def ver_historial_de_compras(self):
        super().ver_historial_compras()
        print(f"Frecuencia de compras: {self._frecuencia_de_compra}")
