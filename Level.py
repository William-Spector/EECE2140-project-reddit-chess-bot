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
        self.song_len = pygame.mixer.Sound.get_length(self.song) * 1000
        self.miss = pygame.mixer.Sound("SFX/miss.wav")
        self.hit = pygame.mixer.Sound("SFX/hit.wav")
        self.prompt = pygame.mixer.Sound("SFX/prompt.wav")
        self.playing = False
        self.next_note = 0
        self.hits = []
        self.onscreen_time = 120000/self.chart.bpm  #120,000 ms is 2 minutes, divided by n beats per minute to get ms per 2 beats
        self.success = 0

    def modify_surface(self, surface, time_mod):
        '''
        Uses information in self.gfx to modify a Pygame surface
        inputs:
            surface		    pygame.Surface
            time_mod		timing data for finding current time since 
        outputs:
            goto_menu       bool
        '''
        if not self.playing: #if paused, do nothing
            return
        current_note = self.chart.notes[self.next_note] #get the next note to render
        tm = time_mod.get_elapsed()/1000000          #get the current time since level start in ms
        if current_note != None and tm > (current_note.timing - (self.onscreen_time)): 
            pygame.mixer.Sound.play(self.prompt)
        while current_note != None and tm > (current_note.timing - (self.onscreen_time)): #while notes need to be printed
            if current_note.color == 0:                 #"green" note, can be any key
                self.hits.append([50, current_note.location, pygame.Color(0,255,0), current_note.timing, False, 0])
            elif current_note.color == 1:               #"blue" note, button1set
                self.hits.append([50, current_note.location, pygame.Color(255,0,0), current_note.timing, False, 1])
            elif current_note.color == 2:               #"red" note, button2set
                self.hits.append([50, current_note.location, pygame.Color(0,0,255), current_note.timing, False, 2])
            if self.hits[len(self.hits)-1][1][0] == -1: #will be -1, -1 if these are meant to be random
                self.hits[len(self.hits)-1][1] = (randint(81,1200), randint(81,640))
            self.next_note += 1                         #advance next_note, get next_note
            current_note = self.chart.notes[self.next_note]
        surface.fill(black)                             #reset screen for drawing the next frame
        tm = time_mod.get_elapsed()/1000000             #reset current time before getting animations
        for circle in self.hits:
            circle[0] = 50*((circle[3]-tm)/self.onscreen_time) #calculate proper radius for circle
            pygame.draw.circle(surface,circle[2],circle[1],circle[0]) #draw a circle with correct radius, center, color
            if(circle[4] and tm > circle[3]):
                pygame.mixer.Sound.play(self.hit)
            if(circle[3] < tm - self.chart.leniency * 60000 / self.chart.bpm):
                self.hits.remove(circle)                # when it's past ideal hit time, stop rendering it
        pygame.display.flip()
        if(tm > self.song_len):         #if the song is over, return to title, else continue
            self.next_note = 0
            return True
        return False
        
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
        
    def check_hit(self, button, time_mod, tm = None, hits = None):
        '''
        Process data to confirm whether or not a button press constitutes a hit
        prints sucess/failure/no note, timing information
        inputs:
            button      int
            time_mod    timing data
        '''
        if tm == None:
            tm = time_mod.get_elapsed()/1000000 #setting time is priority number 1
        if hits == None:
            hits = self.hits
        lnc = self.chart.leniency * 60000 / self.chart.bpm #compute leniency in ms
        if(len(hits) == 0): #If there's no notes left to check for a hit
            print("none\t", tm, lnc, "fail" "", sep="\t",)
            pygame.mixer.Sound.play(self.miss)
            return
        if(tm > hits[0][3]):        #Hit counts but is after perfect
            if (hits[0][4]):
                self.check_hit(button, time_mod, tm, hits[1:])
            elif(hits[0][5] == 0 or hits[0][5] == button):
                pygame.mixer.Sound.play(self.hit)
                print(hits[0][3], tm, lnc, "success", sep="\t",end="")
                self.success+=1
            else:
                self.check_hit(button, time_mod, tm, hits[1:])
        elif(tm > (hits[0][3] - lnc)): #Hit counts but is before erasure
            if (hits[0][4]):
                self.check_hit(button, time_mod, tm, hits[1:])
            else:
                if(hits[0][5] == 0 or hits[0][5] == button):
                    pygame.mixer.Sound.play(self.hit)
                    print(hits[0][3], tm, lnc, "success", sep="\t",end="")
                    self.success += 1
                else:
                    self.check_hit(button, time_mod, tm, hits[1:])
        else:   #if it's too far before the current note
            print(hits[0][3], tm, lnc, "fail",sep="\t",end="")
            pygame.mixer.Sound.play(self.miss)
        print("")
       
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
        
    def reset(self):
        '''
        Resets values that change while playing a level (no inputs/outputs)
        '''
        self.next_note = 0
        self.hits = []
        self.success = 0
