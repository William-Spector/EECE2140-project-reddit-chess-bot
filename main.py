import sys, pygame, time
from random import randint
#import python modules

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
    K_RETURN,
    KEYDOWN,
    QUIT,
)               #easy access to keys used for input. More or fewer special keys may be necessary in the final product

button2set = {K_q, K_w, K_e, K_r, K_t, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v}
button1set = {K_SPACE, K_y, K_u, K_i, K_o, K_p, K_a, K_s, K_d, K_f, K_g, K_b, K_n, K_m}

from Level import Level
from timing_ctrl import timing

pygame.init()           #initialize pygame
menu = True             #start in the "menu" (currently waits for enter key to begin level)
levels = [Level("Levels/SpoonsDraft.json", "Music/Spoons-1.wav")] #only one level for now, level[0] using song "spoons"

size = width, height = 1280, 720    #window is 720p for now. Perhaps will find a way to change that if I implement settings, but this is extremely low-priority

screen = pygame.display.set_mode(size)  #set size of the screen
black = 0,0,0                           #create color tuple for black
time_struct = timing()                  #new time struct for timing. Perhaps should be part of the Level class based on other data, but then again it works as it is.

screen.fill(black)                      #for now, start with black screen
pygame.display.flip()
current_level = 0

while True:                             #begin game loop: start in "menu," meaning wait for return
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()    #allow for quit by clicking x
            if event.type == pygame.KEYDOWN:        #if it's a key, check if it's the key that will cause the level to start
                if event.key == K_RETURN:
                    menu = False                    #leave menu
                    current_level = 0               #set current level (currently the only implemented level, level 0)
    levels[current_level].start_level(screen, time_struct)
    while not menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()    #allow for quit by clicking x
            if event.type == pygame.KEYDOWN:            #check keys, pause on Esc, check hit on other buttons
                if event.key == K_ESCAPE:
                    levels[current_level].pause(time_struct)
                elif event.key in button1set:
                    time_struct.hit()
                    levels[current_level].check_hit(1, time_struct)
                elif event.key in button2set:
                    time_struct.hit()
                    levels[current_level].check_hit(2, time_struct)
                
        levels[0].modify_surface(screen, time_struct) #compute and render next frame