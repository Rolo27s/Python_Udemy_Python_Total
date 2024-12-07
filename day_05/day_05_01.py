"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""

def devolver_distintos(a,b,c):
    """
    Funcion que devuelve distintos
    :return: int
    """
    lista = [a,b,c]
    lista.sort()
    total = sum(lista)

    if total > 15:
        return lista[2]
    elif 15 >= total >= 10:
        return lista[1]
    else:
        return lista[0]
    return 0 # Return de error

sol = devolver_distintos(4,1,3)
print(sol)
