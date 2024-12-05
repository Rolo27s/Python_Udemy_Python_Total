"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
"""

def break_word(word):
    chars = list()
    for c in word:
        chars.append(c)

    chars_setted = set(chars) # clean duplicates
    chars_cleaned = list(chars_setted) # recover list
    chars_cleaned.sort()
    return chars_cleaned

sol = break_word("entretenido")
print(sol)