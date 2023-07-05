import random
import pygame
from pygame import *

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la ventana
window_width = 600
window_height = 800

# Crear la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mi Juego")

# Definir los colores (en formato RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir las coordenadas y dimensiones del rectángulo
rect_width = 50
rect_height = 50
rect_x = window_width // 2 - rect_width // 2
rect_y = window_height - rect_height

# Velocidad de movimiento del rectángulo
rect_speed = 1

# Definir las coordenadas y dimensiones de los obstáculos
obstacle_width = 100
obstacle_height = 100
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 0.7
obstacle_growth_rate = 0.04
obstacle_max_width = 200
obstacle_max_height = 200

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Mover el rectángulo horizontalmente
    #rect_x += rect_speed

     # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el rectángulo basado en las teclas presionadas
    if keys[K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[K_RIGHT] and rect_x < window_width - rect_width:
        rect_x += rect_speed
    if keys[K_UP] and rect_y > 0:
        rect_y -= rect_speed
    if keys[K_DOWN] and rect_y < window_height - rect_height:
        rect_y += rect_speed

    # Actualizar la posición del obstáculo
    obstacle_y += obstacle_speed
    obstacle_width += obstacle_growth_rate
    obstacle_height += obstacle_growth_rate

    # Limitar el crecimiento del obstáculo
    if obstacle_width > obstacle_max_width:
        obstacle_width = obstacle_max_width
    if obstacle_height > obstacle_max_height:
        obstacle_height = obstacle_max_height

    # Verificar si el obstáculo ha salido de la pantalla
    if obstacle_y > window_height:
        # Reiniciar la posición y tamaño del obstáculo
        obstacle_x = random.randint(0, int(window_width) - int(obstacle_width))
        obstacle_y = -obstacle_height
        obstacle_width = 100
        obstacle_height = 100

    # Limpiar la pantalla
    window.fill(WHITE)

    # Dibujar el rectángulo en la pantalla
    pygame.draw.rect(window, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Dibujar el obstáculo en la pantalla
    pygame.draw.rect(window, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Verificar la colisión entre el rectángulo y el obstáculo
    if rect_x < obstacle_x + obstacle_width and \
            rect_x + rect_width > obstacle_x and \
            rect_y < obstacle_y + obstacle_height and \
            rect_y + rect_height > obstacle_y:
        # Si hay colisión, terminar el juego
        running = False

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
