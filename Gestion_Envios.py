class Envio:
    def _init_(self, orden_compra, servicio_envio, datos_motorizado=None, costo=0):
        self.orden_compra = orden_compra
        self.servicio_envio = servicio_envio
        self.datos_motorizado = datos_motorizado
        self.costo = costo
        self.fecha = None  # Se puede establecer al registrar el envío

    def registrar_envio(self):
        # Lógica para registrar el envío
        pass

    def buscar_envio(self, **filtros):
        # Lógica para buscar envíos según los filtros
        pass