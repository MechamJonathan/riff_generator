
class Scale:
    def __init__(self, key, scale_type):
        self.key = key
        self.scale_type = scale_type
        self.scale_notes = self.set_scale()

    def set_scale(self):
        scales = {"E_Minor": ["E", "F#", "G", "A", "B", "C", "D"],
                  "E_Major": ["E", "F♯", "G♯", "A", "B", "C♯", "D♯"],
                  "E_Pentatonic":["E", "G", "A", "B", "D"]}
        return scales[f"{self.key}_{self.scale_type}"]
    
    def get_scale_notes(self):
        return self.scale_notes