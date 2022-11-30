import pygame, time
from Chart import Chart
from random import randint

black = 0,0,0

class Level():
    '''
    class Level
    Class for controlling the current level
    Contains information on how to draw the level, load the level's music, and any non-default graphics options (TODO)
    '''
    def __init__(self, levelfile: str, songfile: str):
        '''
        initializer for Level
        levelfile contains chart info
        songfile is audio, should be wav
        '''
        self.chart = Chart(levelfile)
        self.song = pygame.mixer.Sound(songfile)
        self.playing = False
        self.next_note = 0
        self.hits = []
        self.onscreen_time = 120000/self.chart.bpm  #120,000 ms in 2 minutes, divided by n beats per minute to get ms per 2 beats

    def get_next_note(self):
        '''
        function get_next_note
        Finds the timing for the next note to draw
        Probably will go unimplemented, unused and be deleted in a future commit
        '''
        pass

    def modify_surface(self, surface, time_mod):
        '''
        Uses information in self.gfx to modify a Pygame surface
        inputs:
            surface		    pygame.Surface
            time_mod		timing data for finding current time since 
        '''
        if not self.playing: #if paused, do nothing
            return
        current_note = self.chart.notes[self.next_note] #get the next note to render
        tm = time_mod.get_elapsed()/1000000          #get the current time since level start in ms
        print(tm) #debugging print statement
        while current_note != None and tm > (current_note.timing - (self.onscreen_time)): #while notes need to be printed
            if current_note.color == 0:                 #"green" note, can be any key
                self.hits.append([50, current_note.location, pygame.Color(0,255,0), current_note.timing])
                print("green")
            elif current_note.color == 1:               #"blue" note, button1set
                self.hits.append([50, current_note.location, pygame.Color(0,0,255), current_note.timing])
                print("blue")
            elif current_note.color == 2:               #"red" note, button2set
                self.hits.append([50, current_note.location, pygame.Color(255,0,0), current_note.timing])
                print("red")
            if self.hits[len(self.hits)-1][1][0] == -1: #will be -1, -1 if these are meant to be random
                self.hits[len(self.hits)-1][1] = (randint(81,1200), randint(81,1200))
            self.next_note += 1                         #advance next_note, get next_note
            current_note = self.chart.notes[self.next_note]
        surface.fill(black)                             #reset screen for drawing the next frame
        for circle in self.hits:
            circle[0] = 50*((circle[3]-tm)/self.onscreen_time) #calculate proper radius for circle
            pygame.draw.circle(surface,circle[2],circle[1],circle[0]) #draw a circle with correct radius, center, color
            if(circle[0] <= 0):
                self.hits.remove(circle)                # when it's past ideal hit time, stop rendering it
        pygame.display.flip()
        
    def pause(self, time_mod):
        '''
        Pauses and resumes the game during the level
        Stores the current elapsed time to calculate how far forward time_mod needs to jump
        Inputs:
            time_mod        timing data
        '''
        if self.playing:
            self.pausetime = time_mod.get_elapsed()
            pygame.mixer.pause()
            self.playing = False
        else:
            time_mod.skip(self.pausetime)
            pygame.mixer.unpause()
            self.playing = True
            del self.pausetime
        pass
        
    def check_hit(self, button, time_mod):
        '''
        Process data to confirm whether or not a button press constitutes a hit
        inputs:
            button      int
            time_mod    timing data
        '''
        pass
       
    def start_level(self, surface, time_mod):
        '''
        generate data and start music for a level
        Inputs:
            surface     pygame surface or window
            time_mod    timing data
        '''
        pygame.mixer.Sound.play(self.song)  #start music
        time_mod.reset()                    #set initial time
        self.playing = True                 #set playing status
