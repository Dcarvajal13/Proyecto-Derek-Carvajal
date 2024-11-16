class Producto:
    def __init__(self, nombre, descripcion, precio, categoria, inventario, modelo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.inventario = inventario
        self.modelos = []

    def mostrar_producto(self):
        print(f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nCategoria: {self.categoria}\nInventario: {self.inventario}\nModelos: {self.modelos}")

    