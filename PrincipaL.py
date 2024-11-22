from Vendedor import Vendedor
from Cliente import Cliente
from ClienteFrecuente import ClienteFrecuente
from ClienteVIP import ClienteVIP

def main():
    # Crear instancias
    vendedor = Vendedor("Juan", "juan@email.com", "123456789", "Tienda XYZ", ["Producto1", "Producto2"])
    cliente = Cliente("Ana", "ana@email.com", "987654321", "Calle 123")
    cliente_frecuente = ClienteFrecuente("Carlos", "carlos@email.com", "555666777", "Avenida Siempre Viva", 3)
    cliente_vip = ClienteVIP("Elena", "elena@email.com", "444555666", "Boulevard 456", 2, 100)

    # Usar los métodos de las clases
    vendedor.publicar_producto("Producto3")
    vendedor.gestionar_inventario()

    cliente.realizar_compra("Producto1")
    cliente.ver_historial_compras()

    cliente_frecuente.calcular_total_gastado()
    cliente_frecuente.aplicar_descuento(20)

    cliente_vip.acumular_puntos(50)
    cliente_vip.canjear_puntos_vip(30)
    cliente_vip.aplicar_descuento_vip(100)

if __name__ == "__main__":
    main()
