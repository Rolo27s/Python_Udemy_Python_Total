import zipfile
import os
import re
from datetime import datetime
import timeit

with zipfile.ZipFile("Proyecto+Dia+9.zip", "r") as archivo_zip:
    print("Archivos contenidos:\n", "\n".join(archivo_zip.namelist()))

    # Leer un archivo específico dentro del .zip
    with archivo_zip.open("Instrucciones.txt") as archivo:
        contenido = archivo.read().decode("utf-8")
        print("Contenido del archivo:\n", contenido)

    # Extraer todos los archivos contenidos en el ZIP si aún no se hizo
    if not (os.path.exists('Mi_Gran_Directorio')):
        archivo_zip.extractall()
        print("\nArchivos extraídos correctamente.")


# Una vez leido y descomprimido el enunciado procedo a generar el buscador de números de serie
# Expresion regular para detectar los números de serie
patron = r'N[a-z]{3}-\d{5}'
# Ruta del directorio a recorrer
directorio = "Mi_Gran_Directorio"

# Función para buscar números de serie en un archivo
def buscar_numeros_en_archivo(ruta_archivo, patron):
    numeros_encontrados = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                numeros_encontrados.extend(re.findall(patron, linea))
    except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError) as e:
        print(f"No se pudo leer el archivo: {ruta_archivo}. Error: {e}")
    return numeros_encontrados

# Recorrer el directorio y buscar en cada archivo
def buscar_numeros_en_directorio(directorio, patron):
    resultados = {}
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            numeros = buscar_numeros_en_archivo(ruta_completa, patron)
            if numeros:  # Si se encuentran números de serie en el archivo
                resultados[ruta_completa] = numeros
    return resultados

# Obtener la fecha actual en formato dd/mm/yy
fecha_actual = datetime.today().strftime('%d/%m/%y')

# Marca para inicio de tiempo de ejecución
inicio_tiempo = timeit.default_timer()

# Ejecutar la búsqueda
resultados = buscar_numeros_en_directorio(directorio, patron)

# Marca para fin de tiempo de ejecución
fin_tiempo = timeit.default_timer()
tiempo_busqueda = round(fin_tiempo - inicio_tiempo, 2)

# Contar el número total de números de serie encontrados
numeros_count = sum(len(numeros) for numeros in resultados.values())

# Mostrar los resultados
if resultados:
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {fecha_actual}\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    for ruta_archivo, numeros in resultados.items():
        nombre_archivo = os.path.basename(ruta_archivo)
        print(f"{nombre_archivo}\t{numeros}")
    print("----------------------------------------------------")
    print(f"Números encontrados: {numeros_count}")
    print(f"Duración de la búsqueda: {tiempo_busqueda} segundos")
else:
    print("No se encontraron números de serie en el directorio.")
