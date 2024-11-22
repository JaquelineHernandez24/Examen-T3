from ClienteFrecuente import ClienteFrecuente
class ClienteVIP(ClienteFrecuente):
    def __init__(self, nombre, email, telefono, direccion_envio, frecuencia_de_compra, puntos_vip):
        super().__init__(nombre, email, telefono, direccion_envio, frecuencia_de_compra)
        self._puntos_vip = puntos_vip

    # Getters y setters
    def get_puntos_vip(self):
        return self._puntos_vip

    def set_puntos_vip(self, puntos_vip):
        self._puntos_vip = puntos_vip

    # Métodos adicionales
    def acumular_puntos(self, puntos):
        self._puntos_vip += puntos
        print(f"Se acumularon {puntos} puntos VIP. Total ahora: {self._puntos_vip}")

    def canjear_puntos_vip(self, puntos):
        if self._puntos_vip >= puntos:
            self._puntos_vip -= puntos
            print(f"{puntos} puntos VIP canjeados.")
        else:
            print("No tienes suficientes puntos VIP.")

    def aplicar_descuento_vip(self, descuento):
        self.aplicar_descuento(descuento * 1.2)
        print(f"Descuento VIP aplicado.")
