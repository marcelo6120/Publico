from Proveedores import proveedor
from Productos import producto
global prov1,prod1
import os
import time 
Opcion = ""
prov1 = proveedor()
prod1 = producto()

while(Opcion!=5):
    print("1. Agregar Proveedor")
    print("2. Crear un Producto")
    print("3. Agregar producto a Proveedor")
    print("4. Listar Productos")
    print("5. Salir")
    print("Ingrese la opcion la desea: ")
    Opcion = int(input())

    if Opcion == 1:
        os.system('cls')
        # CAPTURA DE DATOS DESDE TECLADO
        apellidos = input("Ingrese Apellidos:")
        nombre = input("Ingrese Nombre:")
        telefono = input("Ingrese Telefono:")

        #CREAR EL PROVEEDOR
        prov1.AgregarProveedor(apellidos,nombre,telefono)
        os.system('cls')
    elif Opcion == 2:
        
        os.system('cls')
        # PEDIR INGRESO DE DATOS DEL PRODUCTO
        codigo = int(input("Ingrese codigo del producto: "))
        nomproducto = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese precio del producto: "))
                    
        # CREAR PRODUCTO
        prod1.CrearProducto(codigo,nomproducto,precio)
        os.system('cls')
    elif Opcion == 3:
        os.system('cls')
        prov1.AgregarProductos(prod1)
        time.sleep(3)
        os.system('cls')
    elif Opcion ==4:
        os.system('cls')
        prod1.ListaProductos(prod1)
        time.sleep(3)
        os.system('cls')
    elif Opcion == 5:
        exit
