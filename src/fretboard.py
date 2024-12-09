

class Fretboard():
    tunings = {"Standard_E": ["E", "A", "D", "G", "B", "E"],
               "Drop_D": ["D", "A", "D", "G", "B", "E"]}

    strings = {"Standard_E": [["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"],
                              ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
                              ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#"]]}


    def __init__(self, tuning_key):
        self.tuning_key = tuning_key
        self.strings = self.strings[tuning_key]
    
    def get_strings(self):
        return self.strings

