import json
from Note import Note

class Chart:
    '''
    Class for loading and storing a chart from a json file
    Properties:
        notes               list[Note]
    Methods:
        __init__
        get_next_note
    '''
    def __init__(self, filename: str):
        '''
        Initializer for Chart
        Loads data for Chart based on data in a json file
        inputs:
            filename        str
        Attributes of JSON in chart file:
        Required:
            notes       list[list[int]]
            bpm         number
            leniency    float
        Optional
            gfx         list[dict] (unimplemented)
                attributes of gfx element:
                    image       str                     file path to background image
                    start       number                  when this image is to be displayed
                    scales      list[[int, int]]        when the image is supposed to be at what scale
                    positions   list[[(int, int), int]] when the image is supposed to be where
                    end         number                  when this image is to no longer be displayed
                    transition  int                     option: how the image comes onto screen, 0=jumpcut, 1=crossfade, 2 = zoom
        '''
        levelfile = open(filename)  #open json file at filename
        obj = json.load(levelfile)  #load json from file
        self.notes = []             #create empty list to load notes into
        self.current_note = 0
        for note in obj["notes"]:   #load notes from notes in notes attribute
            self.notes.append(Note(note[0], note[1], (note[2],note[3])))
        self.notes.append(None)     #None object at the end of the list to mark the end. This is a cheap trick, but effective
        self.bpm = obj["bpm"]
        self.leniency = obj["leniency"]
        if "gfx" in dir(obj):       #if gfx attribute exists, load gfx attribute
            self.gfxmods = obj["gfx"]
        else:
            self.gfxmods = None

    def get_next_note(self):
        '''
        method get_next_note
        Finds and returns the next note to draw
        Probably will go unimplemented, unused and may be deleted in a future commit
        '''
        pass
