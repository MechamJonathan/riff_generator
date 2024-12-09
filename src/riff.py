import random


class Riff():
    def __init__(self, scale, fretboard):
        self.scale = scale
        self.fretboard = fretboard
        self.riff = self.generate_riff()
    
    def generate_riff(self):
        riff = []
        rhythm = self.generate_rhythm_pattern()
        note_string_map = {} 

        for i in range(0,2):
            bar = []
            for i in range(len(rhythm)):
                if rhythm[i] == 1:
                    note = random.choice(self.scale.scale_notes)

                    if note in note_string_map:
                        string = note_string_map[note]
                    else:
                        string = random.randint(0, 1)
                        note_string_map[note] = string
                    
                    note_fret = self.fretboard.strings[string].index(note)
                    bar_chord = [
                        (string, note_fret),
                        (string + 1, note_fret + 2),
                        (string + 2, note_fret + 2)
                    ]
                    bar.append(bar_chord)

                else:
                    bar.append(rhythm[i])
            riff.append(bar)
        return riff


    def generate_rhythm_pattern(self):
        possible_rhythm_items= [0, 1, None]
        rhythm = []
        rhythm.append(random.choice([0,1]))
        for i in range(7):
            rhythm.append(random.choice(possible_rhythm_items))
        return rhythm
    

    def get_riff(self):
        return self.riff
