# Problema de lanzar dos dados
from random import randint

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return [dado1, dado2]

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1+dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dados = lanzar_dados()
d1, d2 = dados
jugada = evaluar_jugada(d1, d2)
print(jugada)


def lista_atributos(**kwargs):
    lista = list()
    for key, value in kwargs.items():
        lista.append(value)

    return lista

print(lista_atributos(uno='hola', dos='adios'))