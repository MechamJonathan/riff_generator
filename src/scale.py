
class Scale:
    def __init__(self, key, scale_type):
        self.key = key
        self.scale_type = scale_type
        self.scale_notes = self.set_scale()

    def set_scale(self):
        scales = {

                "A_Minor": ["A", "B", "C", "D", "E", "F", "G"],
                "A_Major": ["A", "B", "C#", "D", "E", "F#", "G#"],
                "A_Pentatonic": ["A", "C", "D", "E", "G"],
                
                "C_Minor": ["C", "D", "D#", "F", "G", "G#", "A#"],
                "C_Major": ["C", "D", "E", "F", "G", "A", "B"],
                "C_Pentatonic": ["C", "G#", "F", "G", "A#"],

                "D_Minor": ["D", "E", "F", "G", "A", "A#", "C"],
                "D_Major": ["D", "E", "F#", "G", "A", "B", "C#"],
                "D_Pentatonic": ["D", "F", "G", "A", "C"],

                "E_Minor": ["E", "F#", "G", "A", "B", "C", "D"],
                "E_Major": ["E", "F#", "G#", "A", "B", "C#", "D#"],
                "E_Pentatonic":["E", "G", "A", "B", "D"],

                "G_Minor": ["G", "A", "A#", "C", "D", "D#", "F"],
                "G_Major": ["G", "A", "B", "C", "D", "E", "F#"],
                "G_Pentatonic": ["G", "A#", "C", "D", "F"],
                  }
        return scales[f"{self.key}_{self.scale_type}"]
    
    def get_scale_notes(self):
        return self.scale_notes