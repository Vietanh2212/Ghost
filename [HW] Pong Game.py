import pygame
from random import choice, randint

height = int(input("Enter the height (<= 720): "))
width = int(input("Enter the width:(<= 720) "))
pygame.init()
pygame.display.set_caption("Core game")

SIZE = (width, height)
BG_COLOR = (52, 76, 52)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
paddle_image = pygame.image.load("assets\paddle.png")
paddle_image_1 = paddle_image
ball = pygame.image.load("assets/ball.png")

x1 = 0
y1 = randint(0, height -100)
x2 = width - 30
y2 = randint(0, height - 100)

w_pressed = False
s_pressed = False

o_pressed = False
l_presssed = False

ball_v_x = choice([i for i in range(-5, 5) if i != 0])
ball_v_y = 6
ballx = width / 2
bally = height / 2

loop = True

while loop:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True
            elif e.key == pygame.K_o:
                o_pressed = True
            elif e.key == pygame.K_l:
                l_presssed = True

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_o:
                o_pressed = False
            elif e.key == pygame.K_l:
                l_presssed = False

    if w_pressed:
        y1 -= 5
    elif s_pressed:
        y1 += 5
    elif o_pressed:
        y2 -= 5
    elif l_presssed:
        y2 += 5

    ballx += ball_v_x
    bally += ball_v_y

    if ballx <= x1 + 25 and bally in range(y1, y1 + 120):
        ball_v_x = - ball_v_x
    elif ballx >= x2 - 25 and bally in range(y2, y2 + 120):
        ball_v_x = -ball_v_x
    elif ballx >= width - 20 or ballx <= 0:
        ball_v_x = - ball_v_x
    elif bally >= height - 20 or bally <= 0:
        ball_v_y = - ball_v_y

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image_1, (x2, y2))
    canvas.blit(ball, (ballx, bally))
    clock.tick(60)
    pygame.display.flip()

