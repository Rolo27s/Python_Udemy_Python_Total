"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""

def contar_primos(n):
    c = 0
    num = int(n) + 1
    lista = list()
    es_primo = list()

    for x in range(2,num):
        lista.append(x)

    # lista.sort(reverse=True)

    for n in lista:
        d = n
        while d >= 1:
            if n % d == 0:
                c += 1
            d -= 1

        if c == 2:
            es_primo.append(n)
        else:
            pass

        c = 0 # Reseteo contador

    print(es_primo)

    return len(es_primo)

sol = contar_primos(17)
print(sol)