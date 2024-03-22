import pygame
import random

colour_1 = "white"
colour_2 = "pink"
colour_3 = "black"
colour_4 = "white"
colour_5 = "darkgreen"
colour_6 = "pink"

pygame.init()
box_len = 1000
box_height = 400

add_caption = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SSSSNAKE GAME")

timer = pygame.time.Clock()
snake_block = 10
snake_speed = 10
display_style = pygame.font.SysFont("arial", 30, "normal")
score_font = pygame.font.SysFont("arial", 40, "normal")


def final_score(score):
    value = score_font.render("Welcome to my snake game------- Your current score is : " + str(score), True, colour_2)
    add_caption.blit(value, [0, 0])


def make_snake(snake_block, list_snake):
    for el in list_snake:
        pygame.draw.rect(add_caption, colour_3, [el[0], el[1], snake_block, snake_block])


def display_msg(msg, color):
    mssg = display_style.render(msg, True, color)
    add_caption.blit(mssg, [box_len / 6, box_height / 3])


def game_start():
    game_over = False
    game_close = False

    value_x1 = box_len / 2
    value_y1 = box_height / 2
    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
    foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            add_caption.fill(colour_6)
            display_msg("You LOST! Do you want another chance? YES(press C)       NO(press Q)", colour_4)
            final_score(snake_len - 1)
            pygame.display.update()

            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if ev.key == pygame.K_c:
                        game_start()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                game_over = True
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif ev.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif ev.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif ev.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0

        value_x1 += new_x1
        value_y1 += new_y1

        if value_x1 >= box_len or value_x1 < 0 or value_y1 >= box_height or value_y1 < 0:
            game_close = True

        add_caption.fill(colour_6)
        pygame.draw.rect(add_caption, colour_5, [foodx_pos, foody_pos, snake_block, snake_block])

        snake_head = []
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)

        if len(list_snake) > snake_len:
            del list_snake[0]

        for el in list_snake[:-1]:
            if el == snake_head:
                game_close = True

        make_snake(snake_block, list_snake)
        pygame.display.update()

        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
            foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
            snake_len += 1

        timer.tick(snake_speed)

    pygame.quit()
    quit()


game_start()
