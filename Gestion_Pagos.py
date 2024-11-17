class Pago:
    def _init_(self, cliente, monto, moneda, tipo_pago, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_pago = tipo_pago
        self.fecha = fecha

    def registrar_pago(self):
        # Lógica para registrar el pago
        pass

    def buscar_pago(self, **filtros):
        # Lógica para buscar pagos según los filtros
        pass