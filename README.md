# Another Two Button Rhythm Game (A2BRG)

![A2BRG Logo][/GFX/A2BRG-Icon.png]

## Summary

A2BRG is a 2 button rhythm game written in pygame, a multimedia library for Python. It takes users to a "menu screen," which is a static screen containing two images, a title and the keyboard layout, and a caption telling them how they may proceed. From there when they press the enter key, it will then begin a song playing and begin to prompt users for inputs. When a new note comes on screen, it plays a kick drum to indicate the presence of the note. Two beats after a note begins, the user must hit the corresponding key within a time window defined by the level parameters (red on the left of the home row, blue on the right, vice versa for the other two rows of keys. The spacebar is a red key). If they successfully do it within this timing window, it will play a snare; whenever they hit a button which does not fall within the timing window, or press the wrong key, it plays a weak cymbal crash. They can pause and play at any time by hitting escape. When the game is paused, they can quit back to the menu by pressing the Q key. Additionally, when the song ends, it brings the user back to the menu.

Many parts of A2BRG draw inspiration from other games:

- Osu! *graphics*
- Rhythm Journey, Unbeatable, MuseDash *keyboard layout, kind of*
- Rhythm Doctor *hit timing/indication*
- A Dance Of Fire And Ice *level graphics options, eventually*

## Overview of Code

The game is run using main.py. This function holds the code for the static menu screen, and controls the loop which checks key strokes and calls the functions which render frames. In addition to this are four classes used in the final program: Level, Chart, Note, and timing. Each of these are in their own files, (timing is in timing\_ctrl.py) and do not inherit. However, Main only imports Level and timing, Level only imports Chart, and Chart only imports Note. The script in Main includes logic to create one Level, but could handle multiple Levels. Each Level contains one Chart, but Charts contain many Notes. Exactly one timing is used by the entire program. 

Each class other than Note contains a number of functions to manipulate its own data. The function modify\_surface in Level is the renderer function used in Main. 

Additionally, A2BRG uses a number of files which do not appear in this main folder. Graphics, songs, sound effects, and levels are all held within their own subfolders. Graphics (in /GFX) are type .png and were created using [GIMP](https://gimp/org). Songs and sound effects are .wav. Levels are .json text files, which when imported create dicts in python, and have a list of note information (each contained in a list), an integer representation of tempo in beats per minute, and a hit leniency, as well as any graphics options should this ever be implemented.

## Instructions for Use

If python is not installed, proceed to python.org, and install the package. Presently, this will install python 3.11.
Alternatively, python is available through many package managers:

apt: `sudo apt install python`
pacman:  `pacman -S python`
homebrew: `brew install python`

If using python 3.11, pygame is not presently available through pip. Thus, the following command may be used to install a pre-release version (note that on python releases 3.10 or newer on MacOS, this command is pip3, not pip):
```
pip install pygame --pre
```
If using python 3.10 or earlier, simply use:
```
pip install pygame
```
If the pip command is not recognized by the command line, instead use the following, changing the python call by platform:
```pythoon -m pip install pygame --pre```

Next, clone this repository, and navigate to the folder. Once installed, execute the following based on platform:
Windows:
```py main.py```
Linux:
```python main.py```
MacOS:
```python3 main.py```

## Suggested Feature Direction:

Many mid- and low-priority features remain incomplete, including: 

- Menus
- Scores
- Saving
- Graphics Options
- Lose condition
- Tutorial Stage
- Extra Songs
- Multiple Difficulty Levels
- Selectible Song Speed

The highest priority among these are scores and saving, followed by menus and graphics options. Currently, the Level object keeps track of successful hits, but does nothing with this information. While there is a "menu" currently, it is fairly incomplete. Additionally, a pause menu indicating that one can quit or resume would be a smart addition. Having a dynamic menu would also give the starting menu more polish. 

Largely, this game is a very complete proof of concept, but it lacks polish. I hope to come back to this project in the future.