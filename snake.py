import pygame
import time
import random
import sys

pygame.init()


# Definir colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definir el tamaño de la pantalla
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ProGit')

# Definir la velocidad del juego
snake_block = 10
snake_speed = 10

# Definir la fuente y el tamaño del texto
font_style = pygame.font.SysFont(None, 25)

# Función para dibujar la serpiente en la pantalla
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Función para mostrar el puntaje en la pantalla
def Your_score(score):
    value = font_style.render("Tus punticos: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Función para mostrar el mensaje de derrota
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])






# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Inicializar la posición de la serpiente
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Inicializar el cambio en la posición de la serpiente
    x1_change = 0
    y1_change = 0

    # Inicializar la longitud de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Inicializar la posición de la comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("¡Perdiste! Presiona C para jugar otra vez o Q para salir", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    game_close = True

        # Verificar si la serpiente sale de la pantalla
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Actualizar la posición de la serpiente
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Generar una nueva posición para la comida cuando la serpiente la come
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()

pygame.init()

