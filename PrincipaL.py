from Vendedor import Vendedor
from Cliente import Cliente
from ClienteFrecuente import ClienteFrecuente
from ClienteVIP import ClienteVIP

class Principal:
    def __init__(self):
        print("=" * 50)
        print("🛒 Bienvenido a Comercio Electrónico 🛒")
        print("=" * 50)

    def ejecutar(self):
        while True:
            print("\nPor favor, seleccione una opción para comenzar:")
            print("1. Registrar un vendedor")
            print("2. Registrar un cliente")
            print("3. Registrar un cliente frecuente")
            print("4. Registrar un cliente VIP")
            print("5. Salir")
            print("=" * 50)

            opcion = input("Ingrese su opción (1/2/3/4/5): ")

            if opcion == "1":
                self.registrar_vendedor()

            elif opcion == "2":
                self.registrar_cliente()

            elif opcion == "3":
                self.registrar_cliente_frecuente()

            elif opcion == "4":
                self.registrar_cliente_vip()

            elif opcion == "5":
                print("\n¡Gracias por utilizar Comercio Electrónico! 👋")
                break

            else:
                print("\nOpción no válida. Intente nuevamente.\n")

    def registrar_vendedor(self):
        print("\n--- Registro de Vendedor ---")
        nombre = input("Ingrese el nombre del vendedor: ")
        email = input("Ingrese el email del vendedor: ")
        telefono = input("Ingrese el teléfono del vendedor: ")
        nombre_tienda = input("Ingrese el nombre de la tienda: ")
        productos_en_venta = input("Ingrese los productos en venta separados por comas: ").split(",")

        vendedor = Vendedor(nombre, email, telefono, nombre_tienda, productos_en_venta)
        print(f"\n¡Vendedor {nombre} registrado exitosamente!")
        print(f"Tienda: {nombre_tienda}, Productos: {productos_en_venta}\n")

    def registrar_cliente(self):
        print("\n--- Registro de Cliente ---")
        nombre = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        direccion_envio = input("Ingrese la dirección de envío: ")

        cliente = Cliente(nombre, email, telefono, direccion_envio)
        print(f"\n¡Cliente {nombre} registrado exitosamente!")
        print(f"Dirección de Envío: {direccion_envio}\n")

    def registrar_cliente_frecuente(self):
        print("\n--- Registro de Cliente Frecuente ---")
        nombre = input("Ingrese el nombre del cliente frecuente: ")
        email = input("Ingrese el email del cliente frecuente: ")
        telefono = input("Ingrese el teléfono del cliente frecuente: ")
        direccion_envio = input("Ingrese la dirección de envío: ")
        frecuencia_de_compra = int(input("Ingrese la frecuencia de compra (en compras mensuales): "))

        cliente_frecuente = ClienteFrecuente(nombre, email, telefono, direccion_envio, frecuencia_de_compra)
        print(f"\n¡Cliente frecuente {nombre} registrado exitosamente!")
        print(f"Frecuencia de Compra: {frecuencia_de_compra}\n")

    def registrar_cliente_vip(self):
        print("\n--- Registro de Cliente VIP ---")
        nombre = input("Ingrese el nombre del cliente VIP: ")
        email = input("Ingrese el email del cliente VIP: ")
        telefono = input("Ingrese el teléfono del cliente VIP: ")
        direccion_envio = input("Ingrese la dirección de envío: ")
        frecuencia_de_compra = int(input("Ingrese la frecuencia de compra (en compras mensuales): "))
        puntos_vip = int(input("Ingrese los puntos VIP iniciales: "))

        cliente_vip = ClienteVIP(nombre, email, telefono, direccion_envio, frecuencia_de_compra, puntos_vip)
        print(f"\n¡Cliente VIP {nombre} registrado exitosamente!")
        print(f"Puntos VIP: {puntos_vip}, Frecuencia de Compra: {frecuencia_de_compra}\n")


# Para ejecutar el programa
if __name__ == "__main__":
    app = Principal()
    app.ejecutar()
