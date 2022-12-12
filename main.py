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
pygame.display.set_caption('A2BRG')
black = 0,0,0                           #create color tuple for black
time_struct = timing()                  #new time struct for timing. Perhaps should be part of the Level class based on other data, but then again it works as it is.

#Load and setup as much data as possible
icon = pygame.image.load("GFX/A2BRG-Icon.png")  #dock/taskbar icon
title = pygame.image.load("GFX/A2BRG-Title.png")  #title icon for menu
pygame.Surface.convert_alpha(icon)
pygame.Surface.convert_alpha(title)
title_size = title.get_rect().size
title = pygame.transform.scale(title, (width/3, width/3*title_size[1]/title_size[0]))
pygame.display.set_icon(icon)
keyboard_img = pygame.image.load("GFX/keyboard_layout.png")  #keyboard layout graphics for menu
pygame.Surface.convert_alpha(keyboard_img)
key_img_size = keyboard_img.get_rect().size
keyboard_img = pygame.transform.scale(keyboard_img, (width/2, width/2*key_img_size[1]/key_img_size[0]))
font = pygame.font.Font("Fonts/timeburnerbold.ttf", int(height/20))  #press enter to play font
proceed_caption = font.render("Press enter to play", False, (0,0,255,255))
capt_size = proceed_caption.get_rect().size
pygame.Surface.convert_alpha(proceed_caption)

current_level = 0

while True:                             #begin game loop: start in "menu," meaning wait for return
    screen.fill(black)
    screen.blit(title,(width/3,0))
    screen.blit(keyboard_img,(width/4,height/2))
    screen.blit(proceed_caption,(width/2-capt_size[0]/2,height-1.5*capt_size[1]))
    pygame.display.flip()
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
                elif not levels[current_level].playing:
                    if event.key == K_q:                #Quit on escape -> Q
                        levels[current_level].reset()
                        menu = True
                        print('quitting level...')
                elif event.key in button1set:
                    if levels[current_level].playing:
                        time_struct.hit()
                        levels[current_level].check_hit(1, time_struct)
                elif event.key in button2set:
                    if levels[current_level].playing:
                        time_struct.hit()
                        levels[current_level].check_hit(2, time_struct)
        if not menu:
            menu = levels[0].modify_surface(screen, time_struct) #compute and render next frame
    levels[current_level].resset()