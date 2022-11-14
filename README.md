# EECE2140-project-rhythm-game

**A basic rhythm game in the vein of Osu!**

# Structure

Main loop (starts as Game Scene, eventually Menu and Game scene will be separated if time allows for menu)
- Spawns window, possibly draws menu which will spawn game scene
- Game scene pulls Level, which contains Chart, audio, any graphics
- either Main loop or Game scene starts audio and begins pulling notes
- This loop will draw notes at correct times and graphically (maybe audio too?) indicate hit timing
- Keep track of hits/misses during song (audio feedback for hits/misses)
- Save top score to file

### High Priority:
Level class, contains Chart, song audio file, graphics information   
Chart class, contains collections of Notes   
Note class, contains timing information, location information

### Low Priority:
Menu class, contains strings and funcitons for game navigation
JSON interpretation and saving so levels (maybe scores, but this could also be CSVs) are their own object files

# Features:

## High Priority:

- Working audio playback
- Game interface
- Timing Response
- Minimum 1 working song
- Charting for said song(s)
- Basic spritework

## Medium Priority

- Menus/UI
- Scores
- Saving
- Lose condition
- Tutorial Stage

## Low Priority

- Extra Songs
- Multiple Difficulty Levels
- Selectible Song Speeds
- Level object JSON files

# Libraries

- [pygame](https://www.pygame.org/)
- [json](https://docs.python.org/3/library/json.html)
