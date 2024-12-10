import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):  # Define el constructor de Cliente
        super().__init__(nombre, apellido)  # Llama al constructor de Persona
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, cantidad):
        cantidad = float(cantidad)
        self.balance += cantidad
        return self.balance

    def retirar(self, cantidad):
        cantidad = float(cantidad)
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Error en el retiro. No tiene suficiente sueldo.")

    def __str__(self):
        return(f"""Usuario: {self.nombre} {self.apellido}
        Numero de cuenta: {self.numero_cuenta}
        Balance: {self.balance}
        """)

def crear_cliente():
    print("Ingreso de nuevo cliente")
    nombre = input("Nombre del nuevo cliente: ")
    apellido = input("Apellido del nuevo cliente: ")
    numero_cuenta = 3245 # Será algo parecido a una PK AUTOINCREMENT, si no ella misma
    balance = 0 # Se inicia el cliente con el balance a cero
    cliente_nuevo = Cliente(nombre,apellido,numero_cuenta,balance)
    return cliente_nuevo

def inicio():
    cliente1 = crear_cliente()
    opcion = 0
    while opcion != 3:
        print(f"""
        Bienvenido,
        {cliente1}""")
        input("presiona enter para continuar...")
        os.system('cls')
        print(f"""
        MENU CAJERO
        1. Depositar
        2. Retirar
        3. Salir
        """)
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            cantidad = input("Introduce el monto a depositar: ")
            cliente1.depositar(cantidad)
        elif opcion == 2:
            cantidad = input("Introduce el monto a retirar: ")
            cliente1.retirar(cantidad)
        elif opcion == 3:
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            break
        else:
            print(f"Opción {opcion} no válida.")
        input("Presiona Enter para continuar...")

inicio()
