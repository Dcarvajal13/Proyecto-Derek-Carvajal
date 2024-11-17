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
        self.mostrar_menu_principal()

    lista_productos = []
    lista_ventas = []
    lista_envios = []
    lista_pagos = []

    def mostrar_menu_principal(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Productos")
           
            print("2. Clientes")
            print("3. Ventas")
            print("4. Pagos")
            print("5. Envios")
            print("6. Indicadores")
            print("7. Salir")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.menu_productos()   
            elif opcion == "2":
                self.menu_cliente()
            elif opcion == "3":
                self.menu_ventas()
            elif opcion == "4":
                self.menu_pagos()
            elif opcion == "5":
                self.menu_envios()
            elif opcion == "6":
                self.menu_indicadores()
            elif opcion == "7":
                print('Gracias por preferirnos, hasta luego')
                break
            else:
                print("Opción no válida")

        
                    
    
    def menu_cliente(self):
        while True:
            print("Bienvenido al sistema de clientes\n\n"
                '--------MENU CLIENTES--------\n\n'
                "1. Registrar cliente\n"
                "2. Modificar cliente\n"
                "3. Eliminar cliente\n"
                "4. Buscar cliente\n"
                "5. Regresar\n\n")
            
            
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
                    
            elif opcion == "5":  #Regresar a menu principal
                self.start()
            else:
                print("Opcion no valida")

    def menu_productos(self):
        while True:
            print('Bienvenido al sistema de productos\n\n'
                  '--------MENU PRODUCTOS--------\n\n'
                  '1. Agregar nuevos productos\n'
                  '2. Buscar productos\n'
                  '3. Modificar productos\n'
                  '4. Eliminar productos\n'
                  '5. Regresar\n\n')
            
            opcion = input('Seleccione una opcion: ')

            if opcion == '1':
                Producto.agregar_producto(Producto)
            elif opcion == '2':
                Producto.buscar_producto(Producto)
            elif opcion == '3':
                Producto.modificar_producto(Producto)
            elif opcion == '4':
                Producto.eliminar_producto(Producto)
            elif opcion == '5':
                break
            else:
                print('Opcion no valida')

    
    