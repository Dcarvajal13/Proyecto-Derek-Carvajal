class Venta:
    def __init__(self, cliente, productos, cantidades, metodo_pago, metodo_envio):
        self.cliente = cliente
        self.productos = productos
        self.cantidades = cantidades
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.subtotal = self.calcular_subtotal()
        self.descuentos = self.calcular_descuentos()
        self.iva = self.calcular_iva()
        self.igtf = self.calcular_igtf()
        self.total = self.calcular_total()
        self.fecha = None  # Se puede establecer al registrar la venta

    def calcular_subtotal(self):
        return sum(p.precio * c for p, c in zip(self.productos, self.cantidades))

    def calcular_descuentos(self):
        # Lógica para calcular descuentos
        return 0  # Placeholder

    def calcular_iva(self):
        return self.subtotal * 0.16

    def calcular_igtf(self):
        return self.total * 0.03 if self.metodo_pago == "divisas" else 0

    def calcular_total(self):
        return self.subtotal - self.descuentos + self.iva + self.igtf

    def registrar_venta(self):
        # Lógica para registrar la venta
        pass

    def generar_factura(self):
        # Lógica para generar la factura de la venta
        pass

    def buscar_venta(self, **filtros):
        # Lógica para buscar ventas según los filtros
        pass