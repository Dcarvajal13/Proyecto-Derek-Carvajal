class Cliente:
    def __init__(self, nombre, apellido, cedula, correo, direccion_envio, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.direccion_envio = direccion_envio
        self.telefono = telefono

class Cliente_Juridico(Cliente):
    def __init__(self, nombre, apellido, cedula, correo, direccion_envio, telefono, razon_social):
        super().__init__(nombre, apellido, cedula, correo, direccion_envio, telefono)
        self.razon_social = razon_social

    