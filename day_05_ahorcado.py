# Juego de 'El ahorcado'

from random import choice
import re

palabras = ["matricula", "robot", "copiloto", "inteligente", "shaco", "mozart", "ajedrez", "alistar"]

palabra = choice(palabras)
palabra_descompuesta = []
for letra in palabra:
    palabra_descompuesta.append(letra)

vida = 6
lista_incorrectas = set()
lista_encontradas = set()

def iniciar_juego(letras):
    line_list = []
    for x in range(len(letras)):
        line_list.append("_")

    palabra_inicial_oculta = " ".join(line_list)
    print("Juego de 'El Ahorcado'")
    print(f"Tienes {vida} vida/s")
    if len(lista_incorrectas) != 0:
        print(lista_incorrectas)
    print(palabra_inicial_oculta)

def pedir_letra():
    l = input("Dime una letra: ")
    reg_ex_char = re.match("^[a-z]$", l)
    if reg_ex_char:
        return l
    else:
        print("Input incorrecto...")
        pedir_letra()

def set_vida(v):
        return v-1

def buscar_letra(v, l):
    c = 0
    for letra_input in palabra_descompuesta:
        if l == letra_input:
            print("Letra encontrada!")
            c += 1
            return letra_input
        else:
            pass
    if c == 0:
        print("Fallaste. Letra no encontrada...")
        set_vida(v)
        return -1

def jugando(le, pd):
    palabr = []
    for l1 in pd:
        c = 0
        for l2 in le:
            if l1 == l2:
                # print(l2)
                palabr.append(l2)
                c += 1
            else:
                pass
        if c == 0:
            # print("_")
            palabr.append("_")


    palabra_f = "".join(palabr)
    print(palabra_f)

    e = 0
    for l in palabra_f:
        if l != "_":
            e = 0
        else:
            e += 1

    if e == 0:
        print("Enhorabuena! Has ganado el juego")
        return palabra_f

    return palabra_f


iniciar_juego(palabra_descompuesta)

while vida >= 1:
    li = pedir_letra()

    # Si no se encuentra la letra se pierde una vida y se actualiza la variable global
    if buscar_letra(vida, li) == -1:
        vida = set_vida(vida)
        print(f"Tienes {vida} vida/s")
        lista_incorrectas.add(li)
    else:
        lista_encontradas.add(li)

    solucion = jugando(lista_encontradas, palabra_descompuesta)

    if palabra == solucion:
        break

    print(f"Letras incorrectas: {lista_incorrectas}")
    print(f"Letras encontradas: {lista_encontradas}")

if vida == 0:
    print("Has muerto")
    print("x x")
    print("---")
