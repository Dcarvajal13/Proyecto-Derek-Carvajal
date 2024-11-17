class Cliente:
     lista_clientes = []

     def verificar_cedula_rif(cedula_rif):
            """Verifica si una cédula o RIF ya está registrado."""
            return any(cliente.cedula_rif == cedula_rif for cliente in Cliente.lista_clientes)

     
     def Modificar_cliente(self):
        cedula_rif = input("Ingrese la cédula o RIF del cliente que desea modificar: ")

        # Buscar al cliente en la lista
        cliente_encontrado = next((cliente for cliente in Cliente.lista_clientes if cliente.cedula_rif == cedula_rif), None)

        if cliente_encontrado:
            # Determinar si es Cliente Natural o Jurídico
            if isinstance(cliente_encontrado, Cliente_natural):
                print("\nCliente encontrado: (Cliente Natural)")
                print("Nombre:", cliente_encontrado.nombre)
                print("Apellido:", cliente_encontrado.apellido)
            elif isinstance(cliente_encontrado, Cliente_juridico):
                print("\nCliente encontrado: (Cliente Jurídico)")
                print("Razón Social:", cliente_encontrado.nombre)
                print("Nombre del Contacto:", cliente_encontrado.nombre_contacto)
                print("Teléfono del Contacto:", cliente_encontrado.telefono_contacto)   
                print("Correo del Contacto:", cliente_encontrado.correo_contacto)
            print("Correo:", cliente_encontrado.correo)
            print("Dirección:", cliente_encontrado.direccion)
            print("Teléfono:", cliente_encontrado.telefono)

            # Mostrar menú de modificación específico según el tipo de cliente
            if isinstance(cliente_encontrado, Cliente_natural):
                print("\n¿Qué desea modificar?\n"
                      "1. Nombre\n"
                      "2. Apellido\n"
                      "3. Correo electrónico\n"
                      "4. Dirección\n"
                      "5. Teléfono\n"
                      "6. Cancelar\n")
            elif isinstance(cliente_encontrado, Cliente_juridico):
                print("\n¿Qué desea modificar?\n"
                      "1. Razón Social\n"
                      "2. Correo electrónico\n"
                      "3. Dirección\n"
                      "4. Teléfono\n"
                      "5. Nombre del Contacto\n"
                      "6. Teléfono del Contacto\n"
                      "7. Cancelar\n")

            opcion_modificar = input("Seleccione una opción: ")

            # Procesar modificación según el tipo de cliente
            if opcion_modificar == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre o razón social: ").lower().strip()
                cliente_encontrado.nombre = nuevo_nombre
                print("Nombre o Razón Social modificado.")
            elif opcion_modificar == "2" and isinstance(cliente_encontrado, Cliente_natural):
                nuevo_apellido = input("Ingrese el nuevo apellido: ").strip().lower()
                cliente_encontrado.apellido = nuevo_apellido
                print("Apellido modificado.")
            elif opcion_modificar == "2" and isinstance(cliente_encontrado, Cliente_juridico):
                nuevo_correo = input("Ingrese el nuevo correo: ").strip().lower()
                cliente_encontrado.correo = nuevo_correo
                print("Correo modificado.")
            elif opcion_modificar == "3":
                nueva_direccion = input("Ingrese la nueva dirección: ").strip().lower()
                cliente_encontrado.direccion = nueva_direccion
                print("Dirección modificada.")
            elif opcion_modificar == "4":
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                cliente_encontrado.telefono = nuevo_telefono
                print("Teléfono modificado.")
            elif opcion_modificar == "5" and isinstance(cliente_encontrado, Cliente_juridico):
                nuevo_nombre_contacto = input("Ingrese el nuevo nombre del contacto: ").strip().lower()
                cliente_encontrado.nombre_contacto = nuevo_nombre_contacto
                print("Nombre del contacto modificado.")
            elif opcion_modificar == "6" and isinstance(cliente_encontrado, Cliente_juridico):
                nuevo_telefono_contacto = input("Ingrese el nuevo teléfono del contacto: ")
                cliente_encontrado.telefono_contacto = nuevo_telefono_contacto
                print("Teléfono del contacto modificado.")
            elif opcion_modificar in ("6", "7") and isinstance(cliente_encontrado, Cliente_juridico):
                print("Modificación cancelada.")
                return
            elif opcion_modificar == "6" and isinstance(cliente_encontrado, Cliente_natural):
                print("Modificación cancelada.")
                return
            else:
                print("Opción no válida.")

            # Confirmar modificaciones
            print("\nCliente modificado exitosamente:")
            if isinstance(cliente_encontrado, Cliente_natural):
                print("Nombre:", cliente_encontrado.nombre)
                print("Apellido:", cliente_encontrado.apellido)
            elif isinstance(cliente_encontrado, Cliente_juridico):
                print("Razón Social:", cliente_encontrado.nombre)
                print("Nombre del Contacto:", cliente_encontrado.nombre_contacto)
            print("Correo:", cliente_encontrado.correo)
            print("Dirección:", cliente_encontrado.direccion)
            print("Teléfono:", cliente_encontrado.telefono)
        else:
            print("\nCliente no encontrado.")
            
     def eliminar_cliente(self):

            cedula_rif = input("Ingrese la cédula o RIF del cliente que desea eliminar: ")

            # Buscar al cliente en la lista
            cliente_encontrado = next((cliente for cliente in Cliente.lista_clientes if cliente.cedula_rif == cedula_rif), None)

            if cliente_encontrado:
                # Determinar si es Cliente Natural o Jurídico
                if isinstance(cliente_encontrado, Cliente_natural):
                    print("\nCliente encontrado: (Cliente Natural)")
                    print("Nombre:", cliente_encontrado.nombre)
                    print("Apellido:", cliente_encontrado.apellido)
                elif isinstance(cliente_encontrado, Cliente_juridico):
                    print("\nCliente encontrado: (Cliente Jurídico)")
                    print("Razón Social:", cliente_encontrado.nombre)
                    print("Nombre del Contacto:", cliente_encontrado.nombre_contacto)
                    print("Teléfono del Contacto:", cliente_encontrado.telefono_contacto)   
                    print("Correo del Contacto:", cliente_encontrado.correo_contacto)
                print("Correo:", cliente_encontrado.correo)
                print("Dirección:", cliente_encontrado.direccion)
                print("Teléfono:", cliente_encontrado.telefono)

                confirmacion = input("¿Está seguro de que desea eliminar a este cliente? (si/no): ")

                if confirmacion.lower() == "si":
                    Cliente.lista_clientes.remove(cliente_encontrado)
                    print("Cliente eliminado exitosamente.")
                else:
                    print("Eliminación cancelada.")

     def buscar_cliente_cedula(self):
        cedula_rif = input("Ingrese la cédula o RIF del cliente que desea buscar: ")

        # Buscar al cliente en la lista
        cliente_encontrado = next((cliente for cliente in Cliente.lista_clientes if cliente.cedula_rif == cedula_rif), None)

        if cliente_encontrado:
            # Determinar si es Cliente Natural o Jurídico
            if isinstance(cliente_encontrado, Cliente_natural):
                print("\nCliente encontrado: (Cliente Natural)")
                print("Nombre:", cliente_encontrado.nombre)
                print("Apellido:", cliente_encontrado.apellido)
            elif isinstance(cliente_encontrado, Cliente_juridico):
                print("\nCliente encontrado: (Cliente Jurídico)")
                print("Razón Social:", cliente_encontrado.nombre)
                print("Nombre del Contacto:", cliente_encontrado.nombre_contacto)
                print("Teléfono del Contacto:", cliente_encontrado.telefono_contacto)   
                print("Correo del Contacto:", cliente_encontrado.correo_contacto)
            print("Correo:", cliente_encontrado.correo)
            print("Dirección:", cliente_encontrado.direccion)
            print("Teléfono:", cliente_encontrado.telefono)
        else:
            print("\nCliente no encontrado.")
            
     def buscar_cliente_correo(self):
        correo = input("Ingrese el correo del cliente que desea buscar: ")

        # Buscar al cliente en la lista
        cliente_encontrado = next((cliente for cliente in Cliente.lista_clientes if cliente.correo == correo), None)

        if cliente_encontrado:
            # Determinar si es Cliente Natural o Jurídico
            if isinstance(cliente_encontrado, Cliente_natural):
                print("\nCliente encontrado: (Cliente Natural)")
                print("Nombre:", cliente_encontrado.nombre)
                print("Apellido:", cliente_encontrado.apellido)
            elif isinstance(cliente_encontrado, Cliente_juridico):
                print("\nCliente encontrado: (Cliente Jurídico)")
                print("Razón Social:", cliente_encontrado.nombre)
                print("Nombre del Contacto:", cliente_encontrado.nombre_contacto)
                print("Teléfono del Contacto:", cliente_encontrado.telefono_contacto)   
                print("Correo del Contacto:", cliente_encontrado.correo_contacto)
            print("Correo:", cliente_encontrado.correo)
            print("Dirección:", cliente_encontrado.direccion)
            print("Teléfono:", cliente_encontrado.telefono)
        else:
            print("\nCliente no encontrado.")

class Cliente_natural(Cliente):
    def __init__(self, nombre, apellido, cedula_rif, correo, direccion_envio, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula_rif = cedula_rif
        self.correo = correo
        self.direccion = direccion_envio
        self.telefono = telefono

    def registrar_cliente_natural(self):
            while True: 
                    nombre = input("Ingrese el nombre del cliente: ").strip().lower()
                    if  nombre.isdigit() or nombre == "":  # Si son solo números o está vacío
                        print("El nombre solo debe contener letras. Inténtelo de nuevo.")
                    else: 
                        break
            while True: 
                    apellido = input("Ingrese el apellido del cliente: ").strip().lower()
                    if  apellido.isdigit() or apellido == "":  # Si son solo números o está vacío
                        print("El apellido solo debe contener letras. Inténtelo de nuevo.")
                    else: 
                        break
            while True: 
                    cedula_rif = input("Ingrese la cedula del cliente: ")
                    if not cedula_rif.isdigit() or cedula_rif == "":
                        print("La cedula debe contener solo números. Inténtelo de nuevo.")
                    elif Cliente.verificar_cedula_rif(cedula_rif):
                        print("Esta cédula ya está registrada. Inténtelo con otra.")
                    else: 
                        break
            correo = input("Ingrese el correo del cliente: ").strip().lower()
            direccion= input("Ingrese la direccion de envio: ").strip().lower()
            while True: 
                    telefono = input("Ingrese el telefono del cliente: ")
                    if not telefono.isdigit() or telefono == "":    
                        print("El teléfono debe contener solo números. Inténtelo de nuevo.")
                    else: 
                        break
            cliente_natural = Cliente_natural(nombre, apellido, cedula_rif, correo, direccion, telefono)
            Cliente.lista_clientes.append(cliente_natural)
            print("Cliente natural registrado exitosamente.")


class Cliente_juridico(Cliente):
    def __init__(self, nombre, cedula_rif, correo, direccion, telefono, nombre_contacto, telefono_contacto, correo_contacto):
        # Llamamos al constructor de la clase base
        self.nombre = nombre
        self.cedula_rif = cedula_rif
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
    

    def registrar_cliente_juridico(self):
            while True: 
                    razon_social = input("Ingrese el nombre de la empresa: ").strip().lower()
                    Cliente_juridico.nombre = razon_social.split()
                    if razon_social.isdigit():  
                        print("El nombre debe contener solo letras. Inténtelo de nuevo.")
                    else: 
                        break
            while True: 
                    cedula_rif = input("Ingrese el RIF de la empresa: ")
                    if not cedula_rif.isdigit() or cedula_rif == "":     
                        print("El RIF debe contener solo numeros. Inténtelo de nuevo.")
                    elif Cliente.verificar_cedula_rif(cedula_rif):
                        print("Este RIF ya está registrado. Inténtelo con otro.")
                    else: 
                        break
            correo = input("Ingrese el correo de la empresa: ").strip().lower()
            direccion = input("Ingrese la direccion de la empresa: ").strip().lower()
            while True: 
                    telefono = input("Ingrese el telefono de la empresa: ")
                    if not telefono.isdigit() or telefono == "": 
                        print("El telefono debe contener solo numeros. Inténtelo de nuevo.")
                    else: 
                        break
            while True: 
                    nombre_contacto = input("Ingrese el nombre del contacto: ").strip().lower()
                    if nombre_contacto.isdigit() or nombre_contacto == "":  
                        print("El nombre del contacto debe contener solo letras. Inténtelo de nuevo.")
                    else: 
                        break
            while True: 
                    telefono_contacto = input("Ingrese el telefono del contacto: ")
                    if not telefono_contacto.isdigit() or telefono_contacto == "": 
                        print("El telefono del contacto debe contener solo numeros. Inténtelo de nuevo.")
                    else: 
                        break
            correo_contacto = input("Ingrese el correo del contacto: ").strip().lower()
            cliente_juridico = Cliente_juridico(razon_social, cedula_rif, correo, direccion, telefono, nombre_contacto, telefono_contacto, correo_contacto)
            Cliente.lista_clientes.append(cliente_juridico)
            print("Cliente jurídico registrado exitosamente.")
         