import time

class timing():
    '''
    class timestruct
    Class for keeping track of time within a level
    Contains functions for starting and resetting time, and controlling hits
    '''
    def __init__(self):
        '''
        initializer for timing
        '''
        self.start = time.time_ns()
        self.hits = []
        
    def reset(self):
        '''
        reset start time
        Inputs: none
        '''
        self.start = time.time_ns()
        
    def hit(self):
        '''
        Adds to hits in case asynchronous computing is necessary. I think the way pygame works it won't be but nevertheless this is here
        '''
        self.hits.append(self.get_elapsed())
        
    def get_elapsed(self):
        '''
        Get the difference between the current time and the start time in nanoseconds
        '''
        return time.time_ns()-self.start
        
    def skip(self, oldtime):
        '''
        Move start time forward as though time between now and oldtime didn't happen
        '''
        self.start += (self.get_elapsed() - oldtime)