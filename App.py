import requests
from Gestion_Clientes import Cliente, Cliente_juridico, Cliente_natural
from Gestion_Productos import Producto
from Gestion_Ventas import Venta
from Gestion_Envios import Envio
from Gestion_Pagos import Pago
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

class APP:

    def start(self):
        self.menu_cliente()

    lista_productos = []
    lista_ventas = []
    lista_envios = []
    lista_pagos = []

    def menu_cliente(self):
        while True:
            print("Bienvenido al sistema de ventas\n\n"
                '--------MENU--------\n\n'
                "1. Registrar cliente\n"
                "2. Modificar cliente\n"
                "3. Eliminar cliente\n"
                "4. Buscar cliente\n"
                "5. Salir\n\n")
            
            
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                tipo_cliente = input("Seleccione el tipo de cliente:\n"
                                    '1. Natural\n'
                                    '2. Juridico\n\n')
                
                if tipo_cliente == "1":
                    Cliente_natural.registrar_cliente_natural(Cliente_natural)

                elif tipo_cliente == "2":
                    Cliente_juridico.registrar_cliente_juridico(Cliente_juridico)
                else:
                    print("Tipo de cliente no valido")

            elif opcion == "2":  # Modificar cliente
                Cliente.Modificar_cliente(Cliente)

            elif opcion == "3":  # Eliminar cliente
                Cliente.eliminar_cliente(Cliente)

            elif opcion == "4":  # Buscar cliente
                forma_busqueda = input("Seleccione la forma de busqueda:\n"
                                    '1. Por cedula o por RIF\n'
                                    '2. Por correo\n\n')
                if forma_busqueda == "1":
                    Cliente.buscar_cliente_cedula(Cliente)
                elif forma_busqueda == "2":
                    Cliente.buscar_cliente_correo(Cliente)
                else:
                    print("Opcion no valida")