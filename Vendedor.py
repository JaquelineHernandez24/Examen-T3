from Usuario import Usuario
class Vendedor(Usuario):
    def __init__(self, nombre, email, telefono, nombre_tienda, productos_en_venta):
        super().__init__(nombre, email, telefono)
        self._nombre_tienda = nombre_tienda
        self._productos_en_venta = productos_en_venta

    # Getters y setters
    def get_nombre_tienda(self):
        return self._nombre_tienda

    def set_nombre_tienda(self, nombre_tienda):
        self._nombre_tienda = nombre_tienda

    def get_productos_en_venta(self):
        return self._productos_en_venta

    def set_productos_en_venta(self, productos_en_venta):
        self._productos_en_venta = productos_en_venta

    # Métodos adicionales
    def publicar_producto(self, producto):
        self._productos_en_venta.append(producto)
        print(f"Producto {producto} publicado.")

    def gestionar_inventario(self):
        print(f"Gestionando inventario para la tienda {self._nombre_tienda}.")

    def procesar_pedido(self, pedido):
        print(f"Procesando pedido: {pedido}")
