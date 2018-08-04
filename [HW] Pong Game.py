import pygame
from random import choice, randint

pygame.init()
pygame.display.set_caption("Core game")

SIZE = (640, 480)
BG_COLOR = (52, 76, 52)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
paddle_image = pygame.image.load("assets\paddle.png")
paddle_image_1 = paddle_image
ball = pygame.image.load("assets/ball.png")

x1 = 0
y1 = randint(0, 480 -100)
x2 = 640 - 30
y2 = randint(0, 480 - 100)

w_pressed = False
s_pressed = False

o_pressed = False
l_pressed = False

ball_v_x = choice([i for i in range(-5, 5) if i != 0])
ball_v_y = 6
ballx = 320
bally = 240

# ball_v_x = 0
# ball_v_y = 6
# ballx = 600
# bally = 100

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
                l_pressed = True

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_o:
                o_pressed = False
            elif e.key == pygame.K_l:
                l_pressed = False

    if w_pressed:
        y1 -= 5
    elif s_pressed:
        y1 += 5
    elif o_pressed:
        y2 -= 5
    elif l_pressed:
        y2 += 5

    ballx += ball_v_x
    bally += ball_v_y

    if ballx <= x1 + 25:
        if y1 <= bally <= y1 + 120:
            ball_v_x = - ball_v_x
        elif y1 - 20 <= bally <= y1 + 20 or y1 + 120 <= bally <= y1 + 125:
            ball_v_y = - ball_v_y
    if ballx >= x2 - 15:
        if y2 <= bally <= y2 + 120:
            ball_v_x = - ball_v_x
        elif y2 - 20 <= bally <= y2 + 20 or y2 + 120 <= bally <= y2 + 125:
            ball_v_y = - ball_v_y
    if ballx >= 640 - 20 or ballx <= 0:
        ball_v_x = - ball_v_x
    elif bally >= 480 - 20 or bally <= 0:
        ball_v_y = - ball_v_y

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image_1, (x2, y2))
    canvas.blit(ball, (ballx, bally))
    clock.tick(60)
    pygame.display.flip()

