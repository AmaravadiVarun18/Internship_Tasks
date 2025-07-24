import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game with Levels")

# Colors
bg_color = (30, 30, 60)
snake_color = (0, 255, 150)
food_color = (255, 100, 100)
text_color = (255, 255, 255)

# Snake settings
block_size = 20

# Fonts
score_font = pygame.font.SysFont('Arial', 24)
msg_font = pygame.font.SysFont('Arial', 36)

clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(win, snake_color, [x, y, block_size, block_size], border_radius=6)

def draw_food(x, y):
    pygame.draw.rect(win, food_color, [x, y, block_size, block_size], border_radius=6)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, text_color)
    win.blit(value, [10, 10])

def game_over_screen():
    win.fill(bg_color)
    msg = msg_font.render("Game Over! C - Continue | Q - Quit", True, text_color)
    win.blit(msg, [width // 8, height // 3])
    pygame.display.update()

def select_difficulty():
    selecting = True
    while selecting:
        win.fill(bg_color)
        title = msg_font.render("Select Difficulty", True, text_color)
        easy = score_font.render("1. Easy 🐢", True, text_color)
        medium = score_font.render("2. Medium 🐍", True, text_color)
        hard = score_font.render("3. Hard ⚡", True, text_color)

        win.blit(title, [width // 3 - 30, 60])
        win.blit(easy, [width // 3, 140])
        win.blit(medium, [width // 3, 180])
        win.blit(hard, [width // 3, 220])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 8  # Easy
                elif event.key == pygame.K_2:
                    return 12  # Medium
                elif event.key == pygame.K_3:
                    return 20  # Hard

def game_loop():
    snake_speed = select_difficulty()

    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:
        while game_close:
            game_over_screen()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        win.fill(bg_color)
        draw_food(food_x, food_y)

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_score(length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
