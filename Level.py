import pygame

class Level():
    '''
    class Level
    Class for controlling the current level
    Contains information on how to draw the level, load the level's music, and any non-default graphics options (TODO)
    '''
    def __init__(self, levelfile: str, songfile: str, gfx=None)
        '''
        initializer for Level
        '''
        self.chart = chart(levelfile)
        self.song = songfile
        if(gfx == None):
            pass
        self.gfx = gfx

    def get_next_note(self):
        '''
        function get_next_note
        Finds the timing for the next note to draw
        '''
        pass

    def modify_surface(self, surface, time_cur)
        '''
        Uses information in self.gfx to modify a Pygame surface
        inputs:
            surface		pygame.Surface
            time_cur		the current ms since level starting
       '''
       pass
