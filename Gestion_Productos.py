class Producto:
    lista_productos = []
    def __init__(self, nombre_producto, descripcion, precio, categoria, inventario, modelo_vehiculo):
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria 
        self.inventario = inventario
        self.modelo_vehiculo = modelo_vehiculo

    def __str__(self):
        return f"Nombre: {self.nombre_producto}, Descripcion: {self.descripcion}, Precio: {self.precio}, Categoria: {self.categoria}, Inventario: {self.inventario}, Modelo de Vehiculo: {self.modelo_vehiculo}"

    def agregar_producto(self):
            nombre_producto = input('Ingrese el nombre del nuevo producto: ')
            descripcion = input('Ingrese la descripcion del producto: ')
            precio = input('Ingrese el precio del producto: ')
            categoria = input('Ingrese la categoria del producto: ')
            while True:
                inventario = input('Ingrese la cantidad en stock: ')
                if not inventario.isdigit():
                     print('La cantidad debe ser solo en numeros. Intentelo de nuevo')
                else:
                     invetario = int(inventario)
                     break
            modelo_vehiculo = input('Ingrese los modelos de carros para los cuales su producto aplica: ')
            lista_modelo_vehiculo = modelo_vehiculo.split(',')

            nuevo_productos = Producto(nombre_producto, descripcion, precio, categoria, inventario, modelo_vehiculo)
            Producto.lista_productos.append(nuevo_productos)
            print('Su producto ha sido agregado exitosamente')

    def buscar_producto(self):
         ke


        


