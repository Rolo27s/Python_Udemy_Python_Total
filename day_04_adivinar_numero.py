"""# Repaso de conceptos basicos
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

print("----------------")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for index, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(index)

print("----------------")
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
print(edad_minima)"""

# reto del dia. Adivinar un numero entre en 1 y el 100
from random import randint
numR = randint(1,101)
c = 1 # numero de intentos (contador)
nombre = input("Nombre: ")
print(f"Hola {nombre}, he pensado un numero entre el 1 y el 100.\nTienes 8 intentos para adivinar el número...\n")
print("Te sugiero empezar con el 50...")
aMin = 0
aMax = 100
while c <= 8:
    num = int(input(f"Intento numero {c}. ¿Que numero es?: "))
    c += 1 # sumo un intento
    match numR:
        case numR if (num < 1 or num > 100):
            print("Ha elegido un número que no está permitido")
            c -= 1 # no se contabiliza el intento en caso de error
        case numR if num == numR:
            print(f"Has acertado!\nEl numero era el {numR}")
            break
        case numR if num > numR:
            print("Es un numero mas pequeño")
            aMax = num
            print(f"Te sugiero probar con el {(aMax+aMin)//2}")
        case numR if num < numR:
            print("Es un numero mas grande")
            aMin = num
            print(f"Te sugiero probar con el {(aMax+aMin)//2}")
        case _:
            print("Input incorrecto")
            c -= 1  # no se contabiliza el intento en caso de error

if c > 8:
    print(f"********\nSe agotaron los intentos\nVuelve a intentarlo\n********")

# Me gustaria estudiar las probabilidades de este juego inventado cuales son