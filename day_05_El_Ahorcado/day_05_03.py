"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def check_zero(*args):
    zero_counter = 0
    for arg in args:
        if arg == 0:
            zero_counter += 1
        else:
            zero_counter = 0

        if zero_counter == 2:
            return True

    return False

sol = check_zero(6,0,5,1,0,3,0,1)
print(sol)