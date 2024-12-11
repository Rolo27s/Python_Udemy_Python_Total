"""
Ejercicio del día 8.
Turnero para comercio.
Archivo que contiene generador y decorador, además de la clase.
"""

class Comercio:
    def __init__(self, nombre = 'F', numero = 1):
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"{self.nombre} - {self.numero}"


def generador_comercio(nombre):
    """
    Genera números para un comercio específico.
    El contador se reinicia al llegar a 99.
    """
    numero = 1
    while True:
        yield Comercio(nombre, numero)
        numero += 1
        if numero > 99:
            numero = 1


def simple_decorator(func):
    """
   Decorador que envuelve una función con mensajes adicionales.
   """
    def wrapper(obj):
        print("Su turno es:")
        func(obj) # Aquí irá un print del objeto Comercio porque le modifiqué el __str__ y está preparado directo
        print("Aguarde y será atendido/a")
    return wrapper

@simple_decorator
def mensaje(obj):
    """
    Muestra el mensaje con el turno del cliente.
    """
    print(obj)
