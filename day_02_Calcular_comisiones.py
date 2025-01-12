# Cobro el 13% en comisiones. Segun hayas vendido, eso que ganas.
# Vble nombre y ventas.
# Solucion: Nombre este mes has ganado tanto.

nombre = input("Dime tu nombre: ")
ventas = float(input("Dame el valor de tus ventas: "))
sueldo = round(ventas*0.13,2)

print(f"{nombre}, este mes cobras {sueldo}")
