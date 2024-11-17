class Producto:
    def __init__(self, nombre_producto, descripcion, precio, categoria, inventario, modelo_vehiculo):
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria 
        self.inventario = inventario
        self.modelo_vehiculo = modelo_vehiculo

    def __str__(self):
        return f"Nombre: {self.nombre_producto}, Descripcion: {self.descripcion}, Precio: {self.precio}, Categoria: {self.categoria}, Inventario: {self.inventario}, Modelo de Vehiculo: {self.modelo_vehiculo}"

    
class Gestion_Productos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre_producto == nombre_producto:
                return producto
        return None

    def eliminar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre_producto == nombre_producto:
                self.productos.remove(producto)
                return True
        return False

    def modificar_producto(self, nombre_producto, producto_modificado):
        for i, producto in enumerate(self.productos):
            if producto.nombre_producto == nombre_producto:
                self.productos[i] = producto_modificado
                return True
        return False