# Simple Metal Riff Generator
A Python application that generates custom heavy metal guitar riffs in tablature format. Users can specify the scale, tuning, and other parameters to create unique riffs. The project also includes functionality to save riffs to a folder for future reference.

## Features 
- Customizable Inputs: Choose the key, scale, and tuning for your riff.
- Dynamic Rhythm Patterns: Generates rhythmically varied riffs.
- Realistic Guitar Techniques: Incorporates powerchords and palm mutes
- Tablature Formatting: Outputs riffs as clean and aligned guitar tabs.
- File Saving: Gives option to save generated riffs in a designated folder.

## Installation 
1. Clone the Repository:
```
git clone https://github.com/MechamJonathan/simple_metal_riff_generator.git
cd simple_metal_riff_generator
```

2. Ensure Python3.8+ is installed

## Run Application
In the src directory run the following command:
```
python3 ./main.py
```

## How It Works
- Fretboard Representation: Models strings and frets based on user-specified tuning.
- Rhythm Generator: Randomly selects rhythm patterns that include rests, power chords, and palm-muted chugs.
- Note Placement: Ensures logical placement of notes and chords for realistic playability.
- Tab Formatting: Aligns notes into clean guitar tablature.
- File Saving: Automatically creates a MyRiffs directory and prevents overwriting existing riffs.

## Example
Generated riff example:
```
E|------------------------|------------------------|
B|------------------------|------------------------|
G|4--------4--------------|---------2--------------|
D|4-----2--4-----5--------|2-----5--2-----12-------|
A|2-----2--2-----5--------|2-----5--0-----12-------|
E|---0--0--------3-----0--|0--0--3--------10----0--|
```

