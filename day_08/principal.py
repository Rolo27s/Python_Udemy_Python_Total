"""
Ejercicio del día 8.
Turnero para comercio.
Archivo que contiene el main de la app
"""

from time import sleep as zzz
from os import system

from numeros import generador_comercio, mensaje

def main():
    # Crear generadores para los tres comercios
    turneros = {
        "P": generador_comercio("P"),  # Perfumería
        "F": generador_comercio("F"),  # Farmacia
        "C": generador_comercio("C"),  # Cosmética
    }

    while True:
        print("\nTurnero para comercios:")
        print("1. Generar turno para Perfumería (P)")
        print("2. Generar turno para Farmacia (F)")
        print("3. Generar turno para Cosmética (C)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            turno = next(turneros["P"])
            mensaje(turno)
        elif opcion == "2":
            turno = next(turneros["F"])
            mensaje(turno)
        elif opcion == "3":
            turno = next(turneros["C"])
            mensaje(turno)
        elif opcion == "4":
            print("Gracias por usar el turnero. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

        if opcion != 4:
            zzz(2)
            system("cls")

if __name__ == "__main__":
    main()
