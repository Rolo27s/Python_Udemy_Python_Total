# Ejercicio simple de select info en dict
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

# valor del boolean (True:1, False:0)
a = True
b = int(a)
b = str(b)
a = str(a)
print(a + " - " + b)


"""
La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. 
Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta. 
"""

texto = input("Ingresa un texto: ")
a,b,c = input("Ingresa 3 letras: ")

# Pasamos a minuscula para evitar problemas
texto = texto.lower()
a = a.lower()
b = b.lower()
c = c.lower()
letras = [a,b,c]

# 1. Contador de letras
for letra in letras:
    n = texto.count(letra)
    n = str(n)
    print("Numero de veces que aparece la letra '" + letra + "': " + n)

#2. Text to list
text_list = texto.split()
numero_palabras = len(text_list)
print(f"Numero de palabras en el texto: {numero_palabras}")

#3. Primera y ultima letra del texto
print(f"Primera letra: {texto[0]}\nUltima letra: {texto[-1]}")

#4. Invertir orden de lista y aunar en string para formar texto inverso por palabras
text_list.reverse()
reverse_string = " ".join(text_list)
print(f"Texto invertido: {reverse_string}")

#5. "Python" into text?
python = "python" in text_list
if python:
    print("La palabra Python existe en el texto")
else:
    print("La palabra Python NO existe en el texto")
