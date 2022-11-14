import sys, pygame, time
from random import randint

from pygame.locals import (
    K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p,
    K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l,
    K_z, K_x, K_c, K_v, K_b, K_n, K_m,
    K_SPACE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

button2set = {K_q, K_w, K_e, K_r, K_t, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v}
button1set = {K_SPACE, K_y, K_u, K_i, K_o, K_p, K_a, K_s, K_d, K_f, K_g, K_b, K_n, K_m}

circles = []

pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)
black = 0,0,0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in button1set:
                circles.append([0,(randint(81,1200),randint(81,640)),pygame.Color(0,0,255)])
            if event.key in button2set:
                circles.append([0,(randint(81,1200),randint(81,640)),pygame.Color(255,0,0)])
    
    screen.fill(black)
    for circle in circles:
        pygame.draw.circle(screen,circle[2],circle[1],circle[0])
        if(circle[0] > 80):
            circles.remove(circle)
        circle[0] += 1
    pygame.display.flip()
    time.sleep(0.05)
        