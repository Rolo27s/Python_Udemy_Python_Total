import pygame
import random
import math
from pygame import mixer
import io

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("space-gun.png")
pygame.display.set_icon(icono)

# Agregar musica de fondo
mixer.music.load("base.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)  # Se reproduce en loop

# Fondo de pantalla
fondo = pygame.image.load("space.png")
fondo = pygame.transform.scale(fondo, (800, 600))

# Jugador
img_jugador = pygame.image.load("nave.png")
# Redimensionar la imagen a 64x64 píxeles
img_jugador = pygame.transform.scale(img_jugador, (64, 64))
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img = pygame.image.load("enemigo.png")
    img = pygame.transform.scale(img, (48, 48))
    img_enemigo.append(img)
    enemigo_x.append(random.randint(0, 752))
    enemigo_y.append(10)
    enemigo_x_cambio.append(3)
    enemigo_y_cambio.append(50)

# Bala
img_bala = pygame.image.load("bala.png")

bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 8  # Velocidad de la bala
bala_visible = False

# Funcion que transforma la fuente de Strings a objeto Byte (Se usa la libreria io)
def fuente_bytes(fuente):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuente, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        # Crea un objeto BytesIO a partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)


# Score
puntaje = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 22)
texto_x = 10
texto_y = 10

# Fuente de fin de juego
fuente_final = pygame.font.Font(fuente_como_bytes, 32)
texto_x_final = 300
texto_y_final = 220

# Bandera para controlar la reproducción del sonido de explosión final
explosion_reproducida = False

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Score: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 30, y + 32))  # Para que la bala salga desde el centro de la nave

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 30:
        return True
    else:
        return False

def texto_final(x, y):
    texto = fuente_final.render(f"Fin del juego", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Loop del juego
se_ejecuta = True
fin_juego = False
while se_ejecuta:
    # Fondo de pantalla
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 4
            if evento.key == pygame.K_SPACE and not bala_visible:
                bala_x = jugador_x
                disparar_bala(bala_x, bala_y)
                sonido_bala = mixer.Sound("laser.mp3")
                sonido_bala.play()

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación nave
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > 736:
        jugador_x = 736

    # Modificar ubicación enemiga
    for e in range(cantidad_enemigos):
        # Revisar si un enemigo nos mata
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final(texto_x_final, texto_y_final)
            fin_juego = True
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo (Dentro de X. En Y existirá colisión)
        if enemigo_x[e] < 0:
            enemigo_x_cambio[e] = 3
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] > 752:
            enemigo_x_cambio[e] = -3
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1

            # Reseteamos al enemigo
            enemigo_x[e] = random.randint(0, 752)
            enemigo_y[e] = 10

            sonido_colision = mixer.Sound("explosion.mp3")
            sonido_colision.play()

        # Llamada a función de lanzamiento de enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Recarga de la bala
    if bala_y < -64:
        bala_y = 500
        bala_visible = False

    # Movimiento de la bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Llamada a función de lanzamiento de jugador
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # Reproducir sonido de explosión final solo una vez
    if fin_juego and not explosion_reproducida:
        explosion_final = mixer.Sound("latest_explosion.mp3")
        explosion_final.play()
        explosion_reproducida = True  # Marcar que el sonido ya se reprodujo

    # Update de la pantalla de juego
    pygame.display.update()
