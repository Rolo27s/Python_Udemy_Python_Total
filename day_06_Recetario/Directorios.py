import os
from pathlib import Path
import shutil

def listar_categorias(ruta_carpeta):
    """ Lista las categorias de las recetas y las devuelve en una lista """
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Comprobar si la carpeta existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return

        # Filtrar solo las subcarpetas que serían las categorias
        categorias = [categoria.name for categoria in ruta.iterdir() if categoria.is_dir()]

        # Mostrar las subcarpetas encontradas
        print("Categorías encontradas:")
        for categoria in categorias:
            print(f"- {categoria}")

        return categorias

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta.")

def listar_recetas(ruta_carpeta):
    """ Lista las recetas de la categoria y las devuelve en una lista """
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Comprobar si la carpeta existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return

        # Listar archivos .txt en la categoría
        archivos = list(ruta.glob("*.txt"))
        if not archivos:
            print(f"No se encontraron recetas en la categoría '{ruta.name}'.")
            return

        # Mostrar archivos disponibles
        print(f"Recetas disponibles en '{ruta.name}':")
        for i, archivo in enumerate(archivos, start=1):
            print(f"{i}. {archivo.name}")

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta o archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def leer_receta(ruta_carpeta):
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Comprobar si la carpeta existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return
        # Listar archivos .txt en la categoría
        archivos = list(ruta.glob("*.txt"))
        # Pedir al usuario que elija un archivo
        while True:
            try:
                if len(archivos) == 0:
                    return

                eleccion = int(input("\nElige el número de la receta que deseas leer: "))
                if 1 <= eleccion <= len(archivos):
                    archivo_seleccionado = archivos[eleccion - 1]
                    break
                else:
                    print(f"Por favor, elige un número entre 1 y {len(archivos)}.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        # Leer y mostrar el contenido del archivo seleccionado
        with archivo_seleccionado.open("r", encoding="utf-8") as file:
            contenido = file.read()
            print(f"\nContenido de la receta '{archivo_seleccionado.name}':")
            print(contenido)

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta o archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def crear_receta(ruta_carpeta):
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Comprobar si la carpeta existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return

        # Pedir el nombre de la nueva receta
        receta_nueva = input("Nombre de la receta nueva (sin extensión): ").strip()
        receta_nueva = receta_nueva.capitalize() + ".txt"

        # Construir la ruta completa del archivo de la receta
        ruta_receta = ruta / receta_nueva

        # Comprobar si la receta ya existe
        if ruta_receta.exists():
            print("La receta ya existe.")
        else:
            print(f"Se genera la receta '{receta_nueva}'")
            contenido = input("Descripción de la nueva receta:\n")

            # Crear el archivo y escribir el contenido
            with ruta_receta.open("w", encoding="utf-8") as file:
                file.write(contenido)

            print(f"La receta '{receta_nueva}' ha sido creada correctamente.")

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta o archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def contar_categorias(ruta_carpeta):
    """ Cuenta las categorias y devuelve el numero de cuantas hay """
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Contador
        c = 0

        # Comprobar si la carpeta existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return

        # Filtrar solo las subcarpetas que serían las categorias
        categorias = [categoria.name for categoria in ruta.iterdir() if categoria.is_dir()]

        for categoria in categorias:
            c += 1

        print(f"Se han encontrado {c} categoria/s")

        return c

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta.")

def contar_recetas(ruta_carpeta):
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_carpeta)

        # Comprobar si la carpeta principal existe
        if not ruta.exists():
            print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
            return

        # Inicializar contadores
        total_recetas = 0
        categorias = []

        # Recorrer las subcarpetas (categorías)
        for carpeta in ruta.iterdir():
            if carpeta.is_dir():
                # Contar archivos .txt en la subcarpeta
                recetas = list(carpeta.glob("*.txt"))
                num_recetas = len(recetas)
                total_recetas += num_recetas
                categorias.append((carpeta.name, num_recetas))

        # Mostrar resultados
        print("Recetas por categoría:")
        for categoria, cantidad in categorias:
            print(f"- {categoria}: {cantidad} recetas")

        print(f"\nTotal de recetas: {total_recetas}")

    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta.")

def crear_categoria(ruta_recetas):
    try:
        # Convertir la ruta a un objeto Path
        ruta_principal = Path(ruta_recetas)

        # Verificar si la carpeta principal existe
        if not ruta_principal.exists():
            print(f"Error: La carpeta principal '{ruta_recetas}' no existe.")
            return

        # Pedir el nombre de la nueva categoría
        nueva_categoria = input("Nombre de la nueva categoría: ").strip()
        nueva_categoria = nueva_categoria.capitalize()  # Capitalizar el nombre
        ruta_categoria = ruta_principal / nueva_categoria  # Crear la ruta completa

        # Verificar si la categoría ya existe
        if ruta_categoria.exists():
            print(f"La categoría '{nueva_categoria}' ya existe.")
        else:
            ruta_categoria.mkdir()  # Crear la nueva carpeta
            print(f"Categoría '{nueva_categoria}' creada correctamente.")

    except PermissionError:
        print("Error: No tienes permisos para crear carpetas en esta ubicación.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def eliminar_categoria(ruta_recetas):
    try:
        # Convertir la ruta principal a un objeto Path
        ruta_principal = Path(ruta_recetas)

        # Verificar si la carpeta principal existe
        if not ruta_principal.exists():
            print(f"Error: La carpeta principal '{ruta_recetas}' no existe.")
            return

        # Listar las categorías disponibles
        categorias = [carpeta.name for carpeta in ruta_principal.iterdir() if carpeta.is_dir()]
        if not categorias:
            print("No hay categorías disponibles para eliminar.")
            return

        print("Categorías disponibles:")
        for idx, categoria in enumerate(categorias, start=1):
            print(f"{idx}. {categoria}")

        # Seleccionar la categoría a eliminar
        try:
            opcion = int(input("Selecciona el número de la categoría que deseas eliminar: "))
            if opcion < 1 or opcion > len(categorias):
                print("Opción inválida.")
                return
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            return

        # Confirmar la eliminación
        categoria_a_eliminar = categorias[opcion - 1]
        ruta_categoria = ruta_principal / categoria_a_eliminar

        confirmacion = input(f"¿Estás seguro de que deseas eliminar la categoría '{categoria_a_eliminar}'? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return

        # Verificar si la carpeta está vacía y eliminarla
        if any(ruta_categoria.iterdir()):
            print(f"La categoría '{categoria_a_eliminar}' no está vacía. Eliminando todo su contenido...")
            shutil.rmtree(ruta_categoria)
        else:
            ruta_categoria.rmdir()  # Eliminar carpeta vacía

        print(f"Categoría '{categoria_a_eliminar}' eliminada correctamente.")

    except PermissionError:
        print("Error: No tienes permisos para eliminar esta categoría.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def eliminar_receta(ruta_categoria):
    try:
        # Convertir la ruta a un objeto Path
        ruta = Path(ruta_categoria)

        # Verificar si la categoría existe
        if not ruta.exists() or not ruta.is_dir():
            print(f"Error: La categoría '{ruta_categoria}' no existe o no es una carpeta válida.")
            return

        # Listar recetas disponibles
        recetas = [archivo.name for archivo in ruta.glob("*.txt")]
        if not recetas:
            print("No hay recetas disponibles para eliminar en esta categoría.")
            return

        print("Recetas disponibles:")
        for idx, receta in enumerate(recetas, start=1):
            print(f"{idx}. {receta}")

        # Seleccionar la receta a eliminar
        try:
            opcion = int(input("Selecciona el número de la receta que deseas eliminar: "))
            if opcion < 1 or opcion > len(recetas):
                print("Opción inválida.")
                return
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            return

        # Confirmar la eliminación
        receta_a_eliminar = recetas[opcion - 1]
        ruta_receta = ruta / receta_a_eliminar

        confirmacion = input(f"¿Estás seguro de que deseas eliminar la receta '{receta_a_eliminar}'? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return

        # Eliminar la receta
        ruta_receta.unlink()
        print(f"La receta '{receta_a_eliminar}' ha sido eliminada correctamente.")

    except PermissionError:
        print("Error: No tienes permisos para eliminar esta receta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def handler(opcion, ruta):
    """ Funciona como funcion para elegir una opcion del menu.
        Necesita para trabajar la opcion elegida y la ruta de las recetas.
    """
    if opcion == 1:
        # elegir categoria + leer receta
        categorias = listar_categorias(ruta)
        elegir_categoria = input("Selecciona categoría: ").capitalize()
        if elegir_categoria in categorias:
            print(f"Categoría seleccionada {elegir_categoria}")
            ruta_receta = Path(ruta) / elegir_categoria
            listar_recetas(ruta_receta)
            leer_receta(ruta_receta)
        else:
            print(f"La categoría {elegir_categoria} no existe")

    elif opcion == 2:
        # elegir categoria + crear receta
        categorias = listar_categorias(ruta)
        elegir_categoria = input("Selecciona categoría: ").capitalize()
        if elegir_categoria in categorias:
            print(f"Categoría seleccionada {elegir_categoria}")
            ruta_receta = Path(ruta) / elegir_categoria
            listar_recetas(ruta_receta)
            crear_receta(ruta_receta)
        else:
            print(f"La categoría {elegir_categoria} no existe")

    elif opcion == 3:
        # crear categoria
        listar_categorias(ruta)
        crear_categoria(ruta)

    elif opcion == 4:
        # elegir categoria + eliminar receta
        categorias = listar_categorias(ruta)
        elegir_categoria = input("Selecciona categoría: ").capitalize()
        if elegir_categoria in categorias:
            print(f"Categoría seleccionada {elegir_categoria}")
            ruta_receta = Path(ruta) / elegir_categoria
            eliminar_receta(ruta_receta)
        else:
            print(f"La categoría {elegir_categoria} no existe")

    elif opcion == 5:
        # eliminar categoria
        listar_categorias(ruta)
        eliminar_categoria(ruta)


# Inicio del programa
usuario = input("Escribe tu nombre: ")
os.system('cls')
print(f"Bienvenido {usuario}")

# Ruta absoluta a la carpeta 'Recetas'
ruta_absoluta = Path.cwd() / "Recetas"
print(f"La ruta absoluta es '{ruta_absoluta}'")

# Ruta relativa a la carpeta 'Recetas'
ruta_relativa = "Recetas"
print(f"La ruta relativa es '{ruta_relativa}'")

# Llamar a la función para contar categorías
contar_categorias(ruta_relativa)

# Llamar a la función para contar recetas
contar_recetas(ruta_relativa)

input("Presiona INTRO para mostrar el menu del programa ...")
os.system('cls')

opcion = 1
while not opcion == 6:
    print("""
    Menu principal
    ---------------------------------------
    1. elegir categoria + leer receta
    2. elegir categoria + crear receta
    3. crear categoria
    4. elegir categoria + eliminar receta
    5. eliminar categoria
    6. salir
    """)

    opcion = input("ingresa opcion: ")
    try:
        opcion = int(opcion)
        if 1 <= opcion <= 6:
            if opcion != 6:
                print(f"Has elegido la opcion {opcion}")
                handler(opcion, ruta_relativa)
                input("Presiona INTRO para continuar ...")
        else:
            print(f"La opcion seleccionada no existe")
            input("Presiona INTRO para continuar ...")
    except ValueError:
        print("Valor ingresado no válido")
        input("Presiona INTRO para continuar ...")

    os.system('cls')

    # Despedida
    if opcion == 6:
        print("Hasta pronto! 😊")