class Cliente:

    # Defino el constructor de la clase:
    def __init__(self, nombre, email, contrasenia, telefono, direccion, intereses):

        # Defino sus atributos:
        self.nombre = nombre
        self.email = email
        self.__contrasenia = contrasenia
        self.__telefono = telefono
        self.__direccion = direccion
        self.intereses = intereses

    # Defino el primer método para comprar un producto:
    def comprar(self, producto, tienda):
        print(f"Usted acaba de comprar el producto {producto} en {tienda}.")
        print(f"Se ha enviado un correo a {self.email} con la confirmación de la compra.")
        print(">>>>>")

    # Defino el segundo método para pagar un producto:
    def pagar(self, producto):
        print(f"Usted acaba de iniciar el proceso de pago del producto {producto}.")
        print(f"Por favor, realice el pago con el medio seleccionado y luego recibirá un mail de confirmación.")
        print(">>>>>")

    # Defino el tercer método para proceso de devolución de producto:
    def devolver(self, producto, tienda):
        print(f"Usted ha solicitado la devolución del producto {producto} comprado en {tienda}.")
        print(f"Se ha enviado un correo a {self.email} con las instrucciones.")
        print(">>>>>")

    # Defino el cuarto método que será el __str__ para dar el nombre del cliente
    def __str__(self):
        return f">>>>>\nNuevo cliente creado: {self.nombre}\nEmail: {self.email}\nIntereses: {self.intereses}\n>>>>>"